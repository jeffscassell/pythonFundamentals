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

############################
# Model relationship options
############################

#==========================
# Backref vs back_populates
#==========================

# Using backref:
class Artist1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paintings = db.relationship('Painting1', backref='artist')
    
class Painting1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist1.id'))
    # 'artist' attribute is automatically created

# Using back_populates:
class Author1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    books = db.relationship('Book1', back_populates='author')
    
class Book1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author1_id = db.Column(db.Integer, db.ForeignKey('author1.id'))
    author2_id = db.Column(db.Integer, db.ForeignKey('author2.id'))
    author3_id = db.Column(db.Integer, db.ForeignKey('author3.id'))
    
    # Must explicitly declare both sides
    author = db.relationship('Author1', back_populates='books')
    
#=====================
# Lazy loading options
#=====================

class Author2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

# 1. lazy='select' (default)
    books = db.relationship('Book1', lazy='select')
    """
    - Loads related data only when accessed
    - Generates new SQL query when relationship is accessed
    - Can lead to N+1 query problem
    """
    # Example of N+1 problem:
        # authors = Author.query.all()  # First query
        # for author in authors:
        #     print(len(author.books))  # New query for EACH author!

# 2. lazy='joined'
    books = db.relationship('Book1', lazy='joined')
    """
    - Loads related data immediately with JOIN
    - Single SQL query loads all data
    - Best when you know you'll need the related data
    """
    # Example:
        # author = Author.query.first()  # Loads author AND books in one query
        # print(len(author.books))  # No additional query needed

# 3. lazy='dynamic'
    books = db.relationship('Book1', lazy='dynamic')
    """
    - Returns SQLAlchemy query object instead of results
    - Allows adding filters before loading data
    - Good for relationships with many records
    """
    # Examples:
        # author = Author.query.first()
    
        # Get recent books only
            # recent_books = author.books.filter(Book.published_date > last_month).all()
    
        # Get count without loading all records
            # book_count = author.books.count()
    
        # Complex filtering
            # popular_books = author.books\
            #     .filter(Book.rating > 4)\
            #     .order_by(Book.published_date.desc())\
            #     .limit(5)\
            #     .all()

# 4. lazy='subquery'
    books = db.relationship('Book1', lazy='subquery')
    """
    - Loads all relationship data in a separate query
    - Good for loading relationships across multiple parents
    - Uses a subquery to fetch related data
    """
    # Example:
        # authors = Author.query.all()  # First query for authors
        
        
        # for author in authors:  # Single additional query loads books for ALL authors
        #     print(len(author.books))  # No additional queries
    
#================
# Cascade options
#================

class Author3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    # Different cascade options:
    
    # "all" - Includes all cascade options except delete-orphan
    books = db.relationship('Book1', cascade="all")
    
    # "all, delete-orphan" - Like "all" but also deletes orphaned records
    books = db.relationship('Book1', cascade="all, delete-orphan")
    # Example:
        # author = Author.query.first()
        # db.session.delete(author)  # This will also delete all associated books
    
    # Individual cascade options:
    # "save-update" - When you save/update the parent, do the same to children
    books = db.relationship('Book1', cascade="save-update")
    
    # "delete" - When parent is deleted, delete children
    books = db.relationship('Book1', cascade="delete")
    
    # "delete-orphan" - Delete children when they're removed from relationship
    books = db.relationship('Book1', cascade="delete-orphan, delete")  # delete must go with it
    # Example:
        # author.books = []  # This will delete all books
    
    # "merge" - When merging parent, merge children
    books = db.relationship('Book1', cascade="merge")
    
    # Multiple options can be combined
    books = db.relationship('Book1', cascade="save-update, delete")


###############
# Simple models
###############

#=========================
# One-to-many relationship
#=========================

# "one" side of one-to-many relationship
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    
    # not an actual column. references the class, so note the capital "Post." creates an ORM pseudo-column that can be used on Post
    # to access the entire User object
    # the lazy keyword signifies that when fetching the object, it will also fetch all of the associated objects (Posts in this case)
    posts = db.relationship("Post", backref="author", lazy=True)
    
    def __repr__(self):
        return f"<User {self.id}>: {self.name}, posts: {self.posts}"

# "many" side of one-to-many relationship
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now(datetime.timezone.utc))
    
    # IS an actual column, so references the table, which is automatically created/converted to snake_case. note the "user.id"
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    def __repr__(self):
        return f"<Post {self.id}>: {self.title}"

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
    following = db.relationship("Channel", secondary=viewer_channel, back_populates="followers")
    
    def __repr__(self):
        return f"<Viewer {self.id}>: {self.name}, following: {self.following}"


class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    
    followers = db.relationship("Viewer", secondary=viewer_channel, back_populates="following")
    
    def __repr__(self) -> str:
        return f"<Channel {self.id}>: {self.name}"
    
#===========================
# Working with Simple Models
#===========================

def makeFreshDatabase():
    with app.app_context():
        # create fresh, empty database every time it starts
        db.drop_all()
        db.create_all()
    

