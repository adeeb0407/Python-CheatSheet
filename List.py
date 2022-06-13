#Basics of Lists
#list are ordred, mutable and allows duplicate elemnets in it
friends = ["Kevin", "Hendry", 20,30,False]
print(friends[0]);
print(friends[-1]);

#list Slicing methods
print(friends[2:])
print(friends[:4])
print(friends[0:2])
print(friends[::2]) #step index here the step is 2 so every 2 elemts distance is printed
print(friends[::-1]) #clever way to reverse the List

#create a black list

list = list()
print(list)
#functions/ Methods with List

languages = ["German", "French", "English", "Hindi"]
age = [20,30,40,50,60,20];

languages.extend(age); # extend method/function appends another list to the existing one
print(languages);

languages.append("Arabic"); #append function add another item to the pre existing list at the last index
print(languages);

languages.insert(1, "Polish"); # insert function add item/elemnt into list at desired index
print(languages);

languages.remove("German"); # remove function removest he elemnt ftom the list
print(languages);

languages.pop(); #removes the last elemnt of the list
print(languages);

print(languages.index("French")); # checks the index of the elemnt value

languages.clear(); # clears the list.. removes all elements 
print(languages)

print(age.count(20)); # gives the count of the given elemnt in the list

age.sort() # sorts the list any dataType String or numeric
print(age);
#this sort will change the original list if you dont want that use the sorted menthod
newList = sorted(age)

age.reverse();
print(age); #reverse the List

age2 = age.copy(); #copies the list named age 
print(age2)

#itetrat same elemt by this method
freshList = [0] * 10
print(freshList)

#append 2 lists 
catList = age + freshList
print(catList)

#copy a list
newAge = age.copy()
newAge.append(9000)
print(newAge)
print(age)

#copy list method 2
#newAge2 = list(age)
newAge2 = age[:] # this is called slicing and it slicing the list from statr to end
newAge2.append(67222)
print(newAge2)
print(newAge)
print(age)

#squaring the existing elemts of the list to a new list

squareList = [i*i for i in age]
print(age)
print(squareList)