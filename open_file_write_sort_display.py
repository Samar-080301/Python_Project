file = open('GFG.txt', 'w') 
# Data to be written
for e in range (0,10):
    data =input("Enter a number - ")
# Writing to file 
    file.write(data) 
# Closing file 
file.close() 
# program for reading 
# open file 
h = open('GFG.txt', 'r') 
# Reading from the file 
content = h.readlines() 
# List for storing the nos. 
a = []
# Iterating through the content 
# Of the file 
for line in content: 
	for i in line: 
		# Checking for the digit in 
		# the string 
		if i.isdigit() == True: 
			
			a.append(i) 
a.sort()
#writing sorted list 
file = open('GFG.txt', 'w')
for w in a:
    file.write(w) 
file.close
