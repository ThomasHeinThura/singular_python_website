import streamlit as st 
from pathlib import Path

# page setup
st.set_page_config(page_title="Digital CV", 
                   page_icon=":sunglasses:")


# Remove header and footer
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

# ----- Path settings ----- #
Asia_resume_file = "assests/Thomas_Hein_Thura_CV_Asia_1_July_2023-F.pdf"
US_resume_file = "assests/Thomas_Hein_Thura_CV_EU_US_1_July_2023-F.pdf"

# ------ Load pdf file ------ #
with open(Asia_resume_file, "rb") as pdf_file_asia:
    PDFbyte_Asia = pdf_file_asia.read()

with open(US_resume_file, "rb") as pdf_file_us:
    PDFbyte_us = pdf_file_us.read()


# UI Start
with st.container():
    left_col, right_col = st.columns(2)
    
    with right_col: # Image of own photo, you can add your photo link
        st.image("https://avatars.githubusercontent.com/u/29223772?v=4")
        
        one, two, three, four = st.columns([1,1,1,1])    # This is same pattern as clickable photo and button in home page
        with one: 
            st.write(
            """
            <a href = "https://github.com/ThomasHeinThura" >
            <img src = "https://i.pinimg.com/736x/b5/1b/78/b51b78ecc9e5711274931774e433b5e6.jpg" 
            width="50%" height="50%">
            </a>
            """,unsafe_allow_html=True)
                
        with two:
            st.write(
            """
            <a href = "https://www.linkedin.com/in/thomas-hein-thura/" >
            <img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/640px-LinkedIn_logo_initials.png"
            width="50%" height="50%">
            </a>
            """,unsafe_allow_html=True)
        
        with three:
            st.write(
            """
            <a href = "https://www.kaggle.com/heinthura" >
            <img src = "https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/189_Kaggle_logo_logos-512.png"
            width="50%" height="50%">
            </a>
            """,unsafe_allow_html=True)
        
        with four:
            st.write(
            """
            <a href = "https://medium.com/@thomas.heinthura" >
            <img src = "https://seeklogo.com/images/M/medium-2020-new-icon-logo-454E46D050-seeklogo.com.png"
            width="50%" height="50%">
            </a>
            """,unsafe_allow_html=True)
        
    with left_col:
        
        st.title("Digital CV")
        st.subheader("Thomas Hein Thura")
        st.subheader("Machine Learning Engineer")
        st.write(
        """
        Email: thomas.h.thura@gmail.com   
        Location - Myanmar   
        Phone: +959448000829   
        """
        )
        # CV pdf download button
        st.download_button(
            label = "Download for Asia CV form with photo",
            data = PDFbyte_Asia,
            file_name = Asia_resume_file,
            mime = "application/octet-stream"
            )
            
        st.download_button(
            label = "Download for US EU CV form",
            data = PDFbyte_us,
            file_name = US_resume_file,
            mime = "application/octet-stream"
            )
        

"""
The following section doesn't have heavy techniques.
You simply add your notes, summary in st.write
"""

# ------ Summary Section ------ #
with st.container():
    st.write("---")
    st.subheader("Summary")
    st.write(
    """
    - Google-certified TensorFlow developer, machine learning enthusiast and 
    Linux enthusiast with a strong background in the medical field, 
    seeking a challenging position as a Machine Learning Engineer.  
    
    - Experienced in developing, optimizing, and automating data pipelines, 
    ETL solutions, and model data stores. Proficient in utilizing Big Data technologies 
    and integrating data from various sources. Passionate about advancing analytic performance 
    and contributing to the strategic goals of organizations.  
    
    - Seeking a challenging position to apply my expertise 
    in machine learning, data analytics, and data platform development.

    """
        
    )

# ------ Skill section ------ #
with st.container():
    st.write("---")
    st.subheader("𝑺𝑲𝑰𝑳𝑳𝑺")
    st.write(
    """
    - Machine Learning Modeling (Scikit Learn), 
    - Deep Learning Modeling (CNN, NLP, Time Series, LLM, Transformer) with TensorFlow and PyTorch, 
    - Data Science, Statistical Analysis, Predictive Modeling,
    - Data Engineering (NumPy, Pandas, MLFlow, Prefect, SQL, SQLite, MongoDB, Prometheus),
    - Deployment (Docker, Kubernetes, AWS EC2, S3 bucket), 
    - Monitoring (EvidentlyAI, Grafana), 
    - Version Control and CI/CD (GitHub, Git), 
    - Data Visualization (Matplotlib, Seaborn), 
    - Python, Basic Concept of C++, Linux
    """
    )

# ------ Experience Project sectoin ------ #
with st.container():
    st.write("---")
    st.subheader("EXPERIENCE PROJECTS ")
    st.write(
    """
    Freelance Machine Learning Engineer and Data scientist	(November 2021- Present):  
    - Successfully solved industry-complex data storage, data modeling, 
    and machine learning problems using machine learning and deep learning techniques.

    - Developed a fraud detection classification model for local bank sectors, 
    optimizing accuracy, reducing false positives, and addressing data engineering workload.

    - Implemented an automatic ETL pipeline using AWS services, 
    reducing the data engineering workload by 10% and ensuring real-time data accuracy.

    - Built a Text Summarization website as a personal hobby project, 
    leveraging natural language processing techniques and testing with state-of-the-art models.

    - Utilized oversampling and undersampling techniques to address imbalanced datasets in insurance premium payments 
    and credit card fraud datasets, improving model generalization by 30% and achieving 99% accuracy.

    - Completed various TensorFlow CV and NLP projects, 
    including CIFAR10 classification, sign language classification, GI tract X-ray segmentation, IMDb film rating classifications, 
    Reuters documents with articles classification, sarcasm tweet detection, disaster tweet classification, and BBC articles classification.

    - Developed models for weather temperature detection 
    and energy price detection using time series analysis.

    - Currently working on projects on UW-Madison GI Tract Image Segmentation 
    and brain tumour detection, and ETL automation pipeline in local bank sectors.
    """
    )

# ------ Soft Skills Section ------ #
with st.container():
    st.write("---")
    st.subheader("𝑺𝑶𝑭𝑻 𝑺𝑲𝑰𝑳𝑳𝑺")
    st.write(
    """
    - As a founder of a local charity group, have confidence in communication and 
    organization skills, with a logical approach to problem-solving, time management, 
    leadership, and task prioritization skills.
    - Generalize real-time project issues and seek the best possible solutions.
    """
    )

# ------ Education and Achievemnet ------ #
with st.container():
    st.write("---")
    st.subheader("Education and Achievement")
    st.write(
    """
    - **English** - Business Level proficiency, Myanmar - Native  
    - **Education** - Final year medical student University of Medicine 2, Yangon, MBBS ([projects, paper, presentation](https://www.linkedin.com/in/thomas-hein-thura/details/education/))  
    - **Achievement** - Google TensorFlow Developer Certificate ([Google TensorFlow developer certificate link](https://www.credential.net/17949d75-18f5-45be-83e9-61c95919cb38))  
    - **CURRENT PROJECTS (Freelance + Personal)** - Projects on UW-Madison GI Tract Image Segmentation, Brain tumour detection  
    """
    )