def seedDatabaseWithSimpleModels():
    print()
    print("create simple seeds")
    with app.app_context():
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
        if channel1:
            channel1.name = "ChilledChaosGames"
        print(channel1)
        db.session.commit()

        
def deleteSimpleSeeds():
    print()
    print("delete simple seeds")
    with app.app_context():
        # hard delete
        print(Channel.query.all())
        channel = Channel.query.filter_by(name="ChilledChaosGames").first()
        if channel:
            db.session.delete(channel)
            db.session.commit()
        print(Channel.query.all())
        
        # soft delete
            
###################
# Complex models
# Model Inheritance
###################

class Item(db.Model):
    """
    This is the "instances" Model, which tracks all of the physical copies of inventory.
    It contains only data that is common to all inventory (such as availability and
    inventory serials). Each entry is tied to another child table, like Book or Device.
    
    Each item type requires its own relationship and foriegn key column, but it makes
    handling them much easier (if not simpler).
    """
    
    id = db.Column(db.Integer, primary_key=True)
    
    # shared properties among all inventory
    inventory_serial = db.Column(db.String(20), nullable=False)
    is_availabile = db.Column(db.Boolean, nullable=False, default=True)
    deleted_at = db.Column(db.DateTime, nullable=True, default=None)
    
    item_type = db.Column(db.String(20), nullable=False)  # discriminator column
    
    # separate foreign keys for each item type
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=True)
    device_id = db.Column(db.Integer, db.ForeignKey("device.id"), nullable=True)
    
    # separate relationships for each item type
    book = db.relationship("Book", backref="instances")
    device = db.relationship("Device", backref="instances")
    
    @classmethod
    def getDeleted(cls):
        return cls.query.filter(cls.deleted_at != None)
    
    def __repr__(self):
        return f"<Item {self.id}>: type: {self.item_type}, serial: {self.inventory_serial}"
    

class Book(db.Model):
    """
    This is a "definition" Model. It tracks the unique Book items that the inventory contains,
    without any regard for the number of copies available or any other property that is
    specific to a single INSTANCE of a book.
    
    It is structured this way to avoid data duplication (and thus data entry errors) if
    there are multiple copies of a book. Each copy will have an entry in the Item Model, and
    all of the copies will reference this Book model.
    """
    
    id = db.Column(db.Integer, primary_key=True)    
    title = db.Column(db.String(50), nullable=False)
    retired_at = db.Column(db.DateTime, nullable=True, default=None)
    
    # causes a conflict due to overlapping on the Item.sub_item_id column with Device
    # items = db.relationship("Item", backref="book", lazy=True, primaryjoin="foreign(Item.sub_item_id) == Book.id and Item.item_type == 'book'")
    
    def __repr__(self) -> str:
        return f"<Book {self.id}>: {self.title}"


class Device(db.Model):
    """
    This is another "definition" Model, similiar to Book.
    """
    
    # __tablename__ = "devices"
    
    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String(50), nullable=False)
    retired_at = db.Column(db.DateTime, nullable=True, default=None)
    
    # items = db.relationship("Item", backref="device", lazy=True, primaryjoin="foreign(Item.sub_item_id) == Device.id and Item.item_type == 'device'")
    
    def __repr__(self) -> str:
        return f"<Device {self.id}>: {self.name}"
    
#============================
# Working with Complex Models
#============================
    
def seedComplexModels():
    print()
    print("create complex seeds")
    with app.app_context():
        book1 = Book(title="that was then, this is now")
        book2 = Book(title="i love python")
        db.session.add_all([book1, book2])
        newDevice = Device(name="YI Home Camera")
        db.session.add(newDevice)
        db.session.commit()
        
        #! newBook.id can only be referenced after newBook has been comitted to the database
        bookInstance1 = Item(item_type="book", book=book1, inventory_serial="ICF-1000")
        bookInstance2 = Item(item_type="book", book=book2, inventory_serial="ICF-1001")
        db.session.add_all([bookInstance1, bookInstance2])
        db.session.commit()

    
def printComplexSeeds():
    print()
    print("read complex seeds")
    with app.app_context():
        # read all books
        bookInstances = Item.query.filter_by(item_type="book").all()
        print(bookInstances)
        
        # read all instances of a single book
        bookInstances = Book.query.filter_by(title="that was then, this is now").first().instances
        for bookInstance in bookInstances:
            print(f"{bookInstance}, title: {bookInstance.book.title}")
        
        

def updateComplexSeeds():
    print()
    print("update complex seeds")
    with app.app_context():
        ...
        
        
def deleteComplexSeeds():
    print()
    print("delete complex seeds")
    with app.app_context():
        ...



if (__name__ == "__main__"):
    makeFreshDatabase()
    
    # seedDatabaseWithSimpleModels()  # create
    # printSimpleSeeds()  # read
    # updateSimpleSeeds()  # update
    # deleteSimpleSeeds()  # delete
    
    seedComplexModels()  # create
    printComplexSeeds()  # read
    updateComplexSeeds()  # update
    deleteComplexSeeds()  # delete
