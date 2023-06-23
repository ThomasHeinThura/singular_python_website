import streamlit as st 

st.markdown(
    """
<style>
    # [data-testid="collapsedControl"] {display: none}
    MainMenu {visibility : hidden;}
    footer {visibility : hidden;}
    header {visibility : hidden}
</style>
    """,unsafe_allow_html=True,
)
st.cache_data.clear()


st.title("ETL pipline")
st.write("This project is under construction")