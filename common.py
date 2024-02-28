import streamlit as st
import openai
import speech_recognition as sr
from gtts import gTTS
import time
import playsound
import os
import pygame


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

# playsound 말고 pydub이나 pygame을 사용하는 것이 좋다
# text To Voice
def textToVoice(text):
    tts = gTTS(text=text)
    filename='voice3.mp3'
    tts.save(filename) # 파일을 만들고,
    # Pygame mixer 초기화
    pygame.mixer.init()
    # 오디오 파일 로드
    pygame.mixer.music.load(filename)
    # 오디오 재생
    pygame.mixer.music.play()
    # 재생이 끝날 때까지 대기
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    # 오디오 재생 중단
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    # 오디오 파일 삭제
    os.remove(filename)

def voice_stop():
    # 오디오 재생 중단
    pygame.mixer.music.stop()

def voice_pause():
    print("dubug1, voice_pause")
    # 오디오 일시 정지
    pygame.mixer.music.pause()

def voice_unpause():
    print("dubug2, voice_unpause")

    # 오디오 다시 재생
    filename='voice3.mp3'
    pygame.mixer.music.unpause()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    os.remove(filename)