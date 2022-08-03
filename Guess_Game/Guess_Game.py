Secret_number=9
First_number=0
Last_number=3
while First_number<Last_number:
    number=int(input("Enter guess number:"))
    First_number+=1
    if number==Secret_number:
        print("You win!")
        break
else:
    print("You lose")
