#!/usr/bin/env python3

from sqlalchemy import Column, CreateEnginePlugin, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

if __name__ == '__main__':
    engine = CreateEnginePlugin('sqlite:///students.db')
    Base.metadata.create_all(engine)