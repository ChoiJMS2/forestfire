# -*- coding:utf-8 -*-
import streamlit as st
from google.cloud import bigquery
from utils import credentials
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def analysis():
    # 빅쿼리 클라이언트 객체 생성
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)

    query = """
                SELECT *
                FROM `forestfire-389107.Analysis_Data.Analysis_Data`
                """

    df = client.query(query).to_dataframe()
    df = df.groupby('w_regions')
    return df

def weather_chart():
    df = analysis()

    # 그래프 설정
    region = ['강원중부해안', '강원중부내륙', '강원중부산지','강원북부해안', '강원북부내륙', '강원북부산지', '강원남부해안', '강원남부내륙', '강원남부산지']
    # 선택된 항목들로 데이터 그룹화
    df_groups = [group for _, group in df if _.strip() in region]
    colors = ["pink", "lightgreen", "lightblue"]
    box_width = 1.5  # 박스의 너비 설정
    median_color = 'red'  # 중간 선의 색상 설정

    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (24, 5)
    plt.rcParams['font.size'] = 12
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False

    tab1, tab2, tab3, tab4, tab5 = st.tabs(['기온', '습도', '강수량', '강수 유무', '풍속'])
    with tab1:
        temp = ['평균 기온', '최저 기온', '최고 기온']
        label1 = st.selectbox('데이터 선택', ['평균 기온', '최저 기온', '최고 기온'])

        if label1 == "평균 기온":

            column_mapping1 = {
                '평균 기온': 'avgTa',
                '최저 기온': 'minTa',
                '최고 기온': 'maxTa'
            }

            fig1, ax = plt.subplots()

            for i, group in enumerate(df_groups):
                data = group['avgTa']
                box = ax.boxplot(data, patch_artist=True, positions=[i*4+2], widths=box_width,
                                 boxprops={'linewidth': 1.7, 'edgecolor': 'black'}, whiskerprops={'linewidth': 1.7})

                for patch, color in zip(box["boxes"], colors):
                    patch.set_facecolor(color)

                for median in box["medians"]:
                    median.set(color=median_color)  # 중간 선의 색상 설정

            ax.set_xticks([i * 4 + 2 for i in range(len(df_groups))])
            ax.set_xticklabels(region)

            yticks = np.arange(-30, 50, 10)
            ax.set_yticks(yticks)

            legend_patches = [mpatches.Patch(color=color, label=label) for color, label in zip(colors, label1)]
            ax.legend(handles=legend_patches, loc='lower center', bbox_to_anchor=(0.5, -0.2), fontsize=8.5,
                      ncol=len(df_groups))

            ax.set_title('9개 지역별 평균 기온 데이터', fontweight='bold')
            ax.set_ylabel('온도 (℃)')
            plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)

            st.pyplot(fig1)

    with tab2:
        pass

    with tab3:
        pass

    with tab4:
        pass

    with tab5:
        pass

if __name__ == "__main__":
    weather_chart()