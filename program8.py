'''
Compute the greatest common divisor and least common multiple of two integers.
'''

def fabs(num: int): return num*-1 if num < 0 else num
        

int1 = input("\nEnter 1st integer: ")
# Checking if input is a number (for custom error msg without using try except)
# '-' and '+' are removed before checking to allow signs
# .isnumeric() is used to check if the `str` is a number
if int1.replace('-', '').replace('+', '').isnumeric():
    # Convert to int if it passes the check
    int1 = int(int1)
    
    int2 = input("Enter 2nd integer: ")
    if int2.replace('-', '').replace('+', '').isnumeric():
        int2 = int(int2)
        # <a> should be the greater integer and <b> smaller, hence max and min are used
        # fabs() is used to get the absolute values(positive)
        a = max([fabs(int1), fabs(int2)])
        b = min([fabs(int1), fabs(int2)])
        # <b> will be needed later for lcm, so it is acessed through <_b> to avoid modification
        _b = b
        # Simulating Euclid's Division Lemma
        r = a%_b
        while r > 0:
            _a = _b
            _b = r
            r = _a%_b
        
        gcd = int(_b)
        print(f'\nGreatest Common Divisor = {gcd}')
        
        lcm = int(a*b/gcd)
        print(f'Least Common Multiple   = {lcm}\n')
# ERROR messages
    else:
        print(f"\nERROR: '{int2}' is not a valid integer.\n")
else:
    print(f"\nERROR: '{int1}' is not a valid integer.\n")
