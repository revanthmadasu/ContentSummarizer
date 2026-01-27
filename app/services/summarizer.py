import PyPDF2
import io
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

def extract_text_from_pdf(pdf_bytes):
    text = ""
    reader = PyPDF2.PdfReader(io.BytesIO(pdf_bytes))
    for page in reader.pages:
        page_text = page.extract_text()
        # print("Extracted page text:", page_text)  # Debugging line
        if page_text:
            text += page_text + "\n"
    return text

def chunk_text(text, chunk_size=1000):
    print(f"{text}")  # Debugging line
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def process_pdf_for_ollama(pdf_bytes, chunk_size=1000):
    text = extract_text_from_pdf(pdf_bytes)
    chunks = chunk_text(text, chunk_size)
    embeddings = get_embeddings(chunks)
    store_in_chromadb(chunks, embeddings)
    return [chunks, embeddings]


def get_embeddings(chunks):
    """
    Takes a list of text chunks and returns their embeddings.
    """
    # Load a pre-trained model (you can choose others, e.g., 'all-MiniLM-L6-v2')
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks)
    return embeddings

def store_in_chromadb(chunks, embeddings, collection_name="book_chunks"):
    client = chromadb.Client(Settings(
        persist_directory="./chromadb_data"  # Directory to store DB files
    ))
    collection = client.get_or_create_collection(collection_name)
    # Chroma expects embeddings as lists, not numpy arrays
    for idx, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        collection.add(
            documents=[chunk],
            embeddings=[embedding.tolist()],
            ids=[f"chunk_{idx}"]
        )

def retrieve_chunks_from_chromadb(query, collection_name="book_chunks", top_k=5):
    """
    Given a query string, retrieves the top_k most relevant chunks from ChromaDB.
    """
    # Load embedding model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode([query])[0]

    # Connect to ChromaDB
    client = chromadb.Client(Settings(
        persist_directory="./chromadb_data"
    ))
    collection = client.get_or_create_collection(collection_name)

    # Query ChromaDB for similar chunks
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k,
        include=["documents", "distances"]
    )

    # Return the top_k chunks (documents)
    return results["documents"][0] if results["documents"] else []