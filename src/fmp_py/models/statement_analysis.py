from dataclasses import dataclass


@dataclass
class FinancialScore:
    symbol: str
    altman_z_score: float
    piotroski_score: int
    working_capital: int
    total_assets: int
    retained_earnings: int
    ebit: int
    market_cap: int
    total_liabilities: int
    revenue: int


@dataclass
class Ratios:
    dividend_yield_ttm: float
    dividend_yield_percentage_ttm: float
    pe_ratio_ttm: float
    peg_ratio_ttm: float
    payout_ratio_ttm: float
    current_ratio_ttm: float
    quick_ratio_ttm: float
    cash_ratio_ttm: float
    days_of_sales_outstanding_ttm: float
    days_of_inventory_outstanding_ttm: float
    operating_cycle_ttm: float
    days_of_payables_outstanding_ttm: float
    cash_conversion_cycle_ttm: float
    gross_profit_margin_ttm: float
    operating_profit_margin_ttm: float
    pretax_profit_margin_ttm: float
    net_profit_margin_ttm: float
    effective_tax_rate_ttm: float
    return_on_assets_ttm: float
    return_on_equity_ttm: float
    return_on_capital_employed_ttm: float
    net_income_per_ebt_ttm: float
    ebt_per_ebit_ttm: float
    ebit_per_revenue_ttm: float
    debt_ratio_ttm: float
    debt_equity_ratio_ttm: float
    longterm_debt_to_capitalization_ttm: float
    total_debt_to_capitalization_ttm: float
    interest_coverage_ttm: float
    cash_flow_to_debt_ratio_ttm: float
    company_equity_multiplier_ttm: float
    receivables_turnover_ttm: float
    payables_turnover_ttm: float
    inventory_turnover_ttm: float
    fixed_asset_turnover_ttm: float
    asset_turnover_ttm: float
    operating_cash_flow_per_share_ttm: float
    cash_per_share_ttm: float
    operating_cash_flow_sales_ratio_ttm: float
    free_cash_flow_operating_cash_flow_ratio_ttm: float
    free_cash_flow_per_share_ttm: float
    cash_flow_coverage_ratios_ttm: float
    short_term_coverage_ratios_ttm: float
    capital_expenditure_coverage_ratio_ttm: float
    dividend_paid_and_capex_coverage_ratio_ttm: float
    price_book_value_ratio_ttm: float
    price_to_book_ratio_ttm: float
    price_to_sales_ratio_ttm: float
    price_earnings_ratio_ttm: float
    price_to_free_cash_flows_ratio_ttm: float
    price_to_operating_cash_flows_ratio_ttm: float
    price_cash_flow_ratio_ttm: float
    price_earnings_to_growth_ratio_ttm: float
    price_sales_ratio_ttm: float
    enterprise_value_multiple_ttm: float
    price_fair_value_ttm: float
    dividend_per_share_ttm: float


@dataclass
class KeyMetrics:
    revenue_per_share_ttm: float
    net_income_per_share_ttm: float
    operating_cash_flow_per_share_ttm: float
    free_cash_flow_per_share_ttm: float
    cash_per_share_ttm: float
    book_value_per_share_ttm: float
    tangible_book_value_per_share_ttm: float
    shareholders_equity_per_share_ttm: float
    interest_debt_per_share_ttm: float
    market_cap_ttm: int
    enterprise_value_ttm: float
    pe_ratio_ttm: float
    price_to_sales_ratio_ttm: float
    pocf_ratio_ttm: float
    pfcf_ratio_ttm: float
    pb_ratio_ttm: float
    ptb_ratio_ttm: float
    ev_to_sales_ttm: float
    enterprise_value_over_ebitda_ttm: float
    debt_to_market_cap_ttm: float
    ev_to_operating_cash_flow_ttm: float
    dividend_per_share_ttm: float
    ev_to_free_cash_flow_ttm: float
    earnings_yield_ttm: float
    free_cash_flow_yield_ttm: float
    debt_to_equity_ttm: float
    debt_to_assets_ttm: float
    net_debt_to_ebitda_ttm: float
    graham_net_net_ttm: float
    return_on_tangible_assets_ttm: float
    current_ratio_ttm: float
    interest_coverage_ttm: float
    income_quality_ttm: float
    dividend_yield_ttm: float
    dividend_yield_percentage_ttm: float
    payout_ratio_ttm: float
    sales_general_and_administrative_to_revenue_ttm: float
    research_and_developement_to_revenue_ttm: float
    intangibles_to_total_assets_ttm: float
    capex_to_operating_cash_flow_ttm: float
    capex_to_revenue_ttm: float
    capex_to_depreciation_ttm: float
    stock_based_compensation_to_revenue_ttm: float
    graham_number_ttm: float
    roic_ttm: float
    working_capital_ttm: float
    tangible_asset_value_ttm: float
    net_current_asset_value_ttm: float
    invested_capital_ttm: float
    average_receivables_ttm: int
    average_payables_ttm: int
    average_inventory_ttm: int
    days_sales_outstanding_ttm: float
    days_payables_outstanding_ttm: float
    days_of_inventory_on_hand_ttm: float
    receivables_turnover_ttm: float
    payables_turnover_ttm: float
    inventory_turnover_ttm: float
    capex_per_share_ttm: float
    roe_ttm: float
