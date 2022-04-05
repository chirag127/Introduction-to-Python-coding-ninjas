def printLeaders(arr, n):
    for i in range(n):
        for j in range(i, n):
            if (arr[i] < arr[j]):
                break
            if (j == n - 1):
                print(arr[i],end=' ')

n=int(input())
arr=[int(x) for x in input().split()]
printLeaders(arr, len(arr))
