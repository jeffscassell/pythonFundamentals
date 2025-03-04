# The * (unpacking) operator
# Behaves differently if used on function parameters compared to being used on variables.


#====================
# Function Parameters
#====================


# *args
# Creates a tuple (like a list, but immutable) of all passed arguments that can be iterated through.

def sum(*args: int) -> int:
    total = 0
    
    for x in args:
        total += x
    
    return total

print(sum(1, 2, 3, 4))
print()


# **kwargs
# Creates a dictionary from all keyword arguments that can be iterated through,
# e.g., a="something", b="something else", c=12, ... would create:
# dictionary = {
#     "a": "something",
#     "b": "something else",
#     "c": 12
# }

def concat(**kwargs: str) -> str:
    """ Expects all arguments to be strings. """
    
    string = ""
    
    for value in kwargs.values():
        value = value[0].upper() + value[1:]  # force camelCase
        string += value
        
    return string

print(concat(a="Python", b="is", c="so", d="powerful!"))
print()


#==========
# Variables
#==========


# The singular unpacking operator (*) will expand any iterable into its constituent elements,
# wherever it is being used. Includes strings, lists, tuples, and sets.
# Can also be used for interesting variable assignments.

myList = [1, 2, 3, 4]
a, *b, c = myList  # a will be the first element and c will be the last, while b contains the rest
# a = 1
# b = (2, 3)
# c = 4

print("Printing the list:", myList)  # print([1, 2, 3, 4])
print("Printing the unpacked list:", *myList)  # print(1, 2, 3, 4)
print("Variables that have been assigned from the list:", a, b, c)
print("The sum function using the unpacked list:", sum(*myList))
print("The sum function using the unpacked list, twice:", sum(*myList, *myList))
print("Can also unpack a string, since it's iterable:", *"string")
print()


# The double unpacking operator (**) will only work on dictionaries and it is used to do a similar thing as the
# singular operator. It will expand to key=value items, such as what a **kwargs parameter is expecting.

myDict = {
    "a": "something",
    "b": "something else",
    "c": 12,
    "d": 1
}

def printDict(**kwargs) -> None:
    a = kwargs.get("a")
    b = kwargs.get("b")
    c = kwargs.get("c")
    print(a, b, c)
    return

printDict(**myDict)  # printDict(a="something", b="something else", c=12, d=1)