# Home page
# import library
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import requests # this library is for animation pic 



st.set_page_config(page_title = "Thomas Hein Thura", 
                   page_icon = ":sun_with_face:",
                   layout="wide") # page become wide

# removing the header and footer
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

# option header bar 
selected = option_menu(
    None,
    options=["Home", "Articles", "Github", "Edu"],
    icons=['house', 'book-half', "github", 'mortarboard'],
    default_index=0, 
    orientation="horizontal"
)

# ----- Loading assets ------#
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_0yfsb3a1.json")
lottie_article = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_zSGy1w.json")


# ----- Intro Home SECTION ----- #
if selected == "Home":
    with st.container():
        left_col, right_col = st.columns(2)
        
        with right_col: # photo
            st.image("https://avatars.githubusercontent.com/u/29223772?v=4")
            st.markdown("#### Hello there, I am Thomas Hein Thura :wave:")
            
            """
            link icon 
            I took five cols even though it need only four. 
            The last fifth col is just take space to look nice in UI
            The code and link are hard coded. you can add your link in 
            - url link
            - photo link
            """
            one, two, three, four,five = st.columns([1,1,1,1,7.5])    
            
            with one: 
                st.write( # This is for github png and button
                """
                <a href = "https://github.com/ThomasHeinThura" >
                <img src = "https://i.pinimg.com/736x/b5/1b/78/b51b78ecc9e5711274931774e433b5e6.jpg" 
                width="50%" height="50%">
                </a>
                """,unsafe_allow_html=True)
                    
            with two:
                st.write( # This is for LinkedIn png and button
                """
                <a href = "https://www.linkedin.com/in/thomas-hein-thura/" >
                <img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/640px-LinkedIn_logo_initials.png"
                width="50%" height="50%">
                </a>
                """,unsafe_allow_html=True)
            
            with three:
                st.write( # This is for kaggle png and button
                """
                <a href = "https://www.kaggle.com/heinthura" >
                <img src = "https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/189_Kaggle_logo_logos-512.png"
                width="50%" height="50%">
                </a>
                """,unsafe_allow_html=True)
            
            with four:
                st.write( # This is for medium png and button
                """
                <a href = "https://medium.com/@thomas.heinthura" >
                <img src = "https://seeklogo.com/images/M/medium-2020-new-icon-logo-454E46D050-seeklogo.com.png"
                width="50%" height="50%">
                </a>
                """,unsafe_allow_html=True)
                
                
            
        with left_col: # You can edit your introduction 
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
if selected == "Articles":
    with st.container():
        st.write("---")
        st.subheader("The articles I wrote [@Medium](https://medium.com/@thomas.heinthura)")
        st.write("##")

        """
        To get clickable photo with caption, This section is hard coded. 
        You can your link in this pattern
        - link
        - img
        - label or title or caption
        """
        column_one, column_two, column_three, column_four = st.columns(4)
        with column_one:
            st.write( # article 1
            """
            <a href = "https://medium.com/@thomas.heinthura/do-you-really-need-a-data-storage-server-for-deep-learning-5bb5dc50c02d" >
            <img src = "https://miro.medium.com/v2/resize:fit:720/format:webp/1*6llGP0fQ-5kDe_nVBiqoqg.jpeg" 
            width="100%" height="50%">
            <p align= center > Do you really need a data storage server for deep learning </p>
            </a>
            """,unsafe_allow_html=True)

        with column_two:
            st.write( # article 2
            """
            <a href = "https://medium.com/@thomas.heinthura/server-for-deep-learning-a-deeper-insight-fcb8b7dbb93e" >
            <img src = "https://miro.medium.com/v2/resize:fit:720/format:webp/1*oie2fuMbIGM0jZOlx3uD6w.png" 
            width="100%" height="50%">
            <p align= center > Server for deep learning: A deeper insight </p>
            </a>
            """,unsafe_allow_html=True)


        with column_three:
            st.write( # article 3
            """
            <a href = "https://medium.com/@thomas.heinthura/changing-career-transition-is-challenging-93d35f6ac744/" >
            <img src = "https://miro.medium.com/v2/resize:fit:720/format:webp/1*QKMar94oUNu7bYTfX1xlDQ.jpeg" 
            width="100%" height="50%">
            <p align= center > Changing career transition is challenging!!! </p>
            </a>
            """,unsafe_allow_html=True)

        with column_four: # animation
            st.lottie(lottie_article, key='article')


