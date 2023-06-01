# 데이터 탭
# 라이브러리
import streamlit as st
import glob
from google.cloud import bigquery
from utils import credentials

client = bigquery.Client(credentials=credentials, project=credentials.project_id)

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(cols,table_id):
    # 빅쿼리 클라이언트 객체 생성
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)
    # 쿼리 작성
    project_id = 'forestfire-388501'
    dataset_id = 'combin_forest_fire'
    query = f"""
    SELECT {cols}
    FROM `{project_id}.{dataset_id}.{table_id}`
    """
    # 쿼리 실행 및 결과를 데이터프레임으로 변환
    df = client.query(query).to_dataframe()
    # 데이터프레임 출력
    st.dataframe(df)

def load_data1():
    tableNames = st.selectbox("Table", ('combin_forest_fire',''))
    if tableNames == 'combin_forest_fire':
        query = """
            SELECT STRING_AGG(column_name)
            FROM `forestfire-388501.combin_forest_fire.combin_forest_fire.INFORMATION_SCHEMA.COLUMNS`
            """

        df = client.query(query).to_dataframe()
        all_cols = df.values[0][0].split(",")
        columns = st.multiselect("컬럼명 선택", all_cols, default=all_cols)
        temp_Strings = ", ".join(columns)
        load_data1(temp_Strings,tableNames)
    else:
        st.warning("please select table")

    # Streamlit 애플리케이션 실행
    if __name__ == '__main__':
        load_data1()