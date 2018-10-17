list1=['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]

def dolist(some):
    newlist=[]
    for new in some:
        p=type(new)
        if p is tuple or p is list:
            for i in dolist(new):
                newlist.append(i)
        else:
            newlist.append(new)
    return newlist
print(dolist(list1))