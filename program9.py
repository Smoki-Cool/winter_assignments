'''
Count and display the number of vowels, consonants, uppercase, lowercase characters in string.
'''

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


print('┌─────────────────────┬─────────┐')

insert_ = ' ' * (7 - len(str(vowels)))
print(f'│ Vowels              │  {vowels}{insert_}│')

print('├─────────────────────┼─────────┤')

insert_ = ' ' * (7 - len(str(consonants)))
print(f'│ Consonants          │  {consonants}{insert_}│')

print('├─────────────────────┼─────────┤')

insert_ = ' ' * (7 - len(str(uppercase)))
print(f'│ Uppercase           │  {uppercase}{insert_}│')

print('├─────────────────────┼─────────┤')

insert_ = ' ' * (7 - len(str(lowercase)))
print(f'│ Lowercase           │  {lowercase}{insert_}│')

print('└─────────────────────┴─────────┘')

print('')
