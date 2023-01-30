'''
Create a dictionary with the roll number, name and marks of n students in a class and display the names of students
who have scored marks above 75.
'''

n = input('\nEnter number of students: ')
# Checking if input is a number (for custom error msg without using try except)
# Only .isnumeric() is used to check if the `str` is a whole number
if n.isnumeric():
    # Convert to int if it passes the check
    n = int(n)
    
    record = {}
    roll = 1
    # while loop is used so that a roll number can be redone again instead of starting over in case user
    # makes mistake while entering mark and enters a non-numeric number
    while roll <= n:
        name = input(f'\nEnter name of roll no. {roll}: ')
        mark = input(f"Enter {name}'s mark: ")
        # Checking if entered mark is a number or not
        if mark.isnumeric():
            mark = int(mark)
            record[roll] = [name, mark]
            
            roll += 1
        # ERROR message for non-numeric number
        else:
            print(f"\nERROR: '{mark}' is not a valid mark.")
        
    print(f'\nCreated dictionary is: {record}')
    print('\nNames of Students scoring marks above 75:')
    # Printing the names and marks of students scoring over 75
    for roll, [name, mark] in record.items():
        if mark >= 75:
            print(f'{name} - {mark}')
    
    print()
# ERROR message
else:
    print(f"\nERROR: '{n}' is not a valid number of students.\n")
