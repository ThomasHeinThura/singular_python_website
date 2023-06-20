import streamlit as st
import torch
from transformers import pipeline

st.cache_data.clear()
st.title("Text Summerization")

# to do
# you have to make cache to reduce to model memory usage.


# ----- The whole text summerization will be here ----- #
base_model = "pszemraj/long-t5-tglobal-base-16384-book-summary"
model = pipeline("summarization", base_model)


def evaluate(Text_to_summarize):
    # with st.spinner("Loading the model ......"):
    result = model(Text_to_summarize)
    return result[0]["summary_text"]


# ----------------------------------------------------- #

text_input = st.text_area("Input text to summarization.", height=200)
submit = st.button("Submit")

if submit:
    with st.spinner("Summarization the text..."):
        output = evaluate(text_input)  # final result from process
        # output = text_input.upper()

        st.text_area(label="Text Summarization Output", value=output, height=150)

### have to watch streamlit nv bar
