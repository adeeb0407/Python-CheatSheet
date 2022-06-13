
try:
    number = int(input("Enter a Number: "))
    print(number)
except ValueError as err:  
    print("Invalid Input")
    print(err)
finally : # OPTIONAL 
    print("Your Done")