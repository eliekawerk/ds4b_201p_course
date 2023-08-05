import pandas as pd
import numpy as np
import pycaret.classification as clf
import mlflow

# MODEL LOAD FUNCTION ----

def model_score_leads(
    data,
    model_path = "models/blended_models_final"
    ):
    """ PyCaret Model Lead Scoring Function

    Args:
        data (DataFrame): Leads data from els.
        db_read_and_process_els_data().
        model_path (str, optional): _description_.A model stored in the models/ directory.
        Defaults to "models/blended_models_final".

    Returns:
        DataFrame: Leads Data with a column "Score" added.
    """
    mod = clf.load_model(model_path)
    predictions_df = clf.predict_model(
        estimator = mod,
        data      = data
    )
    
    df = predictions_df 
    
    predictions_df['Score'] = np.where(df['Label']==0, 1-df['Score'], df['Score'])
    
    leads_scored_df = pd.concat(
        [predictions_df['Score'], data],
        axis = 1
    )
    
    return leads_scored_df


def mlflow_get_best_run(
        experiment_name, n= 1,
        metric = 'metrics.AUC', ascending = False,
        tag_source = ['finalize_model','h2o_automl_model']
):
    """ Return the beast run from an MLFlow Experiment Name

    Args:
        experiment_name (str): An MLFlow Experiment Name
        
        n (int,optional):the number to return. Defaults to 1.
        
        metric(str, optional): MLFlow metric to use. Defaults  to 'metrics.AUC'
        
        ascending(bool, optional): Whetheror not to sort the metric ascending or descending.
         Metrics like log loss should be ascending. AUC should be descending. Defaults to False.
        
        tag_source(list, optional): Tag. Source in MLFlow to use in production. Defaults to 
        ['finalize_model','h2o_automl_model']

    Returns:
        _string: The best run id found.
    """
    experiment = mlflow.get_experiment_by_name(experiment_name)
    experiment_id = experiment.experiment_id

    logs_df = mlflow.search_runs(experiment_id)

    best_run_id = logs_df.query(f"`tags.Source` in {tag_source}")\
    .sort_values(metric, ascending = False)\
    ['run_id']\
    .values[n-1]
    
    return best_run_id


def mlflow_score_leads(data, run_id):
    """ This function scores the leads using an MLFlow run id to select the model

    Args:
        data (DataFrame): leads data from els.db_read_and_process_els_data()
        run_id (string): An MLFlow run id from best run. Recommended to use mlflow_get_best_run()

    Returns:
        DataFrame: A DataFrame with the leads score column added.
    """
    logged_model = f'runs:/{run_id}/model'
    
    print(logged_model)

    loaded_model = loaded_model = mlflow.pyfunc.load_model(logged_model)

    # Predict
    try:
        predictions_array = loaded_model.predict(pd.DataFrame(data))['p1']

    except:
        predictions_array = loaded_model._model_impl.predict_proba(data)[:,1]    



    predictions_series = pd.Series(predictions_array, name = "Score")

    ret = pd.concat([predictions_series, data], axis = 1 )

    return ret
