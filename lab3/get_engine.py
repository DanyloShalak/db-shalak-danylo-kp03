from local_settings import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_engine_url(settings):
    url = f"postgresql://{settings['username']}:{settings['password']}@{settings['host']}:{settings['port']}/{settings['database']}"
    return url

def get_engine():
    engine = create_engine(get_engine_url(settings))
    return engine

def get_session():
    engine = get_engine()
    session = sessionmaker(bind=engine)()
    return session