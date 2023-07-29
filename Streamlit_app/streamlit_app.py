import os
import streamlit as st
from langchain.llms import OpenAI
st.set_page_config(page_title="ML for Monsters Quick LLM App")
st.title('ML for Monsters Quick LLM App')

st.write(
    "Has environment variables been set:",
    os.environ["key"] == st.secrets["xyz"],
)

openai_api_key = st.secrets["xyz"]

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What do you call a communist cat?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)