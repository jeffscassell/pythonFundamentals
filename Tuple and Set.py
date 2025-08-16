# Tuple
# Essentially, immutable version of a list.

# tuples use parenthesis instead of list's square bracket
tup = (10, 20, 30, 15, 12)

# attempting to add another value will throw an error
try:
    tup[0] = 0  # type: ignore
except TypeError:
    print("tuples cannot be changed (they are immutable)")



# Set
# prioritizes speed over all else. there is no sequencing (the contents are stored randomly), and a value may occur
# only once. because it is unsequenced, it cannot be indexed

# sets use curly braces
s = {5, 21, 1, 0, 55, 10, 5}
print(s)

# cannot use indexing
try:
    s[0]  # type: ignore
except TypeError:
    print("sets do not support indexing (subscripting)")
