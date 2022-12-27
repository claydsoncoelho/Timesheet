import streamlit as st
import pandas as pd
import snowflake.connector

# streamlit run /Users/claydsoncoelho/Documents/GitHub/Timesheet/Timesheet.py

tab1, tab2, tab3 = st.tabs(["Time Entry", "Reports", "Team"])


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
        st.write(my_data)
    cnx.close()
    return my_data


with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("Team")
    name = st.text_input("Name", value="", key="Name")
    rate = st.number_input("Rate", value=0.00, key="Rate")

    if st.button("Save member"):
        if name and rate:
            msg = insert_resource(name, rate)
            st.success(msg, icon="✅")

    resource_list = get_all_resources()
    resource_list.columns = ['Name', 'Rate']
    #resource_list['Rate'] = resource_list['Rate'].apply(lambda x: x * 0.01)
    st.dataframe(resource_list, use_container_width=True)

