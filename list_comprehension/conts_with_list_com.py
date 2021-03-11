sentence = 'The rocket, who was named Ted, came back from Mars because he missed his friends.'

def consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

consonants = [i for i in sentence if consonant(i)]
print(consonants)
