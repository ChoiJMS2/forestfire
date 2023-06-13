# -*- coding: utf-8 -*-
import pandas as pd
import streamlit as st
from google.cloud import bigquery
from streamlit_pandas_profiling import st_profile_report

from data.query import run_query
from utils import credentials

# 빅쿼리 클라이언트 객체 생성
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

def run_data_preview():
    """
       Display the dataframe, data types, and describe statistics in a Streamlit-style format.

       :param dataframe: The input dataframe.
       :return: None
    """
    st.header("Data Set List")
    # 데이터셋 목록 가져오기
    datasets = list(client.list_datasets())
    # 데이터셋 목록을 담을 빈 리스트
    dataset_list = []
    # 각 데이터셋에 대해 데이터셋 ID를 가져와 리스트에 추가
    for dataset in datasets:
        dataset_list.append(dataset.dataset_id)

    dataset_list = st.selectbox("DateSet", ('Analysis_Data', 'PreProcessing_Data', 'Raw_Data'),
                                label_visibility='collapsed')  # 원하는 데이터셋 ID로 변경
    # 특정 데이터셋의 테이블 목록 조회
    st.subheader("Data Table List")
    dataset_id = dataset_list
    tables = list(client.list_tables(dataset_id))
    datatable_list = []
    for table in tables:
        datatable_list.append(table.table_id)
    df_tables = pd.DataFrame({"Table List": datatable_list})
    tablenames = st.selectbox("DataTable", df_tables, label_visibility='collapsed')

    tab1, tab2 = st.tabs(["📝Data Preview", "✅View Columns"])
    with tab1:
        st.subheader("📝Data Description")
        col1, col2 = st.columns([3, 2])
        with col1:
            st.title("📣 Data")
            if tablenames:
                table_id = tablenames
                query = f"""
                    SELECT *
                    FROM `forestfire-389107.{dataset_id}.{table_id}`
                    """
                # 쿼리 실행 및 결과를 데이터프레임으로 변환
                combined_df = client.query(query).to_dataframe()
                # 데이터프레임 출력
                st.dataframe(combined_df)
            with st.expander("Report"):
                st.write("pandas profiling")
                # pr = combined_df.profile_report()
                # st_profile_report(pr)

        with col2:
            st.title("📣 Describe")
            st.write("*Appendix 메뉴의 Codebook 참고")
    #        st.dataframe(dataframe.describe(), height=350, width=650)
    with tab2:
        if tablenames:
            dataset_id = dataset_list
            query = f"""
                SELECT STRING_AGG(column_name)
                FROM `forestfire-389107.{dataset_id}.INFORMATION_SCHEMA.COLUMNS`
                group by table_name
                """
            df = client.query(query).to_dataframe()
            all_cols = df.values[0][0].split(",")
            st.markdown("#### Select Columns")
            columns = st.multiselect("컬럼명 선택", all_cols, default=all_cols, label_visibility='collapsed')
            temp_Strings = ", ".join(columns)
            run_query(temp_Strings, dataset_id, tablenames)
        else :
            st.warning("error")

if __name__ == "__main__":
    run_data_preview()