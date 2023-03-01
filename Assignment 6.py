from nltk.corpus import brown
# from nltk import word_tokenize


word = input("Enter word : ")
# word = "criticla"
corpus = input("Enter corpus name : ")

# For bigram
def bigram(word):
    l = []
    for i in range(len(word)-1):
        l.append(word[i:i+2])
    return l
a = bigram(word)
print("Bigram : ", a)

tokens = brown.words()[:10000]

w = len(a)//2


x = set()
dic = {}
for i in range(len(tokens)):
    p = bigram(tokens[i])
    count = 0
    for j in range(min(len(p), len(a))):
        if a[j] in p:
            count += 1
    if count >= w:
        x.add(tokens[i])
        dic[tokens[i]] = count


print(len(dic))
for key, values in dic.items():
    print(key, values)

print("\n\n\t\t*************\n\n")



# A Dynamic Programming based Python program for edit
# distance problem


def editDistDP(str1, str2, m, n):
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],	 # Insert
                                dp[i-1][j],	 # Remove
                                dp[i-1][j-1]) # Replace

    return dp[m][n]


for keys, values in dic.items():
    dic[keys] = editDistDP(keys, word, len(keys), len(word))
    print(f"Minimum edit distance for {keys} : ", editDistDP(keys, word, len(keys), len(word)))
    # p = editDistDP(keys, word, len(keys), len(word))

print(dic)