'''
Determine whether a number is a perfect number, an armstrong number or a palindrome.
'''

n = input('\nEnter a whole number: ')
if n.isnumeric():
    n = int(n)
    
    sum = 1

    i = 2
    while i * i <= n:
        if n%i == 0:
            sum = sum + i + n/i
        i += 1
    
    
    if sum == n and n!=1:
        print(f'\n{n} is a Perfect Number.\n')
    
    else:
        p = len(str(n))
        sum = 0
        
        for i in str(n):
            sum += int(i)**p
        
        if sum == n:
            print(f'\n{n} is an Armstrong Number.\n')
        
        else:
            rev = str(n)[::-1]
            
            if int(rev) == n:
                print(f'\n{n} is a Palindrome.\n')
    
else:
    print(f"\nERROR: '{n}' is not a valid argument.\n")
