import streamlit as st

st.cache_data.clear()

st.set_page_config(
    page_title = "Multipage App",
    page_icon = ":tada:",
    layout = "wide"
)


st.sidebar.success("select the pages")

# ----- Intro SECTION ----- # 
with st.container():
    st.subheader("Hello there, I am Thomas Hein Thura :wave:")
    st.title("A Freelance Machine Learning Engineer from Myanmar.")
    st.write("I am passionate about finding ways to use Python")
    st.write("[Learn More in github >](https://github.com/ThomasHeinThura?tab=repositories)")
    st.markdown("### This is the test.")
    st.write(
    """
    I am the freelance machine learning engineer from myanmar that do blah blah blah
    - blah blah blah
    - blu blu blu
    - blal blal blal 
    """
    )
    ### Need to add contact section and all the link I have. And Introduction from others.
    ### add lottie file for animation 
    
# ------ Article Section ----- #
with st.container():
    st.write("---")
    st.subheader("The articles I write : ")
    st.write("##")
    
    st.write("The articles are :")
    


# ----- Projects Section ----- #
with st.container():
    st.write("---")
    st.subheader("The projects I write : ")
    st.write("##")

# ----- Education Section ----- # 
with st.container():
    st.write("---")
    st.subheader("The projects I involved during University.")
    st.write("##")

# ------ Charity Section ------ # 
with st.container():
    st.write("---")
    st.subheader("The local charity group I found during University days.")
    st.write("##")
