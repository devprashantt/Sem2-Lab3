num = int(input("Enter a number ( greater than 1)\n"))  
f = 0
i = 2
while(i <= num / 2):
    if num % i == 0:
        f=1
        break
    i=i+1
    
if f==0:
    print("The entered number is a PRIME number")
    count = 0
    while (num != 0):
        num //= 10
        count += 1
    print(f"Number Of Digits {count}")    
    
else:
    print("The entered number is not a PRIME number")
 