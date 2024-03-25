import streamlit as st 
from pandasai import SmartDataframe
from langchain_community.llms import Ollama
import os
import pandas as pd

os.environ["PANDASAI_API_KEY"] = "" #Your API Key Here 

llm = Ollama(model="mistral")


def chat_with_csv(df,prompt):
    llm = Ollama(model="mistral")
    sdf = SmartDataframe(df, config={"llm": llm})
    result = sdf.chat(prompt)
    print(result)
    return result

st.set_page_config(layout='wide')

st.title("CellTalk: Unraveling Data, One Conversation at a Time")

input_csv = st.file_uploader("Upload your CSV file", type=['csv'])

if input_csv is not None:

        col1, col2 = st.columns([1,1])

        with col1:
            st.info("CSV Uploaded Successfully")
            data = pd.read_csv(input_csv)
            st.dataframe(data, use_container_width=True)

        with col2:

            st.info("Chat Below")
            
            input_text = st.text_area("Enter your query")

            if input_text is not None:
                if st.button("Chat with CSV"):
                    st.info("Your Query: "+input_text)
                    result = chat_with_csv(data, input_text)
                    st.success(result)
