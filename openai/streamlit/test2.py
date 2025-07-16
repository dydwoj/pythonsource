import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.title("데이터 프레임")

df = pd.DataFrame(
    {
        "first_column": [1, 2, 3, 4],
        "second_column": [10, 20, 30, 40],
    }
)

st.dataframe(df, use_container_width=False)
st.table(df)

st.metric(label="온도", value="10", delta="1.2")
st.metric(label="삼성전자", value="61,000", delta="-1,200")

res = {"name": "과학 박람회", "date": "금요일", "participants": ["Alice", "Bob"]}
st.json(res)

data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(data)
st.bar_chart(data)

# matplotlib

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)

# plotly
fig = go.Figure(
    data=go.Scatter(
        x=[1, 2, 3, 4],
        y=[10, 11, 12, 13],
        mode="markers",
        marker=dict(size=[40, 60, 80, 100], color=[0, 1, 2, 3]),
    )
)
st.plotly_chart(fig, use_container_width=True)

# form 요소
btn = st.button("버튼 클릭")

if btn:
    st.write(":blue[버튼] 이 클릭됨 :sparkles:")

# 텍스트 요소
title = st.text_input(label="여행지를 입력해주세요", placeholder="여행지 입력")
st.write(f"당신이 선택한 여행지는? :violet[{title}]")

# 체크박스
agree = st.checkbox("동의 하십니까?")
if agree:
    st.write("동의해주셔서 감사합니다. :100:")

mbti = st.radio("당신의 MBTI는 무엇입니까?", ("ISTJ", "ENTP", "모름"))
if mbti == "ISTJ":
    st.write("당신은 :blue[현실주의자]")
elif mbti == "ENTP":
    st.write("당신은 :blue[활동가]")
else:
    st.write("당신에 대해 :red[알고 싶어요]")


# select
mbti = st.selectbox("당신의 MBTI는 무엇입니까?", ("ISTJ", "ENTP", "모름"), index=2)
if mbti == "ISTJ":
    st.write("당신은 :blue[현실주의자]")
elif mbti == "ENTP":
    st.write("당신은 :blue[활동가]")
else:
    st.write("당신에 대해 :red[알고 싶어요]")
