class User:
    def __init__(self, username, id):
        self.username = username
        self.id = id

user1 = User("jack", 12)
print(user1.id)


user2 = User("Habeeb", 13)
print(user2.username)
user1.username = "Habeeb"
user1.id = 13

print(user1.id)