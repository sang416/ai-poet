import streamlit as st 
from langchain_openai import ChatOpenAI

st.title("시 작성기")
chat_model = ChatOpenAI()

content = st.text_input("시 작성을 위한 키워드를 입력해주세요.")

if st.button("시 작성 요청하기") :
    with st.spinner("시 작성 중...") :
        result = chat_model.invoke(content + "에 대한 시를 써주세요.")
        st.write(result.content)
