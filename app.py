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
In the dynamic world of artificial intelligence, LangChain has emerged as a transformative framework that is revolutionizing how developers and researchers approach generative and agentic intelligence. 
Developed as an open-source library, LangChain addresses the critical challenge of transforming large language models from simple text generators into sophisticated, context-aware intelligent systems. 
At its core, the framework provides a modular architecture that allows developers to chain together multiple AI components, create dynamic workflows, and build applications that transcend traditional prompt-response interactions. 
The magic of LangChain lies in its ability to introduce advanced prompt engineering techniques, sophisticated memory management, and powerful reasoning capabilities that enable AI agents to autonomously navigate complex tasks. 
By providing robust abstractions like agents, tools, chains, and memory mechanisms, LangChain empowers developers to create intelligent systems that can reason, learn, and adapt across various domains. 
From intelligent research assistants and advanced customer support systems to complex data analysis tools and creative content generation platforms, LangChain is bridging the gap between raw computational power and meaningful, context-aware intelligence. 
Its technical sophistication is matched by its potential to democratize access to advanced AI capabilities, offering developers a flexible framework to explore the frontiers of artificial intelligence. 
As the field of generative AI continues to evolve, LangChain stands at the forefront, representing not just a technological innovation, but a paradigm shift in how we conceptualize and implement intelligent computing systems. 
The framework challenges traditional boundaries by enabling AI agents to understand context, make nuanced decisions, and interact with external resources in ways that were previously unimaginable. 
While the potential is immense, LangChain also demands a thoughtful approach that prioritizes ethical AI development, robust error handling, and a deep understanding of the complex interactions between language models and intelligent applications. 
For developers and researchers alike, LangChain offers an exciting pathway into the future of artificial intelligence, where machines can not just process information, but truly understand, reason, and interact in increasingly sophisticated ways.
"""

blog2 = """
In the rapidly evolving landscape of technological innovation, Agentic AI emerges as a groundbreaking paradigm that transcends traditional computational boundaries, reimagining artificial intelligence as more than just a tool—but as an autonomous, adaptive, and intelligent system capable of complex reasoning and independent decision-making. Unlike conventional AI models that primarily respond to direct inputs, agentic AI represents a quantum leap in machine intelligence, enabling systems to understand context, formulate strategies, and take proactive actions with a level of sophistication that mirrors human cognitive processes.

The fundamental essence of Agentic AI lies in its ability to move beyond reactive computation to a more dynamic, self-directed approach. These intelligent systems are designed to not just process information, but to comprehend complex scenarios, generate multiple potential solutions, evaluate their efficacy, and execute strategies with minimal human intervention. This represents a profound shift from traditional programming models, where every action is predefined, to a more fluid, adaptive intelligence that can learn, improvise, and evolve in real-time.

At the core of Agentic AI are several transformative capabilities that distinguish it from previous generations of artificial intelligence. These systems leverage advanced machine learning algorithms, sophisticated natural language processing, and intricate reasoning frameworks to create AI agents that can break down complex problems, understand nuanced contexts, and develop multi-step action plans. The intelligence is not just about processing speed or data retrieval, but about cognitive flexibility, strategic thinking, and the ability to navigate uncertain and dynamic environments.

The potential applications of Agentic AI span across virtually every domain of human endeavor. In scientific research, these intelligent agents can autonomously design experiments, analyze complex datasets, and generate hypotheses that might take human researchers years to conceptualize. In healthcare, agentic AI systems could develop personalized treatment strategies, predict potential health risks, and even coordinate complex medical interventions with unprecedented precision. Financial markets could witness AI agents that not only analyze market trends but dynamically adjust investment strategies in real-time, considering global economic fluctuations and micro-level market sentiments.

However, the rise of Agentic AI is not without its profound ethical and philosophical implications. As these systems become more autonomous and sophisticated, critical questions emerge about accountability, decision-making transparency, and the fundamental boundaries between human and machine intelligence. The development of these systems demands a multidisciplinary approach that integrates technological innovation with robust ethical frameworks, ensuring that the pursuit of intelligent autonomy remains aligned with human values and societal well-being.

The technological foundations of Agentic AI are built upon several cutting-edge computational paradigms. Large language models provide the linguistic and contextual understanding, while advanced machine learning algorithms enable continuous adaptation and learning. Reinforcement learning techniques allow these systems to improve their decision-making capabilities through iterative interactions, much like how humans learn from experience. Neural networks with complex architectures enable these agents to recognize patterns, predict outcomes, and generate creative solutions that go beyond traditional algorithmic approaches.

One of the most exciting aspects of Agentic AI is its potential for interdisciplinary collaboration. By creating intelligent systems that can understand and integrate knowledge from multiple domains, we are witnessing the emergence of a new form of computational intelligence that can bridge gaps between scientific disciplines, generate novel insights, and solve complex, multifaceted problems that have historically challenged human cognition.

As we stand on the cusp of this technological revolution, Agentic AI represents more than just a technological advancement—it symbolizes a fundamental reimagining of intelligence itself. These systems challenge our understanding of cognition, problem-solving, and the very nature of intelligent behavior. They invite us to expand our conception of intelligence beyond human-centric models, recognizing that cognitive capabilities can manifest in forms that are both familiar and radically different from our own.

