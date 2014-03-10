def re_emvowel(consonants, vowels):
    f = open('enable1.txt', 'r')
    valid_words = set(f.read().splitlines())
    f.close()

    vowels = list(vowels)
    letters = list(consonants)
    new_str = ''

    while len(vowels) > 0:
        i, j = 0, 1
        vowel = vowels.pop(0)

        while i < len(letters):
            while j < len(letters):
                sub_cons = letters[i:j]
                k = 0
                while k <= len(sub_cons):
                    possible_word = ''.join(sub_cons[0:k]) + vowel + ''.join(sub_cons[k:])

                    if possible_word in valid_words:
                        new_str += possible_word + ' '
                        letters = letters[j:]
                        i, j = 0, 1
                        vowel = vowels.pop(0) if len(vowels) > 0 else ''
                    k += 1

                j += 1
            i, j = i + 1, i + 2
    print(new_str)

re_emvowel('wwllfndffthstrds', 'eieoeaeoi')
re_emvowel('bbsrshpdlkftbllsndhvmrbndblbnsthndlts', 'aieaeaeieooaaaeoeeaeoeaau')
re_emvowel('llfyrbsshvtsmpntbncnfrmdbyncdt', 'aoouiaeaeaoeoieeoieaeoe')
