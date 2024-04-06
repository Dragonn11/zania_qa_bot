import json
from venv import logger
import fitz  # PyMuPDF
from fastapi import HTTPException, UploadFile

logger = logging.getLogger(__name__)

async def read_uploaded_file_content(file: UploadFile, file_type: str) -> str:
    try:
        if file_type == "application/json":
            return await read_json_file_content(file)
        elif file_type == "application/pdf":
            return await read_pdf_file_content(file)
        else:
            raise HTTPException(status_code=415, detail="Unsupported file type")
    except Exception as e:
        logger.error(f"Error reading file: {e}")
        raise HTTPException(status_code=400, detail="Error reading file")

async def read_json_file_content(file: UploadFile) -> str:
    content = await file.read()
    return json.loads(content)

async def read_pdf_file_content(file: UploadFile) -> str:
    content = await file.read()
    text = ""
    try:
        with fitz.open(stream=content, filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        logger.error(f"Error reading PDF: {e}")
        raise HTTPException(status_code=400, detail="Error reading PDF")
    return text