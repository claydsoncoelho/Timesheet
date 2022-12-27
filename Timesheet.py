import streamlit as st
import pandas as pd
import snowflake

# streamlit run /Users/claydsoncoelho/Documents/GitHub/Timesheet/Timesheet.py

tab1, tab2, tab3 = st.tabs(["Time Entry", "Reports", "Resources"])
name_list = []
rate_list = []


def insert_row_snowflake(cnx, name, rate):
  with cnx.cursor() as my_cur:
    sql_cmd = "INSERT INTO DB_TIMESHEET.PUBLIC.RESOURCES VALUES('" + name + "', " + str(rate) + ")"
    st.write(sql_cmd)
    my_cur.execute(sql_cmd)
    return "Thanks for adding " + name

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

    if name and rate:
        my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
        msg = insert_row_snowflake(my_cnx, name, rate)
        st.write(msg)


    def load_data():
        return pd.DataFrame(
            {
                "Name": name_list,
                "Rate": rate_list
            }
        )

    df = load_data()
    st.dataframe(df, use_container_width=True)
