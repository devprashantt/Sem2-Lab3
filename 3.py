
count = 0
for i in range(1, 10):
    count = i
    for j in range(1, 10):
        print(count,end=" ")
        count += 1
        if count > 9:
            count = 1
    print()