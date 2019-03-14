import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastId = 0
        self.users = {}
        self.friendships = {}
    
    def add_user(self, name):
        self.lastId += 1
        self.users[self.lastId] = User(name)
        self.friendships[self.lastId] = set()

    def add_friendship(self, userID, friendID):
        if userID == friendID:
            print("Cannot friend yourself")
        else:
            if userID not in self.friendships and friendID not in self.friendships:
                self.friendships[userID].add(friendID)
                self.friendships[friendID].add(userID)
            else:
                print("Already friends with this user.")

    def populate_graph(self, numUsers, avgFriendships):
        if numUsers < avgFriendships:
            return "That is impossible!!"

        # add users
        for i in range(numUsers):
            self.add_user(f"Friend ID {i+1}")

        # add friendships
        friendships = []
        friends_left = numUsers * avgFriendships
        total_friends = numUsers * avgFriendships
        
        for i in range(numUsers):
            if friends_left > 0:
                friends = round(random.random()*avgFriendships*2)
                friends_left -= friends
                friendships.append(friends)
            elif friends <= 0:
                friends.append(0)
        
        while sum(friendships) < total_friends:
            for i in range(len(friendships)):
                if friends_left:
                    friendships[i] += 1
                    friends_left -= 1
        
        for user in self.users:
            if friendships[user-1]:
                for new_friend_index in range(len(friendships)):
                    if friendships[new_friend_index] == friendships[user-1]:
                        pass
                    elif friendships[new_friend_index] and friendships[user-1]:
                        if new_friend_index not in self.friendships[user]:
                            self.add_friendship(user, new_friend_index+1)
                            friendships[new_friend_index] -= 1
                            friendships[user-1] -= 1