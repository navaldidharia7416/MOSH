try:
    age=int(input('Age: '))
    income=0
    risk=income/age
    print(age)
    print(risk)
except ZeroDivisionError:
    print('Age cannot be zero')
# except ValueError:
#     print("Invalid value")
