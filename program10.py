'''
Input a string and determine whether it is a palindrome or not; convert the case of characters in a string.
'''

inp = input("\nEnter your string: ")

refined_inp = ''

for char in inp:
    if char.isalpha():
        refined_inp += char.lower()

if refined_inp == refined_inp[::-1]:
    print("\nIt is a palindrome.")
else:
    print("\nIt is not a palindrome.")


case_swap = ''

for char in inp:
    if char.isupper():
        case_swap += char.lower()
    elif char.islower():
        case_swap += char.upper()
    else:
        case_swap += char

print(f'Case Swap: `{case_swap}`\n')
