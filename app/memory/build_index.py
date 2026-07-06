from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings

from langchain_community.vectorstores import FAISS


# Folder containing company knowledge
MEMORY_DIR = Path(__file__).resolve().parent.parent / "memory_data"

documents = []

# Load every .txt file
for file in MEMORY_DIR.glob("*.txt"):

    loader = TextLoader(str(file), encoding="utf-8")
    documents.extend(loader.load())

print(f"Loaded {len(documents)} documents")


# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")


# Create embeddings
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


# Build FAISS index
vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)


# Save index
vectorstore.save_local("app/memory/memory_index")

print("FAISS index created successfully!")