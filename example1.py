## integrate our code with openai api
import os 
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


os.environ["OPENAI_API_KEY"]=openai_key

# streamlit framework

st.title("Search")
input_text = st.text_input("search the topic you want")

# Prompt Template

first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="tell me about the {name}"
)

# Prompt Template

# second_input_prompt = PromptTemplate(
#     input_variables=['person'],
#     template="when was {person} born"
# )

# OPENAI LLM
# temprature is telling us that how much the control agent should have while providing you the o/p

llm = OpenAI(temperature=0.8)
chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person')
# result1 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob')


# Prompt Template

second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template="when was {person} born"
)

chain1 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob')
parent_chain = SequentialChain(chains=[chain, chain1], input_variables=['name'], output_variables=['person', 'dob'], verbose=True)

if input_text:
    st.write(parent_chain({"name":input_text}))
