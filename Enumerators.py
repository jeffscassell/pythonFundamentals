"""
Enum (enumerator)
Used when there are going to be set values used repeatedly and you want to avoid mistyping something.
Ensures consistency and readability across a codebase

It is always recommended to use the StrEnum or IntEnum classes, rather than the base Enum class, so its use
is more explicit and so that you can use the values directly.
e.g., StatusCodes.OK will insert the literal integer value 200, without having to implement anything beyond the key/value pairs,
whereas this is not the case if your class is using Enum
"""

from enum import IntEnum, Enum



class IntStatusCodes(IntEnum):
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401  # client is unknown
    FORBIDDEN = 403  # client is known, and does not have permission
    NOT_FOUND = 404
    TIMEOUT = 408
    CONFLICT = 409
    GONE = 410
    UNSUPPORTED_MEDIA_TYPE = 415  # type of media sent to the server is not supported by the server
    TOO_MANY_REQUESTS = 429
    INTERNAL_ERROR = 500

class BaseStatusCodes(Enum):
    OK = 200
    CREATED = 201
    

# Both of these work fine

if (200 in IntStatusCodes):
    print("Status 200 found in IntStatusCodes")
    
if (200 in BaseStatusCodes):
    print("Status 200 found in BaseStatusCodes")

# But under the hood they are handled differently

print("IntEnum member:", IntStatusCodes.OK)
print("Enum member:", BaseStatusCodes.OK)

print("Accessing members by name:", BaseStatusCodes.OK)
print("Accessing members by value:", BaseStatusCodes(200))
