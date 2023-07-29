import os
import streamlit as st
from langchain.llms import OpenAI

#Streamlit "st." is a library of templates for easy app development and deployment
st.set_page_config(page_title="ML for Monsters Quick LLM App")
st.title('ml-for-monsters.streamlit.app')

openai_api_key = st.secrets["xyz"]

#the below is a simple function for retrieving a response from OpenAI's GPT models
def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

#the input to the UX forms on the webapp are assigned to components
#generate_response() is used to hit OpenAI's API endpoint
with st.form('my_form'):
  text = st.text_area('Enter text:', 'What do you call a communist cat?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)