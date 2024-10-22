def equiv_res(values: list[float]) -> float:
    """Calculate the equivalent parallel resistance.

    Args:
        values (list[float]): A list containing the resistor values in ohms (\u03A9)

    Returns:
        float: The equivalent resistance of the resistors in parallel
    """
    try:
        denominator = 0
        for value in values:
            denominator += 1 / value
        eq_resistance = 1 / denominator
        return eq_resistance

    except ZeroDivisionError:
        print("No valid input")


if __name__ == "__main__":
    # value = usr_input()
    # print(f"\nEquivalent Resistance: {value} \u03A9")
    pass
