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
    
    
    
# Custom context managers can also be created, both with classes and functions,
# but the functions require more in-depth knowledge specific to Python so I'll
# avoid those details

class SampleContextManager():
    
    # if we didn't have this, we would just initialize with PrintContextManager() -- no arguments
    def __init__(self, message: str):
        self.message = message
    
    def __enter__(self):
        print("Entering context manager...")
        return self.message  # could also return a pre-defined value instead
    
    def __exit__(self, exceptionType, exceptionInstance, exceptionTraceback):
        """
        Is called when exiting the context manager. If there is an exception that has occurred,
        Then the exception type, an instance of the exception, and the traceback are passed into this
        function.
        
        By default, this function returns False, which means that any exceptions are forwarded along to
        the rest of the program and need to be handled. If we instead return True, exceptions are
        "swallowed" and stop here.
        """
        
        print("Exiting context manager...")
        print(exceptionType, exceptionInstance, exceptionTraceback, sep="\n")  # print each value, separated by a newline (\n)
        print()
        
        if (isinstance(exceptionInstance, IndexError)):
            print("IndexError occurred!")
            return True


with SampleContextManager("a random string :)") as message:
    print(message)


# Exception handling within the context manager is still necessary

with SampleContextManager("a random string :)") as message:
    print(message)
    
    try:
        print(message[100])
    except:
        print("Exception occurred, but was caught by a try statement, so we can continue")
    
    # an uncaught exception will immediately call the __exit__() function with the relevant arguments
    
    print(message[100])
    print("We never reach here because execution stops within context after an error, if uncaught")
    
print("Execution continues outside of context after an error (if handled within)")
print()

#==================
# Recursive context
#==================

class Indenter:
    def __init__(self):
        self.level = -1

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.level -= 1

    def print(self, text):
        print("    " * self.level + text)
        

with Indenter() as indent:
    indent.print("level 1")
    
    with indent:
        indent.print("level 2")
        
        with indent:
            indent.print("level 3")
    
    indent.print("and we're back to level 1")