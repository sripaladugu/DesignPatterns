In Python, both Abstract Base Classes (ABC) and Protocols are used to define interfaces or contracts that can be implemented by other classes. However, they serve slightly different purposes and have different implications for the design of your code.

** Abstract Base Classes (ABC) **
Abstract Base Classes are a way to define interfaces in Python that can enforce the implementation of certain methods in subclasses. They are part of the abc module and are used when you want to ensure that a derived class implements specific methods.

** Key Characteristics of ABC: **

- Method Enforcement: Using ABCs allows you to define abstract methods that must be implemented by any subclass.
- Instantiation: You cannot instantiate an ABC directly; you must subclass it and implement its abstract methods.
- Decorator: Abstract methods are defined using the @abstractmethod decorator.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())  # Output: 78.5
```

** Protocols **
Protocols, introduced in Python 3.8 with PEP 544, provide a way to define "structural" subtyping (also known as "duck typing"). Unlike ABCs, protocols do not enforce method implementation; instead, they specify a set of methods or properties that a class must have to be considered as implementing the protocol.

** Key Characteristics of Protocols: **

- Structural Typing: Protocols define a set of method signatures that can be implemented by any class without needing explicit subclassing.
- Flexibility: Classes that have the required methods are considered as implementing the protocol, even if they do not inherit from the protocol.

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None:
        ...

class Circle:
    def draw(self) -> None:
        print("Drawing a circle")

def render(shape: Drawable):
    shape.draw()

circle = Circle()
render(circle)  # This works because Circle has a draw() method
```
