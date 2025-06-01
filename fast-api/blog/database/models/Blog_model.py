from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from blog.database.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base


class Blog(Base):
    __tablename__: str = 'Blogs'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str]
    body: Mapped[str]
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('Users.id'))
    creator: Mapped['Users'] = relationship("Users", back_populates="blogs")
