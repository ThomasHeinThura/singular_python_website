import streamlit as st 
import torch
from transformers import pipeline

st.title("Text Summerization")

text_input = st.text_area("Input text to summarization.", height = 400)
submit = st.button("Submit")

# ----- The whole text summerization will be here ----- #

base_model = "pszemraj/long-t5-tglobal-base-16384-book-summary" ## you can download and save pertrained is another options
model = pipeline(
    "summarization",    
    base_model,
    device=0 if torch.cuda.is_available() else -1,)

def evaluate(Text_to_summarize):
    result = model(Text_to_summarize)
    return result[0]["summary_text"]

# ----------------------------------------------------- #

# output =  evaluate(text_input) # final result from process
output = text_input.upper()

st.text_area(
    label = "Text Summarization Output",
    value = output,
    height = 350
             )

### have to watch streamlit nv bar