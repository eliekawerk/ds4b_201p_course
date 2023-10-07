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



# 1.0 GET: EXPOSE THE EMAIL SUBSCRIBER DATA AS AN ENDPOINT

    
    
# 2.0 POST: PASSING DATA TO AN API




# 3.0 MAKING PREDICTIONS FROM AN API




# 4.0 POST: MAKE LEAD SCORING STRATEGY




# DEFINE THE API PORT
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
