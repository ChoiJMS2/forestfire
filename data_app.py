# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import utils
from google.cloud import bigquery
from streamlit_pandas_profiling import st_profile_report
from data import load_data
from testdata import load_data1

@st.cache_data(ttl=600)
def run_erd():
    pass

def run_data1():
    """
       Display the dataframe, data types, and describe statistics in a Streamlit-style format.

       :param dataframe: The input dataframe.
       :return: None
    """
    st.subheader("📝[Data1] Data Description")
    col1, col2 = st.columns([3, 2])
    with col1:
        st.title("📣 Data")
#        st.dataframe(dataframe, height=810, width=1200)

    with col2:
        st.title("📣 Describe")
#        st.dataframe(dataframe.describe(), height=350, width=650)
    with st.expander("Report"):
        st.markdown("Report")
#                pr = data1.profile_report()
#                st_profile_report(pr)
def run_data2():
    tab1, tab2, tab3 = st.tabs(["**📝Description**", "**📣 Data**", "**📊 Report**"])
    with tab1:
        st.title("📝[Data1] Data Description")
    with tab2:
        st.title("📣 Data")
    with tab3:
        with st.expander("Report"):
            st.markdown("Report")
def run_data3():
    load_data()

def run_data4():
    load_data1()

def appendix():
    st.subheader(":white_check_mark: Codebook")
    st.markdown("**데이터 정의서**")
    st.subheader(":white_check_mark: 부록")
    option = st.selectbox(
        "#### 첨부 목록",
        ('첨부1 : 코드 목록', '첨부2 : 지점 번호', '첨부3 : 뭐 이런것들?'))

def run_data():
    st.sidebar.markdown("## Select Data")
    Data_List = st.sidebar.radio(" ", ['ERD', 'Data1', 'Data2', 'Data3', 'Data4','Appendix'], label_visibility='collapsed')
    if Data_List == 'ERD':
        st.markdown("## ERD")
        run_erd()
    elif Data_List == 'Data1':
        run_data1()
    elif Data_List == 'Data2':
        run_data2()
    elif Data_List == 'Data3':
        st.markdown("## Data3 Int")
        run_data3()
    elif Data_List == 'Data4':
        st.markdown("## Data4 Int")
        run_data4()
    elif Data_List == 'Appendix':
        appendix()
