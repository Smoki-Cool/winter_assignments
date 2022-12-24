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

print('\nPATTERN 1:\n')

for i in range(1, 6):
    for j in range(1, i+1):
        print('*', end='')
    
    print('')
    
print('')


print('\nPATTERN 2:\n')

for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end='')
    
    print('')
    
print('')


print('\nPATTERN 3:\n')

for i in range(1, 6):
    for j in range(65, 65+i):
        print(chr(j), end='')
    
    print('')
    
print('')
