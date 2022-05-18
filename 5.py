n=int(input("Enter number: "))

temp=n
rev=0

while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10

if(temp==rev):
    num = 1
    while temp >= 1:
        num = num * temp
        temp = temp - 1
    print("The number is a palindrome!")
    print(f"The Factorial Is {num}")
else:
    print("The number isn't a palindrome!")