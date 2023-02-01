from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

word_limit = int(input("Enter word limit : "))

para_1 = "India has the second-largest population in the world. India is also knowns as Bharat, Hindustan and sometimes Aryavart. It is surrounded by oceans from three sides which are Bay Of Bengal in the east, the Arabian Sea in the west and Indian oceans in the south. Tiger is the national animal of India. Peacock is the national bird of India. Mango is the national fruit of India. “Jana Gana Mana” is the national anthem of India. “Vande Mataram” is the national song of India. Hockey is the national sport of India. People of different religions such as Hinduism, Buddhism, Jainism, Sikhism, Islam, Christianity and Judaism lives together from ancient times. India is also rich in monuments, tombs, churches, historical buildings, temples, museums, scenic beauty, wildlife sanctuaries, places of architecture and many more. The great leaders and freedom fighters are from India.".replace(".", "").replace(",", "")
para_2 = "India is a famous country all over the world. India has the second-largest population in the world. Geographically, our country is located to the south of the Asia continent. India is a high population country and well protected from all directions naturally. It is a famous country for its great cultural and traditional values all across the world. It contains a mountain called Himalaya, which is the biggest in the world.Three big oceans surround it in three directions: the south with the Indian Ocean, the east with the Bay of Bengal, and the west with the Arabic sea. India is a democratic country that ranks second in its population. The national language of India is Hindi however, almost fourteen nationally recognized languages are spoken here.".replace(".", "").replace(",", "")

stop_words = set(stopwords.words('english'))


word_tokens_1 = word_tokenize(para_1)
# print(word_tokens_1)
print("Words in document 1 : ",len(word_tokens_1))
word_tokens_2 = word_tokenize(para_2)
# print(word_tokens_2)
print("Words in document 2 : ",len(word_tokens_2))


'''
# Document 1
filtered_sentence_1 = [w for w in word_tokens_1 if not w.lower() in stop_words]
filtered_sentence_1 = []
for w in word_tokens_1:
	if w not in stop_words:
		filtered_sentence_1.append(w)

print("Length after removing stop words : ", len(filtered_sentence_1))

# Document 2
filtered_sentence_2 = [w for w in word_tokens_1 if not w.lower() in stop_words]
filtered_sentence_2 = []
for w in word_tokens_2:
	if w not in stop_words:
		filtered_sentence_2.append(w)
print("length after removing stop words : ", len(filtered_sentence_2))

count = 0

doc1 = 0
doc2 = 0

unique_1 = []
unique_2 = []

for i in range(len(filtered_sentence_1)-word_limit):
    a = filtered_sentence_1[i:i+word_limit]
    unique_1.append(a)
    # print(a, "printing")
    doc1 += 1
    for j in range(len(filtered_sentence_2)-word_limit):
        b = filtered_sentence_2[j:j+word_limit]
        if b not in unique_2:
            unique_2.append(b)
        # print(b)
        doc2 += 1
        if a == b:
            print("Equal")
            # print(a)
            # print(b)
            count += 1

print("Permutation in doc 1 : ", doc1)
print("Permutation in doc 2 : ", doc2//doc1)


print("No of equal string : ", count)

'''


count = 0

doc1 = 0
doc2 = 0

unique_1 = []
unique_2 = []

for i in range(len(word_tokens_1)-word_limit):
    a = word_tokens_1[i:i+word_limit]
    unique_1.append(a)
    # print(a, "printing")
    doc1 += 1
    for j in range(len(word_tokens_2)-word_limit):
        b = word_tokens_2[j:j+word_limit]
        if b not in unique_2:
            unique_2.append(b)
        # print(b)
        doc2 += 1
        if a == b:
            print("Match Found!!")
            # print(a)
            # print(b)
            count += 1

print("Permutation in doc 1 : ", len(unique_1))
print("Permutation in doc 2 : ", len(unique_2))


print("No of equal string : ", count)
print("plag1 : ", (count/len(unique_1))*100)
print("plag2 : ", (count/len(unique_2))*100)
