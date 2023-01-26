'''s = "The lake has black fish, brown fish, blue fish in it."
print(s)

# t = open("input.txt", 'r')
# s = t.read()


print("\n\n--------------First Part----------------\n")
# First Part
comma = s.count(",")
fullstop = s.count(".")
d = s.replace(",", "")
d = d.replace(".", "")
print(d)
p = d.split(" ")
print(p)
x = []
for i in p:
    if i not in x:
        x.append(i)
dct = {}
for i in x:
    dct[i] = p.count(i)
# print(dct)
dct[","] = comma
dct["."] = fullstop
print(dct)


print("\n--------------Second Part-------------\n")
# Second Part
s = s.replace(",", "")
s = s.replace(".", "")
p = s.split(" ")
x = []
for i in p:
    if i not in x:
        x.append(i)
dct = {}
for i in x:
    dct[i] = p.count(i)
print(dct)



print("\n---------------Third Part----------------\n")
# Third part
stop = ["is", "in", "for", "where", "when", "to", "at", "The", "has", "it"]
comma = s.count(",")
fullstop = s.count(".")
d = s.replace(",", "")
d = d.replace(".", "")
print(d)
p = d.split(" ")
# print(p)
final = []
for i in p:
    if i not in stop:
        final.append(i)
# print(final)
x = []
for i in final:
    if i not in x:
        x.append(i)
# print(x)
dct = {}
for i in x:
    dct[i] = final.count(i)

print("List of common words : ", stop)
print(dct)

'''
