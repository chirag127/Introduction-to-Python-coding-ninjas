lines = int(input())
i = 1
j = 1
while i <= lines:
    j = 1
    while j <= lines:
        if i == j:
            print("*", end='', flush=True)
        else:
            print("0", end='', flush=True)
        j = j+1
    j = j-1
    print("*", end='', flush=True)
    while j >= 1:
        if i == j:
            print("*", end='', flush=True)
        else:
            print("0", end='', flush=True)
        j = j-1
    print("")
    i = i+1
