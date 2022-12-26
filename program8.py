'''
Compute the greatest common divisor and least common multiple of two integers.
'''

import math


int1 = input("\nEnter 1st integer: ")
if int1.replace('-', '').replace('+', '').isnumeric():
    int1 = int(int1)
    
    int2 = input("Enter 2nd integer: ")
    if int2.replace('-', '').replace('+', '').isnumeric():
        int2 = int(int2)
        
        a = max([math.fabs(int1), math.fabs(int2)])
        b = min([math.fabs(int1), math.fabs(int2)])
        
        _b = b
        r = a%b
        
        while r > 0:
            _a = _b
            _b = r
            r = _a%_b
        
        gcd = math.trunc(_b)
        print(f'\nGreatest Common Divisor = {gcd}')
        
        lcm = math.trunc(a*b/gcd)
        print(f'Least Common Multiple   = {lcm}\n')
        
    else:
        print(f"\nERROR: '{int2}' is not a valid integer.\n")
    
else:
    print(f"\nERROR: '{int1}' is not a valid integer.\n")
