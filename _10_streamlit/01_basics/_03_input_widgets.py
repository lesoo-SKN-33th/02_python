import streamlit as st

st.title('Input widgets')
st.header('button', divider='rainbow')

# 버튼 생성 + 입력값 저장
clicked = st.button("Click Me")
print('clicked:',clicked)

# streamlit 의 경우 사용자와 상호작용 시 soft refresh되어
# input또는 click 등의 동작 수행 시 reload 되어 코드를 다시 읽는다
if clicked:
    st.write('버튼 클릭 됨')
else:
    st.write('아직 버튼 안누름!')

# button 두개 만드니까 하나 누를대마다 다른 버튼 초기화 되는거 개오바
clicked2 = st.button("Click Me2")
print('clicked2:',clicked)

if clicked2:
    st.write('버튼 클릭 됨')
else:
    st.write('아직 버튼 안누름!')

st.button('Reset', type='primary')

st.subheader('Text Input', divider='rainbow')

# 얘는 리로드 돼도 값이 안바뀜
destination = st.text_input(label="가고싶은 여행지", placeholder="여행지를 입력하세요")
st.write("입력된 여행지: ", destination)

st.subheader('Text Area', divider='rainbow')
txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
)

st.write(f"You wrote {len(txt)} characters.")

st.subheader('Radio Button', divider='rainbow')

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")

st.header('SelectBox')
# 선택 박스
mbti = st.selectbox(
    '당신의 MBTI는 무엇입니까?',
    ('ISTJ', 'ISFJ', 'INFJ', 'INTJ',
     'ISTP', 'ISFP', 'INFP', 'INTP',
     'ESTP', 'ESFP', 'ENFP', 'ENTP',
     'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ',
     '모름'),
    index=7
)
if mbti:
    st.write(f'선택한 MBTI는 :red[{mbti}]입니다.')

st.subheader('Check box')
agree = st.checkbox("I agree")

if agree:
    st.write("Great!")

st.subheader('Color Picker')
color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)



