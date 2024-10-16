from cmath import sqrt
a = b = c = 0

again = True

while (again):
    print("Quadratic equation solver")
    print("a*x^2 + b*x + c = 0\n")
    a = float(eval(input("Value of a: ")))
    b = float(eval(input("Value of b: ")))
    c = float(eval(input("Value of c: ")))

    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)

    print(f"x1 = {x1}")
    print(f"x2 = {x2}")

    usr_input = input("Another expression? (y/n): ").lower().strip()
    if (usr_input == "y"):
        again = True
    else:
        again = False
