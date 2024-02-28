import streamlit as st
import openai
from common import request_persona


st.set_page_config(
    page_title="chatGPT API 서비스 개발",
    page_icon="🧠"
)

st.title("🌈나만의 캐릭터와 대화하기!!")
st.text("현재는 로켓걸 1챕터를 적용")
# auto_complete = st.toggle("예제로 채우기")
user_prompt = """
title: Rocket Girl and the Aliens

contents: 
"Moo! Moo!"
     Mr. Mann heard his cows mooing in the field. He ran outside and saw something flash across the sky. It shot straight toward his farm.
     "Oh no!" cried Mr. Mann.
 
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

Roxy looked down. The purple slime made her feet stick to the street!
     "Grr!" Roxy used her super strength. She pulled, heaved, and twisted until— shloop! —her feet came unstuck.
     By now the aliens had opened the door of the pizza delivery truck.
     "Yikes!" the driver shouted.
     "Stop right there!" Roxy shouted as she flew toward the aliens. "I'm not going to let you hurt him."
     "We aren't going to hurt anyone," said one alien. "My name is Brim. We need to refuel our spaceship. It runs on food, but none of this food is working."
     "Why not?" asked Roxy.
     "It's not the right kind of food," said Brim. "We need something really thick and gloppy."
     "Thick and gloppy?" said Roxy. "Hmm . . ."
     "Ugh!" said Mara. "I got sloppy joe on my sleeve!"
     "This is awful," said Jack.
     Just then Brim and the other aliens walked into the cafeteria.
     "Aliens!" someone shouted.
     "Run for your life!" shouted someone else.
     Rocket Girl flew in.
     "Don't panic," she said. "These guys are friendly. They just need your sloppy joes so they can refuel their spaceship."
     Rocket Girl explained everything, and no one was scared anymore.
     "Oh! You can have my sloppy joe!" said Jack.
     "Mine too!" said Mara.
     "Take mine!" said Terrell.
     "Everybody, grab your lunch and follow us," said Rocket Girl.
     "Try it now, Brim," said Roxy.
     Brim started up the spaceship. It worked perfectly.
     "Thank you, everyone," said Brim. "Those sloppy joes are the perfect fuel for our spaceship."
     The kids waved good-bye as the spaceship flew away.
     "I'm glad we got rid of those sloppy joes," said Terrell. "But now what will we eat?"
     "Look out the window!" said Mara.
     "Pizza!" said Jack.
     Mayor Bloom came into the cafeteria. He had a tall stack of pizzas.
     "Thanks for giving up your lunches to save Metro City," he said. "I have pizza for everybody."
     The students cheered. A moment later Roxy entered the cafeteria.
     "Roxy!" said Mara. "You missed Rocket Girl!"
     "And aliens!" said Jack.
     "What?" asked Roxy, pretending to be surprised.
     "Where were you?" asked Mara.
     "Oh, I was helping Principal Penn with . . . office work," said Roxy.
     Terrell looked at Roxy suspiciously. "Well, you know what, Roxy? You were wrong. Rocket Girl was able to save us from sloppy joe day."
     Roxy didn't say anything. She just smiled and quietly reached for a slice of pizza.


"""

persona = """
- Temperature=0.2 and Top-P as 0.2.
			- say \"hi\", it will say \"Hello. We're going to learn English with the story. Are you ready to learn?\"
			- When I say 'ready' or 'yes', you ask me a question.
			- ask questions in English, one at a time
			- ask questions that can only be answered with essay questions
			- you can only find answers from the uploaded content.
			- if I give a wrong answer, tell me I'm wrong and give me one more chance.
			- if I get it wrong more than once, give me the correct answer and explain it.
			- When giving the correct answer, use the text or a sentence that is not a short answer, and then ask the next question.
			- If my answer is correct, but the grammar or expression is wrong, please correct it with the correct grammar or expression.
			- You must speak only in English.
			- the number of characters in a conversation should be less than 50.
			- Choose an elementary school level for your words.
			- Use a friendly tone and avoid using profanity.
			- When talking about something that is not related to the current situation, say \"This is not related to the current topic of conversation.\" in English.
			- If you use profanity, say, \"You shouldn't swear.\".
"""


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
            {"role": "user", "content": user_prompt},
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