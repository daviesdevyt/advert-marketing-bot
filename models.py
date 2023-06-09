from sqlalchemy import create_engine, Column, Text, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import dotenv, os
dotenv.load_dotenv()

base = declarative_base()

class User(base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    email = Column(Text)
    phone = Column(String(20))
    section = Column(String(20), nullable=True, default=None)
    sub_section = Column(String(20), nullable=True, default=None)
    media_platforms = relationship("MediaPlatform")

class MediaPlatform(base):
    __tablename__ = "mediaplatform"
    id = Column(Integer, primary_key=True)
    platform = Column(String(30))
    user = Column(Integer, ForeignKey("user.id"))

class MediaAdRate(base):
    __tablename__ = "mediaadrate"
    id = Column(Integer, primary_key=True)
    station_name = Column(Text)
    state = Column(Text)
    duration = Column(Text)
    card_rate = Column(Float)
    media_type = Column(String(20))

engine = create_engine(os.getenv("DB_URL"))
connection = engine.connect()
base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()