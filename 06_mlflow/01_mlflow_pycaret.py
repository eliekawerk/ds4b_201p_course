# BUSINESS SCIENCE UNIVERSITY
# COURSE: DS4B 201-P PYTHON MACHINE LEARNING
# MODULE 6: MLFLOW 
# PART 1: PYCARET INTEGRATION
# ----

# Core
import pandas as pd
import numpy as np
# Machine Learning
import pycaret.classification as clf
# MLFlow Models
import mlflow
# Lead Scoring
import email_lead_scoring as els

# RECAP 

leads_tags_df = els.db_read_and_process_els_data()

# 1.0 PYCARET'S MLFLOW INTEGRATION ----

# When we setup pycaret, we setup logging experiments with MLFlow

# Job & Experiment Logging: clf.setup()
    # n_jobs = -1,
    # session_id = 123,
    # log_experiment=True,
    # experiment_name = 'email_lead_scoring_1'


# 2.0 MLFLOW UI ----

# !mlflow ui
# http://localhost:5000/

# 1. GUI OVERVIEW: HOW TO FIND THE MODELS YOU'RE LOOKING FOR
# 2. SORTING: AUC 
# 3. SEARCHING: tags.Source = 'finalize_model'
# 4. DRILLING INTO MODELS


# 3.0 MLFLOW TRACKING & EXPERIMENT INTERFACE ----


# 3.1 TRACKING URI (FOLDER WHERE YOUR EXPERIMENTS & RUNS ARE STORED) ----



# 3.2 WORKING WITH EXPERIMENTS (GROUP OF RUNS) ----

# Listing Experiments


# Programmatically Working With Experiments


# 3.3 SEARCHING WITH THE EXPERIMENT NAME ----



# pycaret interface to get experiments





# 4.0 WORKING WITH RUNS ----

# Finding Runs in Experiments


# Finding Runs from Run ID



# 5.0 MAKING PREDICTIONS ----

# Using the mlflow model 



# Issue - Mlflow does not give probability. We need probabilities for lead scoring.

# Solution 1 - Extract out the sklearn model and use the 
#   sklearn .predict_proba() method



# Solution 2 - Predict with Pycaret's prediction function in production




# CONCLUSIONS ----
# 1. Pycaret simplifies the logging process for mlflow
# 2. Pycaret includes a lot of detail (saved metrics) by default
# 3. We haven't actually logged anything of our own 
# 4. Let's explore MLFlow deeper with H2O (We can actually use this process for Scikit Learn too!)
