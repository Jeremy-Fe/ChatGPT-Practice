import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

def request_chat_completion(
    prompt, 
    system_role="당신은 친절하고 유용한 도우미입니다.",
    model="gpt-3.5-turbo",
    stream=False
):
    messages = [
        {"role": "system", "content": system_role},
        {"role": "user", "content": prompt}
    ]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        stream=stream
    )
    return response

# 나의 캐릭터 챗봇 페르소나 출력
def request_persona(
    prompt, 
    system_role="당신은 뛰어난 연기자입니다.",
    model="gpt-3.5-turbo",
    stream=False
):
    messages = [
        {"role": "system", "content": system_role},
        {"role": "user", "content": prompt}
    ]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        stream=stream
    )
    return response.choices[0].message.content
    

def print_streaming_response(response):
    message = ""
    placeholder = st.empty()
    for chunk in response:
        delta = chunk.choices[0].delta
        if hasattr(delta, "content") and delta.content is not None:
            message += delta.content
            placeholder.markdown(message + "▌")
        else:
            break
    placeholder.markdown(message)
    return message

def print_streaming_response_console(response):
    message = ""
    for chunk in response:
        delta = chunk.choices[0].delta
        if hasattr(delta, "content") and delta.content is not None:
            message += delta.content
            print(delta.content, end="")
        else:
            break
    return message

