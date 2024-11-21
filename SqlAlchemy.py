import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# Flask-SQLAlchemy

# I would rather learn base SQLAlchemy as it's more generic and learning it would be more
# agnostic compared to the Flask-specific variant, but this is for work and
# I just need to get this project done already.

app = Flask("SQLAlchemy Testing")  # start the flask app
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"  # specify the database location/name
db = SQLAlchemy(app)  # attach the SQLAlchemy instance to our flask app instance



#=========================
# One-to-many relationship
#=========================

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    
    # not an actual column. references the class, so note the capital "Post." creates an ORM pseudo-column that can be used on Post
    # to access the entire User object
    # the lazy keyword signifies that when fetching the object, it will also fetch all of the associated objects (Posts in this case)
    posts = db.relationship("Post", backref="author", lazy=True)  # one-to-many relationship
    
    def __repr__(self):
        return f"User {self.id}: {self.name}, posts: {self.posts}"
    
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now(datetime.timezone.utc))
    
    # IS an actual column, so references the table, which is automatically created/converted to snake_case. note the "user.id"
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    def __repr__(self):
        return f"Post {self.id}: {self.title}"
    
#==========================
# Many-to-many relationship
#==========================

# An intermediary table is required to track both Models
viewer_channel = db.Table(
    "viewer_channel",
    db.Column("viewer_id", db.Integer, db.ForeignKey("viewer.id")),
    db.Column("channel_id", db.Integer, db.ForeignKey("channel.id"))
)


class Viewer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    
    # adds pseudo-column "following" on Viewer, and pseudo-column "followers" on Channel
    # both can be manipulated as if they were lists
    following = db.relationship("Channel", secondary=viewer_channel, backref="followers")
    
    def __repr__(self):
        return f"Viewer {self.id}: {self.name}, following: {self.following}"


class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    
    def __repr__(self) -> str:
        return f"Channel {self.id}: {self.name}"
            
#=========================
# Joined Table Inheritance (?)
#=========================

class Item(db.Model):
    """
    This is the "instances" Model, which tracks all of the physical copies of inventory.
    It contains only data that is common to all inventory (such as availability and
    inventory serials). Each entry is tied to another child table, like Book or Device.
    
    This requires more manual handling of queries, but cuts down on complexity in the ORM.
    """
    
    id = db.Column(db.Integer, primary_key=True)    
    item_type = db.Column(db.String(20), nullable=False)
    sub_item_id = db.Column(db.Integer, nullable=False)
    inventory_serial = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return f"Item type: {self.item_type}, serial: {self.inventory_serial}"
    

class Book(db.Model):
    """
    This is a "data" Model. It tracks the unique Book items that the inventory contains,
    without any regard for the number of copies available or any other property that is
    specific to a single INSTANCE of a book.
    
    It is structured this way to avoid data duplication (and thus data entry errors) if
    there are multiple copies of a book. Each copy will have an entry in the Item Model, and
    all of the copies will reference this Book entry.
    """
    
    id = db.Column(db.Integer, primary_key=True)    
    title = db.Column(db.String(50), nullable=False)
    
    # causes a conflict due to overlapping on the Item.sub_item_id column with Device
    # items = db.relationship("Item", backref="book", lazy=True, primaryjoin="foreign(Item.sub_item_id) == Book.id and Item.item_type == 'book'")
    
    def __repr__(self) -> str:
        return f"Book: {self.title}"


class Device(db.Model):
    """
    This is another "data" Model, similiar to Book.
    """
    
    # __tablename__ = "devices"
    
    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String(50), nullable=False)
    
    # items = db.relationship("Item", backref="device", lazy=True, primaryjoin="foreign(Item.sub_item_id) == Device.id and Item.item_type == 'device'")
    
    def __repr__(self) -> str:
        return f"Device: {self.name}"
    
#===========================
# Working with Simple Models
#===========================

def seedDatabaseWithSimpleModels():
    print()
    print("create simple seeds")
    with app.app_context():
        # create fresh, empty database every time it starts
        db.drop_all()
        db.create_all()
        
        # create one-to-many samples
        user1 = User(name="jeff")
        user2 = User(name="jr")
        post1 = Post(title="post 1", author=user1)
        
        #! user_id can also be used, but the reference (User) must already be comitted in the database
        post2 = Post(title="post 2", author=user2)
        
        # create many-to-many samples
        viewer1 = Viewer(name="jeff")
        viewer2 = Viewer(name="jr")
        channel1 = Channel(name="ChilledChaos")
        channel2 = Channel(name="Viva La Dirt League D&D")
        viewer2.following.append(channel2)
        
        db.session.add_all([viewer1, viewer2, user1, user2, post1, post2, channel1, channel2])
        db.session.commit()
        
        
def printSimpleSeeds():
    print()
    print("read simple seeds")
    with app.app_context():
        users = User.query.all()
        for user in users:
            print(user)
        print()
            
        posts = Post.query.all()
        for post in posts:
            print(f"{post}, author: {post.author.name}")
        print()
            
        viewers = Viewer.query.all()
        for viewer in viewers:
            print(viewer)
        print()
            
        channels = Channel.query.all()
        for channel in channels:
            print(f"{channel}, followers: ", end="")
            for follower in channel.followers:
                print(follower.name, end=", ")
            print()
            
    
def updateSimpleSeeds():
    print()
    print("update simple seeds")
    with app.app_context():
        channel1 = Channel.query.filter_by(name="ChilledChaos").first()
        print(channel1)
        channel1.name = "ChilledChaosGames"
        print(channel1)
        db.session.commit()

        
def deleteSimpleSeeds():
    print()
    print("delete simple seeds")
    with app.app_context():
        print(Channel.query.all())
        
        channel = Channel.query.filter_by(name="ChilledChaosGames").first()
        if channel:
            db.session.delete(channel)
            db.session.commit()
        
        print(Channel.query.all())
    
#============================
# Working with Complex Models
#============================
    
def seedComplexModels():
    with app.app_context():
        newBook = Book(title="that was then, this is now")
        db.session.add(newBook)
        newDevice = Device(name="YI Home Camera")
        db.session.add(newDevice)
        db.session.commit()
        
        #! newBook.id can only be referenced after newBook has been comitted to the database
        bookInstance = Item(item_type="book", sub_item_id=newBook.id, inventory_serial="ICF-1000")
        db.session.add(bookInstance)
        db.session.commit()

    
def printComplexSeeds():
    with app.app_context():
        # read all books
        books = Item.query.filter_by(item_type="book").all()
        print(books)



if (__name__ == "__main__"):
    seedDatabaseWithSimpleModels()  # create
    printSimpleSeeds()  # read
    updateSimpleSeeds()  # update
    deleteSimpleSeeds()  # delete
    
    seedComplexModels()
    printComplexSeeds()