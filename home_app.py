# -*- coding:utf-8 -*-

import streamlit as st
from PIL import Image

def run_home():
    """
        Renders the introduction section of the app, including tabs for overview, objectives, and analysis phases.
    """
    tab1, tab2, tab3 = st.tabs([":desktop_computer: Introduction", ":trophy: Goals", ":bar_chart: Analysis "])
    with tab1:
        st.subheader(":white_check_mark: Project by")
        st.markdown(
            "Member|Skills|GitHub & Blog \n |:--:|:--:|:--:| \n |Beom-Mo Kim|-------- | ![git](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FJVyru%2FbtseBexHPj3%2FVcOibIVPqoCkgLTA8mpP61%2Fimg.png) : https://github.com/KingBeeM ![blog](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Ftc61f%2FbtseGWwjM0C%2FD4Su9TE8awMKMdyhstKAO0%2Fimg.jpg) : -----| \n |Sang-Il Bae|------- | ![git](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FJVyru%2FbtseBexHPj3%2FVcOibIVPqoCkgLTA8mpP61%2Fimg.png) : https://github.com/BaeSang1 ![blog](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Ftc61f%2FbtseGWwjM0C%2FD4Su9TE8awMKMdyhstKAO0%2Fimg.jpg) : https://tkddlf288.tistory.com/| \n |Yeol-Min Sung| -------| ![git](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FJVyru%2FbtseBexHPj3%2FVcOibIVPqoCkgLTA8mpP61%2Fimg.png) : https://github.com/YulminSung ![blog](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Ftc61f%2FbtseGWwjM0C%2FD4Su9TE8awMKMdyhstKAO0%2Fimg.jpg) : https://muhanyuljung.tistory.com/ | \n |Sung-Jun Oh|------- | ![git](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FJVyru%2FbtseBexHPj3%2FVcOibIVPqoCkgLTA8mpP61%2Fimg.png) : https://github.com/sjohjun ![blog](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Ftc61f%2FbtseGWwjM0C%2FD4Su9TE8awMKMdyhstKAO0%2Fimg.jpg) : https://djohjun.tistory.com/ | \n |Gwang-Hyeon Yim | -------|![git](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FJVyru%2FbtseBexHPj3%2FVcOibIVPqoCkgLTA8mpP61%2Fimg.png) : https://github.com/Kwanghyun97/ ![blog](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Ftc61f%2FbtseGWwjM0C%2FD4Su9TE8awMKMdyhstKAO0%2Fimg.jpg) :  https://techtalkwithkwanghyun.tistory.com/manage | \n |Jae-Myoung Choi|------- | ![git](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FJVyru%2FbtseBexHPj3%2FVcOibIVPqoCkgLTA8mpP61%2Fimg.png) : https://github.com/ChoiJMS2m  ![blog](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Ftc61f%2FbtseGWwjM0C%2FD4Su9TE8awMKMdyhstKAO0%2Fimg.jpg) : https://james-choi88.tistory.com|")
        st.subheader(":white_check_mark: Project Calender")
        img = Image.open("img/home/wbs.png")
        st.image(img)

        st.subheader(":white_check_mark: Analytic Language & Tools")
        col1, col2, col3 = st.columns(3)
        with col1:
            img1 = Image.open("img/logo/pycharm.png")
            st.image(img1, width=300)

        with col2:
            img2 = Image.open("img/logo/python.png")
            st.image(img2, width=300)

        with col3:
            img3 = Image.open("img/logo/streamlit.png")
            st.image(img3, width=300)
        col4, col5 = st.columns(2)
        with col4:
            img4 = Image.open("img/logo/openapi.PNG")
            st.image(img4, width=450)
        with col5:
            img7 = Image.open("img/logo/bigquery.png")
            st.image(img7, width=450)


    with tab2:
        st.header(":white_check_mark: 프로젝트 목표")
        img5 = Image.open("img/home/bp.png")
        st.image(img5)
        st.markdown("\n")
        st.header(":white_check_mark: 주요 설정 지수")
        col6, col7, col8 = st.columns(3, gap="medium")
        with col6:
            st.markdown("#### 🌡️ 실효 습도")
            st.markdown("**✔** 목재 건조도 or **:red[화재 위험성을 나타내는 지수]**")
            st.markdown("**✔** 수 일간 상대습도에 **:red[가중치를 적용]** 하여 산출하는 **:red[평균습도]**")
            st.markdown("       👉 일반적으로 당일 포함,  **:red[5일 간의 평균 상대 습도]** 의 누적치")
            st.markdown("**✔** 실효 습도가 **:red[50% 이하]** 가 되면 대형 화재 위험성 🔺")
            st.image("img/home/Effective_humidity.png")
        with col7:
            st.markdown("#### 🔥 산불 위험 등급")
            st.markdown("**✔ :red[산불위험지수 산출]** 에 필요한 정보 : ")
            st.markdown("**👉 기상요인 : :blue[기온, 상대습도, 실효습도, 풍속, 강수량]**")
            st.markdown("**📌** 1~100 까지의 지수를 산출 → **:red[4단계 산불위험등급]** (매우높음, 높음, 보통, 낮음) 으로 구분")
            st.image("img/home/FFRR.png")

        with col8:
            st.markdown("#### 🔥️ 산불 위험 지수(DWI)")
            st.image("img/home/FFRI.PNG")

        st.markdown("\n")
        st.header(":white_check_mark: 평가 지표")
        col9, col10 = st.columns(2)
        with col9:
            st.image("img/home/map.png")
        with col10:
            st.image("img/home/Spatial_Info.png")
        st.image("img/home/LR.png")
        st.image("img/home/model_Evaluation.png")

    with tab3:
        st.header(":white_check_mark: 프로젝트 순서도")
        img6 = Image.open("img/home/workflow.png")
        st.image(img6)

        st.header(":white_check_mark: 분석방향")
        st.image("img/home/LR.png")
        st.image("img/home/model_Evaluation.png")

