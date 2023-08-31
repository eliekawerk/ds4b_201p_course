# BUSINESS SCIENCE UNIVERSITY
# COURSE: DS4B 201-P PYTHON MACHINE LEARNING
# MODULE 7: ROI  
# PART 2: THRESHOLD OPTIMIZATION & PROFIT MAXIMIZATION
# ----

# LIBRARIES -----

import pandas as pd
import numpy as np
import plotly.express as px
import email_lead_scoring as els

# RECAP ----

leads_df = els.db_read_and_process_els_data()

leads_scored_df = els.model_score_leads(leads_df)


# 1.0 MAKE THE LEAD STRATEGY FROM THE SCORED SUBSCRIBERS:
#   lead_make_strategy()

def lead_make_strategy(leads_scored_ef, thresh = 0.99, for_marketing_team = False, verbose = False):
    
    # Ranking the leads
    leads_scored_small_df = leads_scored_df[['user_email', 'Score', 'made_purchase']]

    leads_ranked_df = leads_scored_small_df\
    .sort_values('Score', ascending = False)\
    .assign(rank = lambda x: np.arange(0, len(x['made_purchase'])) + 1)\
    .assign(gain = lambda x: np.cumsum(x['made_purchase'])/ np.sum(x['made_purchase']))

    # Make the Strategy
    strategy_df = leads_ranked_df \
        .assign(category = lambda x: np.where(x['gain'] <= thresh, "Hot-Lead", "Cold-Lead"))

    if for_marketing_team:
        strategy_for_marketing_df = leads_scored_df \
            .merge(
                right       = strategy_df[['category']],
                how         = 'left',
                left_index  = True,
                right_index = True
            )
    if verbose:
        print("Strategy created")


    return strategy_df

# Workflow

lead_make_strategy(
    leads_scored_df,
    thresh             = 0.90,
    for_marketing_team = False
)

# 2.0 AGGREGATE THE LEAD STRATEGY RESULTS
#  lead_aggregate_strategy_results()


# Workflow


    
# 3.0 CALCULATE EXPECTED VALUE (FOR ONE SET OF INPUTS) ----
#  lead_strategy_calc_expected_value()



# Workflow:



# 4.0 OPTIMIZE THE THRESHOLD AND GENERATE A TABLE
#  lead_strategy_create_thresh_table()



# Workflow:



# 5.0 SELECT THE BEST THRESHOLD
#  def lead_select_optimum_thresh()



# Workflow



# 6.0 GET EXPECTED VALUE RESULTS ----
#  def lead_get_expected_value()




# 7.0 PLOT THE OPTIMAL THRESHOLD ----
#  def lead_plot_optim_thresh()



# Workflow



# 8.0 MAKE THE OPTIMAL STRATEGY ----



# FINAL OPTIMIZATION RESULTS ----
# - Use one function to perform the automation and collect the results
#   def lead_score_strategy_optimization()



# Workflow



# CONCLUSIONS ----

# Business Leaders may freak out if they see a big hit in sales
#  even though it could be beneficial in long term
# Recommend to start with a smaller strategy of focusing on 
#  top 95% 
# We can set this up with the Threshold Override

