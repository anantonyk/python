import re
import xml.etree.cElementTree as ET
res = ET.Element("endings")
words=[]
lines=[]
endings=[]
def get_endings(array, line):
    result = []
    for index in range(len(array)):
        ending_value = re.findall(r'\w\w\w$', array[index])
        if len(ending_value)==1:
            result.extend([{'ending': ending_value, 'data': ({'word': array[index], 'word_position': index+1, 'line': line})}])
    return result
with open('text.txt', 'r') as file:
    arr = file.readlines()
for i in arr:
    z=i.split()
    lines.append(z)
for i in range(len(lines)):
    endings.extend(get_endings(lines[i], i+1))

data =[]
key=[]
nums=[0]
for i in range(len(endings)-1):
    count=1
    find1 = endings[i].get('ending')
    for j in range(i+1,len(endings)):
        find2 = endings[j].get('ending')
        if  find1 == find2 and find1 !=None:
            data.append(endings[j].get('data'))
            endings[j].clear()
            count+=1
    if count>1:
        data.append(endings[i].get('data'))
        key.append(endings[i].get('ending'))
        nums.append(count)

tupll=[]
s=0
f=0
for c in range(1,len(nums)):
    s+=nums[c-1]
    f+=nums[c]
    print(s)
    print(f)
    tupll.append((data[s:f],))
for i in range(len(nums)-1):
    ET.SubElement(res,"End",name=key[i]).text = " repeated " + str(nums[i+1])+ " times " +str(tupll[i])
tree = ET.ElementTree(res)
tree.write("c.xml")

