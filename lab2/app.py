import psycopg2
from controller.controller import Controller
# from model.postsRepository import PostsRepository 
# from model.commentRepository import CommentsRepository 
# from model.usersRepository import UsersRepository 
from model.model import UsersRepository, PostsRepository, CommentsRepository
from view import View


conn = psycopg2.connect(
    host="localhost",
    database="bd_labs",
    user="postgres",
    password="danylo1")



postRepo = PostsRepository(conn)
commentRepo = CommentsRepository(conn)
userRepo = UsersRepository(conn)
view = View()


contr = Controller(postRepo, userRepo, commentRepo, view)


while(True):
    command = input('Enter command\n')
    if command == 'exit':
        break

    
    try:
        contr.handleCommand(command)
    except Exception as e:
        print(e)
	
