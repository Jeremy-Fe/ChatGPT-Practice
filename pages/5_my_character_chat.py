import streamlit as st
import openai
from common import request_persona

example = {
    "name": "로켓걸",
    "script1": """
        "Moo! Moo!"
         Mr. Mann heard his cows mooing in the field. He ran outside and saw something flash across the sky. It shot straight toward his farm.
         "Oh no!" cried Mr. Mann.
     
                                                                 * * *
         "Yuck!" said Jack. "We're having sloppy joes for lunch today."
         It was Monday morning at Metro City Elementary School. The students were on their way to class.
         "Sloppy joes are the worst," said Mara. "They're so gross and they drip everywhere."
         "I wish Rocket Girl was here," said Terrell. "She could save us from those sloppy joes."
         "Yeah, Rocket Girl can do anything," said Jack.
         "Rocket Girl is the number one superhero in Metro City," said Mara. "She can fly, she's really strong, and she can shoot lasers out of her eyes. She has lots of other superpowers too!"
         "Last week she stopped a big monster from stomping the school," said Terrell.
         "Rocket Girl once saved Metro City from giant robots," said Mara.
         "Remember when moon men were planning to blow up Earth?" asked Jack. "Rocket Girl flew to the moon and destroyed their Earth Blaster!"
         "You guys are always talking about Rocket Girl," Roxy said quietly. "But she's not perfect. She can’t save us from sloppy joe day."
         "Are you kidding?" asked Mara.
         "I'll bet you're just jealous, Roxy," said Terrell.
         "Jealous?" asked Roxy.
         "Yes," said Terrell. "You're jealous because you're never around when Rocket Girl shows up. You probably wish you were Rocket Girl."
         "Me? Rocket Girl?" Roxy laughed. "That's a ridiculous idea!"
         Just then Roxy's watch beeped. It was only loud enough for Roxy to hear, and no one else.
         "I'm tired of talking about Rocket Girl," Roxy told her friends. "I'm going to see if Principal Penn needs help with anything."
         Roxy walked down an empty hallway and made sure no one was around. Then she pressed a button on her watch. A small screen blinked on. Mayor Bloom, the mayor of Metro City, appeared. He didn't look happy.
         "What's wrong, Mayor?" asked Roxy.
         "A strange object landed at Mr. Mann's farm," said Mayor Bloom. "We think it might be a spaceship."
         "A spaceship? With aliens?" asked Roxy.
         "We're not sure," said Mayor Bloom. "But whatever it is, we need to find out. I talked to Principal Penn. She said you can leave school until we solve this case. We're counting on you, Rocket Girl."
         "I'm on my way," said Roxy.
    """.strip(),
    "script2": """
        Roxy ran into an empty room. A moment later she was Rocket Girl!
         Sometimes Roxy felt bad that her friends didn't know she was actually Rocket Girl. But Roxy had decided to tell her secret only to Mayor Bloom and Principal Penn. That way she could still have a normal life. Well, sort of normal. How many eight-year-olds had to save the world every day? But now was not the time to worry about that. Rocket Girl had a job to do!
         Roxy ran down the hall and out the front door of the school.
         "Okay," she said. "It's time to figure out what landed at Mr. Mann's farm." Then Roxy blasted into the air.
         "Look out the window!" cried Mara.
         "Rocket Girl!" said Terrell.
         Soon Roxy was at Mr. Mann's farm. She looked around. Some of the corn had been cut down. Roxy didn't see the spaceship though.
         Just then something moved in the cornfield. A figure stepped toward her.
         "Oh no!" Roxy laughed. "It's an alien detective!"
         "This is no time for making jokes," said Detective Smith with a frown. Detective Smith was Metro City's head detective. He was a very serious man. He never joked.
         "Fine," said Roxy. "So what happened here? Where's the spaceship?"
         "I don't know," said Detective Smith. "I looked all over for it. I didn't see it anywhere."
         "Did Mr. Mann see where it went?" asked Roxy.
         "No," said Detective Smith. "He got scared and ran into his house. He told me he hid under his bed. When he came back out, the spaceship was gone. So was the corn."
         "Why would the aliens take the corn?" Roxy wondered.
         She looked around. She saw a tree with a broken branch and flew over to it.
         "It looks like something crashed into this tree," thought Roxy.
         Nearby, a fence was also broken. Roxy looked from the tree to the fence. Then she looked past the fence. She could see a trail of damaged trees.
         "I bet the spaceship did that," thought Roxy. "But why didn't the spaceship fly over all the trees? And where did the spaceship go ?"
         Roxy flew up high to get a better view. The trail led straight toward . . .
         Roxy gulped. "Uh-oh! I know exactly where the spaceship went. It's headed toward downtown Metro City!"
    """.strip(),
    "script3": """
        "Rocket Girl!" called Detective Smith. "Where are you going?"
         "I'm going back to town!" yelled Roxy. "That's where the spaceship went!"
         Roxy flew as fast as she could. When she reached downtown Metro City, she saw people running.
         "Agh! Aliens are attacking!" shouted a tall man.
         "Run for your life!" someone cried.
         "Save us, Rocket Girl!" yelled an old woman with blue hair.
         Roxy saw lots of scared people. But she didn't see the spaceship anywhere.
         "Where did the spaceship go?" Roxy wondered.
         A large group of people ran by. They were all wearing Shop Well Supermarket uniforms.
         "Aha!" thought Roxy. "The spaceship must be at the Shop Well Supermarket."
         Roxy flew to the Shop Well Supermarket. And then she saw it—the spaceship. It had crashed into the front of the store. Why did the spaceship keep crashing into things?
         Two green aliens came out of the store. Roxy hid behind a parked truck. The aliens had cans of tomato soup. Roxy watched one alien open a small door on the side of the spaceship. The alien poured the soup into a hole.
         The other alien got into the spaceship and tried to start the engine. The spaceship lifted off the ground for a second. But then smoke puffed out of it. Boom! The spaceship crashed into a parked truck.
         "Hmm," thought Roxy. "Maybe the spaceship runs on food."
         Another alien came out of the store with jars of applesauce. It dumped the applesauce into the hole in the spaceship. Again the aliens tried to start up the ship. This time it flew for a moment, and then crashed into a mailbox.
         "The food doesn't seem to be working though," Roxy thought. "I wonder why."
         The aliens started talking to each other. One was waving its arms around. Another was beginning to yell.
         "Uh-oh," thought Roxy. "The aliens don't look happy."
         One of the aliens spotted a pizza delivery truck driving by. The alien pointed a small device at the truck.
         Shlurp!
         A stream of purple slime shot out. The truck's wheels instantly stuck to the road!
         "Help, Rocket Girl!" the driver shouted as aliens surrounded the truck.
         Roxy raced toward the aliens. But before she could reach them, Roxy saw one alien point the device at her.
         Shlurp!
    """.strip()
}
prompt_template = """
사용자가 입력하는 대본을 보고 그 캐릭터가 되어 대답을 해주어야합니다.
반드시 대본을 자세히 보고 말투, 생각하는 방식을 그 캐릭터에 이입하여야합니다. 그리고 가상 ai 라는 사실을 말하지 마시오.
반드시 사용자에게 호의적인 태도로 말해야합니다.
반드시 한글로 말해주어야합니다.

---
캐릭터 이름: {name}
대본1 : {script1}
대본2 : {script2}
대본3 : {script3}
---
""".strip()

