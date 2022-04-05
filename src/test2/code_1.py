str=input().split()
n,m=int(str[0]),int(str[1])
li = [[int(j) for j in input().split()] for _ in range(n)]
for i in range(n):
    for j in range(m):
        print(li[i][j],end=' ')
    print()

    k=i
    while k<n-1:
        for j in range(m):
            print(li[i][j],end=' ')
        print()
        k+=1
