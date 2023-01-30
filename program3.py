'''
Generate the following patterns using nested loop.
┌───────────────┬───────────────┬───────────────┐
│   Pattern-1   │   Pattern-2   │   Pattern-3   │ 
├───────────────┼───────────────┼───────────────┤
│ *             │ 12345         │ A             │
│ **            │ 1234          │ AB            │
│ ***           │ 123           │ ABC           │
│ ****          │ 12            │ ABCD          │
│ *****         │ 1             │ ABCDE         │
└───────────────┴───────────────┴───────────────┘
'''

# Pattern 1
print('\nPATTERN 1:\n')
# Outer loop to iterate through the rows
for i in range(1, 6):
    # Inner loop to iterate through the columns, printing '*'
    for j in range(1, i+1):
        print('*', end='')
    # Move to the next row
    print('')
# Blank line for separation
print('')

# Pattern 2
print('\nPATTERN 2:\n')
# Outer loop to iterate through the rows in reverse order
for i in range(5, 0, -1):
    # Inner loop to iterate through the columns, printing the value of j
    for j in range(1, i+1):
        print(j, end='')
    # Move to the next row
    print('')
# Blank line for separation
print('')

# Pattern 3
print('\nPATTERN 3:\n')
# Outer loop to iterate through the rows
for i in range(1, 6):
    # Inner loop to iterate through the columns, printing the character represented by the ASCII value of j
    for j in range(65, 65+i):
        print(chr(j), end='')
    # Move to the next row
    print('')
# Blank line for separation
print('')
