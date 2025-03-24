import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import time

st.set_page_config(layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json() 

lottie_loader = load_lottieurl("https://lottie.host/353802f9-b26e-4b0e-8a70-ffafb5de768e/2poy6FrsEo.json")
lottie_loader2 = load_lottieurl("https://lottie.host/71738967-3ac7-4d0b-8575-966de19b97e0/kiXgOnUw7Z.json")
header_ani = load_lottieurl("https://lottie.host/ffc18d17-c4da-4c89-9ccf-ad8bc1049595/ExIAIVoHhL.json")
image = Image.open("Screenshot 2025-03-24 024654.png")
# image2 = Image.open("E:\Portfolio\Portfolio - Streamlit\Images\unnamed (1).jpg")
image2 = Image.open("Screenshot 2025-03-24 042423.png")
main , starter =  st.columns(2)
with main:
    # st_lottie(header_ani, height=150, width= 300)
    st.title("Nishant B. Surwade")
    st.write("Welcome to My AI Portfolio! I'm a Generative AI & Agentic AI Engineer passionate about building cutting-edge AI solutions, from LLMs and RAG systems to multi-agent automation and scalable AI deployments. Explore my projects and innovations!", )
    st.write("---")
    st.write("Connect with me...")
    gmail, linked, insta, github, tweet= st.columns(5)
    with gmail:
        st.button("",use_container_width=True,icon=":material/mail:")
    with linked:
        st.button("linked-in",use_container_width=True)
    with insta:
        st.button("insta", use_container_width=True)
    with github:
        st.link_button("github","https://github.com/Nishant982001", use_container_width=True)
    with tweet:
        st.button("X", use_container_width=True)
with starter:
    st_lottie(lottie_loader2, height=385, width=700)

st.write('---')
with st.container():
    selected = option_menu(
        menu_title=None,
        options= ['About','Projects','Blogs','Quotes'],
        icons=['person','code-slash','feather','pin'],
        orientation='horizontal'
    )

edu = """
B.E. Artificial Intelligence & Data Science, June 2024 (K.K.W.I.E.E.R., SPPU)                           Nashik, Maharashtra
Cumulative GPA: 8.12                               
"""

text = """
1. Expert in Generative AI and Agentic AI, specializing in LLMs like GPT-4, LLaMA-3, Claude, Gemini-Pro, and frameworks such as LangChain, CrewAI, LangGraph. 

2. Proficient in vector search & retrieval using ChromaDB, Pinecone, FAISS, Neo4j, CassandraDB, with deep expertise in Retrieval-Augmented Generation (RAG) and Hybrid Search (BM25 + Dense Retrieval). 

3. Hands-on experience with NVIDIA NIM, OpenAI, Groq, Hugging Face for optimizing AI workflows. 

4. Skilled in model fine-tuning, deployment, and orchestration using PyTorch, TensorFlow and ONNX, with advanced MLOps pipelines via Docker, Kubernetes, MLflow, and Ray Serve. 

5. Experienced in multimodal AI with Whisper, CLIP, DALL·E, Stable Diffusion, and SpeechBrain, and deploying scalable AI solutions on AWS, Azure, and GCP. 

6. Strong in data engineering with Apache Spark, Dask, Pandas, and NumPy, ensuring high-performance AI applications.

"""

achiev2 = """ 
RUNNER UP - RDP IIT BOMBAY TECHFEST 2022 IN ASSOCIATION WITH TATA SONS\n - Built the given problem statement Research Discovery Platform and Being the only team from Maharashtra, and youngest off all the other teams, we honoured to achieve the 2nd position with a cash prize. 

WINNER - GMRT & IIK PUNE ORGANISED NATIONAL LEVEL SCIENCE PROJECT COMPETITION\n - Secured 1st Place among the 650 projects from 329 institutions and 9 states. Our team of four built fluent and ecofriendly mechanism for cleaning and managing the floating trash in river without disrupting the traffic and harming the aquatic life.
"""

soci = """
INDIAN SOCIETY FOR TECHNICAL EDUCATION. (ISTE). Nashik, Maharashtra\r\n 
Core Committee Member (Nov 2022 - Jun 2024)\r\n
•	Organised four events and led promotional activities; Footfall: 1500+\r\n
•	Mentored 14 selected students over 100 days to enhance their various skills for annual flagship event Master Students Program. Being the part of 30 members committee I was able to upscale my Management, Leadership, Coordination skills. 

"""
def stream_data(tex):
    for word in tex.split(" "):
        yield word + " "
        time.sleep(0.03)

if selected == 'About':
    # col1, col2  = st.columns(2)
    # with col1:
    st.subheader("Click To Generate The Response")
    education, skills, workex, achiev, society = st.columns(5)
    mainbox = st.container( border=True, height=300 )
    with education:
        if st.button("Education",use_container_width=True):
           with mainbox:
               (st.write_stream(stream_data(edu)))
    with skills:
        if st.button("Skills",use_container_width=True):
            with mainbox:
                st.write_stream(stream_data(text))
    with workex:
        if st.button("workex",use_container_width=True):
            with mainbox:
                st.write_stream(stream_data(text))
    with achiev:
        if st.button("Achievements",use_container_width=True):
            with mainbox:
                st.write_stream(stream_data(achiev2))
    with society:
        if st.button("Socienties",use_container_width=True):
            with mainbox:
                st.write_stream(stream_data(soci)) 
    # with st.container(border=True,height=300):
    #     if st.button("click"):
    #         st.write_stream(stream_data(text))
        # with col2:
        #     st_lottie(lottie_loader, height=400, width=800,)
    st.write("---")

    with st.container():
        col3,col4 = st.columns(2)

if selected == "Projects":
    with st.container():
        st.subheader("My Personal Projects")
        col5 , col6 = st.columns({1,2})
        with col5:
            st.image(image)
        with col6:
            st.subheader("AI-BlogCrafter-Multi-Agent-YouTube-to-Blog-Automation")
            st.write("""
                    Built with a combination of CrewAI, Langchain, OpenAI's GPT models, and Streamlit,
                    this application demonstrates how multiple AI agents can work together 
                    to accomplish complex tasks that would typically require significant human effort.
                    """)
            col11, col12, col13 = st.columns(3)
            with col11: 
                st.link_button("Github Repo","https://github.com/Nishant982001/AI-BlogCrafter-Multi-Agent-YouTube-to-Blog-Automation",use_container_width=True) 
            with col12: 
                st.link_button("View Demo","https://ai-blogcrafter.streamlit.app/",use_container_width=True)
            with col13:
                st.link_button("Comments","",use_container_width=True)
        st.write("---")    
        
        col7 , col8 = st.columns({1,2})
        with col7:
            st.image(image2)
        with col8:
            st.subheader("NVIDIA-NIM-RAG-AI-Powered-Document-Querying-with-FAISS")
            st.write("""
                    What if AI could retrieve precise answers instantly using the best-suited model for your task? Introducing NVIDIA NIM Explorer, an AI-powered document retrieval system that combines NVIDIA NIM’s cutting-edge LLMs, FAISS vector search, and LangChain to enable customizable, efficient, and context-aware Q&A from large text corpora.
                    """)
            col21, col22, col23 = st.columns(3)
            with col21:
                st.link_button("Github Repo","https://github.com/Nishant982001/NVIDIA-NIM-RAG-AI-Powered-Document-Querying-with-FAISS",use_container_width=True)
            with col22:
                st.link_button("View Demo","https://ai-blogcrafter.streamlit.app/",use_container_width=True)
            with col23:
                st.link_button("Comments","",use_container_width=True)
        st.write("---")  

        

