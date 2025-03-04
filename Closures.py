from typing import Callable



# Closures:
# Higher-order functions that accept and return other functions, similar to how variables are handled by lower-
# order functions.

def makeHtmlTagWrapperFunction(tag: str) -> Callable[[str], None]:  # returns a function (a function is "Callable") that accepts a str variable and returns None
    
    def printTextWithTag(text: str) -> None:
        print("<" + tag + ">" + text + "</" + tag + ">")
    
    return printTextWithTag

# returns access to the inner function printTextWithTag() -- but does not execute it yet
printWithH1Tag = makeHtmlTagWrapperFunction("h1")

# executes the printTextWithTag() function and prints <h1>here is a header!</h1>
# it also "remembers" the original "h1" that had been passed in to the first function
printWithH1Tag("here is a header!")



# this accepts a function, which itself accepts 2 integers and returns an integer
# this then returns a function, which itself accepts 2 integers and returns None
def addLoggingToFunction(function: Callable[[int, int], int]) -> Callable[[int, int], None]:
    
    # could also use "a, b" as variable parameters to be more explicit, but the type checking is performed by the return type (Callable[[int, int], None]),
    # so it isn't strictly necessary
    def functionToLog(*args):
        print(function(*args))
        
    return functionToLog


def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

addWithLogging = addLoggingToFunction(add)
subtractWithLogging = addLoggingToFunction(subtract)

subtractWithLogging(5, 3)
addWithLogging(5, 5)