import csv

import streamlit as st
import pandas as pd

# pandas 란?
# 데이터 분석과 조작을 위해 설계된 파이썬 라이브러리
# 특히 구조화도니 데이터(표 형식) 처리에 특화
# dataFrame 이라는 구조를 중심으로 빠르고 직관적인 데이터 처리 및 분석을 지원한다

st.title('Data Visualization')

st.header('pandas `DataFrame`')

student_df = pd.DataFrame({
    'name':['홍길동', '이순신', '신사임당','V'],
    'age':[99, 300, 400, 32],
    'Score':[88, 99, 100, 99]
})

st.dataframe(student_df)

st.subheader('DataFrame + csv', divider=True)
sample_df = pd.read_csv('../02_data/annual-enterprise-survey-2023.csv')
st.dataframe(sample_df)

st.subheader('DataFrame 강조기능', divider=True)
data = {
    'Product': ['a', 'b', 'c','d'],
    'Sales':[500,300,400,600],
    'Growth(%)':[10, -5, 15, 7]
}
df = pd.DataFrame(data)
st.dataframe(df.style
             .highlight_max(subset=['Sales'], color='lightgreen')
             .highlight_min(subset=['Growth(%)'], color='pink')
             )

# 열 설정을 추가한 DataFrame 표시
st.dataframe(df, column_config={
    "Sales": st.column_config.NumberColumn("Total Sales", format="%d units"),
    "Growth(%)": st.column_config.NumberColumn("Growth Percentage", format="%.1f%%") #소수점 1자리까지 표현, %% -> %
}, width="stretch")


