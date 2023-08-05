# BUSINESS SCIENCE UNIVERSITY
# COURSE: DS4B 201-P PYTHON MACHINE LEARNING
# MODULE 6: MLFLOW 
# PART 3: PREDICTION FUNCTION 
# ----

import pandas as pd
import mlflow
import email_lead_scoring as els

leads_df = els.db_read_and_process_els_data()



# 1.0 GETTING THE BEST RUN FOR PRODUCTION ----

EXPERIMENT_NAME = 'email_lead_scoring_0'

EXPERIMENT_NAME = 'automl_lead_scoring_1'

experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)

experiment_id = experiment.experiment_id

logs_df = mlflow.search_runs(experiment_id)

logs_df.head()

logs_df.query("`tags.Source` in ['finalize_model','h2o_automl_model']")\
.sort_values('metrics.AUC', ascending = False)\
['run_id']\
.values[0]

# Function

def mlflow_get_best_run(
        experiment_name, n= 1,
        metric = 'metrics.AUC', ascending = False,
        tag_source = ['finalize_model','h2o_automl_model']
):
    experiment = mlflow.get_experiment_by_name(experiment_name)
    experiment_id = experiment.experiment_id

    logs_df = mlflow.search_runs(experiment_id)

    best_run_id = logs_df.query("`tags.Source` in ['finalize_model','h2o_automl_model']")\
    .sort_values('metrics.auc', ascending = False)\
    ['run_id']\
    .values[0]
    
    return best_run_id


mlflow_get_best_run('automl_lead_scoring_1')
mlflow_get_best_run('email_lead_scoring_0')

# 2.0 PREDICT WITH THE MODEL (LEAD SCORING FUNCTION)

# Load model as a PyFuncModel.

# H2O
import h2o
h2o.init()
run_id = mlflow_get_best_run('automl_lead_scoring_1')

#logged_model = f'runs:/{run_id}/model'

logged_model = f'C:/Users/daver/OneDrive/DESKTOP/DS4B_201P/ds4b_201p_course/mlruns/2/{run_id}/artifacts/model'

loaded_model = mlflow.pyfunc.load_model(logged_model)
loaded_model.predict(leads_df)['p1']

# Sklearn / Pycaret (Extract)
run_id = mlflow_get_best_run('email_lead_scoring_0')
#logged_model = f'runs:/{run_id}/model'
loaded_model = mlflow.pyfunc.load_model(logged_model)

loaded_model._model_impl.predict_proba(leads_tags_df)[:,1]
# Function



# 3.0 TEST WORKFLOW ----


