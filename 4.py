n=int(input("Enter the range of number:\n"))
sum=0
p=9
for i in range(1,n+1):
    sum += p
    p=(p*10)+9
print("The sum of the series 9 + 99 + 999 ... = ",sum)