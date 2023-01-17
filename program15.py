'''
Create a dictionary with the roll number, name and marks of n students in a class and display the names of students
who have scored marks above 75.
'''

NAME = 0
MARK = 1

n = input('\nEnter number of students: ')
if n.isnumeric():
    n = int(n)
    
    record = {}
    roll = 1
    while roll <= n:
        name = input(f'\nEnter name of roll no. {roll}: ')
        mark = input(f"Enter {name}'s mark: ")
        if mark.isnumeric():
            mark = int(mark)
            record[roll] = [name, mark]
            
            roll += 1
        
        else:
            print(f"\nERROR: '{mark}' is not a valid mark.")
        
    print(f'\nCreated dictionary is: {record}')
    print('\nNames of Students scoring marks above 75:')
    
    for roll, [name, mark] in record.items():
        if mark >= 75:
            print(f'{name} - {mark}')
    
    print()
    
else:
    print(f"\nERROR: '{n}' is not a valid number of students.\n")
