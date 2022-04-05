lines = int(input())
j = 1
for i in range(1, lines + 1):
    j = 1
    while j <= lines:
        if i == j:
            print("*", end='', flush=True)
        else:
            print("0", end='', flush=True)
        j += 1
    j -= 1
    print("*", end='', flush=True)
    while j >= 1:
        if i == j:
            print("*", end='', flush=True)
        else:
            print("0", end='', flush=True)
        j -= 1
    print("")
