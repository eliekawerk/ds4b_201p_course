import pandas as pd
import pycaret.classification as clf

# MODEL LOAD FUNCTION ----

def model_score_leads(
    data,
    model_path = "models/blended_models_final"
):
    mod = clf.load_model(model_path)
    predictions_df = clf.predict_model(
        estimator = mod,
        data      = data,
        raw_score = True
    )
    return predictions_df 