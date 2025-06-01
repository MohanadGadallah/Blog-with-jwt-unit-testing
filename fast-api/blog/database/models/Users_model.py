from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from uuid import uuid4
from sqlalchemy.orm.relationships import _RelationshipDeclared
from typing import Any
from blog.database.base import Base
from blog.database.models.Blog_model import Blog


class Users(Base):
    __tablename__: str = 'Users'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str]
    blogs: Mapped[list[Blog]] = relationship(
        "Blog", back_populates="creator")
