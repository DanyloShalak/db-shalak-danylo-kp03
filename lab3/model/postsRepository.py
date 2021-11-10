import psycopg2
from orm_entites import Post, Tag, PostsTags

class PostsRepository:
    
    def __init__(self, connection, session):
        self.connection = connection
        self.session = session
    
    def insertPost(self, data):
        newPost = Post(post_content=data[0], author_id=data[1], publication_date=data[2])
        self.session.add(newPost)
        self.subscribeTags(data[3], newPost.post_id)



    def updatePost(self, postData):
        update_post = self.session.query(Post).get(postData[1])
        update_post.post_content = postData[0]
        self.session.commit()

    
    def deletePost(self, postData):
        self.session.delete(self.session.query(Post).get(postData[0]))
        self.session.commit()



    def subscribeTags(self, tags, postId):
        for tag in tags:
            current_tag = self.session.query(Tag).filter_by(tag_name=tag).first()
            if current_tag == None:
                current_tag = Tag(tag_name=tag)
                self.session.add(current_tag)
                self.session.commit()

            post_tag = PostsTags(post_id=postId, tag_id=current_tag.tag_id)
            self.session.add(post_tag)
        self.session.commit()


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
                CURRENT_TIMESTAMP + ( seq || 'minute' ) :: interval 
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
