'''
The aim of the kata is to decompose n! (factorial n) into its prime factors.
Prime numbers should be in increasing order. When the exponent of a prime is 1 don't put the exponent.
    Notes
the function is decomp(n) and should return the decomposition of n! into its prime factors in increasing order of the primes, as a string.
factorial can be a very big number (4000! has 12674 digits, n can go from 300 to 4000).
In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.

n = 12; decomp(12) -> "2^10 * 3^5 * 5^2 * 7 * 11"
since 12! is divisible by 2 ten times, by 3 five times, by 5 two times and by 7 and 11 only once.

n = 22; decomp(22) -> "2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19"

n = 25; decomp(25) -> 2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23


'''
from math import sqrt


def resultToString(result):
    final = ""
    items = list(result.items())

    print(result)
    print(items)
    for i in range(len(items)):

        final = final + str(items[i][0])
        if items[i][1] != 1:
            final += "^" + str(items[i][1])
        if i < len(items) - 1:
            final += " * "

    return final


def saveExponent(result, act):
    if act not in result:
        result[act] = 1
    else:
        result[act] += 1
    return result


def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def factorial(n):
    product = n
    n -= 1
    while (n > 1):
        product = product * n
        n -= 1
    return product


def decomp(n):
    result = {}
    if n == 0 or n == 1:
        return 1
    if isPrime(n):
        result[n] = 1
        return result
    nFactorial = factorial(n)
    # First I start getting the factorial of n
    # I need to subtract from n
    while n > 1:
        # Check all posible factors that can be
        for act in range(2, int(sqrt(n) + 1)):
            # Check if it divisible by 2 < i < act
            if isPrime(act):
                while (n % act == 0):
                    # Save the exponent
                    result = saveExponent(result, act)
                    n = n / act
                if n == 1:
                    break
                # If n is prime

    return resultToString(result)


if __name__ == "__main__":
    print(decomp(5))
    print(decomp(24))
