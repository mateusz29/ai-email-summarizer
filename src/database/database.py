import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()


engine = create_engine(os.getenv("DATABASE_URL"))
session_maker = sessionmaker(engine)


def get_session():
    return session_maker()
