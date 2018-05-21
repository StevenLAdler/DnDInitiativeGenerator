from random import randint
from operator import itemgetter
import collections

names = []
def enterNames():
	print("enter a name then press enter\nenter a blank line when you are done")
	while True:
		name = input('')
		if name == '':
			break
		names.append(name)
		
def init():
	people = []
	for name in names:
		people.append((name,randint(1,20),randint(1,20),randint(1,20),randint(1,20),randint(1,20)))
	people.sort(key=itemgetter(1,2,3,4,5), reverse = True)
	val_1=collections.Counter([v for (u,v,w,x,y,z) in people])
	val_2=collections.Counter([(v,w) for (u,v,w,x,y,z) in people])
	val_3=collections.Counter([(v,w,x) for (u,v,w,x,y,z) in people])
	val_4=collections.Counter([(v,w,x,y) for (u,v,w,x,y,z) in people])
	#val_5=collections.Counter([(v,w,x,y) for (u,v,w,x,y,z) in people])
	print("\n")
	for person in people:
		if(val_1[person[1]]==1):
			print(person[0]+"\t"+str(person[1]))
		elif(val_2[person[1],person[2]]==1):
			print(person[0]+"\t"+str(person[1])+" "+str(person[2]))
		elif(val_3[person[1],person[2],person[3]]==1):
			print(person[0]+"\t"+str(person[1])+" "+str(person[2])+" "+str(person[3]))
		elif(val_4[person[1],person[2],person[3],person[4]]==1):
			print(person[0]+"\t"+str(person[1])+" "+str(person[2])+" "+str(person[3])+" "+str(person[4]))
		else:
			print(person[0]+"\t"+str(person[1])+" "+str(person[2])+" "+str(person[3])+" "+str(person[4])+" "+str(person[5]))
	print("\n")

enterNames()
while True:
	inp = input('type init for a new init order\ntype restart to enter new names\ntype exit to exit\n')
	if inp == 'init':
		init()
	elif inp == 'restart':
		names = []
		enterNames()
	elif inp == 'exit':
		exit()
	else:
		print('invalid option')