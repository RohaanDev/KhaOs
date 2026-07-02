import tkinter as tk
import time
import random

root = tk.Tk()
root.title("Calculator")
root.geometry("360x800")

root.grid_columnconfigure(200, weight=1)
root.grid_columnconfigure(1, weight=1)
score = 0
direction = None
def loop():
	global direction 
	x = square.winfo_x()
	y = square.winfo_y()
	if direction == "right":
		x += 30
		check()
	if direction== "left":
		x -= 30
		check()
	if direction== "up":
		y -= 30
		check()
	if direction== "down":
		y += 30
		check()
	square.place(x = x , y = y)
	root.after (100 , loop)
	
		



screen = tk.Entry(root, font=("Arial", 30), justify="right")
screen.grid(row=0, column=0, columnspan=4, sticky="ew" )
label = tk.Label(root , font = ("Arial" , "20"))
label.grid(row = 1 , column = 0 , columnspan = 4)
label1 = tk.Label(root ,text = score)
label1.place(x = 7 , y = 9)

screen.focus_set()

square = tk.Label(root , bg= "Blue" , fg = "Blue" , width = 10 , height = 5)
square.place(x = 2 , y = 5)
yx = random.randint(0 , 300)
xx = random.randint(0, 500)
player  = tk.Label(root , bg= "Red" , fg = "Red" , width = 5, height = 2 )
player.place(x = xx , y = yx )

def checkcol():
		xx = random.randint(0, 800)
		xy = random.randint(0, 800)
		player.place(x=xx , y = xy)
	



def check():
	global score
	px = player.winfo_x()
	py =player.winfo_y()
	pw =player.winfo_width()
	ph = player.winfo_height()
	bx =square.winfo_x()
	by =square.winfo_y()
	bw = square.winfo_width()
	bh = square.winfo_width()
	if (px < bx + bw and px + pw > bx and py < by + bh and py + ph > by):
		checkcol()
		score += 1
		label.config(text=f"{score}")
		
	else:
		square.config(bg = "blue")
			
	
def move():
	global direction 
	direction = "right"

def moveleft():
	global direction 
	direction = "left"
	
def moveup():
	
	global direction 
	direction = "up"

def movedown():
	global direction 
	direction = "down"



btn1 = tk.Button(root , text="▶" , command = move)
btn1.grid(row=2 , column = 3)

btn2 = tk.Button(root , text="◀" , command = moveleft)
btn2.grid(row=2 , column = 2)

btn3 = tk.Button(root , text="▲" , command = moveup)
btn3.grid(row=3, column = 4)

btn4 = tk.Button(root , text="▼" , command = movedown)
btn4.grid(row=4 , column = 4)


#def calc():
#	result = eval(screen.get())
#	screen.delete(0 , tk.END)
#	screen.insert(tk.END , result)
#def u_time():
#	ctime = time.strftime("%I:%M:%S")
#	label.config(text = ctime)
#	root.after(1000 , u_time)
#u_time()	

#def click(val):
#    if val == "=":
#    	calc()
#    elif val == "AC":
#    	screen.delete(0 , tk.END)
#    elif val == "b":
#    	screen.delete( len(screen.get()) -1 , tk.END)
#    else:
#	    screen.insert(tk.END, val)
#    
#    
#buttons = ["1" , "2" , "3" , "+" , 
#"4" , "5" , "6" , "-", 
#"7" , "8" , "9" , "*",
#"0" , "/" , "=" , "AC" , "b"]




#row = 1
#col = 0
#for b in buttons:
#	tk.Button(root , text = b , command=lambda x=b: click(x)).grid(row=row , column=col , sticky = "ew")
#	col += 1
#	if col > 3:
#		col = 0
#		row+= 1

loop()

root.mainloop()