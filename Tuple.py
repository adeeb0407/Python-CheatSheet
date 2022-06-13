#tuples are immutable and ordred (values cannot be changed)
# List use [] to intialize where as tuple use ()
#tuple carry less memory then lists


from sys import getsizeof


coordinates = (4,5,6,"Boston",59,60, False);
#withput paranthesis also tuples are recognised
newTuple = "Adeeb",3,6
#for a sinlge element in a tuple if not put a comma it will read it to be a string
noComma = ("Adeeb")
print(type(noComma))
singleEle = ("Adeeb",)
print(type(singleEle))


# coordinates[0] = 8 will not work cause immutable 
#accesing elemts are similar to Lists reffer to List.py for entire information
print(coordinates[0])

#cnversion-  tuple form a list and vise versa

list = ["Max", 20, 20, False, "Adeeb"]
print(list)
newTup = tuple(list)
print(newTup)

#priting a tuple 

for i in newTup:
    print(i)

#checking if an elemt is in the tupe (similar to List)
if "Adeeb" in newTup:
    print("Yes")
else:
    print("No")

#counting how many of the element mentioned are presnt in the tuple
#here we used the number 20 how mant 20 int are presnt in the tupe newTup
print(newTup.count(20))

#chekcing the size of a tuple adn list with same elemets

list1 = [1,"Adeeb", False, 59]
tuple1 = (1,"Adeeb", False, 59)
#inorder to cat a int witha str use comma or else just conver the int tostr with str()
print("list Size: " , getsizeof(list1), " bytes")
print("Tuple Size: " , getsizeof(tuple1), " bytes")

print("list Size: " + str(getsizeof(list1))+ " bytes")
print("Tuple Size: " + str(getsizeof(tuple1))+ " bytes")