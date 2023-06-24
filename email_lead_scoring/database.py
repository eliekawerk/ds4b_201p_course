
# LIBRARIES ----

import pandas as pd
import sqlalchemy as sql


# IMPORT RAW DATA ----

# Read & Combine Raw Data

def db_read_els_data(conn_string =  "sqlite:///00_database/crm_database.sqlite"):
    """Function to read in the Subsribers, Tags and Transactions tables and combine them into a DataFrame
    with tag_count and made_purchase columns.

    Args:
        conn_string (str, optional): _description_. Defaults to "sqlite:///00_database/crm_database.sqlite".

    Returns:
        Pandas DataFrame
    """
    
    # Connect to Engine
    
    engine = sql.create_engine(conn_string)
    
    # Raw Data Collection
    with engine.connect() as conn:
        
        # Subscribers
        subscribers_df = pd.read_sql(
        sql = f"SELECT * FROM Subscribers",
        con =conn
        )
        
        subscribers_df['mailchimp_id'] = subscribers_df['mailchimp_id'].astype('int')

        subscribers_df['member_rating'] = subscribers_df['member_rating'].astype('int')

        subscribers_df['optin_time'] = subscribers_df['optin_time'].astype('datetime64')

        # Tags
        tags_df = pd.read_sql("SELECT * FROM Tags", conn)

        tags_df['mailchimp_id'] = tags_df['mailchimp_id'].astype('int')
        
        # MERGE TAG COUNTS
        user_events_df = tags_df\
            .groupby('mailchimp_id')\
            .agg(dict(tag = 'count'))\
            .set_axis(['tag_count'], axis = 1)\
            .reset_index()  
        
        subscribers_joined_df = subscribers_df\
            .merge(user_events_df, how ='left')\
            .fillna(dict(tag_count = 0)) 
        
        subscribers_joined_df['tag_count'] = subscribers_joined_df['tag_count'].astype('int')        
        # Transactions
        transactions_df = pd.read_sql("SELECT * FROM Transactions", conn)
        transactions_df['purchased_at'] = transactions_df['purchased_at'].astype('datetime64')
        transactions_df['product_id'] = transactions_df['product_id'].astype('int')
        
        # MERGE TARGET VARIABLE
        emails_made_purchase = transactions_df['user_email'].unique()

        subscribers_joined_df['made_purchase'] = subscribers_joined_df['user_email']\
            .isin(emails_made_purchase)\
            .astype('int')    
        
        
        
    return subscribers_joined_df

# Read Table Names

def db_read_els_table_names(conn_string = "sqlite:///00_database/crm_database.sqlite"):
    """Reads the Table Names for each table in CRM database.

    Args:
        conn_string (str, optional): _description_. Defaults to "sqlite:///00_database/crm_database.sqlite".

    Returns:
        List with names of tables.
    """
    engine = sql.create_engine(conn_string)
    inspect = sql.inspect(engine)
    table_names = inspect.get_table_names()

    return table_names


# Get Raw Table

def db_read_raw_ets_table(table ="Products", conn_string = "sqlite:///00_database/crm_database.sqlite"):
    """Reads a single raw table from the CRM database

    Args:
        table (str, optional): _Table Name. Defaults to "Products". 
        See db_read_els_table_names() to get full list of table names.
        conn_string (str, optional): _description_. Defaults to "sqlite:///00_database/crm_database.sqlite".

    Returns:
        Pandas DataFrame
    """
    engine = sql.create_engine(conn_string)
    with engine.connect() as conn:

        table_df = pd.read_sql(
        sql = f"SELECT * FROM {table}",
        con = conn
        )
    
    return table_df