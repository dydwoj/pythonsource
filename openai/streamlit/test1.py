import streamlit as st

st.title("이것은 타이틀 입니다.")

st.header("이것은 hearder 입니다.", divider="gray")
st.subheader("이것은 subhearder 입니다.", divider=True)

st.caption("캡션 적용")
sample_code = """
def function():
    print("Hello World")
"""

st.code(sample_code, language="python")

st.text("일반적인 텍스트 입력")
title = st.text_input(label="여행지 입력", placeholder="여행지를 입력해 주세요")

# 마크다운 문법
st.markdown("streamlit 은 **마크다운 문법 적용** 됩니다.")
st.markdown("---")
st.markdown("텍스트 색상을 : green[초록색], **blue[파란색]** 볼드체 설정")
