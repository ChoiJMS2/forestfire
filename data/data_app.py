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
def appendix():
    st.subheader(":white_check_mark: Codebook")
    st.markdown("**데이터 정의서**")
    st.subheader(":white_check_mark: 부록")
    option = st.selectbox(
        "#### 첨부 목록",
        ('첨부1 : 코드 목록', '첨부2 : 지점 번호', '첨부3 : 뭐 이런것들?'))
    if option == '첨부2 : 지점 번호':
        st.image("img/WSN.png")
    else:
        pass

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
        appendix()