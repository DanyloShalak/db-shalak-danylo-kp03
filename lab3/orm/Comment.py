from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()

class Comment(Base):
    __tablename__ = 'comments'

    comment_id = Column(Integer, Sequence('comments_comment_id_seq'), primary_key=True)
    content_content = Column(String(100), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.post_id',
                     ondelete='CASCADE'), nullable=False)
    author_id = Column(Integer, ForeignKey('users.user_id',
                         ondelete='CASCADE'), nullable=False)
    publication_date = Column(DateTime, nullable=False)

    user = relationship('User', backref='users')
    post = relationship('Post', backref='posts')

    def __repr__(self):
        return "<User(content_content='%s', post_id='%s', author_id='%s', publication_date='%s')>" % (
                self.content_content, self.post_id, self.author_id, self.publication_date)