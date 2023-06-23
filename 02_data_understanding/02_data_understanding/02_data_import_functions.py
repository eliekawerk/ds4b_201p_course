# BUSINESS SCIENCE UNIVERSITY
# COURSE: DS4B 201-P PYTHON MACHINE LEARNING
# MODULE 2: DATA UNDERSTANDING
# PART 2: DATA IMPORT FUNCTIONS
# ----

# LIBRARIES ----

import pandas as pd
import numpy as np
import sqlalchemy as sql


# IMPORT RAW DATA ----

# Read & Combine Raw Data

def db_read_els_data(conn_string =  "sqlite:///00_database/crm_database.sqlite"):
    
    # Connect to Engine
    
    engine = sql.create_engine(conn_string)
    
    # Raw Data Collection
    with engine.connect() as conn:
        
        # Subscribers
        
        # Tags
        
        # Transactions
    
    
    # Read Table Names



    # Get Raw Table





    # TEST IT OUT -----



