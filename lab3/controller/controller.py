import querydata
import time

class Controller:
    def __init__(self, pRepo, uRepo, cRepo, view):
        self.usersRepository = uRepo
        self.postsRepository = pRepo
        self.commentsRepository = cRepo
        self.view = view
        self.controller_dict = {}
        self.controller_dict["insertPost"] = self.postsRepository.insertPost
        self.controller_dict["insertComment"] = self.commentsRepository.insertComment
        self.controller_dict["insertUser"] = self.usersRepository.insertUser
        self.controller_dict["deleteUser"] = self.usersRepository.deleteUser
        self.controller_dict["deletePost"] = self.postsRepository.deletePost
        self.controller_dict["deleteComment"] = self.commentsRepository.deleteComment
        self.controller_dict["generateUser"] = self.usersRepository.generateUsers
        self.controller_dict["generatePost"] = self.postsRepository.generatePosts
        self.controller_dict["generateComment"] = self.commentsRepository.generateComments
        self.controller_dict["updateUser"] = self.usersRepository.renameUser
        self.controller_dict["updatePost"] = self.postsRepository.updatePost
        self.controller_dict["updateComments"] = self.commentsRepository.updateComment
        self.controller_dict["analytics"] = self.usersRepository.getAnalytics
        self.controller_dict["activity"] = self.usersRepository.getActivity
        self.controller_dict["userPost"] = self.postsRepository.get_users_posts
        self.controller_dict["findUser"] = self.usersRepository.search_user_by_login
        self.controller_dict["periodUser"] = self.usersRepository.search_users_regist_in_period
        self.controller_dict["commentsUser"] = self.commentsRepository.commentsUser
        self.controller_dict["userData"] = self.usersRepository.get_user_post_comment_count
        


    def handleCommand(self,command):
        commands = ["insertPost", "insertComment", "insertUser",
         "deletePost", "deleteComment", "deleteUser", "updatePost",
         "updateUser", "updateComment", "generateComment", "generatePost",
         "generateUser", "analytics", "activity", "userPost", "findUser", "periodUser",
         "commentsUser", "userData"]
        commandName = command.split(' ')[0]

        titles = {"analytics" : ["user_id", "login", "posst_count", "comment_count"],
        "activity" : ["user_id", "login", "registration_date", "points"],
        "userPost" : ["post_id", "post_content", "publish_date", "comment_count"],
        "findUser" : ["user_id", "login",  "fullname", "registration_date"],
        "periodUser" : ["user_id", "login",  "fullname", "registration_date"],
        "commentsUser" : ["commet_id", "comment_content", "post_id", "author_id", "pub_date"],
        "userData" : ["comments_count", "posts_count"]}
        

        if commandName not in commands:
            raise Exception("Command '{0}' do not exists".format(commandName))

        commandData = querydata.get_query_data(command)
        if commandName in ["analytics", "activity", "userPost",
                             "findUser", "periodUser", "commentsUser", "userData"]:
            start = time.time()
            fetched_data = self.controller_dict[commandName](commandData)
            self.view.fetch_data_log(titles[commandName], fetched_data)
            end = time.time()
            print("Query time = {0} ms".format(get_time(start, end)))
        else:
            self.controller_dict[commandName](commandData)
            self.view.perform_log(command)

        
def get_time(start, end):
    elapsed = int((end - start) * 1000)
    return elapsed