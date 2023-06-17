## integrate our code with openai api
import os 
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st
from langchain import PromptTemplate
from langchain.chains import LLMChain

os.environ["OPENAI_API_KEY"]=openai_key

# streamlit framework

st.title("Search")
input_text = st.text_input("search the topic you want")

# Prompt Template

first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="tell me about the {name}"
)

# OPENAI LLM
# temprature is telling us that how much the control agent should have while providing you the o/p

llm = OpenAI(temperature=0.8)
result = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True)

if input_text:
    st.write(result.run(input_text))
