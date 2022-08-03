num=int(input("Enter number:"))
sum=0
for i in range(len(str(num))):
    digit=num%10
    sum=sum+digit
    num=num//10
print("Sum is",sum)
