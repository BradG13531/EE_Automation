def expand(a: float, b: float) -> str:
    """Expands a function in the form (ax+b)^2 to ax^2 + bx + c

    Args:
        a (float): Coefficient of variable
        b (float): Constant

    Returns:
        str: The expanded form of the perfect square expression
    """
    a_out = a**2
    b_out = 2 * a * b
    c_out = b**2
    return f"{a_out}x^2 + {b_out}x + {c_out}"
