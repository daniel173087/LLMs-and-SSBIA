import openai
import streamlit as st


st.set_page_config(page_title="questions to existing views")
st.sidebar.header("questions to existing views")

st.title("ChatGPT-like chat")

openai.api_key = st.secrets["API_Key"]

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

st.session_state.messages.append({"role": "system", "content": "You are a database expert for a large industry company from Germany. You will get sql views and should answer questions only regarding these files!"})

for i in st.session_state.view_values:
    st.session_state.messages.append({"role": i["role"], "content": i["content"]})
 


if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})