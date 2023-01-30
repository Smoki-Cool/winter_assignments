'''
Input a string and determine whether it is a palindrome or not; convert the case of characters in a string.
'''

inp = input("\nEnter your string: ")
# Palindrome
# Removing any special characters or spaces from the string
refined_inp = ''
for char in inp:
    if char.isalpha():
        refined_inp += char.lower()
# Checking if the string is a palindrome
if refined_inp == refined_inp[::-1]:
    print("\nIt is a palindrome.")
else:
    print("\nIt is not a palindrome.")

# Case Convert
case_swap = ''
for char in inp:
    # Convert to lower if it's upper
    if char.isupper():
        case_swap += char.lower()
    # Convert to upper if it's lower
    elif char.islower():
        case_swap += char.upper()
    # Join as it is if it's a space or some special character
    else:
        case_swap += char

print(f'Case Swap: `{case_swap}`\n')
