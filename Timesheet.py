import streamlit as st
import pandas as pd
import snowflake.connector

# streamlit run /Users/claydsoncoelho/Documents/GitHub/Timesheet/Timesheet.py

tab1, tab2, tab3 = st.tabs(["Time Entry", "Reports", "Team"])


def insert_resource(name, rate):
    cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    with cnx.cursor() as my_cur:
        sql_cmd = "INSERT INTO TIMESHEET_DB.PUBLIC.RESOURCES VALUES('" + name + "', " + str(rate) + ")"
        my_cur.execute(sql_cmd)
    cnx.close()
    return name + " | " + str(rate)


def get_all_resources():
    cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    with cnx.cursor() as my_cur:
        sql_cmd = "SELECT NAME, RATE FROM TIMESHEET_DB.PUBLIC.RESOURCES"
        my_cur.execute(sql_cmd)
        my_data = my_cur.fetchall()
        name_list = []
        rate_list = []
        for row in my_data:
            name_list.append(row[0])
            rate_list.append(float(row[1]))
        my_data = pd.DataFrame(
            {
                "Name": name_list,
                "Rate": rate_list
            }
        )

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
    st.dataframe(resource_list.style.format({"Rate": "{:.2f}"}), use_container_width=True)

