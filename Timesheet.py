import streamlit as st
import pandas as pd
#import snowflake.connector

# streamlit run /Users/claydsoncoelho/Documents/GitHub/Timesheet/Timesheet.py

tab1, tab2, tab3 = st.tabs(["Time Entry", "Reports", "Resources"])
name_list = []
rate_list = []

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
        name_list.append(name)
        rate_list.append(rate)


    def load_data():
        return pd.DataFrame(
            {
                "Name": name_list,
                "Rate": rate_list
            }
        )

    df = load_data()
    st.dataframe(df, use_container_width=True)
