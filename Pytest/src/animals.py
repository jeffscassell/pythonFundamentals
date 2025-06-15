from abc import ABC, abstractmethod



class Animal(ABC):
    
    @abstractmethod
    def speak(self) -> str: ...


class Cat(Animal):
    
    def speak(self):
        return "meow"
        

class Dog(Animal):
    
    def speak(self):
        return "bark"