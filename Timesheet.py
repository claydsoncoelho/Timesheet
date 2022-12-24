import streamlit as st
import pandas as pd

# streamlit run /Users/claydsoncoelho/Documents/GitHub/Timesheet/Timesheet.py

tab1, tab2, tab3 = st.tabs(["Time Entry", "Reports", "Resources"])

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

    # Cache the dataframe so it's only loaded once
    @st.experimental_memo
    def load_data():
        return pd.DataFrame(
            {
                "first column": [1, 2, 3, 4],
                "second column": [10, 20, 30, 40],
            }
        )

    df = load_data()
    st.dataframe(df, use_container_width=True)
