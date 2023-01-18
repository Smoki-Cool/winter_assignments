'''
Find the largest/smallest number in a list/tuple.
'''

inp = eval(input("\nEnter your list/tuple: "))
if type(inp) == list or type(inp) == tuple:
    cond = True
    
    for i in inp:
        if type(i) == int or type(i) == float:
            pass
        else:
            print(f'\nERROR: All elements of the list must be a number, index {inp.index(i)}, "{i}"\n')
            cond = False
            break
    
    largest = inp[0]
    smallest = inp[0]
    
    if cond:
        for i in inp[1:]:
            if i > largest:
                largest = i
            elif i < smallest:
                smallest = i
            
        print(f'\nLargest Number: {largest}\nSmallest Number: {smallest}\n')

else:
    print("\nERROR: Please enter a list/tuple only.\n")
    