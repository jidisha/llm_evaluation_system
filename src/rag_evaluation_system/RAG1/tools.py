from .indexing import vector_store
from langchain.tools import tool

last_retrieved_context = []


@tool
def collection_info(query: str) -> str:
    """Retrieves information from the PDF based on the given query."""
    global last_retrieved_context
    results = vector_store.similarity_search(query, k=3)
    if not results:
        last_retrieved_context = []
        return "I could not find the answer in the pdf."

    last_retrieved_context = [result.page_content for result in results]
    return " ".join(last_retrieved_context)
