# BUSINESS SCIENCE UNIVERSITY
# COURSE: DS4B 201-P PYTHON MACHINE LEARNING
# MODULE 8: FASTAPI 
# PART 1: BUILDING THE API
# ----

# To Run this App:
# - Open Terminal
# - uvicorn 08_fastapi.app_01_lead_scoring_pycaret_app:app --reload --port 8000
# - Navigate to localhost:8000
# - Navigate to localhost:8000/docs
# - Shutdown App: Ctrl/Cmd + C

# PACKAGES

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse

import json

import pandas as pd
import email_lead_scoring as els


app = FastAPI()

# DATA
leads_df = els.db_read_and_process_els_data()

# 0.0 INTRODUCE YOUR API

@app.get("/")
async def main():

    content = """
    <body>
    <h1>Welcome to the Email Lead Scoring Project</h1>
    <p> This API helps users score leads using our proprietary
    lead scoring models.</p>
    <p> Navigate to the <code>/docs</code> to see the API documentation.</p>
    </body>
    """
    return HTMLResponse(content = content)


# 1.0 GET: EXPOSE THE EMAIL SUBSCRIBER DATA AS AN ENDPOINT
@app.get("/get_email_subscribers")
async def get_email_subscribers():

    json = leads_df.to_json() 

    return JSONResponse(json)

# 2.0 POST: PASSING DATA TO AN API

@app.post("/data")
async def data(request: Request):

    request_body = await request.body()

    #print(request_body)

    data_json = json.loads(request_body)
    leads_df = pd.read_json(data_json)

    #print(leads_df)

    leads_json = leads_df.to_json()

    return JSONResponse(leads_json)

# 3.0 MAKING PREDICTIONS FROM AN API
@app.post("/predict")
async def predict(request: Request):

    # Handle incoming JSON request
    request_body = await request.body()

    data_json = json.loads(request_body)
    leads_df = pd.read_json(data_json)

    # Load model
    leads_scored_df = els.model_score_leads(
        data = leads_df,
        model_path = "models/xgb_model_tuned"
    )

    #print(leads_scored_df)


    # Convert to JSON
    scores = leads_scored_df[['Score']].to_dict()

    #print(scores)

    return JSONResponse(scores)

# 4.0 POST: MAKE LEAD SCORING STRATEGY




# DEFINE THE API PORT
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
