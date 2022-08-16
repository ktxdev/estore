from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class FileMetadata(Base):
    __tablename__ = "files_metadata"

    id = Column(Integer, primary_key=True, index=True)
    original_filename = Column(String(255))
    filename = Column(String(255), unique=True)
    content_type = Column(String(255))
    created_on = Column(DateTime)
