def karatsuba(x, y):
    # Base case: if numbers are small, multiply directly
    if x < 10 or y < 10:
        return x * y

    # Calculate the number of digits
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split the numbers
    a, b = divmod(x, 10**m)
    c, d = divmod(y, 10**m)

    # Recursive calls
    z0 = karatsuba(b, d)
    z1 = karatsuba(b + a, d + c)
    z2 = karatsuba(a, c)

    # Combine the results
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0


# Take input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = karatsuba(num1, num2)
print("Product:", result)
