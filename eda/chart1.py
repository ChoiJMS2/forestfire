# -*- coding:utf-8 -*-
import streamlit as st
from google.cloud import bigquery
from utils import credentials
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

@st.cache_data(ttl=600)
def chart():
    # 빅쿼리 클라이언트 객체 생성
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)

    query = """
    SELECT *
    FROM `forestfire-389107.Analysis_Data.Analysis_Data`
    """
    df1= client.query(query).to_dataframe()

    # Figure 스타일, 크기
    plt.style.use('seaborn')
    plt.rcParams['figure.figsize'] = (14, 5)
    plt.rcParams['font.size'] = 12

    # Streamlit figure 생성
    fig, ax = plt.subplots()

    colors = ["pink", "lightgreen", "lightblue"]

    data = [df1["avgTa"], df1["minTa"], df1["maxTa"]]
    box = ax.boxplot(data, patch_artist=True, positions=[1, 2, 3], boxprops={'linewidth': 1.8},
                     whiskerprops={'linewidth': 1.8})

    for patch, color in zip(box["boxes"], colors):
        patch.set_facecolor(color)

    ax.set_xticks([i * 4 + 2 for i in range(len(df1))])

    yticks = np.arange(-30, 50, 10)
    ax.set_yticks(yticks)

    labels = ['Avg Temperature', 'Min Temperature', 'Max Temperature']
    legend_patches = [mpatches.Patch(color=color, label=label) for color, label in zip(colors, labels)]
    ax.legend(handles=legend_patches, loc='lower center', bbox_to_anchor=(0.5, -0.3), fontsize=8.5,
              ncol=len(df1))

    ax.set_xticklabels(["site " + str(i + 1) for i in range(len(df1))])
    ax.set_xlabel('Temp')
    ax.set_ylabel('Value')
    plt.subplots_adjust(left=0.1, right=0.85, bottom=0.1, top=0.9)

    st.pyplot(fig)



if __name__ == "__main__":
    chart()

