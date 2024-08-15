# a = 10
# print(a)
#
# a = "this is my page"
# print(a)

# age:int = 10
# print(age)
#
# # age = "age in string"
# # print(age)
#
# age = 20
# print(age)


# Typing techniques

# def square(num: float):
#     return (num * num)
#
#
# print(square(10.00))

sq: float = 0


def squareDividedBy2(num: float) -> float:  # specify the return type of function
    return (num * num) // 2


sq = squareDividedBy2(10.00)
print(sq)


def square(num: float) -> None:  # specify the return type of function as None
    print(num * num)


square(10.00)

# What if we want this for different data structure?
# numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "abc"]
# print(numbers)
#
# # dict1: dict[int, str] = {1: "abc", 2: "bcd"}
# dict1: dict[int, str] = {1: "abc", "bcd": 2}   # what if we replace the key value data type
# print(dict1)


# numSet: set[str] = {"abc", "efg", "hij", "hij"}
# numSet: set[str] = {"abc", "efg", "hij", "hij", 6}  # what if we introduce int
#
# print(numSet)

# what about list of list?
# ll: list[list[int]] = [[1, 2, 3], [3, 4, 5]]
# ll: list[list[int]] = [[1, 2, 3], [3, 4, 5, "abc"]]
# print(ll)
#
# # what if we have to use list[list[int]] at many places
#
# vector = list[list[int]]
# ll2: vector = [[1, 2, 3], [3, 4, 5, "abc"]]
# print(ll2)

# def greet(name: str = None) -> str: # this name is optional
#     return f"Hello {name}"
# In above code we are getting error in mypy to resolve this try below changes
from typing import Optional, Any


# def greet(name: Optional>>str | None) -> str:
def greet(name: Optional[str] = None) -> str:  # this name is optional
    return f"Hello {name}"


print(greet())


def printingmethod(val: Any):
    print(val)


printingmethod("rr")
printingmethod(1)
printingmethod([1])


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def getPersonName(person: Person) -> str:
    return person.name


getPersonName(Person("John", 22))
# getPersonName("asdas")  # this will throw error


# Generics...

# Assume there is a STACK, and we do not have an idea of "ANY"
# class stack:
#
#     def __init__(self: str) -> None:
#         self.stack: list[str] = []
#
#     def push(self, item: str) -> None:
#         self.stack.append(item)
#
#     def pop(self) -> str:
#         return self.stack.pop()

# If we have to use int in stack
# class stackint:    # this is not a correct way
#
#     def __init__(self: int) -> None:
#         self.stack: list[int] = []
#
#     def push(self, item: int) -> None:
#         self.stack.append(item)
#
#     def pop(self) -> int:
#         return self.stack.pop()

# in the above one we have code duplicates, we have to create class such that it excepts any datatype on runtime
# for that we use below GENERICS

from typing import Generic, TypeVar, Type

# T = TypeVar('T')
#
#
# class Stack(Generic[T]):
#
#     def __init__(self: T) -> None:
#         self.stack: list[T] = []
#
#     def push(self, item: T) -> None:
#         self.stack.append(item)
#
#     def pop(self) -> T:
#         return self.stack.pop()
#
#
# stack1 = Stack[int]()

T = TypeVar("T", int, float)


def add(a1: T, a2: T) -> T:
    return a1 + a2


print(add(1, 1))
print(add(1.0, 1))
print(add(1.0, 1.0))


# print(add(1.0,"1"))

# if we use ANY - it will take any data type at same time - str, int, float
# if we use generics - it allow is to specify the type as int or float , then that datatype is only allow


class A:

    def __init__(self, x: int) -> None:
        self.x = x


class B(A):

    def __init__(self, x: int) -> None:
        self.x = x
        super().__init__(x)


class C(A):

    def __init__(self, x: int) -> None:
        self.x = x
        super().__init__(x)


G = TypeVar('G', bound=A)   # bount to A, so whoever below parent class can use it
