# -*- coding:utf-8 -*-
import streamlit as st
from google.cloud import bigquery
from utils import credentials
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def temp_chart1():
    # 빅쿼리 클라이언트 객체 생성
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)

    query = """
            SELECT *
            FROM `forestfire-389107.Analysis_Data.Analysis_Data`
            """

    df2 = client.query(query).to_dataframe()
    df2 = df2.groupby('w_regions')

    # x축 레이블과 범례 항목 선택
    xticklabel = ['강원중부해안', '강원중부내륙', '강원북부해안', '강원북부내륙', '강원북부산지', '강원남부해안', '강원남부내륙', '강원남부산지']
    xticklabels = st.multiselect('X축 레이블 선택', xticklabel, default=xticklabel)
    temp = ['평균 기온', '최저 기온', '최고 기온']
    labels = st.multiselect('범례 항목 선택', temp, default=temp)

    column_mapping = {
        '평균 기온': 'avgTa',
        '최저 기온': 'minTa',
        '최고 기온': 'maxTa'
    }

    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (24, 5)
    plt.rcParams['font.size'] = 12
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False

    fig, ax = plt.subplots()

    colors = ["pink", "lightgreen", "lightblue"]
    box_width = 0.8  # 박스의 너비 설정

    # 선택된 항목들로 데이터 그룹화
    selected_groups = [group for _, group in df2 if _.strip() in xticklabels]

    for i, group in enumerate(selected_groups):
        data = [group["avgTa"], group["minTa"], group["maxTa"]]
        box = ax.boxplot(data, patch_artist=True, positions=[i * 4 + 1, i * 4 + 2, i * 4 + 3], widths=box_width,
                         boxprops={'linewidth': 2.8}, whiskerprops={'linewidth': 2.8})

        for patch, color in zip(box["boxes"], colors):
            patch.set_facecolor(color)

    xticks = np.arange(len(selected_groups)) * 4 + 1.5
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels, rotation=45, ha='right')

    yticks = np.arange(-30, 50, 10)
    ax.set_yticks(yticks)

    legend_patches = [mpatches.Patch(color=color, label=label) for color, label in zip(colors, labels)]
    ax.legend(handles=legend_patches, loc='lower center', bbox_to_anchor=(0.5, -0.2), fontsize=8.5,
              ncol=len(selected_groups))

    ax.set_title('9개 지역별 기온 데이터', fontweight='bold')
    # ax.set_xlabel('9개 지역별 기온 데이터', fontweight='bold')
    ax.set_ylabel('온도 (℃)')
    plt.subplots_adjust(left=0.1, right=0.85, bottom=0.1, top=0.9)

    st.pyplot(fig)