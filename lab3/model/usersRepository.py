from orm_entites import User
import psycopg2

class UsersRepository:
    
    def __init__(self, connection, session):
        self.connection = connection;
        self.session = session
    
    def insertUser(self, userData):
        newUser = User(login=userData[0], fullname=userData[1], registration_date=userData[2])
        self.session.add(newUser)
        self.session.commit()

    def renameUser(self, userData):
        update_user = self.session.query(User).get(userData[1])
        update_user = userData[0]
        self.session.commit()

    
    def deleteUser(self, userData):
        self.session.delete(self.session.query(User).get(userData[0]))
        self.session.commit()

    
    def generateUsers(self, usersCount):
        query = """insert into users (login, fullname, registration_date)
                    select 
                        'user_' || seq as login, 
                        chr(trunc(65+random()*25)::int) || 
                        chr(trunc(65+random()*25)::int) as fullname,
                        CURRENT_TIMESTAMP + ( seq || 'minute' ) :: interval
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

    def search_user_by_login(self, searchData):
        query = """select * from users where fullname = %s"""
        cursor = self.connection.cursor()
        cursor.execute(query, searchData)
        search_result = cursor.fetchall()
        cursor.close()
        return search_result

    
    def search_users_regist_in_period(self, searchData):
        query = """select * from users where registration_date between %s and %s"""
        cursor = self.connection.cursor()
        cursor.execute(query, searchData)
        search_result = cursor.fetchall()
        cursor.close()
        return search_result

    
    def get_user_post_comment_count(self, data):
        query = """with comm (comments_count) as 
                (
                    select count(*) from comments where author_id = %s
                ),
                post (posts_count) as 
                (
                    select count (*) from posts where author_id = %s
                )
                select * from comm, post
                """
        cursor = self.connection.cursor()
        cursor.execute(query, (data[0], data[0]))
        result = cursor.fetchall()
        cursor.close
        return result
        