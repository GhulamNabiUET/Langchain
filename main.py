## integrate our code with openai api
import os 
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

# streamlit framework

st.title("Langchain Demo with OpenAi API")
input_text = st.text_input("search the topic you want")


# OPENAI LLM
# temprature is telling us that how much the control agent should have while providing you the o/p

llm = OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))
