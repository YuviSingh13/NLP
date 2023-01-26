# classification
# defined
# description
# represent


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "India is a unique country that harbours different kinds of people that speak different languages, eat different foods and wear a variety of clothes. What makes our country special is that despite so many differences, people always live together in peace.Our country, India, lies in South Asia. It is a large country that is home to approximately 139 crore people. Moreover, India is also the biggest democracy in the whole world. Having one of the oldest civilizations, it is a very rich country.Our country has fertile soil that makes it the largest wheat producer in the whole world. India has given birth to famous personalities in the field of literature and science. For instance, Rabindranath Tagore, CV Raman, Dr Abdul Kalam, and others are Indians.It is a country that is home to thousands of villages. Similarly, the fields of India are fed by the mighty rivers. For instance, Ganga, Kaveri, Yamuna, Narmada, and more are rivers of India.Most importantly, the coasts of our country are guarded by the deep oceans and the mighty Himalayas are our natural frontiers. Being a secular state, India has a variety of religions that prosper happily together.The culture of our country is immensely rich and famous worldwide. The different languages we speak and the different Gods we worship does not create differences between us. We all share the same spirit."
# print(len(example.split()))

# example_sent = example.split()

print("Total words in document : ",len(example_sent.split()))
stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
filtered_sentence = []

for w in word_tokens:
	if w not in stop_words:
		filtered_sentence.append(w)

print("\n\n-----------------------**************--------------------------\n\n")
print("List after removing stop words: ")
filtered_sentence.remove(",")
filtered_sentence.remove(".")
filtered_sentence.remove(",")
filtered_sentence.remove(".")
print(filtered_sentence)
print("\n\nLength after removing stop words : ", len(filtered_sentence))

print("\n\n-----------------------**************--------------------------\n\n")


from nltk.stem import PorterStemmer

ps = PorterStemmer()
filtered_sentence.append("boundary")
print("\nWord\t: \tRoot Word\n")
for w in filtered_sentence:
	print(w, " : ", ps.stem(w))
	if "ry" == w[-2:]:
		print("Incorrect word found !!! correct word is below")
		print(w," : " ,w)
	elif "larly" == w[-5:]:
		print("Incorrect word found !!! correct word is below")
		print(w, " : ",w[:len(w)-5]+"lar")
	else:
		print(w, " : ", ps.stem(w))

