def re_emvowel(consonants, vowels):
    f = open('enable1.txt', 'r')
    valid_words = set(f.read().splitlines())
    f.close()

    vowels = list(vowels)
    consonants = list(consonants)
    new_str = ''

    # we need to check if any combination of consonants + vowel is a word
    def has_valid_word(consonants, vowel):
        i = 0
        while i < len(consonants) + len(vowel):
            possible_word = ''.join(consonants[0:i]) + vowel + ''.join(consonants[i:])
            if possible_word in valid_words:
                return possible_word
            i += 1
        return False

    while len(vowels) > 0:
        vowel = vowels.pop(0)

        # length of consonants we will attempt to use, go for the largest words first
        i = len(consonants)
        while i > 0:
            word = has_valid_word(consonants[0:i], vowel)
            if word:
                new_str += word + ' '
                consonants = consonants[i:]
                print(consonants)
                break
            i -= 1

    print(new_str)


re_emvowel('wwllfndffthstrds', 'eieoeaeoi')
re_emvowel('bbsrshpdlkftbllsndhvmrbndblbnsthndlts', 'aieaeaeieooaaaeoeeaeoeaau')
re_emvowel('llfyrbsshvtsmpntbncnfrmdbyncdt', 'aoouiaeaeaoeoieeoieaeoe')
