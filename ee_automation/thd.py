import math


def thd(values: list[float]) -> tuple[float, list[float]]:
    """Calculates the total harmonic distortion

    Args:
        values (list[float]): A list containing the amplitude values of harmonics in dBV starting from f_0 to f_n

    Returns:
        tuple[float, list[float]]: A tuple with the first element returning the total harmonic distortion as a percentage, and the second value returning a list containing the v_rms values of each harmonic in volts
    """

    # Converts each harmonic to a V_rms value
    values = [10 ** (value / 20) for value in values]

    sum = 0
    for i in range(1, len(values)):
        sum += values[i] ** 2

    numerator = math.sqrt(sum)

    thd = (numerator / values[0]) * 100

    return thd, values


if __name__ == "__main__":
    list = [5, 4, 3, 2, 1]
    thd, values = thd(list)
    print(values)
    print(f"thd: {thd}%")
