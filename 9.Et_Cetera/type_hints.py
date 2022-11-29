# Type Hints
# use mypy 
    
def meow(n: int) -> str:
    """Meows n times

    Args:
        n (int): The number of times you want to meow.

    Returns:
        str: A string value that 'Meow' N times
    """
    return "meow\n" * n



number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")


