# List
# mutable, easy to use, all the benefits of an array and a referenced object

# looks a lot like an array, but it's an object
nums = [25, 12, 15, 55]
print(nums, "\n")  # the second argument is appended to the end of the line (on top of the normal \n)

# items are accessed like an array
print(nums[0])

# items can also be accessed in ranges
print(nums[:2])
print(nums[2:])

# indexes can also be called, starting from the end of the list
print(nums[-1])

# python lists can contain multiple data types
variety = ["jeff", 5, 2.2]
print("variety list: " + str(variety))
print()

# the brackets aren't required -- but they are strongly encouraged due to tuples and sets existing
# lists can also contain other lists (2D lists)
combined = nums, variety
print(combined)

# lists are dynamic and items can be added or removed as needed
nums.append(66)
print(nums)
print()

# because the nums lists is referenced in the combined list, it is updated as well
print(combined)
print()

# remove items by value using remove(), or by index using pop()
nums.remove(66)
nums.pop(2)  # not specifying an index will pop the last (just like a stack)
print(nums)
print()

# items can also be added at a specific index -- re-arranging the indexes of everything else -- using insert(index,
# value)
nums.insert(0, 22)
print(nums)

# it is possible to delete a range
del nums[2:]
print(nums)

# and add a range
nums.extend([5, 6, 7])
print(nums)
print()

# a few built-in methods (functions, whatever) for processing lists
print(min(nums))
print(max(nums))
print(nums.count(5))  # counts the occurrences of the given value in the list
print(nums.index(22))  # returns the index of the given value
nums.sort()
print(nums)
