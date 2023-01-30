'''
Count and display the number of vowels, consonants, uppercase, lowercase characters in string.
'''

def insert(var: int): return str(var) + ' ' * (7 - len(str(var)))


inp = (input('\nEnter your string: '))

_vowels = ['a', 'e', 'i', 'o', 'u']

vowels = 0
consonants = 0
uppercase = 0
lowercase = 0

for i in inp:
    if i.lower() in _vowels:
        vowels += 1
    elif i.isalpha():
        consonants += 1
    
    if i.isupper():
        uppercase += 1
    elif i.islower():
        lowercase += 1

# insert() function is used for even number of spacing in the table
print( '┌─────────────────────┬─────────┐')
print(f'│ Vowels              │  {insert(vowels)}│')
print( '├─────────────────────┼─────────┤')
print(f'│ Consonants          │  {insert(consonants)}│')
print( '├─────────────────────┼─────────┤')
print(f'│ Uppercase           │  {insert(uppercase)}│')
print( '├─────────────────────┼─────────┤')
print(f'│ Lowercase           │  {insert(lowercase)}│')
print( '└─────────────────────┴─────────┘')
print('')
