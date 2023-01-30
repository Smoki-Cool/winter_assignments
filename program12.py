'''
Input a list of numbers and swap elements at the even location with the elements at the odd location.
'''

inp: list = eval(input("\nEnter your list of numbers: "))
# Type checking if the input is a list or not
if type(inp) == list:
    # A condition var is created which will be checked later before proceeding
    cond = True
    # Checking if all the elements in the list/tuple is a number or not
    for i in inp:
        if type(i) == int or type(i) == float:
            pass
        else:
            # Error message with the index and element is printed incase there's a non-number element
            print(f'\nERROR: All elements of the list must be a number, index {inp.index(i)}, "{i}"\n')
            # Condition var is changed to False if error is found
            cond = False
            break
    # Proceed only if condition var is True
    if cond:
        # Step 2 is used in `range()` as only even location are swapped with odd
        # which automatically makes the odd location move to even
        for i in range(0, len(inp), 2):
            inp.insert(i + 1, inp.pop(i))
            
        print(inp)
# ERROR message
else:
    print("\nERROR: Please enter a list only.\n")
