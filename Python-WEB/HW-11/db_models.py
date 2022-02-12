from datetime import datetime
from pydoc import describe
from unicodedata import name

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()

# таблица для свази many2many

note_m2m_tag = Table(
    "note_m2m_tag",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("note", Integer, ForeignKey("notes.id")),
    Column("tag", Integer, ForeignKey("tags.id")),
)


class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    created = Column(DateTime, default=datetime.now())
    description = Column(String(150), nullable=False)
    done = Column(Boolean, default=False)
    tags = relationship("Tag", secondary=note_m2m_tag, backref="notes")

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False, unique=True)
    
    def __repr__(self) -> str:
        return self.name
    
if __name__ == "__main__":
    
    engine = create_engine("sqlite:///mynotes.db")
    Base.metadata.create_all(engine)