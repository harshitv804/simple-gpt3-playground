import streamlit as st
import openai

openai.api_key= st.secrets["apikey"]

st.set_page_config(page_title="Simple GPT-3 Playground", page_icon="GPT-3-favicon.png")
st.title("Simple GPT-3 Playground")

user_message = st.text_input("Enter the prompt",key="text")
def generate_answer():
    if len(user_message) !=0:
        result = openai.Completion.create(engine="text-davinci-003", prompt=user_message, max_tokens=500)
        st.write(result.choices[0].text)
    else:
        pass

def clear_text():
    st.session_state["text"] = ""

st.button("Process",on_click=generate_answer())
st.button("Clear All", on_click=clear_text)

