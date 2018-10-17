import xml.etree.cElementTree as ET
import string

res = ET.Element("uniqueWords")
words=[]

with open('text.txt', 'r') as file:
    arr = file.readlines()
print(arr)
for i in arr:
    z=i.split()
    for x in range(len(z)):
        words.append(z[x].strip(string.punctuation).lower())

print(words)
print(len(words))
words.sort()
print(words)
unique=[]
slovo=words[0]

count=1
for i in range(1,len(words) - 1):
    word=words[i]
    if (word == slovo):
        count=count+1
    else:
        unique.append(word)
        ET.SubElement(res,"Word",name=slovo).text = " repeated " + str(count)+ " times "
        count=1
    slovo=word
tree = ET.ElementTree(res)
tree.write("p.xml")