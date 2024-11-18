class User():
    id: int
    name: str
    isAdmin: bool
    
    def __init__(self, id: int, name: str, isAdmin: bool):
        self.id = id
        self.name = name
        self.isAdmin = isAdmin
        
class Post():
    id: int
    title: str
    content: str
    
    def __init__(self, id: int, title: str, content: str):
        self.id = id
        self.title = title
        self.content = content