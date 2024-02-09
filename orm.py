from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column,Integer, String, Date
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from datetime import date
class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = "AUTHOR"

    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    dob = Column(Date)

    def __repr__(self) -> str:
        return f"Author(id={self.id}, name={self.name}, dob={self.dob})"

class Staff(Base):
    __tablename__ = "STAFF"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    dob = Column(Date)
    email = Column(String)

    def __repr__(self) -> str:
        return f"Staff(id={self.id}, name={self.name}, dob={self.dob}, email={self.email})"

class User(Base):
    __tablename__ = "USER"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    dob = Column(Date)
    
    def __repr__(self) -> str:
        return f"USER(id={self.id},name={self.name},email={self.email},password={self.password},dob={self.dob})"