'''
Display the terms of a Fibonacci series.
'''

n = input('\nEnter no. terms to display: ')
if n.isnumeric():
    n = int(n)
    
    terms = ['0', '1']
    sum = 1
    
    for i in range(1, n-1):
        a = int(terms[i-1])
        b = int(terms[i])
        next = a + b
        
        terms.append(str(next))
        sum += next
    
    print('')
    print(f'Fabonacci series:', ', '.join(terms))
    print(f'Sum of the series = {sum}\n')
    
else:
    print(f"\nERROR: '{n}' is not a valid Number.\n")
