import streamlit as st
import openai
import speech_recognition as sr
import pyttsx3
# from gtts import gTTS
# import os


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




# mike To Speech
def voiceToText():
    r = sr.Recognizer()
    try:
        with sr.Microphone(device_index=1) as source:  # 예: device_index를 1로 설정
            print("say something: ")
            audio = r.listen(source)
            said = r.recognize_google(audio)
            print("You said: ", said)
    except Exception as e:
        print("An error occurred: ", str(e))
        said = ""
    
    return said 

# text To Voice
# 한국어 id : HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_KO-KR_HEAMI_11.0
# 영어 ID : HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
def textToVoice(text='hi'):
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine = pyttsx3.init()
    engine.setProperty('voice', voice_id)
    engine.say(text)


    engine.runAndWait()
    # tts = gTTS(text=text)
    # filename='voice3.mp3'
    # tts.save(filename) # 파일을 만들고,

    # # 오디오 파일 삭제
    # os.remove(filename)
