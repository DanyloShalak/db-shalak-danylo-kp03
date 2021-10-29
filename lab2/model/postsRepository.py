import psycopg2

class PostsRepository:
    
    def __init__(self, connection):
        self.connection = connection;
    
    def insertPost(self, data):
        query = """INSERT INTO posts (post_content, author_id, publication_date)
        VALUES (%s, %s, %s) RETURNING post_id"""
        
        cursor = self.connection.cursor()
        
        postData = data[:3]

        cursor.execute(query, postData)
        postId = cursor.fetchall()[0][0]

        cursor.close()
        self.connection.commit()

        self.subscribeTags(data[3], postId)



    def updatePost(self, postData):
        query = """UPDATE posts
                    SET post_content = %s
                    WHERE post_id = %s"""
        cursor = self.connection.cursor()
        cursor.execute(query, postData)

        cursor.close()
        self.connection.commit()

    
    def deletePost(self, postData):
        query = """DELETE FROM posts WHERE post_id = %s"""
        cursor = self.connection.cursor()
        cursor.execute(query, postData)

        cursor.close()
        self.connection.commit()

    
    def is_tag_not_exists(self,tag):
        checkQuery = """SELECT COUNT(*) FROM tags WHERE tag_name = %s"""
        cursor = self.connection.cursor()
        cursor.execute(checkQuery, (tag, ))
        count = cursor.fetchall()[0][0]
        cursor.close()

        return count == 0


    def subscribeTags(self, tags, postId):
        cursor = self.connection.cursor()
        insertQuery = """INSERT INTO tags (tag_name) VALUES (%s)
                         RETURNING tag_id"""
        
        idQuery = """SELECT (tag_id) FROM tags WHERE tag_name = %s"""

        subscribeQuery = """INSERT INTO posts_tags (post_id, tag_id)
                        VALUES (%s, %s)"""
        
        tag_name_id = 1

        for tag in tags:
            if self.is_tag_not_exists(tag) == True:
                cursor.execute(insertQuery, (tag, ))
                tag_name_id = cursor.fetchall()[0][0]
                self.connection.commit()
            else:
                cursor.execute(idQuery, (tag, ))
                tag_name_id = cursor.fetchall()[0][0]

            cursor.execute(subscribeQuery, (postId, tag_name_id, ))
            self.connection.commit()

        cursor.close()


    def generatePosts(self, postsCount):
        query = """insert into posts (post_content, author_id, publication_date)

        With id_table(user_id) AS
        (
            select user_id from users
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


        select generated_data.content, id_table.user_id,
        generated_data.publication_date from id_table,
        generated_data  order by random() limit %s"""

        cursor = self.connection.cursor()
        cursor.execute(query, (postsCount, postsCount,))
        cursor.close()
        self.connection.commit()


    def get_users_posts(self, queryData):
        query = """select posts.post_id, posts.post_content,
         posts.publication_date, count(comments.comment_id) as comment_count
        from posts
        join comments on posts.post_id = comments.post_id and posts.author_id = %s
        group by posts.post_id
        order by comment_count {0}, publication_date {1}
        limit {2}""".format(queryData[1], queryData[2], queryData[3])

        cursor = self.connection.cursor()
        cursor.execute(query, (queryData[0], ))
        data = cursor.fetchall()
        cursor.close()
        
        return data
