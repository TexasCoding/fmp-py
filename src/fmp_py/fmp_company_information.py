from fmp_py.fmp_base import FmpBase, FMP_COMPANY_PROFILE
from fmp_py.models.company_information import CompanyProfile


class FmpCompanyInformation(FmpBase):
    def __init__(self):
        super().__init__()

    def company_profile(self, ticker: str) -> CompanyProfile:
        """
        Retrieves the company profile information for a given ticker symbol.

        Args:
            ticker (str): The ticker symbol of the company.

        Returns:
            CompanyProfile: A dataclass object containing the company profile information.
        """
        url = f"{FMP_COMPANY_PROFILE}{ticker}?apikey={self.api_key}"
        response = self.get_request(url)
        data = response.get("profile", {})

        if not data:
            return CompanyProfile()

        return CompanyProfile(
            symbol=ticker.upper(),
            price=data.get("price", 0.0),
            beta=data.get("beta", 0.0),
            vol_avg=data.get("volAvg", 0),
            mkt_cap=data.get("mktCap", 0),
            last_div=data.get("lastDiv", 0.0),
            range=data.get("range", ""),
            changes=data.get("changes", 0.0),
            company_name=data.get("companyName", ""),
            currency=data.get("currency", ""),
            cik=data.get("cik", ""),
            isin=data.get("isin", ""),
            cusip=data.get("cusip", ""),
            exchange=data.get("exchange", ""),
            exchange_short_name=data.get("exchangeShortName", ""),
            industry=data.get("industry", ""),
            website=data.get("website", ""),
            description=data.get("description", ""),
            ceo=data.get("ceo", ""),
            sector=data.get("sector", ""),
            country=data.get("country", ""),
            full_time_employees=data.get("fullTimeEmployees", ""),
            phone=data.get("phone", ""),
            address=data.get("address", ""),
            city=data.get("city", ""),
            state=data.get("state", ""),
            zip=data.get("zip", ""),
            dcf_iff=data.get("dcfDiff", 0.0),
            dcf=data.get("dcf", 0.0),
            image=data.get("image", ""),
            ipo_date=data.get("ipoDate", ""),
            default_image=data.get("defaultImage", False),
            is_etf=data.get("isEtf", False),
            is_actively_trading=data.get("isActivelyTrading", False),
            is_adr=data.get("isAdr", False),
            is_fund=data.get("isFund", False),
        )
