"""
# SQLAlchemy (Base)

The base SQLAlchemy library is explored here (huzzah, it actually got done!)

There are 2 major aspects of SQLAlchemy: Core and ORM.

## Core

The low-level behind-the-scenes inner workings of SQLAlchemy -- typical
nitty-gritty relational database operations. It handles all the familiar
tables, SQL statements, database connection details, etc. when you use
SQLAlchemy to do a task.

## ORM (Object Relational Mapper)

The user-facing side of SQLAlchemy, in which Models are created, relationships
are defined, etc. It utilizes the Core under the hood to handle all the dirty
details for you.

The typical order of operations:
1. Create engine (setup for a connection to the database)
2. Establish a session (active connection to the database)
"""

import datetime

from sqlalchemy import (
    create_engine,
    text,
)
from sqlalchemy.orm import Session



########
# Engine
########

"""
Defines the connection to a database without actually connecting to it (yet).

Typical engine URL:
dialect+driver://username:password@host:port/database

SQLite URL
SQLite databases are slightly different because they only use the
local filesystem -- no potential networks.
sqlite://<no_host_name_needed>/<relative_path>
sqlite://<no_host_name_needed>//<absolute_path>
sqlite://<no_host_name_needed>/:memory:

Lazy initialization
Creating the engine does not cause an actual connection to the database until
a task is performed against the database (software pattern called
`lazy initialization`).

Echo
create_engine(<URL>, echo=True): create_engine.echo enables logging of all
SQL to standard out, thus is good for experimenting.
"""
engine = create_engine("sqlite:///database.sqlite", echo=True)

############
# Connection
############

"""
To execute tasks on the database, a Connection object is needed (since the
Engine object does not actually connect to the database -- it only sets up
everything to be used later). It isn't usually used manually; rather, the
ORM will utilize the Connection object under the hood. The Session object
is the ORM version that quietly uses the Core's Connection object.

with engine.begin() as connection:
    ...

Engine.connect()
The Connection object returned by this method is a "commit as you go" style
object, in that it requires Connection.commit() be called every time some task
needs to be committed to the database; tasks won't actually be finalized in
the database until this is performed. If the block ends and commit() was
never called, a ROLLBACK is executed (basically an undo). This is used more
frequently for testing/experimenting, as it allows more granular control.

Engine.begin()
This returns a "begin once" style object, in that Connection.commit() calls
are unnecessary; the entire block is committed automatically at the end, so long as
no exception was raised (otherwise a ROLLBACK is executed). This is preferred
for more general usage.

text()
Used for constructing raw SQL queries (i.e., generally should only be used for
demonstration purposes such as this).
"""

with engine.connect() as connection:
    result = connection.execute(text("SELECT 'hello world'"))
    print(result.all())

with engine.begin() as connection:
    connection.execute(text("CREATE TABLE a_table (x int, y int)"))
    connection.execute(
        text("INSERT INTO a_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 2}]
    )

########
# Result
########

"""
The Result object contains the rows returned by a Connection.execute() call
(if any). Each row is represented as its own Row object. Accessing the data
within them can be done in several ways.

Tuple assignment
for x, y in result:
    ...

Integer index
for row in result:
    row[i] ...

Attribute name
NOTE: Depending on the database, the column naming behavior is not always
predictable, but is usually the name assigned by the SQL statements (`SELECT
x, y FROM a_table`).

for row in result:
    row.x
    row.y

Mapping access
for dict_row in result.mappings():
    dict_row["x"]
"""

###########
# Execution
###########

"""
When using textual SQL ("raw" SQL statements), ALWAYS use parameterized
inputs ("bound inputs") to protect against injection attacks. However, textual
SQL is typically rarely, if ever, used with SQLAlchemy.

Optimizing multiple executions
For inputting multiple sets of data (e.g., above when inserting data into
`a_table`), the operation is optimized under the hood with .executemany()
rather than sending multiple .execute()/INSERT statements.
"""

#########
# Session
#########

"""
The Session object is essentially the ORM version of the Core's Connection
object. It actually uses Connection under the hood. When used with non-ORM
constructs, it behaves (generally) the same as Connection, including using
.execute() to perform transactions. It also requires a .commit() before leaving
the `with` block.

from sqlalchemy.orm import Session
with Session(engine) as session:
    session.execute(...)
    session.commit()
"""

with Session(engine) as session:
    result = session.execute(text("SELECT * FROM a_table"))
    print(result.all())

###################
# Database Metadata
###################

"""
'Database metadata' consists of objects that represent SQL concepts like tables,
columns, and data types.
"""

# Core

# ORM

