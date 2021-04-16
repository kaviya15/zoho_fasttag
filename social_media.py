import itertools
uuid = itertools.count(start=101)
class adjacencylist:
    def __init__(self, email, name):
        self.vertex = {
             "name":name,
             "email":email,
             "posts":[]
        }
        self.friends = {}
        self.blockedusers = []

userID = []
class ConnectWorld:
    def __init__(self):
        self.list_of_users = {}

    def registerUSer(self,name,email):
        if userID.count(email)>0:
            print("userId has been already taken")
        else:
            userID.append(email)
            node = adjacencylist(email,name)
            self.list_of_users[email] = node
            print("userId:",email)

    def followUser(self,followerId, follweeId):
       if userID.count(follweeId)==1 and userID.count(followerId)==1:
           followernode = self.list_of_users[followerId]
           self.list_of_users[follweeId].friends[followernode.vertex["email"]] = followernode
           print("Account updated",self.list_of_users[follweeId].vertex,self.list_of_users[follweeId].friends)
       elif userID.count(follweeId)==1 and userID.count(followerId)==0:
           print("No such user found Register the user")
           self.registerUSer(input("Enter name "), input("Enter emailID "))

    def unfollowUser(self,followerId, follweeId):
        followerNode = self.list_of_users[follweeId]
        print(followerNode.friends)
        print(followerNode.friends[followerId])
        followerNode.friends.pop(followerId)

    def postFeed(self,userid,feed):
        post = {
            "feed_id": next(uuid),
            "feed": feed,
            "like": 1,
            'dislike': 0,
            'hide': False
        }
        self.list_of_users[userid].vertex['posts'].append(post)
        print('posted ... Your feed id ' ,post["feed_id"])

    def blockUser(self,currentuserId,userId):
        self.list_of_users[currentuserId].blockedusers.append(self.list_of_users[userId])

    def getUserFeeds(self,userId):
        if len(self.list_of_users[userId].vertex["posts"]) == 0:
            print("No posts so far...")
        else:
            print(self.list_of_users[userId].vertex["posts"]["feed"])

    def getFeedLikesCount(self,userid,feedId) :
            for i in self.list_of_users[userid].vertex["posts"]:
                if i["feed_id"] == feedId:
                    return(i["like"])
            return("No such feedId")

    def getMyFeeds(self,currentUserId):
         if len(self.list_of_users[currentUserId].vertex["posts"])==0:
             print("No posts so far...")
         else:
             print(self.list_of_users[currentUserId].vertex["posts"]["feed"])

    def deleteUser(self,userId):
        self.list_of_users.pop(self.list_of_users[userId])
        print("Deleted  Successfully")


user = ConnectWorld()

name = input("Enter name ")
emailId = input("Enter emailID ")
user.registerUSer(name,emailId)
print("Account registered successfully")
print("Enter your choice (Choose the index number)")
print(" 1.Follow user \n 2.postfeeds \n 3.getFeedLikesCount \n 4.Block user \n 5.unFollow user \n 6.Get user Feeds \n 7.Get my feeds \n 8.Delete user")
output = int(input('Choose '))
def checkdata():
    input_data = repeated_process()
    if input_data.lower() != "no":
        chooseUseroption(int(input_data))
def repeated_process():
     return(input("Do you wanna continue if yes enter your choice else No "))
def chooseUseroption(option):
    if option==1:
        user.followUser(input("Enter the ID to follow "),emailId)
        checkdata()
    elif option==2:
        user.postFeed(emailId, input('upload your Feed '))
        checkdata()
    elif option == 3:
        print(user.getFeedLikesCount(emailId, int(input('Enter FeedID '))))
        checkdata()
    elif option == 4:
        user.blockUser(input('userid needed to block '),emailId)
        checkdata()
    elif option == 5:
        user.unfollowUser(input('enter id needed to unfollow '),emailId)
        checkdata()
    elif option == 6:
        user.getUserFeeds(input('Id to fetch feeds ? '))
        checkdata()
    elif option==7:
        user.getMyFeeds(emailId)
        checkdata()
    elif option == 8:
        user.deleteUser( input('id to be deleted '))
        checkdata()

chooseUseroption(output)

