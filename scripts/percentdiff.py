
print("Percentage Difference Calculator")
print("Difference between a and b:\n")
a = float(eval(input("a: ")))
b = float(eval(input("b: ")))

diff = (abs(a - b) / ((a + b)/2)) * 100
print(f"\n{diff}%")
