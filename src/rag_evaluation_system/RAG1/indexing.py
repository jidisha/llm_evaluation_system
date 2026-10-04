import os
from dotenv import load_dotenv
from file_reader import extract_paragraph
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings

# abc = load_dotenv()  # Load environment variables from .env file
# print(os.getenv("OPENAI_API_KEY") is not None)
# print(f"Environment variables loaded successfully. {abc}")

embedding = OpenAIEmbeddings(model="text-embedding-3-large")
vector_store = InMemoryVectorStore(embedding)
chunks = extract_paragraph("../pdfs/Penguins_ACL.pdf")
vector_store.add_texts(chunks)
print(f"Number of chunks added to the vector store: {len(chunks)}")
