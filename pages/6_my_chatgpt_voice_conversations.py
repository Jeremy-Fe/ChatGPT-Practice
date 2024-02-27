import streamlit as st
from openai import OpenAI
from common import voiceToText, textToVoice

st.set_page_config(
    page_title="chatGPT API 서비스 개발",
    page_icon="🧠"
)

st.title("🌈지피티와 음성 통화?!")
st.subheader("지피티와 음성 통화해보아요!")

# 스트림릿 시크릿에서 OpenAI API 키 설정
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 기본 모델 설정
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# 채팅 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 앱 재실행 시 기록된 채팅 메시지 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 수락
if prompt := st.chat_input("안녕하세요! 어떤 것이 궁금하세요?"):
    # 사용자 메시지를 채팅 기록에 추가합니다.
    st.session_state.messages.append({"role": "user", "content": prompt})
    # 채팅 메시지 컨테이너에 사용자 메시지 표시합니다.
    with st.chat_message("user"):
        st.markdown(prompt)

    # 채팅 메시지 컨테이너에 어시스턴트 응답 표시합니다.
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})

if st.button("마이크 켜기"):
    user_input = voiceToText()
    if user_input is not None:
        st.session_state.messages.append({"role": "user", "content": user_input})
        # 채팅 메시지 컨테이너에 사용자 메시지 표시합니다.
        with st.chat_message("user"):
            st.markdown(user_input)
                # 채팅 메시지 컨테이너에 어시스턴트 응답 표시합니다.
        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
        # TTS api
        textToVoice(response)