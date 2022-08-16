from datetime import datetime

from pydantic import BaseModel
from models.file import FileMetadata as ORMFileMetadata


class FileMetadata(BaseModel):
    id: int
    filename: str
    created_on: datetime
    content_type: str
    original_filename: str

    @staticmethod
    def from_orm_file_metadata(orm_file_metadata = ORMFileMetadata):
        return FileMetadata(
            id=orm_file_metadata.id,
            filename=orm_file_metadata.filename,
            content_type=orm_file_metadata.content_type,
            created_on=orm_file_metadata.created_on,
            original_filename=orm_file_metadata.original_filename
        )

    class Config:
        orm_mode = True
