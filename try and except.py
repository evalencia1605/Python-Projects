
try:
    #answer = 10/0 for zero dividion error
    number = int(input("Enter a number:"))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Wrong input!!")