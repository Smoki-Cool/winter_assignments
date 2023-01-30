'''
Input a number and check if the number is a prime or composite number.
'''

n = input('\nEnter a whole number: ')
# Checking if input is a number (for custom error msg without using try except)
# Only .isnumeric() is used to check if the `str` is a whole number
if n.isnumeric():
    # Convert to int if it passes the check
    n = int(n)
    # Empty list to append the factors
    factors = []
    
    # Simple method of finding factors
    ''' for i in range(1, n+1):
            if n%i == 0:
                factors.append(i) '''
    
    # Finding the factors and appending them to the factors list
    # This method is more efficient as 2 factors are processed at once, i and n/i
    # also, requires lesser loops
    i = 1
    while i * i <= n:
        if n%i == 0:
            factors.append(i) ; factors.append(round(n/i))
        i += 1
    
    # Sorting the factors in ascending order
    factors.sort()
    
    if len(factors) == 2:
        # If the number has only 2 factors, 1 and the number itself, it's a prime number
        print(f'\n{n} is a Prime Number.\n')
    else:
        # Else it's a composite number
        # Factors are printed as a bonus ;)
        print(f'\n{n} is a Composite Number.\nFactors: {factors}\n')
# ERROR message
else:
    print(f"\nERROR: '{n}' is not a valid Number.\n")
