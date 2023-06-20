import streamlit as st
import torch
from transformers import pipeline

st.cache_data.clear()
st.title("Text Summerization")

# to do
# you have to make cache to reduce to model memory usage.
# Check if the model output is already in the cache

# ----- The whole text summerization will be here ----- #
base_model = "pszemraj/long-t5-tglobal-base-16384-book-summary" # This can change to other model
model = pipeline("summarization", base_model)

# input and submit button
text_input = st.text_area("Input text to summarization.", height=200)
submit = st.button("Submit")

def evaluate(Text_to_summarize):
    result = model(Text_to_summarize)
    del model
    return result[0]["summary_text"]

model_cache = {}

if 'model_output' in model_cache:
    output = model_cache['model_output']
else:
    # Perform the computation using the model
    # Replace this with your own code for model inference
    with st.spinner("Summarization the text..."):
        output = evaluate(text_input)  # final result from process
        # output = text_input.upper()
        st.text_area(label="Text Summarization Output", value=output, height=150)

            # Store the output in the cache for future requests
        model_cache['model_output'] = output


# ----------------------------------------------------- #



### have to watch streamlit nv bar
