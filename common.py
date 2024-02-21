import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

def request_chat_completion(
    prompt, 
    system_role="당신은 유용한 도우미입니다.",
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