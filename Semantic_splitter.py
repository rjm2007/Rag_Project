import os
from dotenv import load_dotenv
load_dotenv()
from loader import extract_from_pdf
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings


os.environ['HUGGING_FACE_TOKEN'] = os.getenv('HUGGING_FACE_TOKEN')

embeddings= HuggingFaceEmbeddings(model= 'allenai-specter')

text_splitter = SemanticChunker(embeddings)



def Semantic_split(all_docs):
    pages = text_splitter.split_documents(documents = all_docs)
    return pages