The journey of Agentic AI is just beginning, and its trajectory promises to be as unpredictable as it is exciting. As researchers, developers, and philosophers continue to explore this emerging field, we are not just developing new technologies—we are participating in a profound exploration of intelligence, consciousness, and the complex interplay between human creativity and computational potential.
"""

blog3 = """
In the annals of technological evolution, few innovations have captured the global imagination quite like Generative AI. This groundbreaking technology has emerged as a transformative force that is fundamentally reshaping how we create, innovate, and conceptualize human potential across virtually every domain of human endeavor. Far more than a mere technological tool, generative AI represents a paradigm shift that blurs the boundaries between human creativity and machine intelligence, offering unprecedented capabilities that are simultaneously awe-inspiring and profoundly disruptive.

The essence of Generative AI lies in its remarkable ability to create entirely new content—be it text, images, music, code, or complex designs—that is indistinguishable from human-generated work. Unlike traditional AI systems that primarily analyze and process existing information, generative models can produce original, contextually relevant, and often breathtakingly creative outputs. This capability is rooted in advanced machine learning techniques, particularly deep neural networks and transformer models, which have been trained on massive datasets, enabling them to understand and replicate intricate patterns of human creativity.

Across industries, the impact of Generative AI has been nothing short of revolutionary. In creative fields, artists, musicians, and designers are discovering powerful new collaborators that can generate initial concepts, overcome creative blocks, and explore design possibilities that might never have been conceived through traditional methods. Writers are using AI to draft complex narratives, overcome writer's block, and explore multiple narrative directions simultaneously. Graphic designers can now generate complex visual concepts with minimal manual input, dramatically reducing production time and expanding creative possibilities.

The technology's influence extends far beyond creative industries. In healthcare, generative AI is being used to design potential drug compounds, simulate complex biological interactions, and even generate personalized treatment plans. Scientific researchers are leveraging these models to generate hypotheses, design experiments, and explore complex scientific scenarios that would take human researchers years to conceptualize. In engineering and design, generative AI can create optimized architectural designs, generate complex engineering solutions, and simulate potential outcomes with unprecedented precision.

Perhaps most profound is the technology's impact on education and knowledge creation. Generative AI serves as an intelligent tutor, capable of creating personalized learning materials, generating explanatory content across complex subjects, and providing adaptive learning experiences that can be tailored to individual learning styles. Language barriers are being dismantled as these systems can instantaneously translate and generate content across multiple languages, promoting global communication and understanding.

The economic implications are equally transformative. Industries are witnessing unprecedented productivity gains as generative AI automates complex creative and analytical tasks. Startup ecosystems are experiencing a renaissance, with entrepreneurs leveraging AI to rapidly prototype ideas, generate business plans, and create minimum viable products with minimal resources. Small businesses can now access sophisticated marketing materials, content generation, and design capabilities that were previously available only to large corporations with substantial creative teams.

However, the rise of Generative AI is not without significant ethical and philosophical challenges. Questions of originality, intellectual property, and the nature of creativity itself are being fundamentally challenged. Artists and creators are grappling with the implications of AI-generated content, raising critical discussions about authorship, compensation, and the intrinsic value of human creativity. There are legitimate concerns about potential job displacement, the potential for misinformation, and the ethical use of AI-generated content.

The technological sophistication behind Generative AI is rooted in complex machine learning architectures like Generative Adversarial Networks (GANs), transformer models, and diffusion models. These systems learn by understanding intricate patterns within massive datasets, developing an almost intuitive understanding of creative domains. The training process involves complex optimization techniques that allow these models to generate outputs that are not mere replications but genuinely novel interpretations.

As we stand at the cusp of this technological revolution, Generative AI represents more than just a technological tool—it is a mirror reflecting our understanding of creativity, intelligence, and human potential. It challenges us to reimagine the boundaries between human and machine creativity, offering a glimpse into a future where innovation is a collaborative dance between human intuition and machine intelligence.

The journey of Generative AI is still in its early stages, with each passing month bringing breakthrough innovations that expand our understanding of what's possible. As researchers, creators, and innovators continue to explore and refine these technologies, we are collectively writing a new chapter in the story of human innovation—one where the line between human and artificial creativity becomes increasingly blurred, and the potential for creation becomes limitless.
"""

if selected=="Blogs":
    blogbox1 = st.container(border=True)
    blogbox2 = st.container(border=True)
    blogbox3 = st.container(border=True)
    with st.container():
        with blogbox1:
            st.header("LangChain: Bridging the Gap Between Language Models and Intelligent Applications")
            if st.button("Generate", key="b1"):
                         st.write_stream(stream_data(blog1))
        st.write("---")
        with blogbox2:
            st.header("Agentic AI: Unleashing the Cognitive Frontier of Artificial Intelligence")
            if st.button("Generate", key="b2"):
                         st.write_stream(stream_data(blog2))
        # st.write(blog2)
        st.write("---")
        with blogbox3:
            st.header("Generative AI: The Transformative Force Rewriting the Rules of Creation")
            if st.button("Generate", key="b3"):
                st.write_stream(stream_data(blog3))
        st.write("---")

if selected=="Quotes":
    with st.container():
        st.header("THE RAREST OF ALL HUMAN QUALITIES IS CONSISTENCY")
        st.write("---")
    
        

