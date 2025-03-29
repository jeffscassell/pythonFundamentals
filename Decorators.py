from typing import Callable
from functools import wraps



# Decorators:
# Usually a type of closure function (see Closures.py) to dynamically alter or add to the functionality of a wrapped function.

def decoratorFunction(wrappedFunction: Callable) -> Callable:
    
    # Preserves the function.__name__ for various uses (readability/debugging/logging/etc.).
    # Mostly useful when adding multiple decorators (nesting), but best practice is to always use it for future-proofing.
    @wraps(wrappedFunction)
    # This "*args" and "**kwargs" allows us to wrap functions that also accept arguments and pass those arguments along
    def wrapper(*args, **kwargs):
        print("Wrapper function ran")
        return wrappedFunction(*args, **kwargs)
        
    return wrapper


# This decorator is the same thing as:
#   decoratedDisplay = decoratorFunction(displayFunction)
# and then calling decoratedDisplay().
@decoratorFunction
def display():
    print("Display function ran")
    
@decoratorFunction
def displayInfo(name, age):
    print(f"Display info ran with arguments ({name}, {age})")
    
    
display()
print()
displayInfo("Jeff", 35)
print()



# Stacking decorators

def firstDecoratorFunction(wrappedFunction: Callable) -> Callable:
    
    @wraps(wrappedFunction)
    def wrapper(*args, **kwargs):
        print("First decorator ran")
        return wrappedFunction(*args, **kwargs)
        
    return wrapper

def secondDecoratorFunction(wrappedFunction: Callable) -> Callable:
    
    @wraps(wrappedFunction)
    def wrapper(*args, **kwargs):
        print("Second decorator ran")
        return wrappedFunction(*args, **kwargs)
        
    return wrapper


@firstDecoratorFunction
@secondDecoratorFunction
def subtract(a, b):
    print(f"Subtracted {a} - {b}:", a - b)

subtract(5, 5)
print()



# Decorators can also be implemented with classes, but they're less common.
# The benefit is they have added functionality, should it be required.

class DecoratorClass(object):
    function: Callable
    
    def __init__(self, function: Callable):
        self.function = function
        
    def __call__(self, *args, **kwargs):
        print("Call method executed")
        return self.function(*args, **kwargs)
        

@DecoratorClass
def add(a, b):
    print(f"Added {a} + {b}:", a + b)
    

add(1, 2)
print()



# Decorators can take arguments, too.

def argumentDecorator(argument) -> Callable:
    
    def decoratorFunction(wrappedFunction: Callable) -> Callable:
        
        @wraps(wrappedFunction)
        def wrapper(*args, **kwargs):
            print("Ran wrapper function with argument:", argument)
            return wrappedFunction(*args, **kwargs)
        
        return wrapper
    
    return decoratorFunction


@argumentDecorator("something")
def divide(a, b):
    return print(f"Divided {a} by {b}:", a / b)


divide(6, 2)