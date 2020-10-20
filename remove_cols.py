import pandas as pd

us_daily = pd.read_csv("us_daily_ds2.csv")
cols_to_dispose = ["index", "open_covid_region_code", "region_name", "cases_cumulative", "cases_new", "cases_cumulative_per_million", "deaths_cumulative", "deaths_new", "deaths_cumulative_per_million", "tests_new", "tests_cumulative","tests_cumulative_per_thousand", "test_units", "school_closing", "school_closing_flag","workplace_closing", "workplace_closing_flag", "cancel_public_events_flag", "restrictions_on_gatherings", "restrictions_on_gatherings_flag", "close_public_transit","close_public_transit_flag", "stay_at_home_requirements", "stay_at_home_requirements_flag","restrictions_on_internal_movement", "restrictions_on_internal_movement_flag", "international_travel_controls", "income_support", "income_support_flag", "debt_contract_relief", "fiscal_measures", "international_support", "public_information_campaigns", "public_information_campaigns_flag","testing_policy", "contact_tracing", "emergency_investment_in_healthcare",  "investment_in_vaccines","confirmed_cases", "confirmed_deaths", "stringency_index_for_display", "stringency_legacy_index","stringency_legacy_index_for_display","government_response_index_for_display","containment_health_index_for_display", "economic_support_index_for_display" ]
print(us_daily)
# us_daily.drop(cols_to_dispose, axis=1)
for col in cols_to_dispose :
    if col in us_daily : 
        del us_daily[col]
us_daily.drop(us_daily.filter(regex="Unname"),axis=1, inplace=True)
us_daily.to_csv("us_daily_cropped_ds2_1.csv", index=None)