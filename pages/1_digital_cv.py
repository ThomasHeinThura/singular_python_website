import streamlit as st 


st.cache_data.clear()
st.title("Digital CV")
st.write("This project is under construction")
st.write(
    """
    Thomas Hein Thura
    Machine Learning Engineer     
    Email: thomas.h.thura@gmail.com   
    Location - Myanmar   
    Phone: +959448000829   
    ThomasHeinThura@LinkedIn | ThomasHeinThura@Kaggle 	ThomasHeinThura@GitHub | ThomasHeinThura@Medium
    """
)

# ------ SUmmary Section ------ #
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
    st.subheader("Education and Achievement")
    st.write(
        """
        **English** - Business Level proficiency, Myanmar - Native  
        Education - Final year medical student University of Medicine 2, Yangon, MBBS ([projects, paper, presentation](https://www.linkedin.com/in/thomas-hein-thura/details/education/))  
        Achievement - Google TensorFlow Developer Certificate ([Google TensorFlow developer certificate link](https://www.credential.net/17949d75-18f5-45be-83e9-61c95919cb38))  
        CURRENT PROJECTS (Freelance + Personal) - Projects on UW-Madison GI Tract Image Segmentation, Brain tumour detection  
        """
    )