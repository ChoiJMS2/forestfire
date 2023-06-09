# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd

import requests
from bs4 import BeautifulSoup
import json
import lxml

from datetime import datetime, timedelta
import time

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import folium
from folium.plugins import MarkerCluster

from google.cloud import bigquery
from utils import credentials
import pyproj
import plotly.graph_objs as go

@st.cache_data(ttl=600)
def run_map():
    pass

if __name__ == "__main__":
    run_map()