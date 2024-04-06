from typing import List
from fastapi import HTTPException, UploadFile
from .file_service import read_uploaded_file_content
from dotenv import load_dotenv
import os
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OpenAI API key not found.")

chat = ChatOpenAI(temperature=0, openai_api_key=openai_api_key)

async def generate_answer(question: str, context: str) -> str:

    if question is None or context is None:
        raise HTTPException(status_code=400, detail="question and context are required")
    
    messages = [
        SystemMessage(content=context),
        HumanMessage(content=question),
    ]
    return chat(messages).content

async def process_questions(question_file: UploadFile, document_file: UploadFile) -> List[dict]:

    try:
        # Read the content of the uploaded files
        questions_content = await read_uploaded_file_content(question_file, question_file.content_type)
        document_content = await read_uploaded_file_content(document_file, document_file.content_type)

        # Extract questions from the file content
        questions = [question["question"] for question in questions_content]

        answers = []
        for question in questions:
            answer = await generate_answer(question, document_content)
            answers.append({"question": question, "answer": answer})

        return answers
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing questions: {e}")
