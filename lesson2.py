numb = int(input())
degree = int(input())
def func():
    numb_1 = 1
    if degree>0:
        for i in range (degree):
            numb_1 *=numb
    return numb_1
print (func())
