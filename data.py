# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import utils

def run_erd():
    pass

def run_data1():
    pass
def run_data2():
    pass
def run_data3():
    pass
def run_data():

    Data_List = st.sidebar.radio("Select Data", ['ERD', 'Data1', 'Data2', 'Data3'])
    if Data_List == 'ERD':
        st.markdown("## ERD")
        run_erd()
    elif Data_List == 'Data1':
        st.markdown("## Data1 Int")
        run_data1()
    elif Data_List == 'Data2':
        st.markdown("## Data2 Int")
        run_data2()
    elif Data_List == 'Data3':
        st.markdown("## Data3 Int")
        run_data3()
