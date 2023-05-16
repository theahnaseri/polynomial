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

# Main function
def main():
    line1 = input("enter first polynomial: ").strip()
    line2 = input("enter secend polynomial: ").strip()

    poly1 = toPolynomial(line1)
    poly2 = toPolynomial(line2)
    
    print(poly1)
    print(poly2)

if __name__ == "__main__":
    main()

# example: 
# poly1 = x^3 + 4x^2 + 36 + x + 6x^1000
# poly2 = 1x^3 + 5x^100000 + 0x^2 + 2x^1 + 3x^0