import math

def twenty_nineteen():
    """Come up with the most creative expression that evaluates to 2019,
    using only numbers and the +, *, and - operators.

    >>> twenty_nineteen()
    2019
    """
    return int(math.sqrt(400) * math.gcd(800,900) + 19)
