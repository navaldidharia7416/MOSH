num=input("Enter phone number:")
dict={
        "1":"One",
        "2":"Two",
        "3":"Three",
        "4":"Four",
        "5":"Five",
        "6":"Six",
        "7":"Seven",
        "8":"Eight",
        "9":"Nine",
        "0":"Zero"
    }
number=""
for i in num:
    number+=dict.get(i,"!")+" "
print(number)
