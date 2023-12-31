# Prompt the user to input coefficients a, b, and c
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Print the full equation
if a != 0 and b !=0 and c !=0:
    print(f"Equation: {a}x^2 + {b}x + {c} = 0")
if a != 0 and b !=0 and c==0 :
    print(f"Equation: {a}x^2 + {b}x= 0")
if a != 0 and  b== 0 and c !=0:
    print(f"Equation: {a}x^2 + {c} = 0")

if a != 0 and b== 0 and c== 0:
    print(f"Equation: {a}x^2 = 0")


if a == 0:
    # Handle the case of a linear equation
    if b == 0:
        if c == 0:
            print("Infinite solutions (any x is a solution)")
        else:
            print("No solutions (contradiction)")
    else:
        solution = -c / b
        print("Linear equation solution:", solution)
else:
    # Calculate the discriminant for the quadratic equation
    discriminant = b**2 - 4*a*c

    # Check the three cases for the quadratic equation
    if discriminant == 0:
        # One real solution
        solution = -b / (2*a)
        print("1:", solution)

    elif discriminant > 0:
        # Two real solutions
        sqrt_discriminant = discriminant ** 0.5
        solution1 = (-b + sqrt_discriminant) / (2*a)
        solution2 = (-b - sqrt_discriminant) / (2*a)
        print("1:", solution1, "2:", solution2)

    else:
        # No real solutions
        print("No real solutions for these coefficients.")
