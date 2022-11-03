import sys

##Error prone - Dumb way
"""for line in sys.stdin:
    a, b = 0, 1
    line = int(line)
    for i in range(line):
        a, b = b, a+b
    print(a)
"""

##Iterative approach - time complexity of: O(2^n)^2 - very slow
def fib_iter(number):
    number = int(number)
    a, b = 0, 1 
    if number <= 0:
        print("Please enter a positive integer.")
    elif number == 1:
        return number
    else:
        for i in range(number):
            a, b = b, a+b 
        return a 


##Recursive approach - time complexity of: O(n) - better.
"""def fib_recur(number):
    number = int(number)
    a, b = 0, 1
    if number <= 0:
        print("Please enter a positive integer.")
    elif number == 1:
        return number
    else:
        return(fib_recur(number - 1) + fib_recur(number - 2))
"""

##Main 
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    else:
        print(fib_iter(line))