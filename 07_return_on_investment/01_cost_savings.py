# BUSINESS SCIENCE UNIVERSITY
# COURSE: DS4B 201-P PYTHON MACHINE LEARNING
# MODULE 7: ROI
# PART 1: COST VS SAVINGS TRADEOFF & ESTIMATE
# ----

# LIBRARIES -----

import pandas as pd
import numpy as np
import email_lead_scoring as els

# RECAP ----

leads_df = els.db_read_and_process_els_data()

leads_scored_df = els.model_score_leads(
    data = leads_df,
    model_path = "models/xgb_model_tuned"
)

# Optional (MLFlow)
leads_scored_df_2 = els.mlflow_score_leads(
    data=leads_df, 
    run_id = els.mlflow_get_best_run('automl_lead_scoring_1')
)

# REVIEW COSTS ----

els.cost_calc_monthly_cost_table()

els.cost_simulate_unsub_costs()

# 1.0 LEAD TARGETING STRATEGY ----

# 1.1 Make Lead Strategy

leads_scored_small_df =leads_scored_df[['user_email', 'Score', 'made_purchase']]

leads_ranked_df = leads_scored_small_df\
    .sort_values('Score', ascending = False)\
    .assign(rank = lambda x: np.arange(0, len(x['made_purchase'])) + 1)\
    .assign(gain = lambda x: np.cumsum(x['made_purchase'])/ np.sum(x['made_purchase']))

leads_ranked_df

# Threshold Selection

thresh = 0.95

strategy_df = leads_ranked_df \
    .assign(category = lambda x: np.where(x['gain'] <= thresh, "Hot-Lead", "Cold-Lead"))

strategy_for_marketing_df = leads_scored_df \
    .merge(
        right       = strategy_df[['category']],
        how         = 'left',
        left_index  = True,
        right_index = True
    )

strategy_for_marketing_df

# 1.2 Aggregate Results

results_df = strategy_df\
.groupby('category')\
.agg(
    count             = ('made_purchase', 'count'),
    sum_made_purchase = ('made_purchase', 'sum')
)

results_df

# 2.0 CONFUSION MATRIX ANALYSIS ----

email_list_size = 1e5
unsub_rate_per_sales_email = 0.005
sales_emails_per_month = 5

avg_sales_per_month = 250000
avg_sales_emails_per_month = 5

customer_conversion_rate = 0.05
avg_customer_value = 2000

sample_factor = 5

# 2.1 Confusion Matrix Calculations ----


# 2.2 Confusion Matrix Summaries ----


# 3.0 PRELIMINARY EXPECTED VALUE CALCULATIONS

# 3.1 [Savings] Cold That Are Not Targeted



# 3.2 [Cost] Missed Sales That Are Not Targeted



# 3.3 [Cost] Hot Leads Targeted That Unsubscribe

    
    
# 3.4 [Savings] Sales Achieved



# 4.0 FINAL EXPECTED VALUE TO REPORT TO MANAGEMENT

# 4.1 Expected Monthly Sales (Realized)


# 4.2 Expected Monthly Value (Unrealized because of delayed nuture effect)


# 4.3 Expected Monthly Savings (Unrealized until nurture takes effect)


# 4.4 Expected Saved Customers (Unrealized until nuture takes effect)


# 4.5 EXPECTED VALUE SUMMARY OUTPUT





# CONCLUSIONS -----
# - Can save a lot of money with this strategy
# - But there is a tradeoff with the threshold selected
# - Need to somehow optimize for threshold



