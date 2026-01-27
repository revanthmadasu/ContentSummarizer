import PyPDF2
import io
from sentence_transformers import SentenceTransformer

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
    return [chunks, embeddings]


def get_embeddings(chunks):
    """
    Takes a list of text chunks and returns their embeddings.
    """
    # Load a pre-trained model (you can choose others, e.g., 'all-MiniLM-L6-v2')
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks)
    return embeddings

