from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from app.services.summarizer import process_pdf_for_ollama

router = APIRouter()

@router.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        return JSONResponse(status_code=400, content={"error": "File must be a PDF."})

    contents = await file.read()
    chunks = process_pdf_for_ollama(contents)
    return {"num_chunks": len(chunks), "chunks": chunks}