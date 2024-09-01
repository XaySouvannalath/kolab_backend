from typing import Union
from fastapi import APIRouter, HTTPException, File, UploadFile
from fastapi.responses import FileResponse
from models.FollowerLog import FollowerLog
import time
from PIL import Image
from cruds.FollowerLog import *
import os

router = APIRouter(
    prefix="/files"
)

UPLOAD_DIRECTORY = "./uploads"
THUMBNAIL_DIRECTORY = "./thumbnails"
 

# Create directories if they don't exist
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)
    
os.makedirs(THUMBNAIL_DIRECTORY, exist_ok=True)


def save_thumbnail(image_path: str, thumbnail_path: str):
    # Open an image file
    with Image.open(image_path) as img:
        # Generate thumbnail
        img.thumbnail((150, 150))  # Set thumbnail size (150x150)
        img.save(thumbnail_path)



@router.post("/upload/")
async def upload_file(files: List[UploadFile] = File(...)):
    print("uploading.....")
    file_info = []
    for file in files:
        original_filename = file.filename
        timestamp_filename = f"{int(time.time())}_{file.filename}"
        file_path = os.path.join(UPLOAD_DIRECTORY, timestamp_filename)
        
        # Save the file with the timestamp filename
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
        
        # Append both filenames to the response
        file_info.append({
            "filename": timestamp_filename
        })
    return {"uploaded_files": file_info}    


@router.post("/upload_with_thumbnail/")
async def upload_file_with_thumbnail(files: List[UploadFile] = File(...)):
    file_info = []
    for file in files:
        original_filename = file.filename
        timestamp_filename = f"{int(time.time())}_{file.filename}"
        original_file_path = os.path.join(UPLOAD_DIRECTORY, timestamp_filename)
        
        # Save the original file
        with open(original_file_path, "wb") as buffer:
            buffer.write(await file.read())
        
        # Generate and save the thumbnail
        thumbnail_filename = f"thumb_{timestamp_filename}"
        thumbnail_file_path = os.path.join(UPLOAD_DIRECTORY, thumbnail_filename)
        save_thumbnail(original_file_path, thumbnail_file_path)
        
        # Append the file info to the response
        file_info.append({
            "original_filename": original_filename,
            "saved_filename": timestamp_filename,
            "thumbnail_filename": thumbnail_filename
        })
    
    return {"uploaded_files": file_info}

@router.get("")
async def get_file(file_name:str):
    file_path = os.path.join(UPLOAD_DIRECTORY, file_name)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail="File not found")


