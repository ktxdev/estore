import uuid
from pathlib import Path

import aiofiles
from fastapi import APIRouter, UploadFile, HTTPException
from fastapi import Depends
from starlette.responses import FileResponse

from crud import file_crud
from database import SessionLocal
from dependecies import get_db
from schemas.file import FileMetadata

router = APIRouter(
    prefix="/api/v1/files",
    tags=["Files"]
)

UPLOADS_DIR = 'uploads'


@router.post("/", response_model=FileMetadata)
async def upload_file(file: UploadFile, db: SessionLocal = Depends(get_db)):
    filename = await upload(file)
    return file_crud.create_file_metadata(db, file, filename)


@router.post("/multiple", response_model=list)
async def upload_multiple_files(files: list[UploadFile], db: SessionLocal = Depends(get_db)):
    # TODO what happens if any of the files fail to upload?
    files_metadata = []
    for file in files:
        filename = await upload(file)
        file_metadata = file_crud.create_file_metadata(db, file, filename)
        files_metadata.append(FileMetadata.from_orm_file_metadata(file_metadata))
    return files_metadata


@router.delete("/{filename}", response_model=list)
async def upload_multiple_files(filename: str, db: SessionLocal = Depends(get_db)):
    file_crud.delete_file_metadata(db, filename)
    file_path = Path(UPLOADS_DIR).joinpath(filename)
    file_path.unlink(True)


@router.get("/download/{filename}")
async def download_file(filename: str, db: SessionLocal = Depends(get_db)):
    db_file_metadata = file_crud.get_file_metadata_by_filename(db, filename)
    if db_file_metadata is None:
        raise HTTPException(status_code=404, detail=f'File {filename} not found')
    file_path = Path(UPLOADS_DIR).joinpath(db_file_metadata.filename)
    return FileResponse(file_path, media_type=db_file_metadata.content_type,
                        filename=db_file_metadata.original_filename)


@router.get("/", response_model=list[FileMetadata])
async def get_files_metadata(skip: int = 0, limit: int = 100, db: SessionLocal = Depends(get_db)):
    return file_crud.get_file_metadata(db, skip, limit)


async def upload(file: UploadFile):
    original_filename = file.filename
    filename = f'{uuid.uuid4()}.{original_filename[original_filename.rindex(".") + 1:]}'

    uploads_path = Path(UPLOADS_DIR)
    uploads_path.mkdir(exist_ok=True)

    file_path = uploads_path.joinpath(filename)

    async with aiofiles.open(file_path, mode='wb') as out_file:
        content = file.file.read()
        await out_file.write(content)

    return filename
