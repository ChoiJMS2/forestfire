import streamlit as st
from pathlib import Path

import seaborn as sns
import matplotlib.pyplot as plt
from google.cloud import bigquery
from utils import credentials
from eda.map import run_map

import folium

def run_chart1():
    pass
def run_chart2():
    run_map()
def run_chart3():
    pass
def run_chart4():
    pass

def run_eda():
    st.sidebar.markdown("## Exploration for Data")
    eda = st.sidebar.radio('submenu',['Chart1', 'Chart2', 'Chart3', 'Chart4'], label_visibility='collapsed')
    if eda == 'Chart1':
        st.markdown("## Chart1")
        run_chart1()
    elif eda == 'Chart2':
        st.markdown("## Chart2")
        st.warning("please EDA")
        run_chart2()
    elif eda == 'Chart3':
        st.markdown("## Chart3")
        st.warning("please EDA")
        run_chart3()
    elif eda == 'Chart4':
        st.markdown("## Chart4")
        st.warning("please EDA")
        run_chart4()