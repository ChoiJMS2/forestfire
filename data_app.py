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
from data import load_data
from data1 import load_data1
from utils import credentials


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
def run_data_list():

    # BigQuery 클라이언트 생성
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)
    # # 데이터셋 목록 조회
    st.markdown("#### Data Set List")
    # 데이터셋 목록 가져오기
    datasets = list(client.list_datasets())
    # 데이터셋 목록을 담을 빈 리스트
    dataset_list = []
    # 각 데이터셋에 대해 데이터셋 ID를 가져와 리스트에 추가
    for dataset in datasets:
        dataset_list.append(dataset.dataset_id)
    a = pd.DataFrame([{"DataSet List" : [dataset_list[0], dataset_list[1], dataset_list[2]] }])
    st.dataframe(a)
    # 특정 데이터셋의 테이블 목록 조회
    st.markdown("#### Data Table List")
    dataset_list = st.selectbox("Table", ('combin_forest_fire','forest_fire', 'gangwon'), label_visibility='collapsed') # 원하는 데이터셋 ID로 변경
    if dataset_list == 'combin_forest_fire':
        dataset_id = dataset_list
        tables = list(client.list_tables(dataset_id))
        for table in tables:
            st.write(table.table_id)
    elif dataset_list == 'forest_fire':
        dataset_id = dataset_list
        tables = list(client.list_tables(dataset_id))
        for table in tables:
            st.write(table.table_id)
    elif dataset_list == 'gangwon':
        dataset_id = dataset_list
        tables = list(client.list_tables(dataset_id))
        for table in tables:
            st.write(table.table_id)
def appendix():
    st.subheader(":white_check_mark: Codebook")
    st.markdown("**데이터 정의서**")
    st.subheader(":white_check_mark: 부록")
    option = st.selectbox(
        "#### 첨부 목록",
        ('첨부1 : 코드 목록', '첨부2 : 지점 번호', '첨부3 : 뭐 이런것들?'))

def run_data():
    st.sidebar.markdown("## Select Data")
    Data_List = st.sidebar.radio(" ", ['ERD', 'Data List', 'Data1', 'Data2', 'Data3', 'Data4','Appendix'], label_visibility='collapsed')
    if Data_List == 'ERD':
        st.markdown("## 📝 Data Tab 설명")
        st.markdown("### ERD")
        st.write("ERD 이미지 넣기")
        st.markdown("### Data1")
        st.write("데이터 셋 틀 1안")
        st.markdown("### Data2")
        st.write("데이터 셋 틀 2안")
        st.markdown("### Data3")
        st.write("DB 연동 데이터 불러오기 테스트")
        st.markdown("### Data4")
        st.write("DB 연동 데이터 불러오기 테스트 및 컬럼 multiselect 적용")
        st.markdown("### Appendix")
        st.write("부록")
        run_erd()
    elif Data_List == 'Data List':
        run_data_list()
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
