'''
Input a list of numbers and swap elements at the even location with the elements at the odd location.
'''

inp: list = eval(input("\nEnter your list of numbers: "))
if type(inp) == list:
    cond = True
    
    for i in inp:
        if type(i) == int or type(i) == float:
            pass
        else:
            print(f'\nERROR: All elements of the list must be a number, index {inp.index(i)}, "{i}"\n')
            cond = False
            break
    
    if cond:
        for i in range(0, len(inp), 2):
            inp.insert(i + 1, inp.pop(i))
            
        print(inp)
        
else:
    print("\nERROR: Please enter a list only.\n")
