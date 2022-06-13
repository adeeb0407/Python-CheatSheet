#sets are unordred, mutable (just like list and dictionary) but they can not have diplicates (unlike list and dictionary)

mySet = {"Adeeb", 20,60, False, "Sultan",20}
print(mySet)#order is not nesseayr so gives a random order

mySet2 = {80,20,39,16,1,8,27}
print(mySet2)

#adding elemts to a set
mySet2.add("Adnan")
print(mySet2)

#add/merge 2 sets without duplication
updatedSet = mySet.update(mySet2)
print(updatedSet)

#remove elemnts by remove() method
mySet2.remove(80) # if the element does not exisit in the set this will show error sobetter use discard()
mySet2.discard(27) # removes element if present in the set if not does not stop the code and lets it run without throwing an error
print(mySet2)
#remove all elements by clear() 
# use pop() method to remove the last element
#looping is the same
for lol in mySet2:
    print(lol)

#empty set initnaliztion

setTry = set("1234") # read as a set
print(type(setTry))
print(setTry)
setTry2 = {} #read as a Dict
print(type(setTry2))

#union to add/merge 2 sets and sort them
#intersetion to get the elemnts that re present in both the sets

even = {2,4,6,8}
odd = {1,3,5,7}
prime = {2,3,5,7}

print(even.union(odd)) # merges both sets and sortes them
print(even.intersection(prime)) # 2 is common in both sets
#print(even.intersection_update(prime))# changes the original set the old one with only common elemnts in the set named even

#oppsite of intersetion is difference hence it will get the uncommon/different elemnts from both set and give us a new sets
#odd.symmetric_difference(prime) will do the same as difference()
print(odd.difference(prime)) #here only 1 elemnt is different
#print(odd.difference_update(prime))# same as differnce but chnages the real/orginal set there in set named even

set1 = {1,2,3,4,5,6}
set2 = {1,2,3}
#issubset means if an set has all the lemnts of the other set
print(set2.issubset(set1))#retuenstrue as things are all aligned
#superset is when a set has all the elemnts of another set
print(set1.issuperset(set2))#retuns true as there are diff aswell in it compared to theven set

#prozen set woeks as a tuple that cant be changed

a = frozenset([1,2,3,4,5])
#a.add(7)#throws an error
#a.discard(1)#throws an error
#but the interseion union methonds will work