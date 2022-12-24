# Input two numbers and display the larger/smaller number.

num1 = input('\nEnter Number#1: ')
if num1.replace('.', '').replace('-', '').replace('+', '').isnumeric():
    num1 = float(num1) if '.' in num1 else int(num1)

    num2 = input('Enter Number#2: ')
    if num2.replace('.', '').replace('-', '').replace('+', '').isnumeric():
        num2 = float(num2) if '.' in num2 else int(num2)

        if num1 == num2:
            print(f'\nBoth numbers are equal.\n')
        else:
            print(f'\nLarger: {max([num1, num2])}\nSmaller: {min([num1, num2])}\n')

    else:
        print(f"\nERROR: '{num2}' is not a valid Number.\n")

else:
    print(f"\nERROR: '{num1}' is not a valid Number.\n")
