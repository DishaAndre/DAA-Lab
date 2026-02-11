def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    a = x // (10 ** m)
    b = x % (10 ** m)
    c = y // (10 ** m)
    d = y % (10 ** m)

    z0 = karatsuba(b, d)
    z2 = karatsuba(a, c)
    z1 = karatsuba(a + b, c + d) - z2 - z0

    return (z2 * (10 ** (2 * m))) + (z1 * (10 ** m)) + z0


while True:
    x_in = input("Enter 1st transaction amount (minimum 15 digits): ")
    y_in = input("Enter 2nd transaction amount (minimum 15 digits): ")

    if (len(x_in) >= 15 and len(y_in) >= 15):

        x = int(x_in)
        y = int(y_in)

        result = karatsuba(x, y)
        print("High-Precision multiplication:", result)
        break

    else:
        print("Enter minimum 15 digit numbers.\n")
