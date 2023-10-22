# BUSINESS SCIENCE UNIVERSITY
# COURSE: DS4B 201-P PYTHON MACHINE LEARNING
# MODULE 8: FASTAPI 
# PART 2: TESTING SECURITY API KEY
# ----


# [INSERT THE APP 01 API TESTING CODE IN HERE]

# LIBRARIES
import pandas as pd
import requests
import email_lead_scoring as els
API_KEY_NAME = "X-API-KEY"
API_KEY = "my-secret-api-key"

HEADERS = { API_KEY_NAME:API_KEY}

# Converting to JSON
full_data = els.db_read_and_process_els_data()

full_data_json = full_data.to_json()

sample_data = els.db_read_and_process_els_data().head()

sample_data_json = sample_data.to_json()


# 1.0 GET: EXPOSE DATA FROM AN ENDPOINT
res = requests.get(
    "http://127.0.0.1:8000/get_email_subscribers",
    headers = HEADERS
)

res.json()

pd.read_json(res.json())

# 2.0 POST: PASS DATA TO AN API

res = requests.post(
     "http://127.0.0.1:8000/data",
     json   = sample_data_json,
     headers = HEADERS
)

res.json()

pd.read_json(res.json())

# 3.0 POST: PASS DATA AND MAKE PREDICTIONS


res = requests.post(
     "http://127.0.0.1:8000/predict",
     json    = full_data_json,
     headers = HEADERS
)

res.json()

pd.DataFrame(res.json())


# 4.0 POST: PASS DATA AND PARAMETERS
#   TO CALCULATE LEAD STRATEGY FOR MARKETING

res = requests.post(
     "http://127.0.0.1:8000/calculate_lead_strategy",
     json   = full_data_json,
     params = dict(
         monthly_sales_reduction_safeguard=0.9,
         for_marketing_team=True,
         email_list_size=200000.0,
         unsub_rate_per_sales_email=0.005,
         sales_emails_per_month=5,
         avg_sales_per_month=250000,
         avg_sales_emails_per_month=5,
         customer_conversion_rate=0.05,
         avg_customer_value=2000
     ),
     headers = HEADERS
)

res.json().keys()

pd.read_json(res.json()['lead_strategy'])
pd.read_json(res.json()['expected_value'])
pd.read_json(res.json()['thresh_optim_table'])
pd.read_json(res.json()['thresh_optim_table']).style.highlight_max()

els.lead_plot_optim_thresh(
    pd.read_json(res.json()['thresh_optim_table'])
)
