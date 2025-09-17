import streamlit as st
import time

# 초기 변수 설정
잔여시간 = 0
cnt = 0
running = False  # 타이머 동작 여부

# 타이머 시작 함수
def start_timer():
    global 잔여시간, cnt, running
    잔여시간 = 5  # 타이머 설정
    cnt = 0  # 클릭 횟수 초기화
    running = True
    st.session_state.running = True
    st.session_state.잔여시간 = 잔여시간
    st.session_state.cnt = cnt

# 클릭 함수
def click():
    if running:
        st.session_state.cnt += 1
        st.session_state.time_left = st.session_state.time_left - 1
        return True
    return False

# 타이머 업데이트 함수
def update_timer():
    if st.session_state.time_left <= 0:
        st.session_state.running = False
        st.session_state.timer_over = True

# 앱 실행
if 'running' not in st.session_state:
    st.session_state.running = False
    st.session_state.timer_over = False
    st.session_state.time_left = 0
    st.session_state.cnt = 0

st.title("주어진 시간 동안 최대한 많이 클릭하세요!")

if st.session_state.running:
    st.text(f"Time left: {st.session_state.time_left} seconds")
    if st.button('Click Me!'):
        click()
    st.text(f"현재 횟수: {st.session_state.cnt}")
else:
    if st.button('Start Timer'):
        start_timer()

if st.session_state.timer_over:
    st.text(f"최종 횟수: {st.session_state.cnt}")
    if st.button('Reset'):
        st.session_state.timer_over = False
        st.session_state.cnt = 0
        st.session_state.time_left = 0
