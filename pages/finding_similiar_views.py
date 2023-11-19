import sqlparse
import streamlit as st
from chroma_db_from_views_raw import get_collection


st.set_page_config(page_title="finding similiar views")

st.sidebar.header("finding similiar views")

collection = get_collection()

st.title("similarity comparison for views")
st.subheader("When creating new views or any SQL Statements for existing systems you can use this software to check whether something similiar already exists")

def get_similiar_views(input):
    query = collection.query(query_texts=[input], n_results=3)
    return query

def clear_field_value():
    st.session_state["field_value"] = ""

def format_sql(code_input):
     formatted_code = sqlparse.format(code_input, reindent=True)
     return formatted_code

if "view_values" not in st.session_state:
    st.session_state.view_values = []



with st.form("question"):
    st.session_state.view_values = []
    st.write("Give your own view definition which should be checked with existing ones")
    new_view = st.text_area("Give your own view definition which should be checked with existing ones", key="field_value" ,height=400)
    submitted = st.form_submit_button("Senden")
    values = []

    if submitted:
        
        first_word = new_view.split()[0]
        if first_word.lower() == "create":
            existing_views = get_similiar_views(new_view)
            for i in range(0, len(existing_views["ids"][0])):
                entry = existing_views["metadatas"][0][i]["view_content"]
                st.session_state.view_values.append({"role":"user", "content": entry})
                with st.container():
                    result = format_sql(existing_views["metadatas"][0][i]["view_content"])
                    
                    st.code(result, language="sql")
       
        else:
            st.write("Please insert a valid SQL statement")

if submitted:
    st.write("if you have questions to these views go to tab <<questions to existing views>>")







