'''
Find the largest/smallest number in a list/tuple.
'''

inp = eval(input("\nEnter your list/tuple: "))
if type(inp) == list or type(inp) == tuple:
    print(f'\nLargest: {max(inp)}\nSmallest: {min(inp)}\n')

else:
    print("\nERROR: Please enter a list/tuple only.\n")
    