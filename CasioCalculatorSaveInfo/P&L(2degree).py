print("Linear and Parabola")
print('Formula options:')
print("P1: y=ax^2+bx+c")
print("P2: y=a(x-b)^2+c")
print("P3: y=a(x-b)(x-c)+d")

def fix_number_zero(num):
    if num == 0:
        return 0.000
    else:
        return num

def calculate_intersection(formulaP, a, b, c, k, d):
    if formulaP == 1:
        bN = b - k
        cN = c - d
        discriminant = bN*bN - 4 * a * cN
        if discriminant < 0:
            print("No intersection point (discriminant < 0)")
            return
        elif discriminant == 0:
            x = -bN / (2 * a)
            y = a * x*x + b * x + c
            x = fix_number_zero(x)
            y = fix_number_zero(y)
            print("({0:.3f},{1:.3f})".format(x, y))
            return
        else:
            sqrt_d = discriminant ** 0.5
            x1 = (-bN + sqrt_d) / (2 * a)
            y1 = a * x1*x1 + b * x1 + c
            x1 = fix_number_zero(x1)
            y1 = fix_number_zero(y1)
            print("({0:.3f},{1:.3f})".format(x1, y1))
            
            x2 = (-bN - sqrt_d) / (2 * a)
            y2 = a * x2*x2 + b * x2 + c
            x2 = fix_number_zero(x2)
            y2 = fix_number_zero(y2)
            print("({0:.3f},{1:.3f})".format(x2, y2))

    elif formulaP == 2:
        bN = -2 * a * b - k
        cN = a * b*b + c - d
        discriminant = bN*bN - 4 * a * cN
        if discriminant < 0:
            print("No intersection point (discriminant < 0)")
            return
        elif discriminant == 0:
            x = -bN / (2 * a)
            y = a * (x - b)*(x - b) + c
            x = fix_number_zero(x)
            y = fix_number_zero(y)
            print("({0:.3f},{1:.3f})".format(x, y))
            return
        else:
            sqrt_d = discriminant ** 0.5
            x1 = (-bN + sqrt_d) / (2 * a)
            y1 = a * (x1 - b)*(x1 - b) + c
            x1 = fix_number_zero(x1)
            y1 = fix_number_zero(y1)
            print("({0:.3f},{1:.3f})".format(x1, y1))
            
            x2 = (-bN - sqrt_d) / (2 * a)
            y2 = a * (x2 - b)*(x2 - b) + c
            x2 = fix_number_zero(x2)
            y2 = fix_number_zero(y2)
            print("({0:.3f},{1:.3f})".format(x2, y2))
    elif formulaP == 3:
        A = a
        B = -a * (b + c) - k
        e = float(input('Enter e in "y=a(x-b)(x-c)+e": '))
        C = a * b * c + e - d
        discriminant = B * B - 4 * A * C

        if discriminant < 0:
            print("No intersection point (discriminant < 0)")
            return
        elif discriminant == 0:
            x = -B / (2 * A)
            y = A * (x - b) * (x - c) + e
            x = fix_number_zero(x)
            y = fix_number_zero(y)
            print("({0:.3f},{1:.3f})".format(x, y))
            return
        else:
            sqrt_d = discriminant ** 0.5
            x1 = (-B + sqrt_d) / (2 * A)
            y1 = A * (x1 - b) * (x1 - c) + e
            x1 = fix_number_zero(x1)
            y1 = fix_number_zero(y1)
            print("({0:.3f},{1:.3f})".format(x1, y1))

            x2 = (-B - sqrt_d) / (2 * A)
            y2 = A * (x2 - b) * (x2 - c) + e
            x2 = fix_number_zero(x2)
            y2 = fix_number_zero(y2)
            print("({0:.3f},{1:.3f})".format(x2, y2))
    else:
        print("Invalid formula! Enter 1/2/3 only")
        return

def r():
    try:
        formulaP = int(input("Enter formula \ntype (1/2/3): "))
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        k = float(input("Enter k: "))
        d = float(input("Enter d: "))
        calculate_intersection(formulaP, a, b, c, k, d)
    except ValueError:
        print("Error: Enter valid number only")
    except ZeroDivisionError:
        print("Error: a cannot be 0 (not a parabola)")

r()