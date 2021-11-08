from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey


Base = declarative_base()

class Comment(Base):
    __tablename__ = 'comments'

    comment_id = Column(Integer, Sequence('comments_comment_id_seq'), primary_key=True)
    comment_content = Column(String(100), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.post_id',
                     ondelete="CASCADE"), nullable=False)
    author_id = Column(Integer, ForeignKey('users.user_id', 
                        ondelete="CASCADE"), nullable=False)
    publication_date = Column(DateTime, nullable=False)
        

    def __repr__(self):
        return "<Comment(comment_content='%s', post_id='%s', author_id='%s', publication_date='%s')>" % (
                self.comment_content, self.post_id, self.author_id, self.publication_date)



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
    author_id = Column(Integer, ForeignKey('users.user_id',
                        ondelete="CASCADE"), nullable=False)
    publication_date = Column(DateTime, nullable=False)
    

    def __repr__(self):
        return "<Post(post_content='%s', author_id='%s', publication_date='%s')>" % (
                self.post_content, self.author_id, self.publication_date)


class Tag(Base):
    __tablename__ = 'tags'

    tag_id = Column(Integer, Sequence('tags_tag_id_seq'), primary_key=True)
    tag_name = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Tag(tag_name='%s')>" % (self.tag_name)


class PostsTags(Base):
    __tablename__ = 'posts_tags'

    post_id = Column(Integer,  ForeignKey('posts.post_id', ondelete='CASCADE'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.tag_id', ondelete='CASCADE'), primary_key=True)

    def __repr__(self):
        return "<PostsTags(post_id='%s', tag_id ='%s')>" % (self.post_id, self.tag_id)