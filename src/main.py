from termcolor import colored

# Converts string into polynomial
def toPolynomial(line):
    terms = line.split(' + ')
    polynomial = {}
    for term in terms:
        # normal
        if "x^" in term:
            coefficient, power = term.split("x^")
        # x = x^1
        elif "x" in term:
            coefficient, power = term.split("x")
            power = "1"
        # 1 = x^0
        else:
            coefficient, power = int(term), "0"
        # x^2 = 1x^2
        if coefficient == "":
            coefficient = "1"
        polynomial[int(power)] = int(coefficient)
    return polynomial

# Adds two polynomials together
def add(poly1, poly2):
    result = {}
    for power in set(poly1.keys()) | set(poly2.keys()):
        result[power] = poly1.get(power, 0) + poly2.get(power, 0)
    return result

# Converts polynomial into string
def toString(polynomial):
    terms = []
    for power in sorted(polynomial.keys(), reverse=True):
        coefficient = polynomial[power]
        # 2x^0 = 2
        if power == 0:
            terms.append(str(coefficient))
        elif coefficient == 1:
            # 1x^1 = x
            if power == 1:
                terms.append(f"x")
            # 1x^2 = x^2
            else:
                terms.append(f"x^{power}")
        else:
            # 2x^1 = 2x
            if power == 1:
                terms.append(f"{coefficient}x")
            # normal
            else:
                terms.append(f"{coefficient}x^{power}")
    return ' + '.join(terms)

# Calculate the polynomial value
def Calculation(poly, x):
    val = 0
    for power in set(poly.keys()):
        val += poly[power] * (x ** power)
    return val

# Main function
def main():
    # Welcome
    print(colored("===> Hello, Welcome To This Program <=== \n", "blue", attrs=["dark"]))

    # Get Polynomials From User
    line1 = input("enter first polynomial: ").strip()
    line2 = input("enter secend polynomial: ").strip()

    poly1 = toPolynomial(line1)
    poly2 = toPolynomial(line2)
    
    while line1 != "0":
        answer = add(poly1, poly2)
        print(colored("\nAnswer Is: ", "green" , attrs=["dark"]), toString(answer))

        # Get Value Of x From User
        x = int(input("\nx = "))
        val = Calculation(answer, x)
        print(colored(f"\nValue Of Polynomial For x = {x} Is {val}", "magenta" , attrs= ["dark"]))

        # Get Polynomials From User
        line1 = input("\nEnter First Polynomial (Enter 0 If You Want To End This!) : ").strip()
        if line1 != "0":
            line2 = input("Enter Secend Polynomial : ").strip()
        else:
            # Developers
            print(colored("\nThank You For Choosing Us :)\n>>>Developed By Maryam Fakhraei & Amirhossein Naseri<<<", "cyan"))

if __name__ == "__main__":
    main()

# example: 
# poly1 = x^3 + 4x^2 + 36 + x + 6x^1000
# poly2 = 1x^3 + 5x^100000 + 0x^2 + 2x^1 + 3x^0