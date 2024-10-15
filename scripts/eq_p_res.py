
print("Find the equivalent resistance of resistors in parallel")
print("Enter values of resistors or press Enter to calculate\n")

resistor = 0
values = []
while True:
    user_input = input(f"r{resistor} (in \u03A9): ")

    if user_input == "":
        break
        
    try:
        value = float(eval(user_input))
        values.append(value)
        resistor += 1

    except (SyntaxError, NameError, ValueError):
        print("Invalid input")

denominator = 0
for value in values:
    denominator += 1/value
try:
    eq_resistance = 1/denominator
    print(f"\nEquivalent Resistance: {eq_resistance} \u03A9")

except (ZeroDivisionError):
    print("No valid input")
