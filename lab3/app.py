import psycopg2
from controller.controller import Controller
from get_engine import get_session
from model.model import UsersRepository, PostsRepository, CommentsRepository
from view import View


conn = psycopg2.connect(
    host="localhost",
    database="db_labs",
    user="postgres",
    password="danylo1")


session = get_session()
postRepo = PostsRepository(conn, session)
commentRepo = CommentsRepository(conn, session)
userRepo = UsersRepository(conn, session)
view = View()



contr = Controller(postRepo, userRepo, commentRepo, view)



while(True):
    command = input('Enter command\n')
    if command == 'exit':
        break

    
    # try:
    contr.handleCommand(command)
    # except Exception as e:
    #     print(e)
	
