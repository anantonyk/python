def inputnum():
    x=int(input("Input number: "))
    return x

def div():
    while True:
        a=inputnum()
        b = inputnum()
        if a<0 or b<0:
            raise Exception ('Input only positive numbers')
        else:
            break
    if a%b==0:
        print(True)
    else :
        print(False)
div()