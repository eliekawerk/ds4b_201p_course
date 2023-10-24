# BUSINESS SCIENCE UNIVERSITY
# COURSE: DS4B 201-P PYTHON MACHINE LEARNING
# MODULE 9: STREAMLIT 
# STREAMLIT JUMPSTART
# ----

# To run app (put this in Terminal):
#   streamlit run 00_jumpstart/03_streamlit_jumpstart.py


# Import required libraries
import streamlit as st
import pandas as pd
import plotly.express as px


a= 2
# 1.0 Title and Introduction

st.title("Business Dashboard")
st.write("""
This dashboard provides insights into sales, customer demographics
and product performance. Upload your data to get started. 
""")
# 2.0 Data Input
st.header("upload Business Daata")

uploaded_file = st.file_uploader("Choose a CSV file",
                                 type = "csv", accept_multiple_files = False)

# 3.0 App Body 
#  What Happens Once Data Is Loaded?

# * Sales insights


# * Customer Segmentation by Region


# * Product Analysis


# * Feedback Form


# 4.0 Footer



if __name__ == "__main__":
    pass