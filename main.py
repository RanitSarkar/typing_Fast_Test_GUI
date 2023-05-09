# libraries
from tkinter import *
from tkinter.ttk import Combobox
import requests
import time
import pyglet
pyglet.font.add_file("Audiowide/Audiowide-Regular.ttf")

numberofwords=[10,20,30,40,50,60,70,80,90,100]
mins = 0
secs = 0
hours = 0
vlist = ["1","2","3","4","5","6","7","8","9","10"]
text_sentence=""

root=Tk()
root.title("Typing speed test")
root.geometry("490x650")
root.config(padx=15,bg="blue")
root.resizable(False,False)


# get sentence random
def sentence():
	global text_sentence
	if Combo.get() == "1":
		number_words = numberofwords[0]
	elif Combo.get() == "2":
		number_words = numberofwords[1]
	elif Combo.get() == "3":
		number_words = numberofwords[2]
	elif Combo.get() == "4":
		number_words = numberofwords[3]
	elif Combo.get() == "5":
		number_words = numberofwords[4]
	elif Combo.get() == "6":
		number_words = numberofwords[5]
	elif Combo.get() == "7":
		number_words = numberofwords[6]
	elif Combo.get() == "8":
		number_words = numberofwords[7]
	elif Combo.get() == "9":
		number_words = numberofwords[8]
	elif Combo.get() == "10":
		number_words = numberofwords[9]
	else:
		number_words=numberofwords[1]
	url = f"https://random-word-api.herokuapp.com/word?number={number_words}"
	response = requests.get(url)
	sentence_word = response.json()
	text_sentence = ' '.join(sentence_word)


running = BooleanVar(value=False)
start_time = DoubleVar(value=0.0)
elapsed_time = DoubleVar(value=0.0)
time_str = StringVar(value="00:00:00.00")


def update_time_label():
	global mins,secs
	if running.get():
		elapsed_time.set(time.time() - start_time.get())
		hours, rem = divmod(elapsed_time.get(), 3600)
		mins, secs = divmod(rem, 60)
		time_str.set(f"{int(hours):02d}:{int(mins):02d}:{secs:05.2f}")
	if running.get():
		root.after(10, update_time_label)


def start():
	global text_sentence
	start_time.set(time.time())
	running.set(True)
	update_time_label()
	textbox.delete(1.0, END)
	sentence()
	textbox.insert('end', f'{text_sentence}')



def stop():
	running.set(False)

def reset():
	global mins, secs
	hours= 0
	mins = 0
	secs = 0
	textbox.delete(1.0, END)
	time_str.set(f"{int(hours):02d}:{int(mins):02d}:{secs:05.2f}")

def check():
	entryvalue=entrybox.get("1.0", END)
	print(entryvalue)


heading=Label(text="Show how fast you are..!!",font=('Audiowide',30),pady=10,bg="blue")
time_label=Label( textvariable=time_str,bg="blue",font=('Audiowide',20))
frame = Frame(root,bg="blue")
Combo = Combobox(frame, values=vlist,)
Combo.set("Pick the level")
Combo.grid(padx=5, pady=5)
textbox = Text(root, height = 20, width = 52, padx=20)
textbox.insert('end', 'your text will appear here')
# textbox incopyable
textbox.bind('<Control-v>', lambda _:'break')
textbox.bind('<Control-c>', lambda _:'break')
entrybox = Text(root, width=52, height=5, padx=20)
# buttons
start_button = Button(root,text="start", padx=20, command=start)
end_button = Button(root, text="end", padx=20, command=stop)
reset_button = Button(root, text="reset", padx=20, command=reset)



heading.grid(row=0,column=0,columnspan=3)
time_label.grid(row=1, column=0)
frame.grid(row=1, column=2)
textbox.grid(row=2, column=0, columnspan=3, pady=20)
entrybox.grid(row=3, column=0, columnspan=3)
start_button.grid(row=4, column=0, padx=20, pady=20)
end_button.grid(row=4, column=2,padx=20,pady=20)
reset_button.grid(row=4, column=1,padx=20,pady=20)



root.mainloop()
