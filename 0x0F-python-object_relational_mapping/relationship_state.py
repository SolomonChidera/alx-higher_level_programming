#!/usr/bin/python3
"""
State class and an instance of declarative_base() representation
"""
import sys
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)
eat

class State(Base):
    """
    Representation of State class
        args:   __tablename___(str): Name of the table
                id (int): unique identifier of table's row
                name (str): name of states
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='states')
