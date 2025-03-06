#!/usr/bin/env python3

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)

engine = create_engine('sqlite:///students.db')

Base.metadata.create_all(engine)


    

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)