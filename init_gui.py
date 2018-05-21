from guizero import App, PushButton, Text, TextBox
from random import randint
from operator import itemgetter
import collections
import sys

global names
names = []
global values
values = []
global prenames
prenames = []
index = 3

def increment():
    global index
    index = index+1

def reset():
    global index
    index = 3

def get_name():
	names.append(box.get())
	prenames.append(Text(app, text= box.get(),grid=[0,index],align="left"))
	increment()
	box.clear()
	
def enter_names():
	names.clear()
	box.show()
	sub_button.show()
	i = 0
	while(i<len(values)):
		values[i].clear()
		values[i].destroy()
		i+=1
	values.clear()

def exit_():
	sys.exit()
	
def init():
	reset()
	i = 0
	while(i<len(values)):
		values[i].clear()
		values[i].destroy()
		i+=1
	values.clear()
	i = 0
	while(i<len(prenames)):
		prenames[i].clear()
		prenames[i].destroy
		i+=1
	prenames.clear()
	sub_button.hide()
	box.hide()
	people = []
	for name in names:
		people.append((name,randint(1,20),randint(1,20),randint(1,20),randint(1,20),randint(1,20)))
	people.sort(key=itemgetter(1,2,3,4,5), reverse = True)
	val_1=collections.Counter([v for (u,v,w,x,y,z) in people])
	val_2=collections.Counter([(v,w) for (u,v,w,x,y,z) in people])
	val_3=collections.Counter([(v,w,x) for (u,v,w,x,y,z) in people])
	val_4=collections.Counter([(v,w,x,y) for (u,v,w,x,y,z) in people])
	#val_5=collections.Counter([(v,w,x,y) for (u,v,w,x,y,z) in people])
	i=3
	for person in people:
		if(val_1[person[1]]==1):
			values.append(Text(app, text= person[0]+"\t"+str(person[1]),grid=[0,i],align="left"))
		elif(val_2[person[1],person[2]]==1):
			values.append(Text(app, text= person[0]+"\t"+str(person[1])+" "+str(person[2]),grid=[0,i],align="left"))
		elif(val_3[person[1],person[2],person[3]]==1):
			values.append(Text(app, text= person[0]+"\t"+str(person[1])+" "+str(person[2])+" "+str(person[3]),grid=[0,i],align="left"))
		elif(val_4[person[1],person[2],person[3],person[4]]==1):
			values.append(Text(app, text= person[0]+"\t"+str(person[1])+" "+str(person[2])+" "+str(person[3])+" "+str(person[4]),grid=[0,i],align="left"))
		else:
			values.append(Text(app, text= person[0]+"\t"+str(person[1])+" "+str(person[2])+" "+str(person[3])+" "+str(person[4])+" "+str(person[5]),grid=[0,i],align="left"))
		i+=1

		

app = App(title="Initiative Generator", width=250, height=500, layout="grid")
box = TextBox(app,grid=[1,0])
box.hide()
sub_button = PushButton(app, command=get_name, text="submit name", grid=[1,1])
sub_button.hide()
name_button = PushButton(app, command=enter_names, text="enter names\t", grid=[0,0])
init_button = PushButton(app, command=init, text="generate init\t", grid=[0,1])
exit_button  = PushButton(app, command=exit_, text="exit\t\t", grid=[0,2])

app.display()
