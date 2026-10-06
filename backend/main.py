from fastapi import FastAPI
from pydantic import BaseModel

try:
    from .gemini_service import generate_legal_document
except ImportError:
    from gemini_service import generate_legal_document

app = FastAPI(title="LegalEase API")


class DocumentRequest(BaseModel):
    document_type: str
    user_details: str


@app.get("/")
def home():
    return {"message": "LegalEase API is running"}


@app.post("/generate")
def generate_document(request: DocumentRequest):

    document = generate_legal_document(
        request.document_type,
        request.user_details
    )

    return {
        "document": document
    }