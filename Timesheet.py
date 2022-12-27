import streamlit as st
import pandas as pd
import snowflake.connector

# streamlit run /Users/claydsoncoelho/Documents/GitHub/Timesheet/Timesheet.py

tab1, tab2, tab3 = st.tabs(["Time Entry", "Reports", "Resources"])


def insert_resource(name, rate):
    cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    with cnx.cursor() as my_cur:
        sql_cmd = "INSERT INTO DB_TIMESHEET.PUBLIC.RESOURCES VALUES('" + name + "', " + str(rate) + ")"
        my_cur.execute(sql_cmd)
    cnx.close()
    return name + " | " + str(rate)


def get_all_resources():
    cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    with cnx.cursor() as my_cur:
        sql_cmd = "SELECT * FROM DB_TIMESHEET.PUBLIC.RESOURCES"
        my_cur.execute(sql_cmd)
        my_data = pd.DataFrame(my_cur.fetchall())
    cnx.close()
    return my_data


with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("Resources")
    name = st.text_input("Name", key="Name")
    rate = st.number_input("Rate", key="Rate")

    def save_resource():
        if name and rate:
            msg = insert_resource(name, rate)
            st.success(msg, icon="✅")
            st.session_state["Name"] = ""
            st.session_state["Rate"] = ""

    st.button("Save resource", on_click=save_resource)

    resource_list = get_all_resources()
    st.dataframe(resource_list, use_container_width=True)