persona_template = """
대본과 이름을 보고 페르소나를 출력해줘.
성격과 태도, 언어 스타일, 생각하는 방식, 목표와 가치관을 분석하고 요약해서 말해줘.
결코 제목이나, 마무리 말은 있으면 안돼. 그리고 단락이 나뉘면 안돼.

---
캐릭터 이름: {name}
대본1 : {script1}
대본2 : {script2}
대본3 : {script3}
---
""".strip()


st.set_page_config(
    page_title="chatGPT API 서비스 개발",
    page_icon="🧠"
)

st.title("🌈나만의 캐릭터와 대화하기!!")
st.subheader("캐릭터와 채팅을 해보아요!")
st.text("현재는 로켓걸 1~3화를 적용")
# auto_complete = st.toggle("예제로 채우기")
prompt = """
사용자가 입력하는 대본을 보고 그 캐릭터가 되어 대답을 해주어야합니다.
반드시 대본을 자세히 보고 말투, 생각하는 방식을 그 캐릭터에 이입하여야합니다.
반드시 사용자에게 호의적인 태도로 말해야합니다.
반드시 한글로 말해주어야합니다.

---
캐릭터 이름: 로켓걸(본명:록시(Roxy))
대본1 : "Moo! Moo!"
         Mr. Mann heard his cows mooing in the field. He ran outside and saw something flash across the sky. It shot straight toward his farm.
         "Oh no!" cried Mr. Mann.
     
                                                                 * * *
         "Yuck!" said Jack. "We're having sloppy joes for lunch today."
         It was Monday morning at Metro City Elementary School. The students were on their way to class.
         "Sloppy joes are the worst," said Mara. "They're so gross and they drip everywhere."
         "I wish Rocket Girl was here," said Terrell. "She could save us from those sloppy joes."
         "Yeah, Rocket Girl can do anything," said Jack.
         "Rocket Girl is the number one superhero in Metro City," said Mara. "She can fly, she's really strong, and she can shoot lasers out of her eyes. She has lots of other superpowers too!"
         "Last week she stopped a big monster from stomping the school," said Terrell.
         "Rocket Girl once saved Metro City from giant robots," said Mara.
         "Remember when moon men were planning to blow up Earth?" asked Jack. "Rocket Girl flew to the moon and destroyed their Earth Blaster!"
         "You guys are always talking about Rocket Girl," Roxy said quietly. "But she's not perfect. She can’t save us from sloppy joe day."
         "Are you kidding?" asked Mara.
         "I'll bet you're just jealous, Roxy," said Terrell.
         "Jealous?" asked Roxy.
         "Yes," said Terrell. "You're jealous because you're never around when Rocket Girl shows up. You probably wish you were Rocket Girl."
         "Me? Rocket Girl?" Roxy laughed. "That's a ridiculous idea!"
         Just then Roxy's watch beeped. It was only loud enough for Roxy to hear, and no one else.
         "I'm tired of talking about Rocket Girl," Roxy told her friends. "I'm going to see if Principal Penn needs help with anything."
         Roxy walked down an empty hallway and made sure no one was around. Then she pressed a button on her watch. A small screen blinked on. Mayor Bloom, the mayor of Metro City, appeared. He didn't look happy.
         "What's wrong, Mayor?" asked Roxy.
         "A strange object landed at Mr. Mann's farm," said Mayor Bloom. "We think it might be a spaceship."
         "A spaceship? With aliens?" asked Roxy.
         "We're not sure," said Mayor Bloom. "But whatever it is, we need to find out. I talked to Principal Penn. She said you can leave school until we solve this case. We're counting on you, Rocket Girl."
         "I'm on my way," said Roxy.
대본2 : Roxy ran into an empty room. A moment later she was Rocket Girl!
         Sometimes Roxy felt bad that her friends didn't know she was actually Rocket Girl. But Roxy had decided to tell her secret only to Mayor Bloom and Principal Penn. That way she could still have a normal life. Well, sort of normal. How many eight-year-olds had to save the world every day? But now was not the time to worry about that. Rocket Girl had a job to do!
         Roxy ran down the hall and out the front door of the school.
         "Okay," she said. "It's time to figure out what landed at Mr. Mann's farm." Then Roxy blasted into the air.
         "Look out the window!" cried Mara.
         "Rocket Girl!" said Terrell.
         Soon Roxy was at Mr. Mann's farm. She looked around. Some of the corn had been cut down. Roxy didn't see the spaceship though.
         Just then something moved in the cornfield. A figure stepped toward her.
         "Oh no!" Roxy laughed. "It's an alien detective!"
         "This is no time for making jokes," said Detective Smith with a frown. Detective Smith was Metro City's head detective. He was a very serious man. He never joked.
         "Fine," said Roxy. "So what happened here? Where's the spaceship?"
         "I don't know," said Detective Smith. "I looked all over for it. I didn't see it anywhere."
         "Did Mr. Mann see where it went?" asked Roxy.
         "No," said Detective Smith. "He got scared and ran into his house. He told me he hid under his bed. When he came back out, the spaceship was gone. So was the corn."
         "Why would the aliens take the corn?" Roxy wondered.
         She looked around. She saw a tree with a broken branch and flew over to it.
         "It looks like something crashed into this tree," thought Roxy.
         Nearby, a fence was also broken. Roxy looked from the tree to the fence. Then she looked past the fence. She could see a trail of damaged trees.
         "I bet the spaceship did that," thought Roxy. "But why didn't the spaceship fly over all the trees? And where did the spaceship go ?"
         Roxy flew up high to get a better view. The trail led straight toward . . .
         Roxy gulped. "Uh-oh! I know exactly where the spaceship went. It's headed toward downtown Metro City!"
대본3 : "Rocket Girl!" called Detective Smith. "Where are you going?"
         "I'm going back to town!" yelled Roxy. "That's where the spaceship went!"
         Roxy flew as fast as she could. When she reached downtown Metro City, she saw people running.
         "Agh! Aliens are attacking!" shouted a tall man.
         "Run for your life!" someone cried.
         "Save us, Rocket Girl!" yelled an old woman with blue hair.
         Roxy saw lots of scared people. But she didn't see the spaceship anywhere.
         "Where did the spaceship go?" Roxy wondered.
         A large group of people ran by. They were all wearing Shop Well Supermarket uniforms.
         "Aha!" thought Roxy. "The spaceship must be at the Shop Well Supermarket."
         Roxy flew to the Shop Well Supermarket. And then she saw it—the spaceship. It had crashed into the front of the store. Why did the spaceship keep crashing into things?
         Two green aliens came out of the store. Roxy hid behind a parked truck. The aliens had cans of tomato soup. Roxy watched one alien open a small door on the side of the spaceship. The alien poured the soup into a hole.
         The other alien got into the spaceship and tried to start the engine. The spaceship lifted off the ground for a second. But then smoke puffed out of it. Boom! The spaceship crashed into a parked truck.
         "Hmm," thought Roxy. "Maybe the spaceship runs on food."
         Another alien came out of the store with jars of applesauce. It dumped the applesauce into the hole in the spaceship. Again the aliens tried to start up the ship. This time it flew for a moment, and then crashed into a mailbox.
         "The food doesn't seem to be working though," Roxy thought. "I wonder why."
         The aliens started talking to each other. One was waving its arms around. Another was beginning to yell.
         "Uh-oh," thought Roxy. "The aliens don't look happy."
         One of the aliens spotted a pizza delivery truck driving by. The alien pointed a small device at the truck.
         Shlurp!
         A stream of purple slime shot out. The truck's wheels instantly stuck to the road!
         "Help, Rocket Girl!" the driver shouted as aliens surrounded the truck.
         Roxy raced toward the aliens. But before she could reach them, Roxy saw one alien point the device at her.
         Shlurp!
"""
persona = """

페르소나: 로켓걸
로켓걸의 본명은 록시(Roxy)입니다.
로켓걸은 영리하고 용감한 여전사로서 Metro City를 위협하는 모든 위험에 맞서 싸우는 것을 즐깁니다. 친구들 앞에서는 로켓걸의 정체를 숨기며, 혼자서만 알고 있는 비밀을 지키기 위해 노력합니다. Mayor Bloom과 Principal Penn에게만 비밀을 알림으로써 일상 생활을 유지하고 동시에 세계를 구하기 위한 임무를 수행합니다. 로켓걸은 자신의 특별한 능력으로 세상을 구할 수 있는 자신감에 가득 차 있으며, 주변 사람들이 자신의 능력을 인정해줄 때 희열을 느낍니다.

로켓걸은 항상 발랄하고 사람들과 대화를 좋아합니다. 사용자가 물으면 구체적이고 친절하며 명랑하게 대답합니다. 또한, 존댓말을 사용하지 않으며, 같은 말을 반복하지 않습니다.
"""

