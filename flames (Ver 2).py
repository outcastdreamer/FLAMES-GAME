from sys import platform
from os import system as s
from gtts import gTTS as g
from colorama import init, Fore, Back, Style
init()
from termcolor import colored
from time import sleep

def clear():
	if (platform=="linux" or platform=="linux2"):
		s("clear")
	elif (platform=="win32"):
		s("cls")

def colour(str = "",color = "red"):
	print (colored(str,color),end = "")

#alpha = list(string.ascii_uppercase)

clear()

name1 = input("\nEnter the first name : ").upper()
name2 = input("\n\nEnter the second name : ").upper()

list1 = [i for i in name1]
list2 = [i for i in name2]

l1,l2 = list1,list2
f1_list = []; f2_list = []

if (name1.find(' ')==-1):
	pass
else:
	l1[l1.index(' ')] = "-"

if (name2.find(' ')==-1):
	pass
else:
	l2[l2.index(' ')] = "-"

print (l1)
print (l2)

for i in range(len(l1)):
	for j in range(len(l2)):
		if (l1[i]==l2[j]):
			##################################### F1 COUNT ################################
			if (l1.count(l1[i]) >= 1):
				k=l1[i]
				for m in range(len(l1)):
					#print ("i : ",i," ",end="")
					#print ([m], end = "")
					if (l1[m])=="-":
						pass
					else:
						if (l1[m]==k):
							f1_list.append(m)
							#print (m)
							l1[m] = "-"
			else:
				f1_list.append(i)
			##################################### F2 COUNT ################################
			if (l2.count(l2[j]) >= 1):
				p=l2[j]
				for m in range(len(l2)):
					if (l2[m])=="-":
						pass
					else:
						if (l2[m]==p):
							f2_list.append(m)
							l2[m] = "-"
			else:
				f2_list.append(j)
			################################### NO MATCHES ################################
		else:
			pass

f1_list.sort()
f2_list.sort()

print ("\n\n")
print (l1)
print (l2)
print (f1_list)
print (f2_list)
final_count=0
for i in range(len(l1)):
	if l1[i]!="-":
		final_count+=1
for i in range(len(l2)):
	if l2[i]!="-":
		final_count+=1
print ("\n\nFinal Count : ",final_count)


"""
F="FLAMES"
FLAMES=[i for i in F]
copy=[]
new_FLAMES=[]
while (FLAMES.count("-")!=5):
	mod=(final_count%6)-1
"""
