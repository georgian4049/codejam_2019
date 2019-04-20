a=int(input())
k=0
for i in range (0,a):
    b=int(input(""))
    c=input("")
    k=k+1
    print('Case #',i+1,": ",end='',sep='')
    for j in c:
        if j is 'S':
            print('E',end="")
        else:
            print('S',end="")

    print()
