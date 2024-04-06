from fastapi import APIRouter, Depends, UploadFile, File
from ..services import process_file_service

router = APIRouter()

@router.post("/service-qa")
async def question_answer(question_file: UploadFile = File(...), document_file: UploadFile = File(...)):
    return await process_file_service.answer_questions(question_file, document_file)