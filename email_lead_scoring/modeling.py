import pandas as pd
import numpy as np
import pycaret.classification as clf

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