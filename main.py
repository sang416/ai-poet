import streamlit as st 
from langchain_openai import ChatOpenAI
import streamlit.components.v1 as components
from streamlit_extras.buy_me_a_coffee import button

components.iframe("https://ads-partners.coupang.com/widgets.html?id=816332&template=carousel&trackingCode=AF7997393", width=680, height=140)
st.write("이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다.")
st.title("시 작성기")
st.subheader(".....by Sanggyun Lee")
st.write("---")
button(username="sang416", floating=True, width=221)
st.logo(image="kakaopay.jpg", link="https://qr.kakaopay.com/Ej7ksNnpA138809698",size="large")
chat_model = ChatOpenAI()

content = st.text_input("시 작성을 위한 키워드를 입력해주세요.")

if st.button("시 작성 요청하기") :
    with st.spinner("시 작성 중...") :
        result = chat_model.invoke(content + "에 대한 시를 써주세요.")
        st.write(result.content)
