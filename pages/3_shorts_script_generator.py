import streamlit as st
import requests
from bs4 import BeautifulSoup
from common import request_chat_completion, print_streaming_response

def crawl_naver_entertainment(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    article = soup.find("div", class_="article_body").text.strip()
    return article   

prompt_template = """
최신 연예 뉴스 기사가 주어집니다.
뉴스 기사를 참고해서 유튜브 쇼츠 대본을 작성해주세요.
흥미롭고 자극적으로 작성해주세요.
10대 소녀가 친구에게 말하는 듯한 말투로 작성해주세요.
제목, 클립, 대본이 출력될때 반드시 줄바꿈을 하지마세요.

아래 포맷으로 작성해주세요.
[제목] <제목 텍스트>\n\n
[클립] <영상에서 보여줄 이미지나 영상에 대한 묘사>\n
[대본] <나레이션 방식의 대본>\n
[클립] <영상에서 보여줄 이미지나 영상에 대한 묘사>\n
[대본] <나레이션 방식의 대본>\n
...
---
뉴스 기사: {article}
---
""".strip()

st.set_page_config(
    page_title="chatGPT API 서비스 개발",
    page_icon="🧠"
)

st.title("🤴유튜브 쇼츠 대본 생성기")
st.subheader("기사 URL을 입력하면 쇼츠 대본을 만들어줍니다.")
st.write("지금 현재 네이버 TV연예 기사만 가능합니다.")
link_text = "기사 둘러보기!"
link_url = "https://entertain.naver.com/home"

# 링크 생성 및 출력
st.write(f"**[{link_text}]({link_url})**")

example_url = "https://entertain.naver.com/read?oid=144&aid=0000917660"
auto_complete = st.toggle("예제로 채우기")



with st.form("form"):
    url = st.text_input(
        "기사 URL",
        value=example_url if auto_complete else "",
        placeholder=example_url
        )
    submit = st.form_submit_button("제출하기")
if submit:
    if not url:
        st.error("기사 URL을 입력해주세요.")
    if not url.startswith("https://entertain.naver.com"):
        st.error("처리할 수 없는 URL입니다.")
    else:
        article = crawl_naver_entertainment(url)
        prompt = prompt_template.format(article=article)
        system_role = "당신은 교츠 전문 유튜버입니다."
        response = request_chat_completion(
            prompt = prompt,
            system_role = system_role,
            stream = True
        )
        message = print_streaming_response(response)
        scripts = [x.replace("[대본]", "").strip() for x in message.split("\n") if x.startswith("[대본]")]
        st.subheader("파싱된 대본 부분")
        for script in scripts:
            st.markdown(script)





