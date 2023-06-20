# Home page
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image




st.set_page_config(page_title="Multipage App", page_icon=":tada:", layout="wide")
st.sidebar.success("select the pages")


# ----- Loading assets ------#
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl(
    "https://assets5.lottiefiles.com/packages/lf20_0yfsb3a1.json"
)
lottie_article = load_lottieurl(
    "https://assets5.lottiefiles.com/private_files/lf30_zSGy1w.json"
)


# ----- Intro SECTION ----- #
with st.container():
    left_col, right_col = st.columns(2)
    
    with right_col:
        st.image("https://avatars.githubusercontent.com/u/29223772?v=4")
        st.subheader("Hello there, I am Thomas Hein Thura :wave:")
        
    with left_col:
        st.title("A Freelance Machine Learning Engineer from Myanmar.")
        st.write("I am passionate about finding ways to use Python")
        st.write(
            """
        Google-certified TensorFlow developer with a strong background in the medical field.
        Leveraging a broad knowledge of human physiology and pathology, 
        I am excited to apply my expertise in machine learning and deep learning to develop 
        innovative solutions that improve the quality of life.

        Email - thomas.h.thura@gmail.com

        𝑺𝑲𝑰𝑳𝑳𝑺
        - Data engineering with NumPy, Pandas, MLFlow, Prefect, 
        SQL, SQLite, MongoDB, Prometheus, 
        - Deployment with docker, Kubernetes, 
        - Monitoring with EvidentlyAI, Grafana, 
        - Version and CI/CD with GitHub, Git, AWS(EC2, S3 bucket.), 
        - Machine Learning modeling with Scikit Learn,
        - Deep learning modelling(CNN, NLP, Time Series, LLM, Transformer) 
        with TensorFlow and PyTorch,
        - Data visualization with Matplotlib and seaborn, python, basic concept of C++, 

        𝑺𝑶𝑭𝑻 𝑺𝑲𝑰𝑳𝑳𝑺 
        - As a founder of a local charity group, have confidence in communication and 
        organization skills, with a logical approach to problem-solving, time management, 
        leadership, and task prioritization skills.
        - Generalize real-time project issues and seek the best possible solutions.
        """
        )
        
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
    - la la la 
    - Oh la la 
    """
    )
    # Need to add contact section and all the link I have.

# ------ Article Section ----- #
with st.container():
    st.write("---")
    st.subheader(
        "The articles I write [@Medium](https://medium.com/@thomas.heinthura) "
    )
    st.write("##")

    column_one, column_two, column_three, column_four = st.columns(4)
    # with column_one:
    st.markdown(
        "[Do you really need a data storage server for deep learning](https://medium.com/@thomas.heinthura/do-you-really-need-a-data-storage-server-for-deep-learning-5bb5dc50c02d)"
    )
    st.image(
        "https://miro.medium.com/v2/resize:fit:720/format:webp/1*6llGP0fQ-5kDe_nVBiqoqg.jpeg"
    )

    # with column_two:
    st.markdown(
        "[Server for deep learning: A deeper insight](https://medium.com/@thomas.heinthura/server-for-deep-learning-a-deeper-insight-fcb8b7dbb93e)"
    )
    st.image(
        "https://miro.medium.com/v2/resize:fit:720/format:webp/1*oie2fuMbIGM0jZOlx3uD6w.png"
    )

    # with column_three:
    st.write(
        "[![Changing career transition is challenging!!!](https://miro.medium.com/v2/resize:fit:720/format:webp/1*QKMar94oUNu7bYTfX1xlDQ.jpeg)](https://medium.com/@thomas.heinthura/changing-career-transition-is-challenging-93d35f6ac744/)", 
        # height = 100,
        # width = 100
            )
        
        # st.image(
        #     "https://miro.medium.com/v2/resize:fit:720/format:webp/1*QKMar94oUNu7bYTfX1xlDQ.jpeg"
        # )

    # with column_four:
    st.lottie(lottie_article, height=300, key='article')


# ----- Projects Section ----- #
with st.container():
    st.write("---")
    st.subheader(
        "The projects I write [@Github](https://github.com/ThomasHeinThura?tab=repositories) "
    )
    st.write("##")

    column_one, column_two = st.columns(2)
    image = Image.open('assests/project/personal_website.jpg')
    # with column_one:
        # --------- #
    st.markdown(
        "[![Personal website project](https://github.com/ThomasHeinThura/singular_python_website/blob/main/assests/project/personal_website_480.jpg?raw=true)](https://github.com/ThomasHeinThura/singular_python_website)"
    )
    
    # st.markdown("[![Foo](https://github.com/ThomasHeinThura/singular_python_website/blob/main/assests/project/personal_website.jpg?raw=true)](https://github.com/ThomasHeinThura/singular_python_website/)")
    
    
    
    # st.image("assests/project/personal_website.jpg")
    # -------- #
    st.markdown(
        "[Text Summarization website](https://github.com/ThomasHeinThura/Text_summarization_website)"
    )
    st.image("assests/project/text_summarization.jpg")
        # -------- #

    st.markdown(
        "[Credit Card Fraud Detection](https://github.com/ThomasHeinThura/Credit-Card-Fraud-Detection)"
    )
    st.image("assests/project/credit.jpg")
    # -------- #

    # with column_two:
        # -------- #
    st.markdown(
        "[ETL pipeline and CI CD project](https://github.com/ThomasHeinThura/Testing-automation-ETL-pipeline-and-CI-CD-with-docker/)"
    )
    st.image("assests/project/ci_cd.jpg")
    # -------- #
    st.markdown(
        "[Tensorflow Projects](https://github.com/ThomasHeinThura/Tensorflow_projects)"
    )
    st.image("assests/project/tensorflow.jpg")

    st.markdown(
        "[My kaggle solution for Parkinson's Freezing of Gait](https://github.com/ThomasHeinThura/Parkinson-s-Freezing-of-Gait-Prediction)"
    )
    st.image("assests/project/parkison.jpg")


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
