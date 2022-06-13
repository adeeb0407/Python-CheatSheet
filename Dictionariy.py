#similar to Objects in Javascript (Key-Value pair)
#collection datatype which is unordred and mutable

monthDic = {
    "Jan" : "January",
    "Feb" : "Febuary",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July"
}

weekDic = {
    1 : "Sunday",
    2 : "Monday",
    3 : "TuestDay",
    4 : "Wednesday",
    5 : "Thursday",
    6 : "Friday",
    7 : "Saturday"
}

print(monthDic)
print(monthDic["Jan"]);
print(monthDic.get("Apr"))
print(monthDic.get("Luv", "not a Valid Key")) # the get() function will give you a custom error message if the key is not present

if "Feb" in monthDic: # another way to check if the key exisit or not
    print(monthDic["Feb"])
else:
    print("nah nothing here")

#use the dict() to create a new dictionary
myDict = dict()
print(myDict)

#adding a new Elemt to a dictionary
#if the element key already exisit it will overwrite that key value with the new one given to it here it is "August" key is "Aug" 
monthDic["Aug"] = "August"
print(monthDic)

#deleted an key-value pair in a dictionary
del monthDic["Aug"]

try:
    monthDic.pop("Aug") # this will also work
    monthDic.popitem() #removes the last item of the Dict
except:
    print("Already Dleted Value")

print(monthDic.get("Aug", "No Val Found"))
print(monthDic)

#get a list with all the keys of the Dict
listOfKeys = monthDic.keys()
print(listOfKeys)

#looping throught the dict for the values
for key in monthDic:
    print(monthDic[key]+ "---")

#method 2
for val in monthDic.values():
    print("---" + val)
#to loop throu to get only values

for key in monthDic:
    print(key)

#gte both key and values in one loop
#like .items()we have .keys() and .values()
for key, value in monthDic.items():
    print(key, value)

#copying a dict use the dict()

newDict = dict(monthDic)
print(newDict)

#mergeing 2 dictionaries

monthDic.update(weekDic) # monthDic megerings the WeekDic
print(monthDic)
print("\n")
print(weekDic) #but WeekDic remains the same

##note you can use tuples as your keys in dict but nit lost as list are mutable and key cannot be changes when added

key = (3,6)
dict = {key : "adeeb"}
print(dict)