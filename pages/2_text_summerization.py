import streamlit as st
# import torch
# from transformers import pipeline

st.set_page_config(page_title="Text summerization", page_icon="📜")

st.markdown(
    """
<style>
    MainMenu {visibility : hidden;}
    footer {visibility : hidden;}
    header {visibility : hidden}
</style>
    """,unsafe_allow_html=True)

st.cache_data.clear()
st.title("Text Summerization")


# # TODO: you have to make cache to reduce to model memory usage. 
# # TODO: Check if the model output is already in the cache
 

# # ----- The whole text summerization will be here ----- #
# with st.container():
#     base_model = "pszemraj/long-t5-tglobal-base-16384-book-summary" # This can change to other model

#     if 'model' not in st.session_state:
#         st.session_state['model'] = pipeline("summarization", base_model)

#     # input and submit button
#     text_input = st.text_area("Input text to summarization.", height=200)
#     submit = st.button("Submit")

# def evaluate(Text_to_summarize):
#     result = st.session_state['model'](Text_to_summarize)
#     return result[0]["summary_text"]

# with st.container():
#     if submit:
#         with st.spinner("Summarization the text..."):
#             output = evaluate(text_input)  # final result from process
#             st.text_area(label="Text Summarization Output", value=output, height=150)


# # ----------------------------------------------------- #