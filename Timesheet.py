import streamlit as st
import pandas as pd
import snowflake.connector

# streamlit run /Users/claydsoncoelho/Documents/GitHub/Timesheet/Timesheet.py

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
with cnx.cursor() as my_cur:
    #sql_cmd = "SELECT * FROM DB_TIMESHEET.PUBLIC.RESOURCES"
    sql_cmd = "select * from fruit_load_list"
    my_cur.execute(sql_cmd)
my_data = pd.DataFrame(my_cur.fetchall())

st.dataframe(my_data)

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

 my_cnx.close()
