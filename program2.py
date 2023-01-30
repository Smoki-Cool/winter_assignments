'''
Input three numbers and display the largest/smallest number.
'''

num1 = input("\nEnter Number#1: ")
# Checking if input is a number (for custom error msg without using try except)
# '.', '-' and '+' are removed before checking to allow floats and signs
# .isnumeric() is used to check if the `str` is a number
if num1.replace('.', '').replace('-', '').replace('+', '').isnumeric():
    # If input has '.' in it, it is converted to `float` or else to `int`
    num1 = float(num1) if '.' in num1 else int(num1)

    num2 = input("Enter Number#2: ")
    if num2.replace('.', '').replace('-', '').replace('+', '').isnumeric():
        num2 = float(num2) if '.' in num2 else int(num2)

        num3 = input("Enter Number#3: ")
        if num3.replace('.', '').replace('-', '').replace('+', '').isnumeric():
            num3 = float(num3) if '.' in num3 else int(num3)
        
            if num1 == num2 == num3:
                print(f'\nAll the numbers are equal.\n')
            else:
                # Largest and smallest are determined by creating a list inside max() and min() functions
                print(f'\nLargest: {max([num1, num2, num3])}\nSmallest: {min([num1, num2, num3])}\n')
# ERROR messages
        else:
            print(f"\nERROR: '{num3}' is not a valid Number.\n")
    else:
        print(f"\nERROR: '{num2}' is not a valid Number.\n")
else:
    print(f"\nERROR: '{num1}' is not a valid Number.\n")
