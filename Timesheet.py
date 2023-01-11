import streamlit as st
import pandas as pd
import snowflake.connector
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder

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

    resource_list = get_all_resources()
    #st.dataframe(resource_list.style.format({"Rate": "{:.2f}"}), use_container_width=True)
    
    gd = GridOptionsBuilder.from_dataframe(resource_list)
    gd.configure_selection(selection_mode='multiple', use_checkbox=True)
    gridoptions = gd.build()

    grid_table = AgGrid(resource_list, gridOptions=gridoptions, update_mode=GridUpdateMode.SELECTION_CHANGED)

    st.write('## Selected')
    selected_row = grid_table["selected_rows"]
    st.dataframe(selected_row)
    
    if len(selected_row) = 0:
        st.session_state.disabled_delete = True
    elif len(selected_row) > 1:
        st.session_state.disabled_save = True
    else:
        st.session_state.disabled_save = False

    if 'save_button' not in st.session_state:
        st.session_state.disabled_save = False
        
    save_button = st.button("Save member", key='save_button', disabled=st.session_state.disabled_save)
    
    if save_button:
        if name and rate:
            msg = insert_resource(name, rate)
            st.success(msg, icon="✅")
            
    if 'delete_button' not in st.session_state:
        st.session_state.disabled_save = True
        
    delete_button = st.button("Delete member", key='delete_button', disabled=st.session_state.disabled_delete)
