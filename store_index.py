import os
import shutil
from src.helper import repo_ingestion, load_repo, text_splitter, load_embedding
from dotenv import load_dotenv
from langchain.vectorstores import Chroma

load_dotenv()

GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

DB_DIRECTORY = './db'

def clear_vector_db():
    # Remove existing database directory if it exists
    if os.path.exists(DB_DIRECTORY):
        shutil.rmtree(DB_DIRECTORY)
        print("Cleared existing vector database.")

# Ingest new repository
# repo_url = "https://github.com/entbappy/End-to-end-Medical-Chatbot-Generative-AI"
# repo_ingestion(repo_url)

# Clear existing vector database
clear_vector_db()

# Load documents and embeddings for the new repo
documents = load_repo("repo/")
text_chunks = text_splitter(documents)
embeddings = load_embedding()

# Store vectors in Chroma DB
vectordb = Chroma.from_documents(text_chunks, embedding=embeddings, persist_directory=DB_DIRECTORY)
vectordb.persist()
print("New vector database created and persisted.")
