'''
Write a program to input the value of x and n and print the sum of the following series:
$   1 + x + x² + x³ + x⁴ + .... xⁿ
$   1 - x + x² - x³ + x⁴ - .... xⁿ
$   x - x²/2 + x³/3 - x⁴/4 + .... xⁿ/n
$   x + x²/2! - x³/3! + x⁴/4! - .... xⁿ/n!
'''

x = input("\nEnter value of 'x': ")
# Checking if input is a number (for custom error msg without using try except)
# '.', '-' and '+' are removed before checking to allow floats and signs
# .isnumeric() is used to check if the `str` is a number
if x.replace('.', '').replace('-', '').replace('+', '').isnumeric():
    # If input has '.' in it, it is converted to `float` or else to `int`
    x = float(x) if '.' in x else int(x)
    
    n = input("Enter value of 'n' (where, n > 0): ")
    if n.replace('.', '').replace('-', '').replace('+', '').isnumeric():
        # Proceed only if the number is an integer and not a float
        if '.' not in n:
            n = int(n)
        
            # Proceed only if n is greater than 0
            if n > 0:
                
                seq1 = 0
                seq2 = 0
                # seq 3 and 4 are started with x due to the behaviour of the series
                seq3 = x
                seq4 = x
                
                
                for i in range(n+1):
                    # Sequence 1
                    seq1 += x**i
                
                    # Sequence 2
                    if i%2 == 0:
                        # Add if i is even
                        seq2 += x**i
                    else:
                        # Subtract if i is odd
                        seq2 -= x**i
                
                
                for i in range(2, n+1):
                    # Sequence 3
                    if i%2 == 0:
                        # Subtract if i is even
                        seq3 -= (x**i)/i
                    else:
                        # Add if i is odd
                        seq3 += (x**i)/i
                
                    # Sequence 4
                    # Finding factorial for each i term
                    factorial = 1
                    for j in range(1, i+1):
                        factorial *= j
                    
                    if i%2 == 0:
                        # Add if i is even
                        seq4 += (x**i)/factorial
                    else:
                        # Subtract if i is odd
                        seq4 -= (x**i)/factorial
                
                
                print(f'''
1 + x + x² + x³ + x⁴ + .... xⁿ          = {seq1}
1 - x + x² - x³ + x⁴ - .... xⁿ          = {seq2}
x - x²/2 + x³/3 - x⁴/4 + .... xⁿ/ⁿ     = {seq3}
x + x²/2! - x³/3! + x⁴/4! - .... xⁿ/ⁿ! = {seq4}
''')
# ERROR messages
            else:
                print(f"\nERROR: 'n' must be greater than 0.\n")
        else:
            print(f"\nERROR: '{n}' must be an integer, not float.\n")
    else:
        print(f"\nERROR: '{n}' is not a valid Number.\n")
else:
    print(f"\nERROR: '{x}' is not a valid Number.\n")
