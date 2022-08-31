
import pandas as pd
from constants import (FILE_NAME,CAUSES_NAMES,AGREGATE_COLS_NAMES,ID_VARS,DB_NAME)
import sqlite3

def populate_tables():
    #Load Data and Drop Duplicates
    raw_data = pd.read_csv(FILE_NAME,sep=',').drop_duplicates()

    #Rename  Juirisdiction Columun
    raw_data=raw_data.rename(columns={"Jurisdiction of Occurrence": "jurisdiction_name"})

    #Unpivot Causes columns
    raw_jurisdictiondeathcause = pd.melt(
        raw_data
        ,id_vars=ID_VARS, value_vars=CAUSES_NAMES
        ,value_name='total'
        ,var_name='cause_name')

    #Create dataframes for causes and jurisdiction using index as id from raw_jurisdictiondeathcause 
    df_jurrisdiction = raw_jurisdictiondeathcause['jurisdiction_name'].drop_duplicates().reset_index()
    df_causes= raw_jurisdictiondeathcause['cause_name'].drop_duplicates().reset_index()
    df_jurrisdiction['jurisdiction_id'] = df_jurrisdiction.index
    df_causes['deathcause_id'] = df_causes.index

    #Merge raw_jurisdictiondeathcause with created dataframes to create normalized dataframe
    merged_jurisdictiondeathcause = pd.merge(
        pd.merge(raw_jurisdictiondeathcause,df_jurrisdiction ,on='jurisdiction_name',how='left')
        ,df_causes
        ,on='cause_name'
        ,how='left')

    #Drop Extra Columns
    merged_jurisdictiondeathcause.drop(
        columns=['jurisdiction_name','cause_name','index_x','index_y']
        ,inplace=True
        )
    #Create index
    merged_jurisdictiondeathcause['id']=merged_jurisdictiondeathcause.index

    # Insert into Tables Into SQL
    conn = sqlite3.connect(DB_NAME)
    df_causes[['cause_name', 'deathcause_id']].to_sql(
        'deathcause', conn, if_exists='append', index=False)

    df_jurrisdiction[['jurisdiction_name','jurisdiction_id']].to_sql(
        'jurisdiction',conn, if_exists='append', index=False)
    
    merged_jurisdictiondeathcause.to_sql(
        'jurisdictiondeathcause', conn, if_exists='append', index=False)
    
    conn.close()

populate_tables()