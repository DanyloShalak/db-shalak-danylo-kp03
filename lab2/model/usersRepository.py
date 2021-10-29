from typing import Counter
import psycopg2

class UsersRepository:
    
    def __init__(self, connection):
        self.connection = connection;
    
    def insertUser(self, userData):
        query = """INSERT INTO users (login, fullname, registration_date)
        VALUES (%s, %s, %s)"""
        
        cursor = self.connection.cursor()

        cursor.execute(query, userData)

        cursor.close()
        self.connection.commit()


    def renameUser(self, userData):
        query = """UPDATE users
                    SET fullname = %s
                    WHERE user_id = %s"""
        cursor = self.connection.cursor()
        cursor.execute(query, userData)

        cursor.close()
        self.connection.commit()

    
    def deleteUser(self, userData):
        query = """DELETE FROM users WHERE user_id = %s"""
        cursor = self.connection.cursor()
        cursor.execute(query, userData)

        cursor.close()
        self.connection.commit()

    
    def generateUsers(self, usersCount):
        query = """insert into users (login, fullname, registration_date)
                    select 
                        'user_' || seq as login, 
                        chr(trunc(65+random()*25)::int) || 
                        chr(trunc(65+random()*25)::int) as fullname,
                        (timestamp '2000-01-01' + random() * 
                        (timestamp '2021-10-10' - timestamp '2000-01-01'))::date
                        from generate_series(1, %s) seq;"""

        cursor = self.connection.cursor()
        cursor.execute(query, (usersCount, ))
        self.connection.commit()


    def getAnalytics(self, queryData):
        query = """
        with comments_ (user_id, comment_count) as
        (
            select  users.user_id, count(comments.comment_id)
            from users
            join comments on comments.author_id = users.user_id
            group by users.user_id
        ),
        posts_ (user_id, login, post_count) as
        (
            select users.user_id, users.login , count(posts.post_id) as posts_count
            from users
            join posts on posts.author_id = users.user_id
            group by users.user_id, users.login
        )

        select posts_.user_id, posts_.login, posts_.post_count, comments_.comment_count
        from posts_
        join comments_ on comments_.user_id = posts_.user_id
        order by post_count {0}, comment_count {1}
        limit {2}""".format(queryData[0], queryData[1], queryData[2])

        cursor = self.connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()

        return data


    def getActivity(self, activityData):
        query = """with comments_ (user_id, comment_count) as
        (
            select  users.user_id, count(comments.comment_id)
            from users
            join comments on comments.author_id = users.user_id
            group by users.user_id
        ),
        posts_ (user_id, login, reg_date, post_count) as
        (
            select users.user_id, users.login, users.registration_date,
                 count(posts.post_id) as posts_count
            from users
            join posts on posts.author_id = users.user_id
            group by users.user_id, users.login
        )

        select posts_.user_id, posts_.login, posts_.reg_date, posts_.post_count + comments_.comment_count as points
        from posts_
        join comments_ on comments_.user_id = posts_.user_id and posts_.reg_date > %s
		order by points {0}, posts_.reg_date {1}

		limit {2}""".format(activityData[1], activityData[2], activityData[3])

        cursor = self.connection.cursor()
        cursor.execute(query, (activityData[0], ))
        data = cursor.fetchall()

        return data