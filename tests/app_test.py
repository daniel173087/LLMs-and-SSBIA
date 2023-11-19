import streamlit as st
import chromadb
from chromadb.utils import embedding_functions
import pandas as pd
import numpy as np

#open the vector database
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                api_key="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",
                model_name="text-embedding-ada-002"
            )

chroma_client = chromadb.PersistentClient(path="/modules")

collection = chroma_client.get_collection(
    name="report_embedding_automated",
    embedding_function=openai_ef
    )
if "messages" not in st.session_state:
    st.session_state.messages = []



def query_chroma_db(user_input):
    query_result = collection.query(query_texts=[user_input], n_results=3)

    return query_result

def display_chat():
    for message in st.session_state.messages:
        style = {} if message['sender'] == 'user' else {'bg_color': '#F0F2F6'}
        st.text_area("", value=message['text'], height=50, key=message['text'], **style)

def send_message(user_input):
    st.session_state.messages.append({'sender': 'user', 'text': user_input})
    
    db_response = query_chroma_db(user_input)
    st.session_state.messages.append({'sender': 'gpt', 'text': db_response})

# Streamlit UI layout
st.title('GPT Chat Interface with Chroma DB')

user_input = st.text_input("Type your message here:", key="user_input")

if st.button('Send'):
    if user_input:
        send_message(user_input)
        st.experimental_rerun()

display_chat()