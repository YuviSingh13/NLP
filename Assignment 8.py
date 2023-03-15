from datetime import datetime

import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
from pywsd import simple_lesk

nltk.download('all')


def get_semantic(seq, key_word):
    temp = word_tokenize(seq)

    temp = lesk(temp, key_word)
    return temp.definition()


# keyword = "knife"
# seq = "She chopped the vegetable with a knife that has a sharp blade and handle"



# keyword = 'jam'
# seq1 = 'My mother prepares very yummy jam.'
# seq2 = 'Signal jammers are the reason for no signal.'


keyword = "Bank"
seq1 = "he cashed a check at the bank."


print()
print(get_semantic(seq1, keyword), "\n")
# print(get_semantic(seq2, keyword))


# Simple Lesk

key = "bow"
# key = input("Enter keyword : ")
# sen1 = "The bow was tight"
sen2 = "I had to bow for him"
sen1 = input("Enter Sentence : ")

# result = simple_lesk

sentences2 = ['The bow was tight','I had to bow for him']


leskStart = datetime.now()
print ("Lesk", sentences2[0])
answer = lesk(sentences2[0],'bow')

print ("Sense:", answer)
print ("Definition : ", answer.definition())
print(datetime.now()-leskStart)
print(" ")

simpleLeskStart = datetime.now()


print ("Simple_Lesk", sentences2[0])
answer1 = simple_lesk(sentences2[0],'bow')

print ("Sense:", answer1)
print ("Definition : ", answer1.definition())

print(datetime.now()-simpleLeskStart)