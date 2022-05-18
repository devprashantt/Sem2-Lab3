rows = 5
k = 0
for i in range(1, rows + 1):
    k = k+1 
    for j in range(k, rows + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()