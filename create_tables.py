import sqlite3
from constants import DB_NAME
create_jurisdiction_string = """ 
CREATE TABLE jurisdiction(
    jurisdiction_id  INTEGER PRIMARY KEY,
    jurisdiction_name TEXT NOT NULL UNIQUE
);"""

create_deathcause_string = """ 
CREATE TABLE deathcause(
    deathcause_id  INTEGER PRIMARY KEY,
    cause_name TEXT NOT NULL UNIQUE
);"""

create_jurisdictiondeathcause_string = """ 
CREATE TABLE jurisdictiondeathcause(
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    total INTEGER NOT NULL,
    deathcause_id INTEGER NOT NULL,
    jurisdiction_id INTEGER NOT NULL,
    FOREIGN KEY (deathcause_id)
       REFERENCES deathcause (deathcause_id) ,
    FOREIGN KEY (jurisdiction_id)
       REFERENCES jurisdiction (jurisdiction_id) 
    UNIQUE(year,month,deathcause_id,jurisdiction_id)
);"""

def create_tables(conn):
    conn.execute(""" 
    PRAGMA foreign_keys = ON;
    """)
    conn.execute(create_jurisdiction_string)
    conn.execute(create_deathcause_string)
    conn.execute(create_jurisdictiondeathcause_string)

conn = sqlite3.connect(DB_NAME)  
create_tables(conn) 


