# Home page
import streamlit as st


st.set_page_config(page_title="Multipage App", page_icon=":tada:", layout="wide")


st.sidebar.success("select the pages")

# ----- Intro SECTION ----- #
with st.container():
    st.subheader("Hello there, I am Thomas Hein Thura :wave:")
    st.title("A Freelance Machine Learning Engineer from Myanmar.")
    st.write("I am passionate about finding ways to use Python")
    st.write(
        "[Learn More in github >](https://github.com/ThomasHeinThura?tab=repositories)"
    )
    st.markdown("### This is the test.")
    st.write(
        """
    I am the freelance machine learning engineer from myanmar that do blah blah blah
    - blah blah blah
    - blu blu blu
    - blal blal blal 
    """
    )
    # Need to add contact section and all the link I have.
    # And Introduction from others.
    # add lottie file for animation

# ------ Article Section ----- #
with st.container():
    st.write("---")
    st.subheader("The articles I write : ")
    st.write("##")
    # st.markdown("[![Foo](https://github.com/ThomasHeinThura/singular_python_website/blob/main/assests/ci_cd.jpg?raw=true)](https://github.com/ThomasHeinThura/Testing-automation-ETL-pipeline-and-CI-CD-with-docker/)")

    st.write("The articles are :")
    column_one, column_two, column_three, column_four, column_five = st.columns(5)
    with column_one:
        st.markdown(
            "[Personal website project](https://github.com/ThomasHeinThura/singular_python_website)"
        )
        st.image("assests/personal_website.jpg")

    with column_two:
        st.markdown(
            "[ETL pipeline and CI CD project](https://github.com/ThomasHeinThura/Testing-automation-ETL-pipeline-and-CI-CD-with-docker/)"
        )
        st.image("assests/ci_cd.jpg")

        pass

    with column_three:
        st.write("column_three")
        pass

    with column_four:
        st.write("column four")
        pass

    with column_five:
        st.write("column five")
        pass


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

with st.container():
    st.write("---")
    st.subheader("This wil be example")
    st.write("###")
