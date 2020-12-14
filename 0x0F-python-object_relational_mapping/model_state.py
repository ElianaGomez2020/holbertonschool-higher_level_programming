#!/usr/bin/python3
"""contains the class definition of a State"""


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, autoincrement='auto', nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
