from dotenv import load_dotenv
from openai import OpenAI
from typing_extensions import override
from openai import AssistantEventHandler
import streamlit as st

# warning 무시
import warnings

warnings.filterwarnings("ignore")

load_dotenv()

client = OpenAI()
Model = "gpt-4o-mini"


# 어시스턴트 초기화(세션 저장)
if "assistant_id" not in st.session_state:
    assistant = client.beta.assistants.create(
        name="Fruit Advisor",
        instructions="너는 과일 지식이 풍부한 과일 전문가야. 나의 질문에 친절히 답변을 해주는 ChatBot 이야",
        model=Model,
    )
    # 세션 저장
    st.session_state.assistant_id = assistant.id

# 스레드 생성(세션에 없는 경우 새로 생성하기)
if "thread_id" not in st.session_state:
    thread = client.beta.threads.create()
    # 세션 저장
    st.session_state.thread_id = thread.id


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("🍎 Fruit Advisor Chatbot")


# 이전 메세지 표시
for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(msg)

if prompt := st.chat_input("궁금한 과일에 대해 질문하세요"):
    st.chat_message("user").markdown(prompt)
    st.session_state.chat_history.append({"user", prompt})

    # 사용자 질문을 thread 추가
    client.beta.threads.messages.create(
        thread_id=st.session_state.thread_id, role="user", content=prompt
    )

    # 스트리밍 출력 부분
    output_area = st.empty()

    class EventHandler(AssistantEventHandler):
        def __init__(self):
            super().__init__()
            self.text = ""

        @override
        def on_text_created(self, text):
            """
            텍스트 생성 완료 시점에 호출되는 함수
            """
            self.text = ""

        @override
        def on_text_delta(self, delta, snapshot):
            """
            텍스트 생성 중간에 호출되는 함수
            """
            self.text += delta.value
            output_area.markdown(self.text + " ")

        def on_text_done(self, text):
            output_area.markdown(self.text)
            st.session_state.chat_history.append({"assistant", self.text})

    with client.beta.threads.runs.stream(
        thread_id=st.session_state.thread_id,
        assistant_id=st.session_state.assistant_id,
        instructions="사용자를 고객님이라고 부르세요. 사용자에게 프리미엄 계정이 있습니다.",
        event_handler=EventHandler(),
    ) as stream:
        stream.until_done()
