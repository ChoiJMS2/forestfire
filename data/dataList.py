# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
from google.cloud import bigquery
from utils import credentials

# 빅쿼리 클라이언트 객체 생성
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

def run_data_list():

    # 데이터셋 목록 조회
    st.header("Data Set List")
    # 데이터셋 목록 가져오기
    datasets = list(client.list_datasets())
    # 데이터셋 목록을 담을 빈 리스트
    dataset_list = []
    # 각 데이터셋에 대해 데이터셋 ID를 가져와 리스트에 추가
    for dataset in datasets:
        dataset_list.append(dataset.dataset_id)
    df_datasets = pd.DataFrame({"Data Set List": dataset_list})
    st.dataframe(df_datasets)

    # 특정 데이터셋의 테이블 목록 조회
    st.subheader("DataTable List")
    dataset_list = st.selectbox("Select Date Set", ('Analysis_Data', 'PreProcessing_Data', 'Raw_Data'))  # 원하는 데이터셋 ID로 변경
    if dataset_list:
        dataset_id = dataset_list
        tables = list(client.list_tables(dataset_id))
        datatable_list = []
        for table in tables:
            datatable_list.append(table.table_id)
        df_tables = pd.DataFrame({"Table List": datatable_list})
        st.dataframe(df_tables)


if __name__ == "__main__":
    run_data_list()