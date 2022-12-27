import streamlit as st
import pandas as pd
import snowflake.connector

# streamlit run /Users/claydsoncoelho/Documents/GitHub/Timesheet/Timesheet.py

tab1, tab2, tab3 = st.tabs(["Time Entry", "Reports", "Resources"])


def insert_resource(cnx, name, rate):
    with cnx.cursor() as my_cur:
        sql_cmd = "INSERT INTO DB_TIMESHEET.PUBLIC.RESOURCES VALUES('" + name + "', " + str(rate) + ")"
        my_cur.execute(sql_cmd)
    return "Thanks for adding " + name + " - " + str(rate) + "."


def get_all_resources(cnx):
    with cnx.cursor() as my_cur:
        sql_cmd = "SELECT * FROM DB_TIMESHEET.PUBLIC.RESOURCES"
        my_cur.execute(sql_cmd)
        my_data = pd.DataFrame(my_cur.fetchall())
    return pd.DataFrame(my_data)
    #return my_cur.fetchall()


with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("Resources")
    name = st.text_input('Name')
    rate = st.number_input('Rate')

    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    resource_list = get_all_resources(my_cnx)

    if name and rate:
        msg = insert_resource(my_cnx, name, rate)
        st.write(msg)

    def load_data():
        return pd.DataFrame(resource_list)

    df = load_data()
    st.dataframe(resource_list)

    my_cnx.close()
