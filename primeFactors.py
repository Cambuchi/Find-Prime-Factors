#!/usr/bin/env python3
# primeFactors.py - find all Prime Factors (if there are any) and display them from user input.

def primeFactors(num):
    global factors
    factors = []
    d = 2
    while num > 1:
        while num % d == 0:
            factors.append(d)
            num /= d
        d = d + 1
        if d * d > num:
            if num > 1:
                factors.append(num)
                break
    return factors


if __name__ == '__main__':
    try:
        n = int(input('Please enter a positive number: \n'))
        if n < 0:
            print('That was not a positive number.')
    except ValueError:
        print('That was not an integer.')
    primeFactors(n)
    print(factors)
