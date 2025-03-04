from abc import ABC, abstractmethod
from random import shuffle
from typing import Callable



# Strategy Pattern
# Typically, the pattern will use classes, and this is especially useful for
# complex functionality. But it is also possible to use functions to achieve the same thing,
# if the task is fairly simple such as in this example.


#========
# Classes
#========


# Some Ticket objects that will need sorting

class Ticket():
    id: int
    customer: str
    issue: str
    
    def __init__(self, id: int, customer: str, issue: str):
        self.id = id
        self.customer = customer
        self.issue = issue
    
    def __str__(self):
        string = ""\
            f"==============================\n"\
            f"Ticked ID: {self.id}\n"\
            f"Customer: {self.customer}\n"\
            f"Issue: {self.issue}\n"\
            f"=============================="
        return string
    
    
# Throw away function to make some tickets to sort

def makeTickets() -> list[Ticket]:
    tickets = []
    customers = ["Jerry Smith", "Rick Sanchez", "Morty Smith", "Summer Smith", "Beth Smith"]
    issues = [
        "Directions too complicated, got dick stuck in fan",
        "It doesn't print me money",
        "I got lost in space",
        "I'm too busy trying to be popular",
        "I don't know what I want"
    ]
    
    for x in range(3):
        tickets.append(Ticket(x, customers[x], issues[x]))
    
    return tickets


# The different strategies to use
    
class Strategy(ABC):
    
    @abstractmethod
    def sort(self, tickets: list[Ticket]) -> list[Ticket]: ...
    
    
class FIFOStrategy(Strategy):
    def sort(self, tickets: list[Ticket]) -> list[Ticket]:
        print("Using FIFO strategy:")
        return tickets.copy()
    
class FILOStrategy(Strategy):
    def sort(self, tickets: list[Ticket]) -> list[Ticket]:
        print("Using FILO strategy:")
        copy = tickets.copy()
        copy.reverse()
        return copy
    
class RandomStrategy(Strategy):
    def sort(self, tickets: list[Ticket]) -> list[Ticket]:
        print("Using Random strategy:")
        copy = tickets.copy()
        shuffle(copy)
        return copy


def processTicketsWithObjects(tickets: list[Ticket], strategy: Strategy) -> None:
    sortedTickets = strategy.sort(tickets)
    for ticket in sortedTickets:
        print(ticket)
    return


tickets = makeTickets()
processTicketsWithObjects(tickets, FIFOStrategy())
print()
processTicketsWithObjects(tickets, FILOStrategy())
print()
processTicketsWithObjects(tickets, RandomStrategy())
print()


#==========
# Functions
#==========


def fifoStrategy(tickets: list[Ticket]) -> list[Ticket]:
        print("Using FIFO strategy:")
        return tickets.copy()
    
def filoStrategy(tickets: list[Ticket]) -> list[Ticket]:
        print("Using FILO strategy:")
        copy = tickets.copy()
        copy.reverse()
        return copy
    
def randomStrategy(tickets: list[Ticket]) -> list[Ticket]:
        print("Using Random strategy:")
        copy = tickets.copy()
        shuffle(copy)
        return copy
    

def processTicketsWithFunctions(
        tickets: list[Ticket],
        strategy: Callable[[list[Ticket]], list[Ticket]]  # Accepts a function, which takes a list of tickets, and returns a list of tickets
    ) -> None:
    
    sortedTickets = strategy(tickets)
    
    for ticket in sortedTickets:
        print(ticket)
    
    return


processTicketsWithFunctions(tickets, fifoStrategy)
print()
processTicketsWithFunctions(tickets, filoStrategy)
print()
processTicketsWithFunctions(tickets, randomStrategy)
print()