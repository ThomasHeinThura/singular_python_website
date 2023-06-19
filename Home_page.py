import streamlit as st

st.set_page_config(
    page_title = "Multipage App",
    page_icon = ":tada:",
    layout = "wide"
)

st.title("Main Page")
st.sidebar.success("select the pages")

# ----- HEADER SECTION ----- # 
st.subheader("Hello there, I am Thomas Hein Thura :wave:")
