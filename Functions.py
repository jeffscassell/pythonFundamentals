# Functions
# equivalent to java's methods

# define the function
def greet() -> None:  # specifies the return type
    print("Hello, world!")


# call the function
greet()


# simple function that accepts parameters
def add(x, y):
    return x + y


print(add(2, 3))


# a function can return 2 values
def multiReturn(x, y):
    return x+y, x-y


print(multiReturn(2, 3))


# can also define a default value if an argument is not provided
def defaultValue(a, b=5):
    return a + b


print(defaultValue(2))


# can specify multiple of a single parameter
def addMultiple(*b):  # this is technically accepting a tuple
    c = 0
    for i in b:
        c += i
    return c


print(addMultiple(5, 3, 2, 1, 4))

# it is also possible to provide arguments out of order, if they are provided with the variable name
print(multiReturn(y=4, x=5))


# instead of accepting a tuple for multiple arguments, it is possible to accept a dictionary
def printDictionary(a, **b):
    print(a)
    for i, j in b.items():  # .items method returns the dictionary's keys and values in pairs
        print(i, j)


printDictionary("test", name="jeff", age=31, likes="computers")
