# Context Managers

# Provide a way to safely interact with external resources, such as files or network connections.
# They will handle releasing the resource when it is no longer being used, so that
# a resource leak can be avoided.



#========================
# Try...Finally statement
#========================

# Verbose, but general-purpose and language-agnostic.

try:
    file = open("context.txt", "w")
except:
    print("Error opening file: context.txt")


try:
    file.write("some test string here, blah blah blah")
except Exception as error:
    print("An error occurred while trying to write to file: context.txt")
    print(error)
finally:
    file.close()
    
#===============
# With statement
#===============

# Succinct, but specific to Python. Relies on the class implementing the
# __enter__() and __exit__() methods, for use when starting and ending
# the context management block.

with open("context.txt", "w") as file:
    file.write("Some text for our file!")
    
# Custom context managers can also be created, both with classes and functions

# Class

class HelloContextManager():
    def __enter__(self):
        print("Entering context manager...")
        return "Hello!"
    
    def __exit__(self, exceptionType, exceptionValue, exceptionTraceback):
        """ Returns None (x3) if no exception occurs, or the relevant exception details. """
        print("Exiting context manager...")
        print(exceptionType, exceptionValue, exceptionTraceback, sep="\n")  # print each value, separated by a newline (\n)


with HelloContextManager() as hello:
    print(hello)
    
#==========================
# Exception handling within
# the With context manager
#==========================

