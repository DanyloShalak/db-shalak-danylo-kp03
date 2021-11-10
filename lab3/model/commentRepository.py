import psycopg2
from orm_entites import Comment


class CommentsRepository:
    
    def __init__(self, connection, session):
        self.connection = connection
        self.session = session
    
    def insertComment(self, commentData):
        newComment = Comment(comment_content=commentData[0],
            post_id=commentData[1], author_id=commentData[2],
            publication_date = commentData[3])
        self.session.add(newComment)
        self.session.commit()


    def updateComment(self, commentData):
        update_comment = self.session.query(Comment).get(commentData[1])
        update_comment.comment_content = commentData[1]
        self.session.commit()

    
    def deleteComment(self, commentData):
        self.session.delete(self.session.query(Comment).get(commentData[0]))
        self.session.commit()
    
    def generateComments(self, commentsCount):
        query = """insert into comments (comment_content, post_id,
             author_id, publication_date)

        With id_table(post_id, author_id) AS
        (
            select posts.post_id, users.user_id from posts, users
        ),
        generated_data(content, publication_date) AS
        (
            select  
                chr(trunc(65+random()*25)::int) || 
                chr(trunc(65+random()*25)::int) as fullname,
                CURRENT_TIMESTAMP + ( seq || 'minute' ) :: interval
                from generate_series(1, %s) seq
        )

        select generated_data.content, id_table.post_id, id_table.author_id,
        generated_data.publication_date from id_table, generated_data 
        limit %s"""

        cursor = self.connection.cursor()
        cursor.execute(query, (commentsCount[0], commentsCount[0],))

        cursor.close()
        self.connection.commit()
    

    def commentsUser(self, data):
        query = """select * from comments where author_id = %s limit 10"""
        cursor = self.connection.cursor()
        cursor.execute(query, data)
        result = cursor.fetchall()
        cursor.close()
        return result
