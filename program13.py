'''
Input a list/tuple of elements, search for a given element in the list/tuple.
'''

def note():
    '''
    It is recommended to try running and using this code to get a better understanding of what it's doing ;)
    '''


inp: list | tuple = eval(input("\nEnter your list/tuple: "))
# Type checking if the input is a list/tuple or not
if type(inp) == list or type(inp) == tuple:
    ele = eval(input("\nEnter the element to search for: "))
    # Proceed for advanced search if the list/tuple consists the searched element
    if ele in inp:
        count = inp.count(ele)
        index = inp.index(ele)
        
        # Advanced locating of the searched element
        # A slice of atmost 5 elements(2 to the left and 2 to the right of the searched element) is taken out
        # and the searched element is marked with ^^^ with respect to its length accurately
        
        # Start index of the slice is figured out by subtracting 2 from the index and comparing with 0
        s = max(0, index - 2)
        # End index of the slice is figured out by adding 3 to the index and comparing with the len of the list/tuple
        e = min(len(inp), index + 3)
        list_slice = inp[s:e]
        # Additional spaces required for different object types are defined in a `dict`
        _space = {str: 2, int: 0, float: 0, list: 0, tuple: 0}
        # Benchmark space is 8
        space = 8
        # Calculating spaces required upto the searched element with respect to len and type of the preceeding elements
        for x in list_slice[:list_slice.index(ele)]:
            # The +2 at end is for the [] or () characters of the list/tuple
            space += len(str(x)) + _space[type(x)] + 2
        
        # + 1 is added if the searched element is a `str` for the single ' before it
        # Then finally ^ are printed with respect to the len of the searched element
        print(f'\nCount: {count}\
                \nIndex: {index}\
                \nSlice: {list_slice}\
                \n{" "*((space + 1) if type(ele) == str else space) + "^"*len(str(ele))}\n')
    # Element not found message
    else:
        print('\nThe searched element is not found.\n')
# ERROR message
else:
    print("\nERROR: Please enter a list/tuple only.\n")
