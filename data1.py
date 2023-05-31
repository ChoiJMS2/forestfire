from utils import credentials, SERVICE_KEY
client = bigquery.Client(credentials=credentials)

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(cols, name):
    st.write("Load DataFrame")
    sql = f"SELECT {cols} FROM erudite-river-387006.seoul.{name}"
    df = client.query(sql).to_dataframe()

    st.dataframe(df)