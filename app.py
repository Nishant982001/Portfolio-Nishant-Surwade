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
image3 = Image.open("Screenshot 2025-03-24 042423.png")
main , starter =  st.columns(2)
with main:
    # st_lottie(header_ani, height=150, width= 300)
    st.title("Nishant B. Surwade")
    st.write("Welcome to My AI Portfolio! I'm a Generative AI & Agentic AI Engineer passionate about building cutting-edge AI solutions, from LLMs and RAG systems to multi-agent automation and scalable AI deployments. Explore my projects and innovations!", )
    st.write("---")
    st.write("Connect with me...")
    gmail, linked, insta, github, tweet= st.columns(5)
    with gmail:
        st.link_button("","mailto:nishantsurwade982001@gmail.com",use_container_width=True,icon=":material/mail:")
    with linked:
        st.link_button("LINKEDIN","https://www.linkedin.com/in/nishantsurwade8314/",use_container_width=True)
    with insta:
        st.link_button("INSTA","https://www.instagram.com/nishant_surwade.exe/", use_container_width=True)
    with github:
        st.link_button("GITHUB","https://github.com/Nishant982001", use_container_width=True)
    with tweet:
        st.link_button("X","https://x.com/INishantSurwade", use_container_width=True)
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
RUNNER UP - RDP IIT BOMBAY TECHFEST 2022 IN ASSOCIATION WITH TATA SONS 
- Built the given problem statement Research Discovery Platform and Being the only team from Maharashtra, and youngest off all the other teams, we honoured to achieve the 2nd position with a cash prize. 

WINNER - GMRT & IIK PUNE ORGANISED NATIONAL LEVEL SCIENCE PROJECT COMPETITION 
- Secured 1st Place among the 650 projects from 329 institutions and 9 states. Our team of four built fluent and ecofriendly mechanism for cleaning and managing the floating trash in river without disrupting the traffic and harming the aquatic life.
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
    skills, achiev, society, education = st.columns(4)
    mainbox = st.container( border=True, height=300 )
    
    with skills:
        if st.button("Skills",use_container_width=True):
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
    with education:
        if st.button("Education",use_container_width=True):
           with mainbox:
               (st.write_stream(stream_data(edu)))
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

        col9 , col10 = st.columns({1,2})
        with col9:
            st.image(image2)
        with col10:
            st.subheader("RAG-PDFChat: AI-Powered Q&A with Contextual Memory")
            st.write("""
                    RAG-PDFChat is an advanced AI-powered chatbot that enables context-aware question answering over PDFs using Retrieval-Augmented Generation (RAG). It combines LangChain, ChromaDB, Groq API (Gemma-2B-IT), and Hugging Face embeddings to provide precise, multi-turn responses while maintaining chat history for contextual memory..
                    """)
            col31, col32, col33 = st.columns(3)
            with col31:
                st.link_button("Github Repo","https://github.com/Nishant982001/NVIDIA-NIM-RAG-AI-Powered-Document-Querying-with-FAISS",use_container_width=True)
            with col32:
                st.link_button("View Demo","https://ai-blogcrafter.streamlit.app/",use_container_width=True)
            with col33:
                st.link_button("Comments","",use_container_width=True)
        st.write("---") 


blog1 = """
LangChain: Bridging the Gap Between Language Models and Intelligent Applications
In the rapidly evolving landscape of artificial intelligence, LangChain has emerged as a groundbreaking framework that is transforming how developers and researchers approach generative AI and agentic intelligence. This powerful open-source library is not just another tool—it's a game-changer that is reshaping our understanding of how language models can be integrated into sophisticated, intelligent systems.
The Genesis of LangChain
Born out of the need to create more complex and capable AI applications, LangChain addresses a critical challenge in the world of generative AI: turning large language models from simple text generators into intelligent, context-aware agents capable of complex reasoning and task completion.
Key Features That Set LangChain Apart
1. Modular Component Architecture
LangChain's most significant innovation is its modular design. The framework provides a comprehensive set of abstractions that allow developers to:

Chain together multiple AI components
Create dynamic workflows
Build context-aware applications that go beyond simple prompt-response interactions

2. Advanced Prompt Management
Unlike traditional approaches, LangChain introduces sophisticated prompt engineering techniques:

Dynamic prompt templates
Context-aware prompt generation
Ability to create complex reasoning chains that break down intricate tasks into manageable steps

3. Memory and State Management
One of the most powerful features of LangChain is its robust memory management:

Conversation memory tracking
State preservation across multiple interactions
Context retention that enables more nuanced and contextually rich interactions

Revolutionizing Agentic AI
LangChain is at the forefront of the agentic AI revolution, enabling the creation of AI agents that can:

Autonomously reason and make decisions
Execute multi-step tasks
Interact with external tools and APIs
Learn and adapt based on context

Real-World Applications
The potential applications of LangChain are vast and transformative:

Intelligent research assistants that can navigate complex information landscapes
Customer support systems that understand context and provide personalized solutions
Complex data analysis tools that can interpret and synthesize information
Creative writing and content generation platforms with unprecedented depth and understanding

Technical Architecture
At its core, LangChain provides several key abstractions:

Agents: Intelligent systems that can make decisions and take actions
Tools: Interfaces for agents to interact with external resources
Chains: Sequences of calls that combine multiple components to create advanced workflows
Memory: Mechanisms to maintain state and context across interactions

The Future of Generative AI
LangChain represents more than just a technological advancement—it's a paradigm shift in how we conceptualize artificial intelligence. By providing a flexible framework for building intelligent applications, it democratizes access to advanced AI capabilities.
Challenges and Considerations
While LangChain offers incredible potential, developers must be mindful of:

Ethical AI development
Proper context management
Handling complex edge cases
Ensuring robust error handling

Getting Started with LangChain
For developers eager to explore this transformative technology, the journey begins with:

Understanding the core concepts
Experimenting with simple chains
Gradually building more complex agentic systems
Engaging with the vibrant LangChain community

Conclusion
LangChain is not just a library—it's a bridge to the future of intelligent computing. As generative AI continues to evolve, frameworks like LangChain will be crucial in translating the raw potential of large language models into practical, intelligent applications that can truly understand, reason, and interact.
The age of agentic AI is here, and LangChain is leading the charge.
"""

if selected=="Blogs":
    with st.container():
        st.title("LangChain: Bridging the Gap Between Language Models and Intelligent Applications") 
        st.write(blog1)
    
        

