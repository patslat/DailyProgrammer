import string

def disemvowel(str):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    replacer = lambda x: '' if x in vowels or x in ' ' else x
    return ''.join(map(replacer, list(str)))

print(disemvowel("derp de derp de derp"))
