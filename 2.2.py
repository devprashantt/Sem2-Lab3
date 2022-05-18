numberOfRow = int(input("Number Of Rows"))
startingNumber = int(input("Starting Number"))

print("Required pattern is As Follow: ")
for i in range(0, numberOfRow):
    for j in range(0, 7):
        print(startingNumber-i, end=" ")
    print()
