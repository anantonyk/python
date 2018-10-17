a = open("a.txt", "r")
b1 = open("b1.txt", "w")
b2= open("b2.txt", "w")
r=a.read()
a.close()
array=[]
for line in r.split("."):
    array.append(line)
for i in range(0,len(array),1):
    if i%2==0:
        b2.write(array[i].lower())
        b2.write("\n")
    if i % 2 == 1:
        b1.write(array[i].upper())
        b1.write("\n")
