from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from orm.User import User

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


class Post(Base):
    __tablename__ = 'posts'

    post_id = Column(Integer, Sequence('posts_post_id_seq'), primary_key=True)
    post_content = Column(String(100), nullable=False)
    author_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE'),
                 nullable=False)
    publication_date = Column(DateTime, nullable=False)
    
    user = relationship('User', backref='users')

    def __repr__(self):
        return "<User(post_content='%s', author_id='%s', publication_date='%s')>" % (
                self.post_content, self.author_id, self.publication_date)