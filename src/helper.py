import os
from git import Repo
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import LanguageParser
from langchain.text_splitter import Language
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()

HF_TOKEN= os.getenv('HF_TOKEN')
os.environ['HF_TOKEN']= HF_TOKEN


#clone any github repositories 
import os
import shutil
import psutil
from git import Repo

def close_file_handles(path):
    """Close processes locking files in the given directory."""
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            for open_file in proc.open_files():
                if path in open_file.path:
                    print(f"Killing process {proc.info['name']} (PID: {proc.info['pid']})")
                    proc.kill()
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue

def repo_ingestion(repo_url):
    repo_path = "repo/"
    
    # Ensure the repo folder is deleted completely
    if os.path.exists(repo_path):
        print("Attempting to delete existing repo...")
        close_file_handles(repo_path)
        shutil.rmtree(repo_path, ignore_errors=False)
        print(f"Deleted existing '{repo_path}' directory.")
    
    os.makedirs(repo_path, exist_ok=True)
    
    print(f"Cloning repository from {repo_url} into '{repo_path}'...")
    Repo.clone_from(repo_url, to_path=repo_path)
    print("Repository cloned successfully.")






#Loading repositories as documents
def load_repo(repo_path):
    loader = GenericLoader.from_filesystem(repo_path,
                                        glob = "**/*",
                                       suffixes=[".py"],
                                       parser = LanguageParser(language=Language.PYTHON, parser_threshold=500)
                                        )
    
    documents = loader.load()

    return documents




#Creating text chunks 
def text_splitter(documents):
    documents_splitter = RecursiveCharacterTextSplitter.from_language(language = Language.PYTHON,
                                                             chunk_size = 2000,
                                                             chunk_overlap = 200)
    
    text_chunks = documents_splitter.split_documents(documents)

    return text_chunks



#loading embeddings model
def load_embedding():
    embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings
