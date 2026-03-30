def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def divide(a, b):
    """Returns the division of two numbers. Raises ValueError if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b