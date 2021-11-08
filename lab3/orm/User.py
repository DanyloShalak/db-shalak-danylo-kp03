from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Sequence


Base = declarative_base()



class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, Sequence('users_user_id_seq'), primary_key=True)
    login = Column(String(30), nullable=False)
    fullname = Column(String(50), nullable=False)
    registration_date = Column(DateTime, nullable=False)

    def __repr__(self):
        return "<User(login='%s', fullname='%s', registration_date='%s')>" % (
                             self.login, self.fullname, self.registration_date)