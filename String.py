from curses import def_prog_mode

lol = "Hello"
lol1 = "           HEllo           "

print(lol);
print(lol1.strip())#works like trim() in javascript to remove the blank spaces
print(lol.upper().isupper());
print(lol[0])
print(lol.index("H"));
print(lol.find("H"));#retunrs the first index of the letter mention if it cannot gind anything it will return -1
print(lol.replace("Hello", "World"))
print(lol)
print(lol.count('l'))# reutns 2
lol.startswith("H") # return a boolean value
lol.endswith("o") #returns a boolean value 

#Split and Join
stringVal = "Adeeb Shah"
stringVal2 = "Adeeb,Shah"
listOfString = stringVal.split(" ") #retuns a list with2 elemnts as the slpit is happning on a space " "
print(listOfString)
listOfString2 = stringVal2.split(",")
print(listOfString2)

#join will join a list to a string

newStr = " ".join(listOfString)
print(newStr)

#or 
oldStr = " "
newStr2 = oldStr.join(listOfString)
print(newStr2)

##formating Strings

name1 = "Tom"
name2 = "Sultan"
print("Adeeb has Friends Named {} and {}".format(name1,name2))

num = 3.14567

print("The New Val is {:.2f}".format(num)) # :.2f gets the 2 digits after the decimal

#best Way of formating string is this can do operations on runtime like below for multiply
print(f"Adeeb has Friends named {name1*2} and {name2}")
