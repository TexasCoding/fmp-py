import pandas as pd
import pytest
from unittest.mock import patch
from fmp_py.fmp_company_information import FmpCompanyInformation
from fmp_py.models.company_information import CompanyProfile


@pytest.fixture
def fmp_client():
    return FmpCompanyInformation()


# Add mock_get_request function for company_profile
def mock_get_request_profile(url, params):
    if "v3/company/profile" in url:
        return {
            "profile": {
                "price": 150.0,
                "beta": 1.2,
                "volAvg": 1000000,
                "mktCap": 2500000000,
                "lastDiv": 1.2,
                "range": "100-200",
                "changes": 2.5,
                "companyName": "Apple Inc.",
                "currency": "USD",
                "cik": "0000320193",
                "isin": "US0378331005",
                "cusip": "037833100",
                "exchange": "NASDAQ",
                "exchangeShortName": "NASDAQ",
                "industry": "Consumer Electronics",
                "website": "https://www.apple.com",
                "description": "Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide.",
                "ceo": "Tim Cook",
                "sector": "Technology",
                "country": "US",
                "fullTimeEmployees": 147000,
                "phone": "1-408-996-1010",
                "address": "One Apple Park Way",
                "city": "Cupertino",
                "state": "California",
                "zip": "95014-2083",
                "dcfDiff": 20.0,
                "dcf": 170.0,
                "image": "https://logo.clearbit.com/apple.com",
                "ipoDate": "1980-12-12",
            }
        }
    return {}


def mock_get_request_employee_count(url, params):
    if "v4/historical/employee_count" in url:
        return [
            {
                "filingDate": "2023-01-01",
                "acceptanceTime": "2023-01-02 10:00:00",
                "periodOfReport": "2022-12-31",
                "employeeCount": 147000,
                "formType": "10-K",
                "companyName": "Apple Inc.",
            }
        ]
    return []


def mock_get_request_comp_bench(url, params):
    if "v4/executive-compensation-benchmark" in url:
        return [
            {"industryTitle": "Technology", "averageCompensation": 150000.0},
            {"industryTitle": "Healthcare", "averageCompensation": 130000.0},
        ]
    return []


def mock_get_request_screener(url, params):
    if "v3/stock-screener" in url:
        return [
            {
                "companyName": "Apple Inc.",
                "marketCap": 2500000000,
                "price": 150.0,
                "beta": 1.2,
                "volume": 1000000,
                "lastAnnualDividend": 0.82,
                "exchangeShortName": "NASDAQ",
                "isActivelyTrading": True,
                "isEtf": False,
                "isFund": False,
            },
            {
                "companyName": "Microsoft Corporation",
                "marketCap": 1700000000,
                "price": 280.0,
                "beta": 1.5,
                "volume": 800000,
                "lastAnnualDividend": 1.12,
                "exchangeShortName": "NASDAQ",
                "isActivelyTrading": True,
                "isEtf": False,
                "isFund": False,
            },
        ]
    return []


@patch.object(
    FmpCompanyInformation, "get_request", side_effect=mock_get_request_screener
)
def test_stock_screener(mock_get_request_screener, fmp_client):
    filters = {
        "market_cap_more_than": 1000000000,
        "market_cap_lower_than": 3000000000,
        "price_more_than": 100,
        "price_lower_than": 300,
        "is_actively_trading": True,
    }
    df = fmp_client.stock_screener(**filters)
    assert not df.empty
    assert "company_name" in df.columns
    assert "market_cap" in df.columns
    assert df.iloc[0]["company_name"] == "Apple Inc."
    assert df.iloc[0]["market_cap"] == 2500000000
    assert df.iloc[0]["price"] == 150.0
    assert df.iloc[0]["volume"] == 1000000
    assert df.iloc[0]["last_annual_dividend"] == 0.82
    assert df.iloc[0]["exchange_short_name"] == "NASDAQ"
    assert df.iloc[0]["is_actively_trading"]
    assert not df.iloc[0]["is_etf"]
    assert not df.iloc[0]["is_fund"]

    assert df.iloc[1]["company_name"] == "Microsoft Corporation"
    assert df.iloc[1]["market_cap"] == 1700000000
    assert df.iloc[1]["price"] == 280.0
    assert df.iloc[1]["volume"] == 800000
    assert df.iloc[1]["last_annual_dividend"] == 1.12
    assert df.iloc[1]["exchange_short_name"] == "NASDAQ"
    assert df.iloc[1]["is_actively_trading"]
    assert not df.iloc[1]["is_etf"]
    assert not df.iloc[1]["is_fund"]


@patch.object(
    FmpCompanyInformation, "get_request", side_effect=mock_get_request_comp_bench
)
def test_compensation_benchmark(mock_get_request_comp_bench, fmp_client):
    year = 2023
    df = fmp_client.compensation_benchmark(year)
    assert not df.empty
    assert "industry_title" in df.columns
    assert "average_compensation" in df.columns
    assert df.iloc[0]["industry_title"] == "Technology"
    assert df.iloc[0]["average_compensation"] == 150000.0
    assert df.iloc[1]["industry_title"] == "Healthcare"
    assert df.iloc[1]["average_compensation"] == 130000.0


@patch.object(
    FmpCompanyInformation, "get_request", side_effect=mock_get_request_employee_count
)
def test_historical_employee_count(mock_get_request_employee_count, fmp_client):
    symbol = "AAPL"
    df = fmp_client.historical_employee_count(symbol)
    assert not df.empty
    assert df.iloc[0]["employee_count"] == 147000
    assert "filed_date" in df.columns
    assert pd.api.types.is_datetime64_any_dtype(df["filed_date"])
    assert df.iloc[0]["company_name"] == "Apple Inc."


@patch.object(
    FmpCompanyInformation, "get_request", side_effect=mock_get_request_profile
)
def test_company_profile(mock_get_request_profile, fmp_client):
    symbol = "AAPL"
    profile = fmp_client.company_profile(symbol)
    assert isinstance(profile, CompanyProfile)
    assert profile.company_name == "Apple Inc."
    assert profile.ceo == "Tim Cook"
    assert profile.sector == "Technology"
    assert profile.industry == "Consumer Electronics"
    assert profile.country == "US"
    assert profile.cik == "0000320193"
    assert profile.phone == "1-408-996-1010"
    assert profile.address == "One Apple Park Way"
    assert profile.city == "Cupertino"
    assert profile.state == "California"
    assert profile.zip == "95014-2083"
    assert profile.website == "https://www.apple.com"
    assert profile.image == "https://logo.clearbit.com/apple.com"
    assert profile.ipo_date == "1980-12-12"
