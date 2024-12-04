# Dictionary
# key-value pairs. the keys are unique and immutable (but can be deleted), the values are not.

# uses curly braces, with colon to separate the key-value pairs
dic = {1: "jeff", 7: "kalina"}

# can access data like lists, but instead of specifying an index to access a value, the key is specified
print(dic[1])

# preferred way to access data is with the get() method, because if key does not exist no error is returned
print(dic.get(7))
print(dic.get(2, "key 2 does not exist"))
print()

# one way to set a new value is by specifying a key
dic[2] = "dad"
print(dic)

# to remove a key-value pair, use the del() method -- pop() can also be used similarly to lists
del dic[2]
print(dic)
print()

# dictionaries can be built from lists in a slightly complex series of steps
keys = ["jeff", "kalina", "dad", "jr"]
values = ["computers", "art", "relaxing", "weed"]
dic = dict(zip(keys, values))
print(dic)
print()

# combine dictionaries
dict1 = {1: "one", 2: "two"}
dict2 = {3: "three", 4: "four"}
print({**dict1, **dict2})
print()

# key-value pairs do not have to match each other's data types, and can in fact store lists or other dictionaries
programs = {
    "JS": "Atom",
    "CS": "VS",
    "Python": ["PyCharm", "Sublime"],
    "Java": {"JSE": "NetBeans", "JEE": "Eclipse"}
}
print(programs["Python"])
print(programs["Python"][1])
print(programs["Java"]["JEE"])

# check if a key exists in the dictionary
dic = {"jr": "weed"}
if "jr" in dic:
    print("Jr is in the dictionary!")
