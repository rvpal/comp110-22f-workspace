"""A document introducing functions."""

# Building blocks for progress.
# Process abstraction. 
# Task decomposition. 

# Calls, or invocations, are expressions that return a specific type. 
# Definitions are subprograms that define what actually happens, specifying what happens when a function is called. 
# Definitions are built in, imported, or created. 

# Example
# from random import randint
# for i in "string":
#    print(randint(1, 6))

# Function Call Syntax
# 1. Name
# 2. Paranthesis
# 3. Argument list inside parenthesis. Arguments are expressions. 
# --> function(arg1, arg2)
# Example
# max(10 + 1, 10)
# 4. Returns a specific type of data/value. 

# Definition
def my_max(a: int, b: int) -> int:
    """Returns largest argument."""
    if a >= b:
        return a
    else:
        return b