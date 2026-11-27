"""
Custom Decorator Demo

output_decorator wraps any function and prints, in a neat format:
  - the function's name
  - the inputs it was called with
  - the value it returned
The original function's code is not changed at all.
"""

from functools import wraps


def output_decorator(func):
    """A decorator that logs the inputs and the return value of a function."""

    @wraps(func)  # keeps the original name and docstring (func.__name__ etc.)
    def wrapper(*args, **kwargs):
    
        inputs = [str(value) for value in args]
        inputs += [f"{key}={value}" for key, value in kwargs.items()]

        print(f"Calling  : {func.__name__}({', '.join(inputs)})")

        result = func(*args, **kwargs)  # run the real function

        print(f"Returned : {result}")
        print("-" * 35)

        return result  

    return wrapper

@output_decorator
def add(a, b):
    """Add two numbers."""
    return a + b


@output_decorator
def multiply(a, b):
    """Multiply two numbers."""
    return a * b


@output_decorator
def greet(name, greeting="Hello"):
    """Make a greeting message."""
    return f"{greeting}, {name}!"


@output_decorator
def average(*numbers):
    """Find the average of any number of values."""
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    add(5, 3)
    multiply(4, 6)
    greet("Anushka")
    greet("Anushka", greeting="Good morning")
    average(10, 20, 30, 40)

    # The returned value still works normally
    total = add(100, 250)
    print(f"Total stored in a variable: {total}")

    # @wraps keeps the original function's identity
    print(f"Function name is still: {add.__name__}")
    print(f"Docstring is still    : {add.__doc__}")