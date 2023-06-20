# Home page
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Multipage App", page_icon=":tada:", layout="wide")
st.sidebar.success("select the pages")


# ----- Loading assets ------#
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_0yfsb3a1.json")
lottie_article = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_zSGy1w.json")


# ----- Intro SECTION ----- #
with st.container():
    left_col, right_col = st.columns(2)
    
    with right_col:
        st.image("https://avatars.githubusercontent.com/u/29223772?v=4")
        st.markdown("#### Hello there, I am Thomas Hein Thura :wave:")
        
        github_button = st.button(label=":sunglasses:")
        
    with left_col:
        st.title("A Freelance Machine Learning Engineer from Myanmar.")
        st.write(
        """
        Google-certified TensorFlow developer with a strong background in the medical field.
        Leveraging a broad knowledge of human physiology and pathology, 
        I am excited to apply my expertise in machine learning and deep learning to develop 
        innovative solutions that improve the quality of life.

        Email - thomas.h.thura@gmail.com

        𝑺𝑲𝑰𝑳𝑳𝑺 
        - Machine Learning Modeling (Scikit Learn), 
        - Deep Learning Modeling (CNN, NLP, Time Series, LLM, Transformer) with TensorFlow and PyTorch, 
        - Data Science, Statistical Analysis, Predictive Modeling,
        - Data Engineering (NumPy, Pandas, MLFlow, Prefect, SQL, SQLite, MongoDB, Prometheus),
        - Deployment (Docker, Kubernetes, AWS EC2, S3 bucket), 
        - Monitoring (EvidentlyAI, Grafana), 
        - Version Control and CI/CD (GitHub, Git), 
        - Data Visualization (Matplotlib, Seaborn), 
        - Python, Basic Concept of C++, Linux

        𝑺𝑶𝑭𝑻 𝑺𝑲𝑰𝑳𝑳𝑺 
        - As a founder of a local charity group, have confidence in communication and 
        organization skills, with a logical approach to problem-solving, time management, 
        leadership, and task prioritization skills.
        - Generalize real-time project issues and seek the best possible solutions.
        """
        )


# ------ Article Section ----- #
with st.container():
    st.write("---")
    st.subheader("The articles I wrote [@Medium](https://medium.com/@thomas.heinthura)")
    st.write("##")

    column_one, column_two, column_three, column_four = st.columns(4)
    with column_one:
        st.write(
        """
        <a href = "https://medium.com/@thomas.heinthura/do-you-really-need-a-data-storage-server-for-deep-learning-5bb5dc50c02d" >
        <img src = "https://miro.medium.com/v2/resize:fit:720/format:webp/1*6llGP0fQ-5kDe_nVBiqoqg.jpeg" 
        width="100%" height="50%">
        <p align= center > Do you really need a data storage server for deep learning </p>
        </a>
        """,unsafe_allow_html=True)

    with column_two:
        st.write(
        """
        <a href = "https://medium.com/@thomas.heinthura/server-for-deep-learning-a-deeper-insight-fcb8b7dbb93e" >
        <img src = "https://miro.medium.com/v2/resize:fit:720/format:webp/1*oie2fuMbIGM0jZOlx3uD6w.png" 
        width="100%" height="50%">
        <p align= center > Server for deep learning: A deeper insight </p>
        </a>
        """,unsafe_allow_html=True)


    with column_three:
        st.write(
        """
        <a href = "https://medium.com/@thomas.heinthura/changing-career-transition-is-challenging-93d35f6ac744/" >
        <img src = "https://miro.medium.com/v2/resize:fit:720/format:webp/1*QKMar94oUNu7bYTfX1xlDQ.jpeg" 
        width="100%" height="50%">
        <p align= center > Changing career transition is challenging!!! </p>
        </a>
        """,unsafe_allow_html=True)

    with column_four:
        st.lottie(lottie_article, key='article')


# ----- Projects Section ----- #
with st.container():
    st.write("---")
    st.subheader(
        "The projects I wrote [@Github](https://github.com/ThomasHeinThura?tab=repositories) "
    )
    st.write("##")

    column_one, column_two = st.columns(2)
    
    with column_one:
        # 1--------- #
        st.write(
        """
        <a href = "https://github.com/ThomasHeinThura/singular_python_website" >
        <img src = "https://github.com/ThomasHeinThura/singular_python_website/blob/main/assests/project/personal_website.jpg?raw=true" 
        width="100%" height="50%">
        </a>
        <h4 align= center > Singular python website </h4>
        """,unsafe_allow_html=True)
        
        # 2-------- #
        st.write(
        """
        <a href = "https://github.com/ThomasHeinThura/Text_summarization_website" >
        <img src = "https://github.com/ThomasHeinThura/singular_python_website/blob/main/assests/project/text_summarization.jpg?raw=true" 
        width="100%" height="50%">
        </a>
        <h4 align= center > Text summarization website </h4>
        """,unsafe_allow_html=True)
        
        # 3-------- #
        st.write(
        """
        <a href = "https://github.com/ThomasHeinThura/Credit-Card-Fraud-Detection" >
        <img src = "https://github.com/ThomasHeinThura/singular_python_website/blob/main/assests/project/credit.jpg?raw=true" 
        width="100%" height="50%">
        </a>
        <h4 align= center > Credit Card Fraud Detection </h4>
        """,unsafe_allow_html=True)

    with column_two:
        # 4-------- #
        st.write(
        """
        <a href = "https://github.com/ThomasHeinThura/Testing-automation-ETL-pipeline-and-CI-CD-with-docker" >
        <img src = "https://github.com/ThomasHeinThura/singular_python_website/blob/main/assests/project/ci_cd.jpg?raw=true" 
        width="100%" height="50%">
        </a>
        <h4 align= center > Test automation ETL CI CD </h4>
        """,unsafe_allow_html=True)
        
        # 5-------- #
        st.write(
        """
        <a href = "https://github.com/ThomasHeinThura/Tensorflow_projects" >
        <img src = "https://github.com/ThomasHeinThura/singular_python_website/blob/main/assests/project/tensorflow.jpg?raw=true" 
        width="100%" height="50%">
        </a>
        <h4 align= center > Tensorflow projects </h4>
        """,unsafe_allow_html=True)
 
        
        # 6-------- #
        st.write(
        """
        <a href = "https://github.com/ThomasHeinThura/Parkinson-s-Freezing-of-Gait-Prediction" >
        <img src = "https://github.com/ThomasHeinThura/singular_python_website/blob/main/assests/project/parkison.jpg?raw=true" 
        width="100%" height="50%">
        </a>
        <h4 align= center > Parkinson's Freezing of Gait Prediction </h4>
        """,unsafe_allow_html=True)


