
print("Expand a function in the form (ax+b)^2 to ax^2 + bx + c\n")

again = True

while (again == True):
    a = float(eval(input("a: ")))
    b = float(eval(input("b: ")))

    a_out = a**2
    b_out = 2*a*b
    c_out = b**2

    print(f"{a_out}x^2 + {b_out}x + {c_out}")

    usr_input = input("Another expression? (y/n): ")
    if (usr_input == "y"):
        again = True
    else:
        again = False