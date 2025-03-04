from myPackage.models import User, Post



class Form():
    user: User
    post: Post
    
    def __init__(self, user: User, post: Post):
        self.user = user
        self.post = post