"""
prints out numbers 1-100, but multiples of 3 are "Fizz," multiples of 5 are "Buzz," and multiples of both 3 and
5 are "FizzBuzz"
"""
for num in range(100):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
