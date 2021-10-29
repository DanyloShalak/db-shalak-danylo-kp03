import psycopg2

class CommentsRepository:
    
    def __init__(self, connection):
        self.connection = connection;
    
    def insertComment(self, commentData):
        query = """INSERT INTO comments (comment_content, post_id, author_id,
         publication_date) VALUES (%s, %s, %s, %s)"""
        
        cursor = self.connection.cursor()

        cursor.execute(query, commentData)

        cursor.close()
        self.connection.commit()


    def updateComment(self, commentData):
        query = """UPDATE comments
                    SET comment_content = %s
                    WHERE comment_id = %s"""
        cursor = self.connection.cursor()
        cursor.execute(query, commentData)

        cursor.close()
        self.connection.commit()

    
    def deleteComment(self, commentData):
        query = """DELETE FROM comments WHERE comment_id = %s"""
        cursor = self.connection.cursor()
        cursor.execute(query, commentData)

        cursor.close()
        self.connection.commit()

    
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
                (timestamp '2000-01-01' + random() * 
            (timestamp '2021-10-10' - timestamp '2000-01-01'))::date 
                from generate_series(1, %s) seq
        )

        select generated_data.content, id_table.post_id, id_table.author_id,
        generated_data.publication_date from id_table, generated_data 
        limit %s"""

        cursor = self.connection.cursor()
        cursor.execute(query, (commentsCount[0], commentsCount[0],))

        cursor.close()
        self.connection.commit()
            
