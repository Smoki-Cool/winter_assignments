'''
Input a list of numbers and find the smallest and largest number from the list.
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
    # First element is assumed as the Largest and Smallest for comparing
    largest = inp[0]
    smallest = inp[0]
    # Proceed only if condition var is True
    if cond:
        # Logical method of finding largest and smallest instead of using max() and min() functions
        for i in inp[1:]:
            if i > largest:
                largest = i
            elif i < smallest:
                smallest = i
            
        print(f'\nLargest Number: {largest}\nSmallest Number: {smallest}\n')
# ERROR message
else:
    print("\nERROR: Please enter a list only.\n")
