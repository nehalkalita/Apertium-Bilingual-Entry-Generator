# GUI program for a personalised bidix builder

import os
import sys
from tkinter import *
from tkinter import filedialog as fd
import tkinter.font as font

import process_bidix_entries2 as pbe
import webbrowser

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def change_text_1():
    foldername = fd.askdirectory(parent=root) #entry_out.get()
    entry_out.delete(0,END)
    entry_out.insert(0,foldername)

def change_text_2():
    filename = fd.askopenfilename(parent=root, filetypes=[('Text files', ['*.txt', '*.TXT']),('All files', '*'),])
    entry_pdm.delete(0,END)
    entry_pdm.insert(0,filename)

def submit1_a():
    msg_rtn = pbe.process_entries(int(CB1_var.get()), int(CB2_var.get()), entry_out.get(), entry_pdm.get(), L_entry_1.get("1.0","end-1c"), L_entry_2.get("1.0","end-1c"))
    if msg_rtn[1] == 0:
        color_msg = 'blue'
    elif msg_rtn[1] == 1:
        color_msg = '#005000'
    else:
        color_msg = 'red'
    status.configure(fg=color_msg, text='STATUS:  ' + msg_rtn[0])

def ExitWin():
    #sys.exit()
    root.destroy()
    
def OpenContact():
    stem1 = Toplevel() #Tk()
    stem1.geometry('300x130')
    stem1.title("Contact Us")
    stem1.iconbitmap(resource_path("logo.ico"))
    stem1.resizable(0,0)
    
    temp1 = "\nNehal Kalita \nnehalkalita94@gmail.com \n\n\nAnnie Rajan \nann_raj_2000@yahoo.com"
    Label(stem1, text =temp1).pack()

def Settings():
    stem1 = Toplevel() #Tk()
    stem1.geometry('400x140')
    stem1.title("Settings")
    stem1.iconbitmap(resource_path("logo.ico"))
    stem1.resizable(0,0)

    check_button1 = Checkbutton(stem1, text="Generate new output files", variable=CB1_var)
    check_button1.place(relx=0.16, rely=0.15)
    check_button2 = Checkbutton(stem1, text="Avoid default grammar format for LSX entries", variable=CB2_var)
    check_button2.place(relx=0.16, rely=0.50)

def Delete_duplicate():
    msg_rtn = pbe.delete_duplicate(entry_out.get())
    if msg_rtn[1] == 0:
        color_msg = 'blue'
    elif msg_rtn[1] == 1:
        color_msg = '#005000'
    else:
        color_msg = 'red'
    status.configure(fg=color_msg, text='STATUS:  ' + msg_rtn[0])
    return

def Tutorial():
    webbrowser.open_new(r"https://www.youtube.com/watch?v=Rj8smi4btDI")
    return

root = Tk()
root.geometry('854x480') #'1280x720'
root.title("ABEG")
#root.resizable(0,0)
#root.iconbitmap(resource_path("word_type/logo.ico"))
root.iconbitmap(resource_path("logo.ico"))
size_10 = font.Font(size=10)
size_11 = font.Font(size=11)

CB1_var = IntVar()
CB2_var = IntVar()

frame1 = Frame(root, bg='#aaaaaa', bd=5)
#frame1.place(relx=0.499, rely=0.02, relwidth=0.98, relheight=0.3, anchor='n')
frame1.place(relx=0.499, rely=0.02, relwidth=0.98, relheight=0.218, anchor='n')

menubar = Menu(root)
option1 = Menu(menubar, tearoff = 0)
menubar.add_cascade(label= 'Options', menu = option1)
option1.add_command(label= 'Settings', command = Settings)
option1.add_separator()
option1.add_command(label= 'Delete Duplicates', command = Delete_duplicate)
option1.add_separator()
option1.add_command(label= 'Exit', command = ExitWin)
help1 = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Help', menu = help1)
help1.add_command(label= 'Tutorial', command = Tutorial)
help1.add_separator()
help1.add_command(label= 'Contact Us', command = OpenContact)
root.config(menu= menubar)

button_out = Button(root, text="Output directory", font=size_10, height=1, width=15, bg='#cacaca', command=lambda:change_text_1())
button_out.place(relx=0.037, rely=0.05, relwidth=0.17)
entry_out = Entry(root, font=size_10)
entry_out.place(relx=0.24, rely=0.055, relwidth=0.73)

