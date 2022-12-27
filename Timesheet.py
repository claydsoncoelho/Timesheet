import streamlit as st
import pandas as pd
import snowflake.connector

# streamlit run /Users/claydsoncoelho/Documents/GitHub/Timesheet/Timesheet.py

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
with my_cnx.cursor() as my_cur:
    #sql_cmd = "SELECT * FROM DB_TIMESHEET.PUBLIC.RESOURCES"
    #sql_cmd = "select * from fruit_load_list"
    my_cur.execute("select * from fruit_load_list")
my_data = pd.DataFrame(my_cur.fetchall())

st.dataframe(my_data)

my_cnx.close()
