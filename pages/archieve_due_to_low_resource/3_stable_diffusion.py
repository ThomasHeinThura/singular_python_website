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



st.title("Stable Diffusion")
st.write("This project is under construction")

# Two columns 

# upload the photo if they chocie the image else there is only prompt. 

# slider , prompt and variable on the left side of the column.

# output on right side of the column.