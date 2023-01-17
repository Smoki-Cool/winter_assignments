'''
Input a list/tuple of elements, search for a given element in the list/tuple.
'''
  
inp: list | tuple = eval(input("\nEnter your list/tuple: "))
if type(inp) == list or type(inp) == tuple:
    ele = eval(input("\nEnter the element to search for: "))
    
    _type = type(inp)
    if _type == tuple:
        inp = list(inp)
    
    if ele in inp:
        count = inp.count(ele)
        index = inp.index(ele)
        
        s = max(0, index - 2)
        e = min(len(inp), index + 3)
        list_slice = inp[s:e]
        
        _space = {str: 2, int: 0}
        
        space = 8
        for x in list_slice[:list_slice.index(ele)]:
            space += len(str(x)) + _space[type(x)] + 2
        
        print(f'\nCount: {count}\
                \nIndex: {index}\
                \nSlice: {tuple(list_slice) if _type == tuple else list_slice}\
                \n{" "*((space + 1) if type(ele) == str else space) + "^"*len(str(ele))}\n')
        
    else:
        print('\nThe searched element is not found.\n')
    

else:
    print("\nERROR: Please enter a list/tuple only.\n")
