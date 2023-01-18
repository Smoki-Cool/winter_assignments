'''
Input a number and check if the number is a prime or composite number.
'''

n = input('\nEnter Number: ')
if n.isnumeric():
    n = int(n)
    
    factors = []
    
    # for i in range(1, n+1):
    #     if n%i == 0:
    #         factors.append(i)
    
    i = 1
    while i * i <= n:
        if n%i == 0:
            factors.append(i) ; factors.append(round(n/i))
        i += 1
    
    factors.sort()
    
    if len(factors) == 2:
        print(f'\n{n} is a Prime Number.\n')
    else:
        print(f'\n{n} is a Composite Number.\nFactors: {factors}\n')
    
else:
    print(f"\nERROR: '{n}' is not a valid Number.\n")
