# -*- coding:utf-8 -*-
import streamlit as st
from google.cloud import bigquery
from utils import credentials
import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import font_manager as fm
fpath = os.path.join(os.getcwd(), "font/NanumGothicBold.otf")
prop = fm.FontProperties(fname=fpath)

def analysis():
    # 빅쿼리 클라이언트 객체 생성
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)

    query = """
                SELECT *
                FROM `forestfire-389107.Analysis_Data.Analysis_Data`
                """

    df = client.query(query).to_dataframe()
    df = df[df['tm'] < '2023-01-01']
    df = df.groupby('w_regions')

    return df

def weather_chart():
    df = analysis()

    # 그래프 설정
    region = ['강원중부해안', '강원중부내륙', '강원중부산지','강원북부해안', '강원북부내륙', '강원북부산지', '강원남부해안', '강원남부내륙', '강원남부산지']
    # 선택된 항목들로 데이터 그룹화
    df_groups = [group for _, group in df if _.strip() in region]

    plt.style.use('ggplot')
    plt.rcParams['figure.figsize'] = (15, 8)
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.family'] = prop
    plt.rcParams['axes.unicode_minus'] = False

    tab1, tab2, tab3, tab4 = st.tabs(['기온', '습도', '강수량', '풍속'])
    with tab1:
        temp = ['평균 기온', '최저 기온', '최고 기온']
        selected_label = st.selectbox('데이터 선택', temp)
        buf, col1, buf = st.columns([1, 4, 1])
        with col1:

            column_mapping1 = {
                '평균 기온': 'avgTa',
                '최저 기온': 'minTa',
                '최고 기온': 'maxTa'
            }

            fig1, ax = plt.subplots()

            color_palette = ['blue', 'green', 'red']  # 항목별로 지정할 색상 리스트

            for i, group in enumerate(df_groups):
                if selected_label in column_mapping1 and column_mapping1[selected_label] in group.columns:
                    data = [group[column_mapping1[selected_label]]]
                    box = ax.boxplot(data, patch_artist=True, positions=[i * 2], widths=0.8,
                                     boxprops={'linewidth': 1.7, 'edgecolor': 'black', 'facecolor': color_palette[1]},
                                     whiskerprops={'linewidth': 1.7},
                                     medianprops={'color': 'red'})

            xticks = np.arange(len(df_groups)) * 2
            ax.set_xticks(xticks)  # positions 값으로 x축 설정
            ax.set_xticklabels(region, rotation=0, ha='center', fontproperties=prop)

            yticks = np.arange(-30, 50, 10)
            ax.set_yticks(yticks)

            ax.set_title('지역별 {} '.format(selected_label), fontproperties=prop)
            ax.set_ylabel('온도 (℃)', fontproperties=prop)
            plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)

            st.pyplot(fig1)

    with tab2:
        humidity = ['평균 상대습도', '최저 상대습도', '실효습도']
        selected_label2 = st.selectbox('데이터 선택', humidity)
        buf, col2, buf = st.columns([1, 4, 1])
        with col2:

            column_mapping2 = {
                '평균 상대습도': 'avgRhm',
                '최저 상대습도': 'minRhm',
                '실효습도': 'effRhm'
                }

            fig2, ax = plt.subplots()

            color_palette = ['blue', 'green', 'red']  # 항목별로 지정할 색상 리스트

            for i, group in enumerate(df_groups):
                if selected_label2 in column_mapping2 and column_mapping2[selected_label2] in group.columns:
                    data = [group[column_mapping2[selected_label2]]]
                    box = ax.boxplot(data, patch_artist=True, positions=[i * 2], widths=0.8,
                                     boxprops={'linewidth': 1.7, 'edgecolor': 'black', 'facecolor': color_palette[1]},
                                     whiskerprops={'linewidth': 1.7},
                                     medianprops={'color': 'red'})

            xticks = np.arange(len(df_groups)) * 2
            ax.set_xticks(xticks)  # positions 값으로 x축 설정
            ax.set_xticklabels(region, rotation=0, ha='center', fontproperties=prop)

            yticks = np.arange(0, 110, 10)
            ax.set_yticks(yticks)

            ax.set_title('지역별 {}'.format(selected_label2), fontproperties=prop)
            ax.set_ylabel('습도 (%)', fontproperties=prop)
            plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)

            st.pyplot(fig2)


    with tab3:
        rainfall = ['일일 강수량', '7일간 강수량', '비가 오지 않은 날', '강수 여부']
        selected_label3 = st.selectbox('데이터 선택', rainfall)
        buf, col3, buf = st.columns([1, 6, 1])
        with col3:
            if selected_label3 == '강수 여부':
                plt.rcParams['figure.figsize'] = (10, 5)

                fig5, ax = plt.subplots()

                width = 0.35
                x = range(len(region))
                colors = ['steelblue', 'darkorange']

                legend_labels = ['0', '1']

                for i, df in enumerate(df_groups):
                    counts = df['Rntf'].value_counts()

                    ax.bar(x[i] - width / 2, counts[0], width, label=legend_labels[0], color=colors[0])
                    ax.bar(x[i] + width / 2, counts[1], width, label=legend_labels[1], color=colors[1])

                    for j, count in enumerate(counts):
                        ax.text(x[i] + width * (j - 0.5), count + 2, str(count), ha='center', va='bottom', fontproperties=prop)

                ax.set_xticks(x)
                ax.set_xticklabels(region,fontproperties=prop)

                ax.set_ylabel('단위 (건)', fontproperties=prop)
                ax.set_title('지역별 강수 여부', fontproperties=prop)

                legend = ax.legend(handles=[ax.patches[0], ax.patches[len(region)]], labels=legend_labels,
                                   title='강수 여부', fontproperties=prop,
                                   loc='upper center', ncol=2)

                legend.set_bbox_to_anchor((0.5, -0.15))
                legend._legend_box.align = "center"

                plt.tight_layout()
                st.pyplot(fig5)

            elif selected_label3 == '비가 오지 않은 날':
                fig4, ax = plt.subplots()
                for i, group in enumerate(df_groups):
                    data = group["noRn"]
                    plt.scatter([i + 1] * len(data), data, s=100, label=region)

                plt.xticks(range(1, len(region) + 1), region)
                plt.title(f'지역별 {selected_label3}', fontproperties=prop)
                plt.ylabel('단위 (일)', fontproperties=prop)

                st.pyplot(fig4)
            else:
                column_mapping3 = {
                    '일일 강수량': 'sumRn',
                    '7일간 강수량': 'sumRn7'
                }

                fig3, ax = plt.subplots()

                for i, group in enumerate(df_groups):
                    if selected_label3 in column_mapping3 and column_mapping3[selected_label3] in group.columns:
                        data = group[column_mapping3[selected_label3]]
                        plt.scatter([i+1] * len(data), data, s=100, label=region)

                plt.xticks(range(1, len(region)+1), region)
                plt.title(f'지역별 {selected_label3}', fontproperties=prop)
                plt.ylabel('강수량 (mm)', fontproperties=prop)

                st.pyplot(fig3)

    with tab4:
        wind = ['평균 풍속', '최대 풍속', '최대 순간 풍속', '7일간 최대 풍속']
        selected_label4 = st.selectbox('데이터 선택', wind)
        buf, col4, buf = st.columns([1, 6, 1])
        with col4:
            column_mapping4 = {
                '평균 풍속': 'avgWs',
                '최대 풍속': 'maxWs',
                '최대 순간 풍속': 'maxInsWs',
                '7일간 최대 풍속': 'maxwind7'
                }

            fig6, ax = plt.subplots()

            color_palette = ['blue', 'green', 'red']  # 항목별로 지정할 색상 리스트

            for i, group in enumerate(df_groups):
                if selected_label4 in column_mapping4 and column_mapping4[selected_label4] in group.columns:
                    data = [group[column_mapping4[selected_label4]]]
                    box = ax.boxplot(data, patch_artist=True, positions=[i * 2], widths=0.8,
                                     boxprops={'linewidth': 1.7, 'edgecolor': 'black', 'facecolor': color_palette[1]},
                                     whiskerprops={'linewidth': 1.7},
                                     medianprops={'color': 'red'})

            xticks = np.arange(len(df_groups)) * 2
            ax.set_xticks(xticks)  # positions 값으로 x축 설정
            ax.set_xticklabels(region, rotation=0, ha='center', fontproperties=prop)

            if selected_label4 == '평균 풍속':
                yticks = np.arange(0, 20, 5)
            elif selected_label4 == '최대 순간 풍속':
                yticks = np.arange(0, 40, 5)
            else:
                yticks = np.arange(0, 30, 5)
            ax.set_yticks(yticks)

            ax.set_title('지역별 {}'.format(selected_label4), fontproperties=prop)
            ax.set_ylabel('습도 (%)',fontproperties=prop)
            plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)

            st.pyplot(fig6)



if __name__ == "__main__":
    weather_chart()