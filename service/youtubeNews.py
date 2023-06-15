# -*- coding: utf-8 -*-
import streamlit as st
from streamlit_player import st_player, _SUPPORTED_EVENTS

def run_youtubeNews():
    c1, c2, c3 = st.columns([3, 3, 2])

    with c3:
        st.subheader("Parameters")
        with st.expander("SUPPORTED PLAYERS", expanded=True):
            st.write("""
               - Dailymotion
               - Facebook
               - Mixcloud
               - SoundCloud
               - Streamable
               - Twitch
               - Vimeo
               - Wistia
               - YouTube
               <br/><br/>
               """, unsafe_allow_html=True)

    with c1:
        url1 = st.text_input("First URL", "https://www.youtube.com/watch?v=ZP4s4CEGMJw")
        st_player(url1, key="youtube_player1")


    with c2:
        url2 = st.text_input("Second URL", "https://www.youtube.com/watch?v=ya8MurTg4x0")
        st_player(url2, key="youtube_player2")

    c4, c5, c6 = st.columns([3, 3, 2])
    with c4:
        url3 = st.text_input("Third URL", "https://www.youtube.com/watch?v=ECZBcCVNogI")
        st_player(url3, key="youtube_player3")


    with c5:
        url4 = st.text_input("Fourth URL", "https://www.youtube.com/watch?v=cRIGefdVj-g")
        st_player(url4, key="youtube_player4")

if __name__ == "__main__":
    run_youtubeNews()