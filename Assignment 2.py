import math
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
# print(stopwords.words('english'))


print("\n\n\t\t------------------Including Stop Words----------------------\n\n\n")
# t1 = "The game of life is a game of everlasting learning"
# t2 = "The unexamined life is not worth living"


t1 = "Virat Kohli is a world-famous Indian cricketer with fans all around the world." \
    " He has a great and inspiring personality. Born on 5th November 1988 in Delhi's " \
    "Uttam Nagar, Virat Kohli has come a long way. He started playing cricket in his " \
    "school and ended up playing for the Under-19 Indian cricket team."

# p1 = t1.split()
# print(p1)


t2 = "Virat Kohli is the captain of the Indian cricket team and is the beloved " \
    "player of millions. He is a right handed top order batsman. Kohli is considered " \
    "one of the best batsmen in the world. He plays for Royal Challengers Bangalore " \
    "in the Indian Premier League and has been the captain of the team since 2013. " \
    "However, he has decided not to captain from the year 2022. He is the favorite " \
    "player of the youth."
# p2 = t2.split()
# print(p2)

x = []
p1 = t1.split()
print(p1)


p2 = t2.split()
print(p2)



for i in p1:
    if i not in x:
        x.append(i)
for i in p2:
    if i not in x:
        x.append(i)
print(x)


c1 = []
for i in x:
    c1.append(p1.count(i))
print(c1)

c2 = []
for i in x:
    c2.append(p2.count(i))
print(c2)


# print(len(c1), "c1 length")
# print(len(c2), "c2 length")


mag = 0
for i in range(len(c1)):
    mag += c1[i]*c2[i]
print(mag, "d1.d2")

mod1 = 0
mod2 = 0
for i in c1:
    mod1 += i**2
print(mod1, "mod(d1)")


for i in c2:
    mod2 += i**2

print(mod2, "mod(d2)")

cos = mag/(math.sqrt(mod1)*math.sqrt(mod2))
print(cos, "cosine value")


print("\n\n\t\t--------------------Without Including Stop Words-------------------\n\n\n")


t1 = "Virat Kohli is a world-famous Indian cricketer with fans all around the world." \
    " He has a great and inspiring personality. Born on 5th November 1988 in Delhi's " \
    "Uttam Nagar, Virat Kohli has come a long way. He started playing cricket in his " \
    "school and ended up playing for the Under-19 Indian cricket team."

# p1 = t1.split()
# print(p1)


t2 = "Virat Kohli is the captain of the Indian cricket team and is the beloved " \
    "player of millions. He is a right handed top order batsman. Kohli is considered " \
    "one of the best batsmen in the world. He plays for Royal Challengers Bangalore " \
    "in the Indian Premier League and has been the captain of the team since 2013. " \
    "However, he has decided not to captain from the year 2022. He is the favorite " \
    "player of the youth."
# p2 = t2.split()
# print(p2)


print("-------------------*********************----------------------")
x = []
p1 = t1.split()
# print(p1)
mx1 = []
for i in p1:
    if i not in stopwords.words('english'):
        mx1.append(i)
print(mx1)

print(len(mx1), "excluded Stop words")
print("--------------------**********************-------------------")

p2 = t2.split()
# print(p2)
mx2 = []
for i in p2:
    if i not in stopwords.words('english'):
        mx2.append(i)
print(mx2)
print(len(mx2), "excluded stop words")


print("-------------------********************--------------------")

for i in mx1:
    if i not in x:
        x.append(i)
for i in mx2:
    if i not in x:
        x.append(i)
print(x)


c1 = []
for i in x:
    c1.append(mx1.count(i))
print(c1)

c2 = []
for i in x:
    c2.append(mx2.count(i))
print(c2)


# print(len(c1), "c1 length")
# print(len(c2), "c2 length")


mag = 0
for i in range(len(c1)):
    mag += c1[i]*c2[i]
print(mag, "d1.d2")

mod1 = 0
mod2 = 0
for i in c1:
    mod1 += i**2
print(mod1, "mod(d1)")


for i in c2:
    mod2 += i**2

print(mod2, "mod(d2)")

cos = mag/(math.sqrt(mod1)*math.sqrt(mod2))
print(cos, "cosine value")


