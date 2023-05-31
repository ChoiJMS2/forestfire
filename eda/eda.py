# -*- coding:utf-8 -*-
import pandas as pd
import calendar

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import streamlit as st
from pathlib import Path

def run_eda():
    with st.sidebar:
        chart1 = st.checkbox("Chart1")
        chart2 = st.checkbox("Chart2")
        chart3 = st.checkbox("Chart3")

        if chart1:
            st.subheader("chart1")
        elif chart2:
            st.subheader("chart2")
        elif chart3:
            st.subheader("chart3")
        else:
            st.error("Please Check to Chart")