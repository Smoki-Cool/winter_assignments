'''
Write a program to input the value of x and n and print the sum of the following series:
$   1 + x + x² + x³ + x⁴ + .... + xⁿ
$   1 - x + x² - x³ + x⁴ + .... xⁿ
$   x - x²/2 + x³/3 - x⁴/4 + .... xⁿ/n
$   x + x²/2! - x³/3! + x⁴/4! - x⁵/5! + .... + xⁿ/n!
'''

x = input("\nEnter value of 'x': ")
if x.replace('.', '').replace('-', '').replace('+', '').isnumeric():
    x = float(x) if '.' in x else int(x)
    
    n = input("Enter value of 'n' (where, n > 0): ")
    if n.replace('.', '').replace('-', '').replace('+', '').isnumeric():
        n = float(n) if '.' in n else int(n)
        
        if n > 0:
            n = int(n)
            
            seq1 = 0
            seq2 = 0
            seq3 = 0
            seq4 = x
            
            
            for i in range(n+1):
                seq1 += x**i
            
                if i%2 == 0:
                    seq2 += x**i
                else:
                    seq2 -= x**i
            
            
            for i in range(1, n+1):
                if i%2 == 0:
                    seq3 -= (x**i)/i
                else:
                    seq3 += (x**i)/i
            
            
            for i in range(2, n+1):
                factorial = 1
                
                for j in range(1, i+1):
                    factorial *= j
                
                if i%2 == 0:
                    seq4 += (x**i)/factorial
                else:
                    seq4 -= (x**i)/factorial
            
            print(seq1, seq2, seq3, seq4)
        
        else:
            print(f"\nERROR: 'n' must be greater than 0.\n")
        
    else:
        print(f"\nERROR: '{n}' is not a valid Number.\n")
    
else:
    print(f"\nERROR: '{x}' is not a valid Number.\n")
