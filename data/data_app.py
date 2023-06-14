# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# import utils
from google.cloud import bigquery
from streamlit_pandas_profiling import st_profile_report
from utils import credentials
from data.dataList import run_data_list
from data.dataPreview import run_data_preview
from data.appendix import run_appendix


# 빅쿼리 클라이언트 객체 생성
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

def run_data2():
    tab1, tab2, tab3 = st.tabs(["**📝Description**", "**📣 Data**", "**📊 Report**"])
    with tab1:
        st.title("📝[Data1] Data Description")
    with tab2:
        st.title("📣 Data")
    with tab3:
        with st.expander("Report"):
            st.markdown("Report")



def run_data():
    st.sidebar.markdown("## SubMenu")
    Data_List = st.sidebar.radio(" ", ['ERD', 'Data List', 'Data Preview', 'Appendix'], label_visibility='collapsed')
    if Data_List == 'ERD':
        st.header("ERD")
        st.image("img/ERD.png")
    elif Data_List == 'Data List':
        run_data_list()
    elif Data_List == 'Data Preview':
        run_data_preview()
    elif Data_List == 'Appendix':
        run_appendix()