button_pdm = Button(root, text="Paradigm file", font=size_10, height=1, width=15, bg='#cacaca', command=lambda:change_text_2())
button_pdm.place(relx=0.037, rely=0.15, relwidth=0.17)
entry_pdm = Entry(root, font=size_10)
entry_pdm.place(relx=0.24, rely=0.155, relwidth=0.73)
#entry_pdm.place(relx=0.21, rely=0.155, relwidth=0.75)

button_s = Button(root, text="Submit", font=size_10, height=1, width=10, bg='#cacaca', command=lambda:submit1_a())
button_s.place(relx=0.86, rely=0.885, relwidth=0.11)

"""def Scankey(event):
	val = event.widget.get()
	#print(val)
	if val == '':
		data = list
	else:
		data = []
		for item in list:
			if val.lower() in item.lower():
				data.append(item)
	Update(data)

def Update(data):
	listbox.delete(0, 'end')
	# put new data
	for item in data:
		listbox.insert('end', item)

list = ('n','adj','adv',
	'prn','vblex','vbser',
	'm','f','nt','sg','pl','dc',
    'oc','obl','nom')

entry = Entry(root)
entry.place(relx=0.21, rely=0.2, relwidth=0.1)
entry.bind('<KeyRelease>', Scankey)

listbox = Listbox(root, selectmode=SINGLE)
listbox.place(relx=0.21, rely=0.23, relwidth=0.1)
Update(list)

def b1():
    print('value: ', RB_var1.get())
    
def b2():
    print('value: ', RB_var2.get())"""

l_font = font.Font(size=11, weight='bold')
label_l1 = Label(root, text='Language 1', font=l_font, justify= LEFT)
label_l1.place(relx=0.2, rely=0.28)
label_l2 = Label(root, text='Language 2', font=l_font, justify= LEFT)
label_l2.place(relx=0.7, rely=0.28)
status = Label(root, fg='blue', text='STATUS:  No data entered')
status.place(relx=0.035, rely=0.89)

"""RB_var1 = IntVar()
RB_var2 = IntVar()
RB_var1.set(1)
RB_var2.set(3)
button1_a = Radiobutton(root, text="dix", font=size_10, height=1, width=17,  value=1, variable=RB_var1, command=lambda:b1()) #, command=lambda:hide1_b()
button1_a.place(relx=0.01, rely=0.45)
button1_b = Radiobutton(root, text="lsx", font=size_10, height=1, width=17,  value=2, variable=RB_var1, command=lambda:b1()) #, command=lambda:hide1_b()
button1_b.place(relx=0.14, rely=0.45)
button2_a = Radiobutton(root, text="dix", font=size_10, height=1, width=17,  value=3, variable=RB_var2, command=lambda:b2()) #, command=lambda:hide1_b()
button2_a.place(relx=0.51, rely=0.45)
button2_b = Radiobutton(root, text="lsx", font=size_10, height=1, width=17,  value=4, variable=RB_var2, command=lambda:b2()) #, command=lambda:hide1_b()
button2_b.place(relx=0.64, rely=0.45)"""

text_scroll_1h = Scrollbar(root, orient = HORIZONTAL)
text_scroll_1h.place(relx=0.005, rely=0.815, relwidth=0.468)
text_scroll_1v = Scrollbar(root, orient = VERTICAL)
text_scroll_1v.place(relx=0.465, rely=0.338, relheight=0.482)
L_entry_1 = Text(root, xscrollcommand=text_scroll_1h.set, yscrollcommand=text_scroll_1v.set, wrap="none") # Entry for 1st language
L_entry_1.place(relx=0.014, rely=0.35, relwidth=0.45, relheight=0.45)
text_scroll_1h.config(command = L_entry_1.xview)
text_scroll_1v.config(command = L_entry_1.yview)

text_scroll_2h = Scrollbar(root, orient = HORIZONTAL)
text_scroll_2h.place(relx=0.508, rely=0.815, relwidth=0.468)
text_scroll_2v = Scrollbar(root, orient = VERTICAL)
text_scroll_2v.place(relx=0.967, rely=0.338, relheight=0.482)
L_entry_2 = Text(root, xscrollcommand=text_scroll_2h.set, yscrollcommand=text_scroll_2v.set, wrap="none") # Entry for 1st language
L_entry_2.place(relx=0.515, rely=0.35, relwidth=0.45, relheight=0.45)
text_scroll_2h.config(command = L_entry_2.xview)
text_scroll_2v.config(command = L_entry_2.yview)

root.mainloop()