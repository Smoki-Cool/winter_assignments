'''
Display the terms of a Fibonacci series.
'''

n = input('\nEnter no. terms to display: ')
# Checking if input is a number (for custom error msg without using try except)
# Only .isnumeric() is used to check if the `str` is a whole number
if n.isnumeric():
    # Convert to int if it passes the check
    n = int(n)
    # List with first 2 terms to append the next terms
    terms = ['0', '1']
    # Initial sum is taken as 1 as 0 and 1 are the initial terms
    sum = 1
    
    for i in range(1, n-1):
        # Not sure how to explain this part but it's pretty obvious ig
        a = int(terms[i-1])
        b = int(terms[i])
        next = a + b
        
        terms.append(str(next))
        sum += next
    
    print('')
    print(f'Fabonacci series: {", ".join(terms)}')
    print(f'Sum of the series: {sum}\n')
# ERROR message
else:
    print(f"\nERROR: '{n}' is not a valid Number.\n")