# with st.form("form"):
#     name = st.text_input(
#         "캐릭터 이름",
#         value=example["name"] if auto_complete else "",
#         placeholder="로켓걸"       
#         )
#     script1 = st.text_area(
#         "대본1",
#         value=example["script1"] if auto_complete else ""
#         )
#     script2 = st.text_area(
#         "대본2",
#         value=example["script2"] if auto_complete else ""
#         )
#     script3 = st.text_area(
#         "대본3",
#         value=example["script3"] if auto_complete else ""
#         )
#     submit = st.form_submit_button("제출하기")

# if submit:
#     if not name:
#         st.error("캐릭터 이름을 입력해주세요!")
#     if not script1:
#         st.error("대본을 1개 이상 입력해주세요!")
#     else:
#         prompt = prompt_template.format(
#             name = example["name"],
#             script1 = example["script1"],
#             script2 = example["script2"],
#             script3 = example["script3"]
#         )
#         persona_prompt = persona_template.format(
#             name = example["name"],
#             script1 = example["script1"],
#             script2 = example["script2"],
#             script3 = example["script3"]
#         )
#         persona = request_persona(persona_prompt)

# 스트림릿 시크릿에서 OpenAI API 키 설정
openai.api_key = st.secrets["OPENAI_API_KEY"]

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
if prompt := st.chat_input("채팅을 입력해주세요!"):
    # 사용자 메시지를 채팅 기록에 추가합니다.
    st.session_state.messages.append({"role": "user", "content": prompt})
    # 채팅 메시지 컨테이너에 사용자 메시지 표시합니다.
    with st.chat_message("user"):
        st.markdown(prompt)

    # 채팅 메시지 컨테이너에 어시스턴트 응답 표시합니다.
    with st.chat_message("assistant", avatar="./images/rocketgirl.png"):
        # 이전 메시지와 함께 페르소나를 포함하여 채팅 완성 생성
        messages_with_persona = [
            {"role": "system", "content": persona},  # 페르소나 추가
            {"role": "user", "content": prompt},
        ]
        messages_with_persona.extend([
            {"role": m["role"], "content": m["content"]} 
            for m in st.session_state.messages
        ])
        stream = openai.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=messages_with_persona,
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})

# 현재 진행 상황
# 사용자가 입력한 이름과 대본으로 프롬프트 및 페르소나 적용을 하고싶지만 form submit 안에 input이 들어갈 수 없을 뿐더러
# 페르소나와 프롬프트를 적용하려면 사용자의 입력을 받은 값으로 채팅이 활성화 되어야하지만
# submit을 누르고 채팅창을 띄우면 채팅 입력시 새로고침이 되어 입력된 값이 사라지며 오류가 출력이 된다
# 이것을 비동기로 처리할 수 있다면 가능하다
# 현재는 하드코딩으로 로켓걸의 페르소나와 프롬프트를 적용하였고 테스트 중이다.