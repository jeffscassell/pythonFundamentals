# Dictionary
# key-value pairs. the keys are unique and immutable (but can be deleted), the values are not.

# uses curly braces, with colon to separate the key-value pairs
dic = {1: "jeff", 7: "kalina", 3: ""}

# can access data like lists, but instead of specifying an index to access a value, the key is specified
print(dic[1])
print()

# preferred way to access data is with the get() method, because if key does not exist no error is returned
print("access dictionary values")
print("safely accessing a dictionary value using get():", dic.get(2, "key 2 does not exist"))
print(dic.get(7))
print("after calling get(7):", dic)
print(dic.pop(7))
print("after calling pop(7):", dic)
print()

# if pop calls a non-existent key, an error is raised unless a default value is specified
print("popping an empty string:", dic.pop(3))
try:
    print(dic.pop(3))
except KeyError:
    print("KeyError was raised!")
print("accessing a non-existent key:", dic.pop(3, "key missing"))
print()

# one way to set a new value is by specifying a key
dic[2] = "dad"
print(dic)
print()

# to remove a key-value pair, use the del() method -- pop() can also be used similarly to lists
print("remove dictionary pairs")
del dic[2]
print(dic)
print()

# dictionaries can be built from lists in a slightly complex series of steps
print("zip two lists together to create a dictionary")
keys = ["jeff", "kalina", "dad", "jr"]
values = ["computers", "art", "relaxing", "weed"]
dic = dict(zip(keys, values))
print(dic)
print()

# combine dictionaries
print("combine two (or more) dictionaries")
dict1 = {1: "one", 2: "two"}
dict2 = {3: "three", 4: "four"}
print({**dict1, **dict2})
print()

# key-value pairs do not have to match each others' data types, and can in fact store lists or other dictionaries (or even objects)
class TestObject:
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message
    
programs = {
    "JS": "Atom",
    "CS": "VS",
    "Python": ["PyCharm", "Sublime"],
    "Java": {"JSE": "NetBeans", "JEE": "Eclipse"},
    "obj": TestObject("a test object")
}
print(programs["Python"])
print(programs["Python"][1])
print(programs["Java"]["JEE"])
print(programs["obj"])
print()

# check if a key exists in the dictionary
dic = {"jr": "drogas", "jeff": ""}
if "jr" in dic:
    print("Jr is in the dictionary!")
print()