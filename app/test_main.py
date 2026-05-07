from app.services import summarizer
import numpy as np

def test_real_book():
    with open("books/monk_who_sold_ferrari.pdf", "rb") as f:
        pdf_bytes = f.read()
    [chunks, embeddings] = summarizer.process_pdf_for_ollama(pdf_bytes, chunk_size=1500)
    # print(f"Total chunks: {len(chunks)}")
    # print("First chunk preview:\n", chunks[0][:500])

    # Store all chunks in a file
    with open("books/monk_who_sold_ferrari_chunks.txt", "w", encoding="utf-8") as out_file:
        for idx, chunk in enumerate(chunks, 1):
            out_file.write(f"--- Chunk {idx} ---\n")
            out_file.write(chunk)
            out_file.write("\n\n")

    # Store embeddings in a .npy file
    np.save("books/monk_who_sold_ferrari_embeddings.npy", embeddings)
    collection_name = "monk_who_sold_ferrari_collection"
    summarizer.store_in_chromadb(chunks, embeddings, collection_name)

    top_chunks = summarizer.retrieve_chunks_from_chromadb("What is the main lesson from the book?", collection_name, top_k=3)

    print(top_chunks)
    with open("books/summarized_monk_who_sold_ferrari.txt", "w", encoding="utf-8") as out_file:
        for idx, chunk in enumerate(top_chunks, 1):
            out_file.write(f"--- Chunk {idx} ---\n")
            out_file.write(chunk)
            out_file.write("\n\n")

if __name__ == "__main__":
    test_real_book()