"""Examples of optional parameters and Union types."""

from typing import Union


def hello(name: Union[str, int, float] = "World") -> str:
    """A delightful greeting."""
    greeting: str = "Hello, "
    if isinstance(name, str):
        greeting += "COMP " + name
    elif isinstance(name, int):
        greeting += "COMP " + str(name)
    else:
        greeting += "ALIEN LIFE FORM FROM SECTOR " + str(name)    
    return greeting


# Single argument
print(hello("Sally"))

# No argument
print(hello())

# int arg works too
print(hello(110))

# float arg
print(hello(3.1))


def add(lhs: float = 0.0, rhs: Union[str, float] = 0.0) -> float:
    result: float = lhs
    if isinstance(rhs, str):
        result += float(rhs)
    else:
        result += rhs
    return result


print(add(110.0, "100.0"))