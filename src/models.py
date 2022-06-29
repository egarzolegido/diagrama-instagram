import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
class user(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    firstname = Column(String(20))
    lastname = Column(String(20))
    email = Column(String(50), nullable=False)

class follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

class post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    url = Column(String())
    user_id = Column(Integer, ForeignKey('user.id'))

class comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)   
    comment_text = Column(String(350))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class md(Base):
    __tablename__ = 'md'
    id = Column(Integer, primary_key=True)
    comment = Column(String(350))
    user_id = Column(Integer, ForeignKey('user.id'))

class saves(Base):
    __tablename__ = 'saves'
    id = Column(Integer, primary_key=True)
    foto = Column(Integer, ForeignKey('post.id'))




#     def to_dict(self):
#         return {}

# ## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e