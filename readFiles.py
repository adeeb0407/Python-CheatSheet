 # read = 'r'
 # read just reades the file information -- 
 # write 'w'
 # write writes /edit existing information -- 
 # read and Write = 'r='
 # Append = 'a' -- 
 # append add new information withour deleted old and touching the old information

empFile = open("emp.txt", "r");

print(empFile.readable()) #returns a Boolean Val for if its readable or not
# will return a false value if the file is on Write more ("r")

#print(empFile.read()) #prints the entire file items

#this will not rint right now case we ahve 2 lines of txt file adn bothe lines are already printed by the ablove code
#print(empFile.readline()) # reads the first line and moves to nextline but does not print it
#print(empFile.readline()) # reads th second line and moves to the nextLine but does not print it

#here we will get an empty array beacuse the lines are already read commen tthe above code to see the changes

#print(empFile.readlines()[0]) # we get a spesicfiy line

#print(empFile.readlines()) # this will read all the linesa put them into an array


lines = empFile.readlines() # makes the file lines into array of elements
#print(lines[0]) # this will first index (first line of the file)

for text in lines:
    print(text)


empFile.close() # close the file opned
