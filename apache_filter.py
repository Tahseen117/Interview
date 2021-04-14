import re
from collections import Counter

with open("sample apache logs", "r") as file:
	lines= file.readlines()

ip_list=[]
for line in lines:
	IP = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)
	ip_list.extend(IP)

d= Counter(ip_list)
for i in ip_list:
	print(d[i], i)

