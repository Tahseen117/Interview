from collections import Counter
import os

#Reading file in lines variable
with open("passwd.txt", "r") as file:
	lines= file.readlines()

#Extracting the users form the file
for i in lines:
	user=i.split(':')[0]
	f= open("users", "a")
	f.write(user + '\n')
f.close()

#Counting the duplicates using Counter
with open ("users", "r") as f:
	users = f.read().splitlines()
d=Counter(users)

#Printing the number of occurence along with user
for user in users:
	print('{} occurs {} times'.format(user,d[user]))
os.remove("users")
