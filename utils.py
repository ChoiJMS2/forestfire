# -*- coding:utf-8 -*-
import streamlit as st
from google.oauth2 import service_account

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    # Very Important Point
    st.secrets["gcp_service_account"]
)