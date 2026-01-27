from app.services import summarizer

def test_real_book():
    with open("books/monk_who_sold_ferrari.pdf", "rb") as f:
        pdf_bytes = f.read()
    chunks = summarizer.process_pdf_for_ollama(pdf_bytes, chunk_size=1500)
    # print(f"Total chunks: {len(chunks)}")
    # print("First chunk preview:\n", chunks[0][:500])

    # Store all chunks in a file
    with open("books/monk_who_sold_ferrari_chunks.txt", "w", encoding="utf-8") as out_file:
        for idx, chunk in enumerate(chunks, 1):
            out_file.write(f"--- Chunk {idx} ---\n")
            out_file.write(chunk)
            out_file.write("\n\n")

if __name__ == "__main__":
    test_real_book()