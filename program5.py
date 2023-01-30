'''
Determine whether a number is a perfect number, an armstrong number or a palindrome.
'''

n = input('\nEnter a whole number: ')
# Checking if input is a number (for custom error msg without using try except)
# Only .isnumeric() is used to check if the `str` is a whole number
if n.isnumeric():
    # Convert to int if it passes the check
    n = int(n)
    
    # Perfect number
    # Sum is by-default taken as 1, since 1 is a factor of every number
    # and to prevent adding the number itself to sum due to n/i
    sum = 1
    # Finding the factors and adding them to the variable
    # This method is more efficient as 2 factors are processed at once, i and n/i
    # also, requires lesser loops
    i = 2
    while i * i <= n:
        if n%i == 0:
            sum += i + n/i
        i += 1
    
    # If sum of factors(excluding itself) is equal to the number, it's a perfect number
    if sum == n and n!=1:
        print(f'\n{n} is a Perfect Number.\n')
    
    else:
        # Armstrong number
        # Number of digits in n is stored in p
        p = len(str(n))
        sum = 0
        # str(n) is used to iterate through the digits as type `int` is not iterable
        for i in str(n):
            sum += int(i)**p
        
        # If sum of the digits each raised to the power number of digits is equal to the number, it's a armstrong number
        if sum == n:
            print(f'\n{n} is an Armstrong Number.\n')
        
        else:
            # Palindrome
            # Reverse of the number is stored in rev var by converting it to `str` and performing a slice with -1 step
            rev = str(n)[::-1]
            # If reverse of the number is equal to the number, it's a palindrome
            if int(rev) == n:
                print(f'\n{n} is a Palindrome.\n')
# ERROR message
else:
    print(f"\nERROR: '{n}' is not a valid argument.\n")
