import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Contry(Base):
    __tablename__= 'contry'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    contry =Column (Integer, ForeignKey('contry.id'))
    contry_relationship = relationship(Contry)
    email = Column(String(50), unique=True)
    password = Column(String(25))

class Characters(Base):
    __tablename__= 'characters'
    id= Column(String(20), primary_key=True)
    name = Column(String(20),unique=True)
    Hegiht = Column(Integer)
    mass = Column(Integer)

class Fav_Character(Base):
    __tablename__= 'fav_character'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(20),ForeignKey('user.id'))
    user_relationship = relationship(User)
    character_id = Column(Integer,ForeignKey('characters.id'))





class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
