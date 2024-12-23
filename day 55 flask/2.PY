from flask import Flask
import random

app = Flask(__name__)

class User:
    def __init__(self, name):
        self.name = name 
        self.is_logged_in = False

def  is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Habeeb")
new_user.is_logged_in = False
create_blog_post(new_user)





# @app.route("/")
# def hello():
#     return '<h1 style="text-align :center" >Hello World</h1>\
#         <img src = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDN6NDBlZWk1dWQ5cmJrdjZpcGVkcW5jZGNrd3MyNjI5a2UyazgzYiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/I9XrL9Tc1jpe/giphy.gif" width = 200>'

# # @app.route("/<name>")
# def greet(name):
#     return f"Hello {name+12}"

# if __name__ == "__main__":
#     app.run(debug=True)
