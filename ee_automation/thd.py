import math

def thd(values: list[float]) -> tuple[float, list[float]]:
    """Calculates the total harmonic distortion

    Args:
        values (list[float]): A list containing the amplitude values of harmonics in dBV starting from f_0 to f_n

    Returns:
        tuple[float, list[float]]: A tuple with the first element returning the total harmonic distortion as a percentage, and the second value returning a list containing the v_rms values of each harmonic in volts
    """

    for i in range(len(values)):
        values[i] = 10**(values[i] / 20)
        
    sum = 0
    for i in range(1, len(values)):
        sum += values[i]**2

    numerator = math.sqrt(sum)
    thd = (numerator / values[0]) * 1000

    return thd, values


# values = []
# i = 0
# userInput = ''
# print("Enter amplitude values of harmonics in dBV starting from f_0 (Enter anything except a number to calculate):")
# while (userInput != "x"):
#     try:
#         userInput = float(input(f"f{i}: "))
#         values.append(userInput)
#         i += 1
#     except ValueError:
#         break
    
# for i in range(len(values)):
#     values[i] = 10**(values[i] / 20)
     
# sum = 0
# for i in range(1, len(values)):
#     sum += values[i]**2

# numerator = math.sqrt(sum)
# thd = (numerator / values[0]) * 1000

# print(f"\nVoltages in V_rms:")
# for i in range(len(values)):
#     print(f"v{i}_rms: {values[i]} V")

# print("\nTotal Harmonic Distortion:")
# print(f"{thd}%")

if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    thd, values = thd(list)
    print(values)
    print(f"thd: {thd}%")