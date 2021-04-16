import itertools
uuid = itertools.count(start=101)
class adjacencylist:
    def __init__(self, email, name):
        self.vertex = {
             "name":name,
             "email":email,
             "posts":[]
        }
        self.friends =[]
        self.blockedusers = []

userID = []
class ConnectWorld:
    def __init__(self):
        self.list_of_users = {}

    def registerUSer(self,name,email):
        if userID.count(email)>0:
            return("userId has been already taken")
        else:
            userID.append(email)
            node = adjacencylist(email,name)
            print(node.vertex,node.friends,node)
            self.list_of_users[email] = node
            return(email)

    def followUser(self,followerId, follweeId):
       if userID.count(follweeId)==1 and userID.count(followerId)==1:
           followernode = self.list_of_users[followerId]
           self.list_of_users[follweeId].friends.append(followernode)
       elif userID.count(follweeId)==1 and userID.count(followerId)==0:
           return("no such user found")

    def unfollowUser(self,followerId, follweeId):
        followerNode = self.list_of_users[follweeId]
        for i in followerNode.friends:
            if followerId == i.vertex['email']:
                followerNode.friends.remove(i)

    def postFeed(self,userid,feed):
        post = {
            "feed_id": next(uuid),
            "feed": feed,
            "like": 0,
            'dislike': 0,
            'hide': False
        }
        self.list_of_users[userid].vertex['posts'].append(post)
    def blockUser(self,currentuserId,userId):
        self.list_of_users[currentuserId].blockedusers.append(self.list_of_users[userId])

    def getUserFeeds(self,userId):
       return(self.list_of_users[userId].vertex["posts"]["feed"])

    def getFeedLikesCount(self,userid,feedId) :
            for i in self.list_of_users[userid].vertex["posts"]:
                if i["feed_id"] == feedId:
                    return(i["feed"])

    def getMyFeeds(self,currentUserId):
        return (self.list_of_users[currentUserId].vertex["posts"]["feed"])

    def deleteUser(self,userId):
        self.list_of_users.pop(self.list_of_users[userId])
     

user = ConnectWorld()
