# 데이터 탭
# 라이브러리
import streamlit as st
import glob
from google.cloud import bigquery
from utils import credentials
@st.cache_data(ttl=600)
def load_data():

    # 빅쿼리 클라이언트 객체 생성
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)
    # 쿼리 작성
    project_id = 'forestfire-388501'
    dataset_id = 'combin_forest_fire'
    table_id = 'combin_forest_fire'
    query = f"""
    SELECT *
    FROM `{project_id}.{dataset_id}.{table_id}`
    """
    # 쿼리 실행 및 결과를 데이터프레임으로 변환
    df = client.query(query).to_dataframe()
    # 데이터프레임 출력
    st.dataframe(df)
    # Streamlit 애플리케이션 실행
    if __name__ == '__main__':
        load_data()