# ----- Education Section ----- #
with st.container():
    st.write("---")
    st.subheader("The projects I involved during University.")
    st.write("##")
    
    column_one, column_two = st.columns(2)
    
    with column_one:
        # 1--------- #
        st.write(
        """
        <a href = "https://www.linkedin.com/in/thomas-hein-thura/details/education/862177966/multiple-media-viewer/?profileId=ACoAAEBuTxMBogrV1SoierwuRXR3J9bNBmnpwnY&treasuryMediaId=1635518689240" >
        <img src = "https://media.licdn.com/dms/image/C562DAQF_KVeJoJ9_VA/profile-treasury-document-cover-images_480/0/1677852197447?e=1687852800&v=beta&t=QtK3bsTGXx0b8Orgvhfo4VfyaCVHwIFWB64RFNMYBik" 
        width="100%" height="50%">
        <p align= center > Research survery paper </p>
        </a>
        
        """,unsafe_allow_html=True)

        # 2--------- #
        st.write(
        """
        <a href = "https://www.linkedin.com/in/thomas-hein-thura/details/education/862177966/multiple-media-viewer/?profileId=ACoAAEBuTxMBogrV1SoierwuRXR3J9bNBmnpwnY&treasuryMediaId=1635518685908&type=DOCUMENT" >
        <img src = "https://media.licdn.com/dms/image/C562DAQGHk_6h2EhMjg/profile-treasury-document-cover-images_480/0/1677851950965?e=1687852800&v=beta&t=vYI54F7grdhcDTvc6xpkGiSyxw-Prv5F2yJBI_iDlbw" 
        width="100%" height="50%">
        <p align= center > Presentation : Research on Risk factors of acute coronary syndrome patients </p>
        </a>
       
        """,unsafe_allow_html=True)
    
    with column_two:
        # 1--------- #
        st.write(
        """
        <a href = "https://www.linkedin.com/in/thomas-hein-thura/details/education/862177966/multiple-media-viewer/?profileId=ACoAAEBuTxMBogrV1SoierwuRXR3J9bNBmnpwnY&treasuryMediaId=1635518690048&type=DOCUMENT" >
        <img src = "https://media.licdn.com/dms/image/C562DAQEOtuUwuh0V8A/profile-treasury-document-cover-images_480/0/1677852027257?e=1687852800&v=beta&t=EP04opKhkm5KKJoK6l2d2c95rplQwZ2g18hQlqSdNNM" 
        width="100%" height="50%">
        <p align= center > Poster : Research on Risk factors of acute coronary syndrome patients </p>

        </a>
        """,unsafe_allow_html=True)
        
        # 2--------- #
        st.write(
        """
        <a href = "https://www.linkedin.com/in/thomas-hein-thura/details/education/862177966/multiple-media-viewer/?profileId=ACoAAEBuTxMBogrV1SoierwuRXR3J9bNBmnpwnY&treasuryMediaId=1635518688326&type=DOCUMENT" >
        <img src = "https://media.licdn.com/dms/image/C562DAQGpaHu6M5Sz0g/profile-treasury-document-cover-images_480/0/1677851757852?e=1687852800&v=beta&t=kKoixC_0-ezCgARg8izN2gLx93KJVeVHTHRi3of7shs" 
        width="100%" height="50%">
        <p align= center > Presentation : Research of Effects of Mental Stress on Cardiovascular System </p>
        </a>
        """,unsafe_allow_html=True)



# ------ Charity Section ------ #
with st.container():
    st.write("---")
    st.subheader("The local charity group I found during University days.")
    st.write("##")
    
    column_one, column_two = st.columns(2)
    
    with column_one:
        st.write(
    """
    This is to write about summary on my charity
    """
        )
        pass
    
    
    with column_two:
        # 1--------- #
        st.write(
        """
        <a href = "https://www.linkedin.com/in/thomas-hein-thura/details/featured/1635518484926/single-media-viewer/?profileId=ACoAAEBuTxMBogrV1SoierwuRXR3J9bNBmnpwnY" >
        <img src = "https://media.licdn.com/dms/image/C562DAQEJpIQc2X7b7A/profile-treasury-document-cover-images_480/0/1677852890281?e=1687852800&v=beta&t=CehIgCbYe_59YeD7FNafvzjohXA8CwGpOcLPHOsbOcw" 
        width="100%" height="50%">
        <p align= center > Dream Charity Presentation Slide </p>
        </a>
        """,unsafe_allow_html=True)