# ----- Projects Section ----- #
if selected == "Github":
    with st.container():
        st.write("---")
        st.subheader( # this section also is hard coded
            "The projects I wrote [@Github](https://github.com/ThomasHeinThura?tab=repositories) "
        )
        st.write("##")

        column_one, column_two = st.columns(2)
        
        with column_one:
            st.write( # 1--------- #
            """
            <a href = "https://github.com/ThomasHeinThura/singular_python_website" >
            <img src = "https://github.com/ThomasHeinThura/singular_python_website/blob/main/assests/project/personal_website.jpg?raw=true" 
            width="100%" height="50%">
            </a>
            <h4 align= center > Singular python website </h4>
            """,unsafe_allow_html=True)
            
            st.write( # 2-------- #
            """
            <a href = "https://github.com/ThomasHeinThura/Text_summarization_website" >
            <img src = "https://github.com/ThomasHeinThura/singular_python_website/blob/main/assests/project/text_summarization.jpg?raw=true" 
            width="100%" height="50%">
            </a>
            <h4 align= center > Text summarization website </h4>
            """,unsafe_allow_html=True)
            
            st.write( # 3-------- #
            """
            <a href = "https://github.com/ThomasHeinThura/Credit-Card-Fraud-Detection" >
            <img src = "https://github.com/ThomasHeinThura/singular_python_website/blob/main/assests/project/credit.jpg?raw=true" 
            width="100%" height="50%">
            </a>
            <h4 align= center > Credit Card Fraud Detection </h4>
            """,unsafe_allow_html=True)

        with column_two:
            st.write(  # 4-------- #
            """
            <a href = "https://github.com/ThomasHeinThura/Testing-automation-ETL-pipeline-and-CI-CD-with-docker" >
            <img src = "https://github.com/ThomasHeinThura/singular_python_website/blob/main/assests/project/ci_cd.jpg?raw=true" 
            width="100%" height="50%">
            </a>
            <h4 align= center > Test automation ETL CI CD </h4>
            """,unsafe_allow_html=True)
            
            st.write(  # 5-------- #
            """
            <a href = "https://github.com/ThomasHeinThura/Tensorflow_projects" >
            <img src = "https://github.com/ThomasHeinThura/singular_python_website/blob/main/assests/project/tensorflow.jpg?raw=true" 
            width="100%" height="50%">
            </a>
            <h4 align= center > Tensorflow projects </h4>
            """,unsafe_allow_html=True)
    
            st.write( # 6-------- #
            """
            <a href = "https://github.com/ThomasHeinThura/Parkinson-s-Freezing-of-Gait-Prediction" >
            <img src = "https://github.com/ThomasHeinThura/singular_python_website/blob/main/assests/project/parkison.jpg?raw=true" 
            width="100%" height="50%">
            </a>
            <h4 align= center > Parkinson's Freezing of Gait Prediction </h4>
            """,unsafe_allow_html=True)


# ----- Education Section ----- #
if selected == "Edu":
    with st.container():
        st.write("---")
        st.subheader("The projects I involved during University.")
        st.write("##")
        
        column_one, column_two = st.columns(2)
        
        with column_one:
            st.write( # 1 research paper #
            """
            <a href = "https://www.linkedin.com/in/thomas-hein-thura/details/education/862177966/multiple-media-viewer/?profileId=ACoAAEBuTxMBogrV1SoierwuRXR3J9bNBmnpwnY&treasuryMediaId=1635518689240" >
            <img src = "https://github.com/ThomasHeinThura/singular_python_website/blob/main/assests/article/final_part_one_paper.jpg?raw=true" 
            width="100%" height="50%">
            <p align= center > Research survey paper </p>
            </a>
            """,unsafe_allow_html=True)

            st.write( # 2 Presentation ACS #
            """
            <a href = "https://www.linkedin.com/in/thomas-hein-thura/details/education/862177966/multiple-media-viewer/?profileId=ACoAAEBuTxMBogrV1SoierwuRXR3J9bNBmnpwnY&treasuryMediaId=1635518685908&type=DOCUMENT" >
            <img src = "https://github.com/ThomasHeinThura/singular_python_website/blob/main/assests/article/third_year_presentation.jpg?raw=true" 
            width="100%" height="50%">
            <p align= center > Presentation : Research on Risk factors of acute coronary syndrome patients </p>
            </a>
            """,unsafe_allow_html=True)
        
        with column_two:
            st.write( # 3 Poster #
            """
            <a href = "https://www.linkedin.com/in/thomas-hein-thura/details/education/862177966/multiple-media-viewer/?profileId=ACoAAEBuTxMBogrV1SoierwuRXR3J9bNBmnpwnY&treasuryMediaId=1635518690048&type=DOCUMENT" >
            <img src = "https://github.com/ThomasHeinThura/singular_python_website/blob/main/assests/article/third_year_poster.jpg?raw=true" 
            width="100%" height="50%">
            <p align= center > Poster : Research on Risk factors of acute coronary syndrome patients </p>
            </a>
            """,unsafe_allow_html=True)
            
            
            st.write( # 4 Presentation CVS #
            """
            <a href = "https://www.linkedin.com/in/thomas-hein-thura/details/education/862177966/multiple-media-viewer/?profileId=ACoAAEBuTxMBogrV1SoierwuRXR3J9bNBmnpwnY&treasuryMediaId=1635518688326&type=DOCUMENT" >
            <img src = "https://github.com/ThomasHeinThura/singular_python_website/blob/main/assests/article/second_year_2.jpg?raw=true" 
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
            <img src = "https://github.com/ThomasHeinThura/singular_python_website/blob/main/assests/article/dream_charity_presentation.jpg?raw=true" 
            width="100%" height="50%">
            <p align= center > Dream Charity Presentation Slide </p>
            </a>
            """,unsafe_allow_html=True)
