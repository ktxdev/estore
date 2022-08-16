from datetime import datetime
from fastapi import UploadFile
from sqlalchemy.orm import Session
from models.file import FileMetadata


def create_file_metadata(db: Session, file: UploadFile, filename: str):
    db_file_metadata = FileMetadata(
        filename=filename,
        content_type=file.content_type,
        created_on=datetime.now(),
        original_filename=file.filename,
    )
    db.add(db_file_metadata)
    db.commit()
    db.refresh(db_file_metadata)
    return db_file_metadata


def get_file_metadata_by_filename(db: Session, filename: str):
    return db.query(FileMetadata).filter(FileMetadata.filename == filename).first()


def get_file_metadata(db: Session, skip: int = 0, limit: int = 100):
    return db.query(FileMetadata).offset(skip).limit(limit).all()


def delete_file_metadata(db: Session, filename: str):
    db.query(FileMetadata).filter(FileMetadata.filename == filename).delete()
    db.commit()
