from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

app = FastAPI(
    title="Student Question API",
    description="A simple FastAPI backend for a React application",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Welcome to AskMyNotes Backend!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):
    return {
        "question": request.question,
        "answer": "This is a sample answer from AskMyNotes."
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "message": "PDF uploaded successfully."
    }