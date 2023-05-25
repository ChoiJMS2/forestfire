# -*- coding:utf-8 -*-
import streamlit as st
from streamlit_option_menu import option_menu
from home import run_home
from data import run_data

def main():
    """
        Main function to run the Streamlit app.
    """
    st.set_page_config(page_title="Minimize forest fire damage", page_icon=":🔥:",
                            layout = "wide", initial_sidebar_state="expanded")
    # Streamlit 앱 실행
    with st.sidebar:
        selected = option_menu("Main Menu", ['Home', 'Data', 'EDA', 'STAT', 'ML'],
                               icons=['house', 'card-checklist', 'bar-chart', 'clipboard-data', 'gear'],
                               menu_icon="app-indicator", default_index=0, orientation = 'vertical', key='main_option',
                               styles={
                                   "container": {"padding": "5!important", "background-color": "#fafafa"},
                                   "icon": {"color": "orange", "font-size": "25px"},
                                   "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
                                                "--hover-color": "#eee"},
                                   "nav-link-selected": {"background-color": "#02ab21"},
                                   }
                               )
    if selected == 'Home':
        run_home()
    elif selected == 'Data':
        run_data()
    elif selected == 'EDA':
        pass
    elif selected == 'STAT':
        pass
    elif selected == 'ML':
        pass
    else:
        print('error..')


if __name__ == "__main__":
    main()