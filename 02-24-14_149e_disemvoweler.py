import string

def disemvowel(str):
    vowels = set('aeiou')
    replacer = lambda x: '' if x in vowels or x in ' ' else x
    voweler = lambda x: x if x in vowels else ''
    print(''.join(map(replacer, list(str))))
    print(''.join(map(voweler, list(str))))

def disemvowel_v2(str):
    vowels = set('aeiou')
    print(''.join(letter for letter in str if letter not in vowels and letter is not ' '))
    print(''.join(letter for letter in str if letter in vowels))

disemvowel("derp de derp de derp")
disemvowel_v2("derp de derp de derp")
