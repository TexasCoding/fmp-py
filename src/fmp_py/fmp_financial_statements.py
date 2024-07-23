from fmp_py.fmp_base import FmpBase
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


"""
This class is used to retrieve financial statements data from the Financial Modeling Prep API.
Reference: https://site.financialmodelingprep.com/developer/docs#financial-statements

def income_statements(self, symbol: str, period: str = "annual") -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#income-statements-financial-statements

def balance_sheet_statements(self, symbol: str, period: str = "annual", limit: int = 20) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#balance-sheet-statements-financial-statements
    
def cashflow_statements(self, symbol: str, period: str = "annual", limit: int = 20) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#cashflow-statements-financial-statements
    
def income_statements_as_reported(self, symbol: str, period: str = "annual", limit: int = 20) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#income-statements-as-reported-financial-statements
    
def balance_sheet_statements_as_reported(self, symbol: str, period: str = "annual", limit: int = 20) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#balance-statements-as-reported-financial-statements
    
def cashflow_statements_as_reported(self, symbol: str, period: str = "annual", limit: int = 20) -> pd.DataFrame:
    Reference: https://site.financialmodelingprep.com/developer/docs#cashflow-statements-as-reported-financial-statements
"""


class FmpFinancialStatements(FmpBase):
    def __init__(self, api_key: str = os.getenv("FMP_API_KEY")):
        super().__init__(api_key)

    ############################
    # Cash Flow Statements as Reported
    ############################
    def cashflow_statements_as_reported(
        self, symbol: str, period: str = "annual", limit: int = 20
    ) -> pd.DataFrame:
        """
        Retrieves the cash flow statements for a given symbol as reported by the company.

        Args:
            symbol (str): The symbol of the company.
            period (str, optional): The period of the financial statements. Defaults to "annual".
            limit (int, optional): The maximum number of statements to retrieve. Defaults to 20.

        Returns:
            pd.DataFrame: A DataFrame containing the cash flow statements.

        Raises:
            ValueError: If an invalid period is provided.
            ValueError: If no data is found for the provided symbol.
        """

        periods_allowed = ["annual", "quarter"]
        if period not in periods_allowed:
            raise ValueError(
                f"Invalid period. Allowed values are {', '.join(periods_allowed)}"
            )

        url = f"v3/cash-flow-statement-as-reported/{symbol}"
        params = {"period": period, "limit": limit}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the provided symbol.")

        data_df = (
            pd.DataFrame(response)
            .fillna(0)
            .rename(
                columns={
                    "date": "date",
                    "symbol": "symbol",
                    "period": "period",
                    "cashcashequivalentsrestrictedcashandrestrictedcashequivalents": "cash_cash_equivalents_restricted_cash_and_restricted_cash_equivalents",
                    "netincomeloss": "net_income_loss",
                    "depreciationdepletionandamortization": "depreciation_depletion_and_amortization",
                    "sharebasedcompensation": "share_based_compensation",
                    "othernoncashincomeexpense": "other_non_cash_income_expense",
                    "increasedecreaseinaccountsreceivable": "increase_decrease_in_accounts_receivable",
                    "increasedecreaseinotherreceivables": "increase_decrease_in_other_receivables",
                    "increasedecreaseininventories": "increase_decrease_in_inventories",
                    "increasedecreaseinotheroperatingassets": "increase_decrease_in_other_operating_assets",
                    "increasedecreaseinaccountspayable": "increase_decrease_in_accounts_payable",
                    "increasedecreaseinotheroperatingliabilities": "increase_decrease_in_other_operating_liabilities",
                    "netcashprovidedbyusedinoperatingactivities": "net_cash_provided_by_used_in_operating_activities",
                    "paymentstoacquireavailableforsalesecuritiesdebt": "payments_to_acquire_available_for_sale_securities_debt",
                    "proceedsfrommaturitiesprepaymentsandcallsofavailableforsalesecurities": "proceeds_from_maturities_prepayments_and_calls_of_available_for_sale_securities",
                    "proceedsfromsaleofavailableforsalesecuritiesdebt": "proceeds_from_sale_of_available_for_sale_securities_debt",
                    "paymentstoacquirepropertyplantandequipment": "payments_to_acquire_property_plant_and_equipment",
                    "paymentsforproceedsfromotherinvestingactivities": "payments_for_proceeds_from_other_investing_activities",
                    "netcashprovidedbyusedininvestingactivities": "net_cash_provided_by_used_in_investing_activities",
                    "paymentsrelatedtotaxwithholdingforsharebasedcompensation": "payments_related_to_tax_withholding_for_share_based_compensation",
                    "paymentsofdividends": "payments_of_dividends",
                    "paymentsforrepurchaseofcommonstock": "payments_for_repurchase_of_common_stock",
                    "proceedsfromissuanceoflongtermdebt": "proceeds_from_issuance_of_long_term_debt",
                    "repaymentsoflongtermdebt": "repayments_of_long_term_debt",
                    "proceedsfromrepaymentsofcommercialpaper": "proceeds_from_repayments_of_commercial_paper",
                    "proceedsfrompaymentsforotherfinancingactivities": "proceeds_from_payments_for_other_financing_activities",
                    "proceedsfromissuanceofcommonstock": "proceeds_from_issuance_of_common_stock",
                    "paymentstoacquireotherinvestments": "payments_to_acquire_other_investments",
                    "netcashprovidedbyusedinfinancingactivities": "net_cash_provided_by_used_in_financing_activities",
                    "cashcashequivalentsrestrictedcashandrestrictedcashequivalentsperiodincreasedecreaseincludingexchangerateeffect": "cash_cash_equivalents_restricted_cash_and_restricted_cash_equivalents_period_increase_decrease_including_exchange_rate_effect",
                    "incometaxespaidnet": "income_taxes_paid_net",
                    "interestpaidnet": "interest_paid_net",
                }
            )
        ).astype(
            {
                "date": "datetime64[ns]",
                "symbol": "str",
                "period": "str",
                "cash_cash_equivalents_restricted_cash_and_restricted_cash_equivalents": "int",
                "net_income_loss": "int",
                "depreciation_depletion_and_amortization": "int",
                "share_based_compensation": "int",
                "other_non_cash_income_expense": "int",
                "increase_decrease_in_accounts_receivable": "int",
                "increase_decrease_in_other_receivables": "int",
                "increase_decrease_in_inventories": "int",
                "increase_decrease_in_other_operating_assets": "int",
                "increase_decrease_in_accounts_payable": "int",
                "increase_decrease_in_other_operating_liabilities": "int",
                "net_cash_provided_by_used_in_operating_activities": "int",
                "payments_to_acquire_available_for_sale_securities_debt": "int",
                "proceeds_from_maturities_prepayments_and_calls_of_available_for_sale_securities": "int",
                "proceeds_from_sale_of_available_for_sale_securities_debt": "int",
                "payments_to_acquire_property_plant_and_equipment": "int",
                "payments_for_proceeds_from_other_investing_activities": "int",
                "net_cash_provided_by_used_in_investing_activities": "int",
                "payments_related_to_tax_withholding_for_share_based_compensation": "int",
                "payments_of_dividends": "int",
                "payments_for_repurchase_of_common_stock": "int",
                "proceeds_from_issuance_of_long_term_debt": "int",
                "repayments_of_long_term_debt": "int",
                "proceeds_from_repayments_of_commercial_paper": "int",
                "proceeds_from_payments_for_other_financing_activities": "int",
                "net_cash_provided_by_used_in_financing_activities": "int",
                "proceeds_from_issuance_of_common_stock": "int",
                "payments_to_acquire_other_investments": "int",
                "cash_cash_equivalents_restricted_cash_and_restricted_cash_equivalents_period_increase_decrease_including_exchange_rate_effect": "int",
                "income_taxes_paid_net": "int",
                "interest_paid_net": "int",
            }
        )

        return data_df.sort_values(by="date", ascending=True).reset_index(drop=True)

    ############################
    # Balance Sheet Statements as Reported
    ############################
    def balance_sheet_statements_as_reported(
        self, symbol: str, period: str = "annual", limit: int = 20
    ) -> pd.DataFrame:
        """
        Retrieves the balance sheet statements as reported for a given symbol.

        Args:
            symbol (str): The symbol of the company.
            period (str, optional): The period of the statements. Allowed values are "annual" and "quarter". Defaults to "annual".
            limit (int, optional): The maximum number of statements to retrieve. Defaults to 20.

        Returns:
            pd.DataFrame: A DataFrame containing the balance sheet statements.

        Raises:
            ValueError: If an invalid period is provided.
            ValueError: If no data is found for the provided symbol.
        """
        periods_allowed = ["annual", "quarter"]
        if period not in periods_allowed:
            raise ValueError(f"Invalid period. Allowed periods: {periods_allowed}")

        url = f"v3/balance-sheet-statement-as-reported/{symbol}"
        params = {"period": period, "limit": limit}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the provided symbol.")

        data_df = (
            pd.DataFrame(response)
            .fillna(0)
            .rename(
                columns={
                    "date": "date",
                    "symbol": "symbol",
                    "period": "period",
                    "cashandcashequivalentsatcarryingvalue": "cash_and_cash_equivalents_at_carrying_value",
                    "marketablesecuritiescurrent": "marketable_securities_current",
                    "accountsreceivablenetcurrent": "accounts_receivable_net_current",
                    "nontradereceivablescurrent": "non_trade_receivables_current",
                    "inventorynet": "inventory_net",
                    "otherassetscurrent": "other_assets_current",
                    "assetscurrent": "assets_current",
                    "marketablesecuritiesnoncurrent": "marketable_securities_non_current",
                    "propertyplantandequipmentnet": "property_plant_and_equipment_net",
                    "otherassetsnoncurrent": "other_assets_non_current",
                    "assetsnoncurrent": "assets_non_current",
                    "assets": "assets",
                    "accountspayablecurrent": "accounts_payable_current",
                    "otherliabilitiescurrent": "other_liabilities_current",
                    "contractwithcustomerliabilitycurrent": "contract_with_customer_liability_current",
                    "commercialpaper": "commercial_paper",
                    "longtermdebtcurrent": "long_term_debt_current",
                    "liabilitiescurrent": "liabilities_current",
                    "longtermdebtnoncurrent": "long_term_debt_non_current",
                    "otherliabilitiesnoncurrent": "other_liabilities_non_current",
                    "liabilitiesnoncurrent": "liabilities_non_current",
                    "liabilities": "liabilities",
                    "commonstocksharesoutstanding": "common_stock_shares_outstanding",
                    "commonstocksharesissued": "common_stock_shares_issued",
                    "commonstocksincludingadditionalpaidincapital": "common_stocks_including_additional_paid_in_capital",
                    "retainedearningsaccumulateddeficit": "retained_earnings_accumulated_deficit",
                    "accumulatedothercomprehensiveincomelossnetoftax": "accumulated_other_comprehensive_income_loss_net_of_tax",
                    "stockholdersequity": "stockholders_equity",
                    "liabilitiesandstockholdersequity": "liabilities_and_stockholders_equity",
                    "commonstockparorstatedvaluepershare": "common_stock_par_or_stated_value_per_share",
                    "commonstocksharesauthorized": "common_stock_shares_authorized",
                }
            )
        ).astype(
            {
                "date": "datetime64[ns]",
                "symbol": "str",
                "period": "str",
                "cash_and_cash_equivalents_at_carrying_value": "int",
                "marketable_securities_current": "int",
                "accounts_receivable_net_current": "int",
                "non_trade_receivables_current": "int",
                "inventory_net": "int",
                "other_assets_current": "int",
                "assets_current": "int",
                "marketable_securities_non_current": "int",
                "property_plant_and_equipment_net": "int",
                "other_assets_non_current": "int",
                "assets_non_current": "int",
                "assets": "int",
                "accounts_payable_current": "int",
                "other_liabilities_current": "int",
                "contract_with_customer_liability_current": "int",
                "commercial_paper": "int",
                "long_term_debt_current": "int",
                "liabilities_current": "int",
                "long_term_debt_non_current": "int",
                "other_liabilities_non_current": "int",
                "liabilities_non_current": "int",
                "liabilities": "int",
                "common_stock_shares_outstanding": "int",
                "common_stock_shares_issued": "int",
                "common_stocks_including_additional_paid_in_capital": "int",
                "retained_earnings_accumulated_deficit": "int",
                "accumulated_other_comprehensive_income_loss_net_of_tax": "int",
                "stockholders_equity": "int",
                "liabilities_and_stockholders_equity": "int",
                "common_stock_par_or_stated_value_per_share": "float",
                "common_stock_shares_authorized": "int",
            }
        )

        return data_df.sort_values(by="date", ascending=True).reset_index(drop=True)

    ############################
    # Income Statements as Reported
    ############################
    def income_statements_as_reported(
        self, symbol: str, period: str = "annual", limit: int = 20
    ) -> pd.DataFrame:
        """
        Retrieves the income statements for a given symbol as reported by the company.

        Args:
            symbol (str): The symbol of the company.
            period (str, optional): The period of the income statements. Allowed values are "annual" and "quarter". Defaults to "annual".
            limit (int, optional): The maximum number of income statements to retrieve. Defaults to 20.

        Returns:
            pd.DataFrame: A DataFrame containing the income statements data.

        Raises:
            ValueError: If an invalid period is provided.
            ValueError: If no data is found for the provided symbol.
        """

        periods_allowed = ["annual", "quarter"]

        if period not in periods_allowed:
            raise ValueError(f"Invalid period. Allowed periods: {periods_allowed}")

        url = f"v3/income-statement-as-reported/{symbol}"
        params = {"period": period, "limit": limit}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the provided symbol.")

        data_df = (
            pd.DataFrame(response)
            .fillna(0)
            .rename(
                columns={
                    "date": "date",
                    "symbol": "symbol",
                    "period": "period",
                    "revenuefromcontractwithcustomerexcludingassessedtax": "revenue_from_contract_with_customer_excluding_assessed_tax",
                    "costofgoodsandservicessold": "cost_of_goods_and_services_sold",
                    "grossprofit": "gross_profit",
                    "researchanddevelopmentexpense": "research_and_development_expense",
                    "sellinggeneralandadministrativeexpense": "selling_general_and_administrative_expense",
                    "operatingexpenses": "operating_expenses",
                    "operatingincomeloss": "operating_income_loss",
                    "nonoperatingincomeexpense": "non_operating_income_expense",
                    "incomelossfromcontinuingoperationsbeforeincometaxesextraordinaryitemsnoncontrollinginterest": "income_loss_from_continuing_operations_before_income_taxes_extraordinary_items_non_controlling_interest",
                    "incometaxexpensebenefit": "income_tax_expense_benefit",
                    "netincomeloss": "net_income_loss",
                    "earningspersharebasic": "earnings_per_share_basic",
                    "earningspersharediluted": "earnings_per_share_diluted",
                    "weightedaveragenumberofsharesoutstandingbasic": "weighted_average_number_of_shares_outstanding_basic",
                    "weightedaveragenumberofdilutedsharesoutstanding": "weighted_average_number_of_diluted_shares_outstanding",
                    "othercomprehensiveincomelossforeigncurrencytransactionandtranslationadjustmentnetoftax": "other_comprehensive_income_loss_foreign_currency_transaction_and_translation_adjustment_net_of_tax",
                    "othercomprehensiveincomelossderivativeinstrumentgainlossbeforereclassificationaftertax": "other_comprehensive_income_loss_derivative_instrument_gain_loss_before_reclassification_after_tax",
                    "othercomprehensiveincomelossderivativeinstrumentgainlossreclassificationaftertax": "other_comprehensive_income_loss_derivative_instrument_gain_loss_reclassification_after_tax",
                    "othercomprehensiveincomelossderivativeinstrumentgainlossafterreclassificationandtax": "other_comprehensive_income_loss_derivative_instrument_gain_loss_after_reclassification_and_tax",
                    "othercomprehensiveincomeunrealizedholdinggainlossonsecuritiesarisingduringperiodnetoftax": "other_comprehensive_income_unrealized_holding_gain_loss_on_securities_arising_during_period_net_of_tax",
                    "othercomprehensiveincomelossreclassificationadjustmentfromaociforsaleofsecuritiesnetoftax": "other_comprehensive_income_loss_reclassification_adjustment_from_aoci_for_sale_of_securities_net_of_tax",
                    "othercomprehensiveincomelossavailableforsalesecuritiesadjustmentnetoftax": "other_comprehensive_income_loss_available_for_sale_securities_adjustment_net_of_tax",
                    "othercomprehensiveincomelossnetoftaxportionattributabletoparent": "other_comprehensive_income_loss_net_of_tax_portion_attributable_to_parent",
                    "comprehensiveincomenetoftax": "comprehensive_income_net_of_tax",
                }
            )
            .astype(
                {
                    "date": "datetime64[ns]",
                    "symbol": "str",
                    "period": "str",
                    "revenue_from_contract_with_customer_excluding_assessed_tax": "int",
                    "cost_of_goods_and_services_sold": "int",
                    "gross_profit": "int",
                    "research_and_development_expense": "int",
                    "selling_general_and_administrative_expense": "int",
                    "operating_expenses": "int",
                    "operating_income_loss": "int",
                    "non_operating_income_expense": "int",
                    "income_loss_from_continuing_operations_before_income_taxes_extraordinary_items_non_controlling_interest": "int",
                    "income_tax_expense_benefit": "int",
                    "net_income_loss": "int",
                    "earnings_per_share_basic": "float",
                    "earnings_per_share_diluted": "float",
                    "weighted_average_number_of_shares_outstanding_basic": "int",
                    "weighted_average_number_of_diluted_shares_outstanding": "int",
                    "other_comprehensive_income_loss_foreign_currency_transaction_and_translation_adjustment_net_of_tax": "int",
                    "other_comprehensive_income_loss_derivative_instrument_gain_loss_before_reclassification_after_tax": "int",
                    "other_comprehensive_income_loss_derivative_instrument_gain_loss_reclassification_after_tax": "int",
                    "other_comprehensive_income_loss_derivative_instrument_gain_loss_after_reclassification_and_tax": "int",
                    "other_comprehensive_income_unrealized_holding_gain_loss_on_securities_arising_during_period_net_of_tax": "int",
                    "other_comprehensive_income_loss_reclassification_adjustment_from_aoci_for_sale_of_securities_net_of_tax": "int",
                    "other_comprehensive_income_loss_available_for_sale_securities_adjustment_net_of_tax": "int",
                    "other_comprehensive_income_loss_net_of_tax_portion_attributable_to_parent": "int",
                    "comprehensive_income_net_of_tax": "int",
                }
            )
        )

        return data_df.sort_values(by="date", ascending=True).reset_index(drop=True)

    ############################
    # Cash Flow Statements
    ############################
    def cashflow_statements(
        self, symbol: str, period: str = "annual", limit: int = 20
    ) -> pd.DataFrame:
        """
        Retrieves the cash flow statements for a given symbol.

        Args:
            symbol (str): The stock symbol.
            period (str, optional): The period of the statements. Allowed values are "annual" and "quarter". Defaults to "annual".
            limit (int, optional): The maximum number of statements to retrieve. Defaults to 20.

        Returns:
            pd.DataFrame: A DataFrame containing the cash flow statements.

        Raises:
            ValueError: If an invalid period is provided.
            ValueError: If no data is found for the specified parameters.
        """

        periods_allowed = ["annual", "quarter"]

        if period not in periods_allowed:
            raise ValueError(f"Invalid period. Allowed periods: {periods_allowed}")

        url = f"v3/cash-flow-statement/{symbol}"
        params = {"period": period, "limit": limit}

        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the specified parameters.")

        data_df = (
            pd.DataFrame(response)
            .rename(
                columns={
                    "date": "date",
                    "symbol": "symbol",
                    "reportedCurrency": "reported_currency",
                    "cik": "cik",
                    "fillingDate": "filling_date",
                    "acceptedDate": "accepted_date",
                    "calendarYear": "calendar_year",
                    "period": "period",
                    "netIncome": "net_income",
                    "depreciationAndAmortization": "depreciation_and_amortization",
                    "deferredIncomeTax": "deferred_income_tax",
                    "stockBasedCompensation": "stock_based_compensation",
                    "changeInWorkingCapital": "change_in_working_capital",
                    "accountsReceivables": "accounts_receivables",
                    "inventory": "inventory",
                    "accountsPayables": "accounts_payables",
                    "otherWorkingCapital": "other_working_capital",
                    "otherNonCashItems": "other_non_cash_items",
                    "netCashProvidedByOperatingActivities": "net_cash_provided_by_operating_activities",
                    "investmentsInPropertyPlantAndEquipment": "investments_in_property_plant_and_equipment",
                    "acquisitionsNet": "acquisitions_net",
                    "purchasesOfInvestments": "purchases_of_investments",
                    "salesMaturitiesOfInvestments": "sales_maturities_of_investments",
                    "otherInvestingActivites": "other_investing_activites",
                    "netCashUsedForInvestingActivites": "net_cash_used_for_investing_activites",
                    "debtRepayment": "debt_repayment",
                    "commonStockIssued": "common_stock_issued",
                    "commonStockRepurchased": "common_stock_repurchased",
                    "dividendsPaid": "dividends_paid",
                    "otherFinancingActivites": "other_financing_activites",
                    "netCashUsedProvidedByFinancingActivities": "net_cash_used_provided_by_financing_activities",
                    "effectOfForexChangesOnCash": "effect_of_forex_changes_on_cash",
                    "netChangeInCash": "net_change_in_cash",
                    "cashAtEndOfPeriod": "cash_at_end_of_period",
                    "cashAtBeginningOfPeriod": "cash_at_beginning_of_period",
                    "operatingCashFlow": "operating_cash_flow",
                    "capitalExpenditure": "capital_expenditure",
                    "freeCashFlow": "free_cash_flow",
                    "link": "link",
                    "finalLink": "final_link",
                }
            )
            .astype(
                {
                    "date": "datetime64[ns]",
                    "symbol": "str",
                    "reported_currency": "str",
                    "cik": "str",
                    "filling_date": "datetime64[ns]",
                    "accepted_date": "datetime64[ns]",
                    "calendar_year": "int64",
                    "period": "str",
                    "net_income": "int",
                    "depreciation_and_amortization": "int",
                    "deferred_income_tax": "int",
                    "stock_based_compensation": "int",
                    "change_in_working_capital": "int",
                    "accounts_receivables": "int",
                    "inventory": "int",
                    "accounts_payables": "int",
                    "other_working_capital": "int",
                    "other_non_cash_items": "int",
                    "net_cash_provided_by_operating_activities": "int",
                    "investments_in_property_plant_and_equipment": "int",
                    "acquisitions_net": "int",
                    "purchases_of_investments": "int",
                    "sales_maturities_of_investments": "int",
                    "other_investing_activites": "int",
                    "net_cash_used_for_investing_activites": "int",
                    "debt_repayment": "int",
                    "common_stock_issued": "int",
                    "common_stock_repurchased": "int",
                    "dividends_paid": "int",
                    "other_financing_activites": "int",
                    "net_cash_used_provided_by_financing_activities": "int",
                    "effect_of_forex_changes_on_cash": "int",
                    "net_change_in_cash": "int",
                    "cash_at_end_of_period": "int",
                    "cash_at_beginning_of_period": "int",
                    "operating_cash_flow": "int",
                    "capital_expenditure": "int",
                    "free_cash_flow": "int",
                    "link": "str",
                    "final_link": "str",
                }
            )
        )

        return data_df.sort_values(by="date", ascending=True).reset_index(drop=True)

    ################################
    # Balance Sheet Statements
    ################################
    def balance_sheet_statements(
        self, symbol: str, period: str = "annual", limit: int = 20
    ) -> pd.DataFrame:
        """
        Retrieves the balance sheet statements for a given symbol.

        Args:
            symbol (str): The stock symbol.
            period (str, optional): The period of the statements. Defaults to "annual".
            limit (int, optional): The maximum number of statements to retrieve. Defaults to 20.

        Returns:
            pd.DataFrame: A DataFrame containing the balance sheet statements.

        Raises:
            ValueError: If no data is found for the provided symbol.
        """
        periods_allowed = ["annual", "quarter"]

        if period not in periods_allowed:
            raise ValueError(f"Invalid period. Allowed periods: {periods_allowed}")

        url = f"v3/balance-sheet-statement/{symbol}"
        params = {"period": period, "limit": limit}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the provided symbol.")

        data_df = (
            pd.DataFrame(response)
            .rename(
                columns={
                    "date": "date",
                    "symbol": "symbol",
                    "reportedCurrency": "reported_currency",
                    "cik": "cik",
                    "fillingDate": "filling_date",
                    "acceptedDate": "accepted_date",
                    "calendarYear": "calendar_year",
                    "period": "period",
                    "cashAndCashEquivalents": "cash_and_cash_equivalents",
                    "shortTermInvestments": "short_term_investments",
                    "cashAndShortTermInvestments": "cash_and_short_term_investments",
                    "netReceivables": "net_receivables",
                    "inventory": "inventory",
                    "otherCurrentAssets": "other_current_assets",
                    "totalCurrentAssets": "total_current_assets",
                    "propertyPlantEquipmentNet": "property_plant_equipment_net",
                    "goodwill": "goodwill",
                    "intangibleAssets": "intangible_assets",
                    "goodwillAndIntangibleAssets": "goodwill_and_intangible_assets",
                    "longTermInvestments": "long_term_investments",
                    "taxAssets": "tax_assets",
                    "otherNonCurrentAssets": "other_non_current_assets",
                    "totalNonCurrentAssets": "total_non_current_assets",
                    "otherAssets": "other_assets",
                    "totalAssets": "total_assets",
                    "accountPayables": "account_payables",
                    "shortTermDebt": "short_term_debt",
                    "taxPayables": "tax_payables",
                    "deferredRevenue": "deferred_revenue",
                    "otherCurrentLiabilities": "other_current_liabilities",
                    "totalCurrentLiabilities": "total_current_liabilities",
                    "longTermDebt": "long_term_debt",
                    "deferredRevenueNonCurrent": "deferred_revenue_non_current",
                    "deferredTaxLiabilitiesNonCurrent": "deferred_tax_liabilities_non_current",
                    "otherNonCurrentLiabilities": "other_non_current_liabilities",
                    "totalNonCurrentLiabilities": "total_non_current_liabilities",
                    "otherLiabilities": "other_liabilities",
                    "capitalLeaseObligations": "capital_lease_obligations",
                    "totalLiabilities": "total_liabilities",
                    "commonStock": "common_stock",
                    "retainedEarnings": "retained_earnings",
                    "accumulatedOtherComprehensiveIncomeLoss": "accumulated_other_comprehensive_income_loss",
                    "totalStockholdersEquity": "total_stockholders_equity",
                    "totalEquity": "total_equity",
                    "totalLiabilitiesAndStockholdersEquity": "total_liabilities_and_stockholders_equity",
                    "minorityInterest": "minority_interest",
                    "totalLiabilitiesAndTotalEquity": "total_liabilities_and_total_equity",
                    "totalInvestments": "total_investments",
                    "totalDebt": "total_debt",
                    "netDebt": "net_debt",
                    "link": "link",
                    "finalLink": "final_link",
                }
            )
            .astype(
                {
                    "date": "datetime64[ns]",
                    "symbol": "str",
                    "reported_currency": "str",
                    "cik": "str",
                    "filling_date": "datetime64[ns]",
                    "accepted_date": "datetime64[ns]",
                    "calendar_year": "int",
                    "period": "str",
                    "cash_and_cash_equivalents": "int",
                    "short_term_investments": "int",
                    "cash_and_short_term_investments": "int",
                    "net_receivables": "int",
                    "inventory": "int",
                    "other_current_assets": "int",
                    "total_current_assets": "int",
                    "property_plant_equipment_net": "int",
                    "goodwill": "int",
                    "intangible_assets": "int",
                    "goodwill_and_intangible_assets": "int",
                    "long_term_investments": "int",
                    "tax_assets": "int",
                    "other_non_current_assets": "int",
                    "total_non_current_assets": "int",
                    "other_assets": "int",
                    "total_assets": "int",
                    "account_payables": "int",
                    "short_term_debt": "int",
                    "tax_payables": "int",
                    "deferred_revenue": "int",
                    "other_current_liabilities": "int",
                    "total_current_liabilities": "int",
                    "long_term_debt": "int",
                    "deferred_revenue_non_current": "int",
                    "deferred_tax_liabilities_non_current": "int",
                    "other_non_current_liabilities": "int",
                    "total_non_current_liabilities": "int",
                    "other_liabilities": "int",
                    "capital_lease_obligations": "int",
                    "total_liabilities": "int",
                    "common_stock": "int",
                    "retained_earnings": "int",
                    "accumulated_other_comprehensive_income_loss": "int",
                    "total_stockholders_equity": "int",
                    "total_equity": "int",
                    "total_liabilities_and_stockholders_equity": "int",
                    "minority_interest": "int",
                    "total_liabilities_and_total_equity": "int",
                    "total_investments": "int",
                    "total_debt": "int",
                    "net_debt": "int",
                    "link": "str",
                    "final_link": "str",
                }
            )
        )
        return data_df.sort_values(by="date", ascending=True).reset_index(drop=True)

    ################################
    # Income Statements
    ################################
    def income_statements(
        self, symbol: str, period: str = "annual", limit: int = 20
    ) -> pd.DataFrame:
        """
        Retrieves the income statements for a given symbol.

        Args:
            symbol (str): The stock symbol.
            period (str, optional): The period of the income statements. Defaults to "annual".
            limit (int, optional): The maximum number of income statements to retrieve. Defaults to 20.

        Returns:
            pd.DataFrame: A DataFrame containing the income statements data.

        Raises:
            ValueError: If an invalid period is provided.
            ValueError: If no data is found for the specified parameters.
        """

        periods_allowed = ["annual", "quarter"]

        if period not in periods_allowed:
            raise ValueError(f"Invalid period. Allowed periods: {periods_allowed}")

        url = f"v3/income-statement/{symbol}"
        params = {"period": period, "limit": limit}
        response = self.get_request(url, params)

        if not response:
            raise ValueError("No data found for the specified parameters.")

        data_df = (
            pd.DataFrame(response)
            .rename(
                columns={
                    "symbol": "symbol",
                    "date": "date",
                    "reportedCurrency": "reported_currency",
                    "cik": "cik",
                    "fillingDate": "filling_date",
                    "acceptedDate": "accepted_date",
                    "calendarYear": "calendar_year",
                    "period": "period",
                    "revenue": "revenue",
                    "costOfRevenue": "cost_of_revenue",
                    "grossProfit": "gross_profit",
                    "grossProfitRatio": "gross_profit_ratio",
                    "researchAndDevelopmentExpenses": "research_and_development_expenses",
                    "generalAndAdministrativeExpenses": "general_and_administrative_expenses",
                    "sellingAndMarketingExpenses": "selling_and_marketing_expenses",
                    "sellingGeneralAndAdministrativeExpenses": "selling_general_and_administrative_expenses",
                    "otherExpenses": "other_expenses",
                    "operatingExpenses": "operating_expenses",
                    "costAndExpenses": "cost_and_expenses",
                    "interestExpense": "interest_expense",
                    "interestIncome": "interest_income",
                    "depreciationAndAmortization": "depreciation_and_amortization",
                    "ebitda": "ebitda",
                    "ebitdaratio": "ebitda_ratio",
                    "operatingIncome": "operating_income",
                    "operatingIncomeRatio": "operating_income_ratio",
                    "totalOtherIncomeExpensesNet": "total_other_income_expenses_net",
                    "incomeBeforeTax": "income_before_tax",
                    "incomeBeforeTaxRatio": "income_before_tax_ratio",
                    "incomeTaxExpense": "income_tax_expense",
                    "netIncome": "net_income",
                    "netIncomeRatio": "net_income_ratio",
                    "eps": "eps",
                    "epsdiluted": "epsdiluted",
                    "weightedAverageShsOut": "weighted_average_shs_out",
                    "weightedAverageShsOutDil": "weighted_average_shs_out_dil",
                    "link": "link",
                    "finalLink": "final_link",
                }
            )
            .astype(
                {
                    "symbol": "str",
                    "date": "datetime64[ns]",
                    "reported_currency": "str",
                    "cik": "str",
                    "filling_date": "datetime64[ns]",
                    "accepted_date": "datetime64[ns]",
                    "calendar_year": "int",
                    "period": "str",
                    "revenue": "int",
                    "cost_of_revenue": "int",
                    "gross_profit": "int",
                    "gross_profit_ratio": "float",
                    "research_and_development_expenses": "int",
                    "general_and_administrative_expenses": "int",
                    "selling_and_marketing_expenses": "int",
                    "selling_general_and_administrative_expenses": "int",
                    "other_expenses": "int",
                    "operating_expenses": "int",
                    "cost_and_expenses": "int",
                    "interest_expense": "int",
                    "interest_income": "int",
                    "depreciation_and_amortization": "int",
                    "ebitda": "int",
                    "ebitda_ratio": "float",
                    "operating_income": "int",
                    "operating_income_ratio": "float",
                    "total_other_income_expenses_net": "int",
                    "income_before_tax": "int",
                    "income_before_tax_ratio": "float",
                    "income_tax_expense": "int",
                    "net_income": "int",
                    "net_income_ratio": "float",
                    "eps": "float",
                    "epsdiluted": "float",
                    "weighted_average_shs_out": "int",
                    "weighted_average_shs_out_dil": "int",
                    "link": "str",
                    "final_link": "str",
                }
            )
        )

        return data_df.sort_values(by="date", ascending=True).reset_index(drop=True)
