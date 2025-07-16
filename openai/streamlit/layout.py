import streamlit as st

st.set_page_config(page_title="App", layout="wide")

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.header("A cat")
#     st.image("https://static.streamlit.io/examples/cat.jpg")

# with col2:
#     st.header("A dog")
#     st.image("https://static.streamlit.io/examples/dog.jpg")

# with col3:
#     st.header("A owl")
#     st.image("https://static.streamlit.io/examples/owl.jpg")

# st.video("https://www.youtube.com/watch?v=EPAAPX4Eq8A&list=RDEPAAPX4Eq8A&start_radio=1")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.video(
        "https://www.youtube.com/watch?v=EPAAPX4Eq8A&list=RDEPAAPX4Eq8A&start_radio=1"
    )

with st.sidebar:
    add_radio = st.radio("당신의 MBTI는 무엇입니까?", ("ISTJ", "ENTP", "모름"))

tab1, tab2, tab3 = st.tabs(["cat", "dog", "owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with tab3:
    st.header("A owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
