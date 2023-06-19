# -*- coding:utf-8 -*-
import streamlit as st
from google.cloud import bigquery
from utils import credentials
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def run_humidity():
    # 빅쿼리 클라이언트 객체 생성
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)

    query = """
                SELECT *
                FROM `forestfire-389107.Analysis_Data.Analysis_Data`
                """

    df = client.query(query).to_dataframe()
    df = df.groupby('w_regions')

    # x축 레이블과 범례 항목 선택
    xticklabel = ['강원중부해안', '강원중부내륙', '강원중부산지', '강원북부해안', '강원북부내륙', '강원북부산지', '강원남부해안', '강원남부내륙', '강원남부산지']
    xticklabels = st.multiselect('지역 선택', xticklabel, default=xticklabel)
    humidity = ['평균 상대습도', '최저 상대습도', '실효습도']
    labels = st.multiselect('관찰 항목 선택', humidity, default=humidity)

    column_mapping = {
        '평균 상대습도': 'avgRhm',
        '최저 상대습도': 'minRhm',
        '실효습도': 'effRhm'
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
    selected_groups = [group for _, group in df if _.strip() in xticklabels]

    for i, group in enumerate(selected_groups):
        data = [group[column_mapping[label]] for label in labels]
        box = ax.boxplot(data, patch_artist=True, positions=[i * 4 + j for j in range(len(labels))], widths=box_width,
                         boxprops={'linewidth': 1.7}, whiskerprops={'linewidth': 1.7})

        for patch, color in zip(box["boxes"], colors):
            patch.set_facecolor(color)

    xticks = np.arange(len(selected_groups)) * 4 + 1.5
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels, rotation=0, ha='center')

    yticks = np.arange(0, 110, 10)
    ax.set_yticks(yticks)

    legend_patches = [mpatches.Patch(color=color, label=label) for color, label in zip(colors, labels)]
    ax.legend(handles=legend_patches, loc='lower center', bbox_to_anchor=(0.5, -0.2), fontsize=8.5,
              ncol=len(selected_groups))

    ax.set_title('9개 지역별 습도 데이터', fontweight='bold')
    ax.set_ylabel('습도 (%)')
    plt.subplots_adjust(left=0.1, right=0.85, bottom=0.1, top=0.9)

    st.pyplot(fig)


if __name__ == "__main__":
    run_humidity()