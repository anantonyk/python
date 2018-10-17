def isSimple(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True


def simples(a, b):
    count=0
    for i in range(a, b):
        if isSimple(i):
            print(i)
            count+=1
    if count==0:
        print('NoSimpleDigits')
c = int(input('1Number: '))
d = int(input('2Number:'))
simples(c,d)


