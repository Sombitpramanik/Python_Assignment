def calculator(x, y):
    add = x + y
    sub = x - y
    mlt = x * y
    int_div = x // y  # Corrected the variable name
    f_div = x / y     # Floating-point division should use /
    mod_div = x % y   # Changed variable name to mod_div
    expo = x ** y     # Use ** for exponentiation

    return add, sub, mlt, int_div, f_div, mod_div, expo


if __name__ == '__main__':
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))  # Removed an extra int() call here
    addition, subtraction, multiplication, i_division, f_division, m_division, exponent = calculator(a, b)

    print(f"Addition of {a} & {b} is : {addition}")
    print(f"Subtraction of {a} & {b} is : {subtraction}")
    print(f"Multiplication of {a} & {b} is : {multiplication}")
    print(f"Integer division of {a} & {b} is : {i_division}")
    print(f"Floating Division of {a} & {b} is : {f_division}")
    print(f"Modulo Division of {a} & {b} is : {m_division}")
    print(f"Exponent of {a} ^ {b} is : {exponent}")
