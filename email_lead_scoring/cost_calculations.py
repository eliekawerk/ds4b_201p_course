
import pandas as pd
import numpy as np
import janitor as jn
import plotly.express as px

def cost_calc_monthly_cost_table(
    email_list_size            = 1e5,
    email_list_growth_rate     = 0.035,
    sales_emails_per_month     = 5,
    unsub_rate_per_sales_email = 0.005,
    customer_conversion_rate   = 0.05,
    average_customer_value     = 2000,
    n_periods                  = 12
):
    """ This function generates a cost table.

    Args:
        email_list_size (_type_, optional): Email list size. Defaults to 1e5.
        email_list_growth_rate (float, optional): Monthly Email list growth rate. Defaults to 0.035.
        sales_emails_per_month (int, optional): Sales emails per month. Defaults to 5.
        unsub_rate_per_sales_email (float, optional): Unsubscription Rate per Email. Defaults to 0.005.
        customer_conversion_rate (float, optional):Rate of email subscribers that convert to ciustomers. Defaults to 0.05.
        average_customer_value (int, optional): Average customer value. Defaults to 2000.
        n_periods (int, optional): Number of months for our cost table. Defaults to 12.

    Returns:
        DataFrame: Returns a Cost Table.
    """
    # Period
    period_series = pd.Series(np.arange(0, n_periods), name = "period")

    cost_table_df = period_series.to_frame()
    
    # Email Size - No Growth
    
    cost_table_df['email_size_no_growth'] = np.repeat(email_list_size, n_periods)
    
    # Lost Customers - No Growth
    
    cost_table_df['lost_customers_no_growth'] = cost_table_df['email_size_no_growth'] * unsub_rate_per_sales_email * sales_emails_per_month
    
    # Lost Revenue - No Growth
    
    cost_table_df['cost_no_growth'] = cost_table_df['lost_customers_no_growth'] * customer_conversion_rate * average_customer_value
    
    # Email Size - With Growth
    
    cost_table_df['email_size_with_growth'] = cost_table_df['email_size_no_growth'] * (1 + email_list_growth_rate)**cost_table_df['period']
    
    # Lost Customers - With Growth
    
    cost_table_df['lost_customers_with_growth'] = cost_table_df['email_size_with_growth'] * unsub_rate_per_sales_email * sales_emails_per_month     
    
    # Cost - With Growth
    
    cost_table_df['cost_with_growth'] = cost_table_df['lost_customers_with_growth'] *  customer_conversion_rate * average_customer_value

    
    return cost_table_df

def cost_total_unsub_cost(cost_table):
    """ Takes the input from cost_calc_monthly_cost_table(),
    and produces a summary of the total costs.

    Args:
        cost_table (Dataframe):Output from 
        cost_calc_monthly_cost_table()

    Returns:
        Dataframe: summarized total costs from rmail unsubscription 
    """
    
    summary_df = cost_table[['cost_no_growth', 'cost_with_growth']]\
    .sum()\
    .to_frame()\
    .transpose()  
    
    return summary_df