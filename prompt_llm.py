import os
from langchain import hub
import pprint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
prompt = hub.pull('rlm/rag-prompt')

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY") 
model = ChatGroq(model = 'qwen-qwq-32b')
def format_docs(relevant_chunks):
    relevant_doc = "\n".join([doc.page_content for doc in relevant_chunks])
    return relevant_doc
    
def generate_response(retriever):
    rag_chain=(
        {'context':retriever|format_docs,'question':RunnablePassthrough()}
        |
        prompt
        |
        model
        |
        StrOutputParser()
    )
    return rag_chain
    
