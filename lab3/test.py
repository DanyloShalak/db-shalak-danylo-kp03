from get_engine import get_session
import datetime
from orm_entites import User, Post, Comment, Tag, PostsTags


session = get_session()

user = session.query(PostsTags).filter_by(post_id=2, tag_id=3).first()
# session.delete(user)
# session.commit()
print(user)

