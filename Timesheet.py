import streamlit as st

input = st.text_input("text", key="text")


def clear_text():
    st.session_state["text"] = ""


if st.button("clear text input", on_click=clear_text):
    st.write(input)