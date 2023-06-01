# -*- coding:utf-8 -*-
import pandas as pd
import calendar

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import streamlit as st
from pathlib import Path


def run_eda():
    st.sidebar.markdown("## Exploration for Data")
    eda = st.sidebar.radio('',['Chart1', 'Chart2', 'Chart3', 'Chart4'], label_visibility='collapsed')
    if eda == 'Chart1':
        st.markdown("## Chart1")
    elif eda == 'Chart2':
        st.markdown("## Chart2")
    elif eda == 'Chart3':
        st.markdown("## Chart3")
    elif eda == 'Chart4':
        st.markdown("## Chart4")