# BUSINESS SCIENCE UNIVERSITY
# COURSE: DS4B 201-P PYTHON MACHINE LEARNING
# MODULE 9: STREAMLIT 
# FRONTEND USER STREAMLIT APP FOR API - NO SECURITY
# ----

# To run app (put this in Terminal):
#   streamlit run 09_streamlit/01_app_streamlit.py

import streamlit as st
import requests
import pandas as pd

import sys
import pathlib

# NEEDED FOR EMAIL LEAD SCORING TO BE DETECTED
# APPEND PROJECT DIRECTORY TO PYTHONPATH
working_dir = str(pathlib.Path().absolute())
print(working_dir)
sys.path.append(working_dir)

import email_lead_scoring as els

ENDPOINT = 'http://localhost:8000'

# 1.0 TITLE

st.title("Email Lead Scoring Streamlit FrontEnd Application")

# 2.0 DATA INPUT
#   CACHING DATA - NEEDED TO PREVENT REQUIRING DATA TO BE RE-INPUT

uploaded_file = st.file_uploader(
    "Upload Email Subscribers File",
    type                  = ['csv'],
    accept_multiple_files = False
)

@st.cache_data()
def load_data(filename):
    leads_df = pd.read_csv(filename)
    return leads_df

# 3.0 APP BODY

if uploaded_file:

    leads_df = load_data(uploaded_file)
    full_data_json = leads_df.to_json()
    
    # Checkbox - Show Table 
    if st.checkbox("Show Raw Data"):
        st.subheader("Sample of Raw Data (First 10 Rows)")
        st.write(leads_df.head(10))
    

    st.write("---")
    st.markdown("# Lead Scoring Analysis")
    
    # User Inputs - Add Sliders / Buttons
    estimated_monthly_sales = st.number_input(
        "How much in email sales per month ($ on average)", 0, value = 250000, step =1000 )
    monthly_sales_reduction_safe_guard = st.slider(
        "How much of monthly sales should be mantained (%) ?", 0., 1., 0.9, step = 0.1
    )
    
    #print(monthly_sales_reduction_safe_guard)

    sales_limit = "$(:,.0f)".format
    (monthly_sales_reduction_safe_guard * estimated_monthly_sales)

    st.subheader(f"Monthly sales will not go below: {sales_limit}")
    
    
    # Run Analysis 
    
        # Spinner
        
            
            # Make Request
            
            
            
            # Collect JSON / Convert Data
            
            
            
            # Display Results
            
            
            # Display Strategy Summary
            
            
            # Display Expected Value Plot
            
            
            
            # Display Sample Lead Strategy
            
            
            # Download button - Get lead scoring results
            
        
    
