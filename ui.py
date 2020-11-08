from tkinter import * 
from tkinter.ttk import *
import tkinter as tk
from manager import Manager
from fileio import Fileio

# --------------------------------------------------------------- | GLOBALS

BACKGROUND = '#1E1E1E'
LIGHT_ONE = '#252526'
LIGHT_TWO = '#37373D'
LIGHT_THREE = '#333333'
LIGHT_FOUR = '#999999'
FOREGROUND = 'white'
WINDOWSIZE = '1200x600'

Man = Manager()
io = Fileio()

# --------------------------------------------------------------- | BUTTON FUNCTIONS

def pressednewfile():
    consoleoutput("New File Created")
    Man.loaded = []
    Man.generate()
    updateaccountlist()
    accountslist.selection_clear(0, last=len(Man.loaded))

def pressedimportbutton():
    boolean = io.importfile(Man)
    if boolean:
        consoleoutput("File Imported")
        updateaccountlist()

def pressedexporttbutton():
    boolean = io.exportfile(Man)
    if boolean:
        consoleoutput("File Exported")

def pressednewkey():
    Man.generate()
    consoleoutput("New Key Generated")

def pressedcreatebutton():

    accountname = accountnametext.get().upper()
    username = usernametext.get()
    password = passwordtext.get()
    
    if accountname is "" or username is "" or password is "":
        consoleoutput("Cannot Leave Fields Blank")

    else:
        enablebuttons()
        addpanel.pack_forget()
        removebutton.grid_forget()
        Man.loaded.append([accountname, username, password])
        Man.loaded.sort(key=lambda x: x[0])

        accountnametext.delete(0,"end")
        accountnametext.insert(0, "")
        usernametext.delete(0,"end")
        usernametext.insert(0, "")
        passwordtext.delete(0,"end")
        passwordtext.insert(0, "")
        updateaccountlist()

def consoleoutput(sent):
    console['text'] = sent

def pressedcancelbutton():
    enablebuttons()
    accountnametext.delete(0,"end")
    accountnametext.insert(0, "")
    usernametext.delete(0,"end")
    usernametext.insert(0, "")
    passwordtext.delete(0,"end")
    passwordtext.insert(0, "")

    addpanel.pack_forget()
    removebutton.grid_forget()

def pressedaddbutton():
    disablebuttons()
    addpanel.pack()
    consoleoutput("")
    createbutton["command"] = pressedcreatebutton
    createbutton["text"] = "[ Create ]"

def pressededitbutton():
    consoleoutput("")
    if accountslist.curselection() == ():
        return
    else:
        index = accountslist.curselection()[0]
        disablebuttons()
        addpanel.pack()
        removebutton.grid(row=4, column=1, padx=20, pady=50)

        createbutton["text"] = "[ Edit ]"
        createbutton["command"] = replaceitem

        accountnametext.delete(0,"end")
        usernametext.delete(0,"end")
        passwordtext.delete(0,"end")
        accountnametext.insert(0, Man.loaded[index][0])
        usernametext.insert(0, Man.loaded[index][1])
        passwordtext.insert(0, Man.loaded[index][2])

def replaceitem():
    index = accountslist.curselection()[0]
    Man.loaded[index][0] = accountnametext.get()
    Man.loaded[index][1] = usernametext.get()
    Man.loaded[index][2] = passwordtext.get()
    Man.loaded.sort(key=lambda x: x[0])
    enablebuttons()
    addpanel.pack_forget()
    removebutton.grid_forget()
    updateaccountlist()

def pressedremovebutton():
    index = accountslist.curselection()[0]
    del Man.loaded[index]
    consoleoutput("Removed Entry")

    enablebuttons()
    addpanel.pack_forget()
    removebutton.grid_forget()
    updateaccountlist()

def pressedgeneratebutton():
    generatedpassword = Man.generatepassword()
    passwordtext.delete(0,"end")
    passwordtext.insert(0, generatedpassword)

def disablebuttons():
    addbutton["state"] = "disabled"
    editbutton["state"] = "disabled"
    newfilebutton["state"] = "disabled"
    importbutton["state"] = "disabled"
    exportbutton["state"] = "disabled"
    newkeybutton["state"] = "disabled"
    accountslist["state"] = "disabled"

def enablebuttons():
    addbutton["state"] = "normal"
    editbutton["state"] = "normal"
    newfilebutton["state"] = "normal"
    importbutton["state"] = "normal"
    exportbutton["state"] = "normal"
    newkeybutton["state"] = "normal"
    accountslist["state"] = "normal"

def updateaccountlist():
    
    accountslist.delete(0, accountslist.size())

    for i in range(0, (len(Man.loaded))):
        accountslist.insert(i, Man.loaded[i][0])

# --------------------------------------------------------------- | MAIN WINDOW

window = tk.Tk()
window.title("Encryption Buddy")
window.iconbitmap('./images/lock.ico')
window.configure(bg=LIGHT_ONE)
window.geometry(WINDOWSIZE)

# --------------------------------------------------------------- | PANELS

north = tk.Frame(master=window, relief=tk.FLAT, background=BACKGROUND, width=500, height=300, borderwidth=0)
north.pack(fill=tk.X, ipadx=200, ipady=10)

west = tk.Frame(master=window, relief=tk.FLAT, background=LIGHT_THREE, width=250, height=100, borderwidth=0)
west.pack(fill=tk.BOTH, side=tk.LEFT, ipadx=25)

center = tk.Frame(master=window, relief=tk.FLAT, background=LIGHT_ONE, width=500, height=1000, borderwidth=0)
center.pack(fill=tk.BOTH)

# --------------------------------------------------------------- | NORTH FRAME

newfileimage = tk.PhotoImage(file = "./images/selectfile.png") 
newfileimage = newfileimage.zoom(5)
newfileimage = newfileimage.subsample(64)
newfilebutton = tk.Button(north, text="Create A New Password File", bg=BACKGROUND, activebackground=BACKGROUND, borderwidth=0, image = newfileimage, command=pressednewfile)
newfilebutton.pack(side=tk.LEFT, ipadx=10)

importimage = tk.PhotoImage(file = "./images/import.png") 
importimage = importimage.zoom(5)
importimage = importimage.subsample(64)
importbutton = tk.Button(north, text="Import A Password File", bg=BACKGROUND, activebackground=BACKGROUND, borderwidth=0, image = importimage, command=pressedimportbutton)
importbutton.pack(side=tk.LEFT, ipadx=10)

exportimage = tk.PhotoImage(file = "./images/export.png") 
exportimage = exportimage.zoom(5)
exportimage = exportimage.subsample(64)
exportbutton = tk.Button(north, text="Export Work Area", bg=BACKGROUND, activebackground=BACKGROUND, borderwidth=0, image = exportimage, command=pressedexporttbutton)
exportbutton.pack(side=tk.LEFT, ipadx=10)

keyimage = tk.PhotoImage(file = "./images/newkey.png") 
keyimage = keyimage.zoom(5)
keyimage = keyimage.subsample(64)
newkeybutton = tk.Button(north, text="Generate New Key", bg=BACKGROUND, activebackground=BACKGROUND, borderwidth=0, image = keyimage, command=pressednewkey)
newkeybutton.pack(side=tk.LEFT, ipadx=10)

console = tk.Label(north, font=("Arial Bold", 20), text="", bg=BACKGROUND, activebackground=BACKGROUND, fg=FOREGROUND, activeforeground=FOREGROUND, borderwidth=0)
console.pack(side=tk.LEFT, ipadx=10)

# --------------------------------------------------------------- | WEST FRAME

cardsbutton = tk.Button(west, text="Accounts", font=("Arial Bold", 20), bg=LIGHT_THREE, activebackground=LIGHT_THREE, fg=FOREGROUND, activeforeground=FOREGROUND, borderwidth=0)
cardsbutton.pack(side=tk.TOP, padx=10, pady=10)

            # --------------------------------------------------- | CENTER BUTTON FRAME

centerwest = tk.Frame(master=west, relief=tk.FLAT, background=LIGHT_THREE, width=250, height=775, borderwidth=0)
centerwest.pack(fill=tk.BOTH, expand=True)

accountslist = Listbox(master=centerwest, font=("Arial Bold", 15), relief=tk.FLAT, background=LIGHT_THREE, foreground=FOREGROUND, 
    selectmode=tk.SINGLE, selectbackground=LIGHT_ONE, highlightbackground = '#6190FF', exportselection=0, activestyle='none')
accountslist.pack(fill=tk.BOTH, expand=True, ipadx=10)

            # --------------------------------------------------- | BOTTOM BUTTON FRAME

buttonframe = tk.Frame(master=west, relief=tk.FLAT, background=BACKGROUND, width=250, height=20, borderwidth=0)
buttonframe.pack(fill=tk.BOTH, side=tk.BOTTOM)

addimage = tk.PhotoImage(file = "./images/add.png") 
addimage = addimage.zoom(5)
addimage = addimage.subsample(64)
addbutton = tk.Button(buttonframe, text="Add", bg=BACKGROUND, activebackground=BACKGROUND, borderwidth=0, image = addimage, command=pressedaddbutton)
addbutton.pack(side=tk.LEFT, padx=20, pady=20, expand=True)

editimage = tk.PhotoImage(file = "./images/edit.png") 
editimage = editimage.zoom(10)
editimage = editimage.subsample(128)
editbutton = tk.Button(buttonframe, text="Remove", bg=BACKGROUND, activebackground=BACKGROUND, borderwidth=0, image = editimage, command=pressededitbutton)
editbutton.pack(side=tk.RIGHT, padx=20, pady=20, expand=True)

# --------------------------------------------------------------- | CENTER ACCOUNTS FRAME

addpanel = tk.Frame(master=center, relief=tk.FLAT, background=LIGHT_ONE, width=750, height=250, borderwidth=0)

accountnamelabel = tk.Label(addpanel, font=("Arial Bold", 20), text="Account Name", bg=LIGHT_ONE, activebackground=LIGHT_ONE, fg=FOREGROUND, activeforeground=FOREGROUND, borderwidth=0)
accountnamelabel.grid(row=0, column=0, padx=5, pady=20)

usernamelabel = tk.Label(addpanel, font=("Arial Bold", 20), text="Username", bg=LIGHT_ONE, activebackground=LIGHT_ONE, fg=FOREGROUND, activeforeground=FOREGROUND, borderwidth=0)
usernamelabel.grid(row=1, column=0, padx=5, pady=20)

passwordlabel = tk.Label(addpanel, font=("Arial Bold", 20), text="Password", bg=LIGHT_ONE, activebackground=LIGHT_ONE, fg=FOREGROUND, activeforeground=FOREGROUND, borderwidth=0)
passwordlabel.grid(row=2, column=0, padx=5, pady=20)

accountnametext = tk.Entry(addpanel, font=("Arial Bold", 15), text="1", bg=BACKGROUND, fg=FOREGROUND, borderwidth=0, width=30, justify='center')
accountnametext.grid(row=0, column=1, ipadx=15, ipady=15, padx=20)

usernametext = tk.Entry(addpanel, font=("Arial Bold", 15), text="2", bg=BACKGROUND, fg=FOREGROUND, borderwidth=0, width=30, justify='center')
usernametext.grid(row=1, column=1, ipadx=15, ipady=15, padx=20)

passwordtext = tk.Entry(addpanel, font=("Arial Bold", 15), text="3", bg=BACKGROUND, fg=FOREGROUND, borderwidth=0, width=30, justify='center')
passwordtext.grid(row=2, column=1, ipadx=15, ipady=15, padx=20)

cancelbutton = tk.Button(addpanel, font=("Arial Bold", 20), text="[ Cancel ]", bg=LIGHT_ONE, activebackground=LIGHT_ONE, fg='#E20000', activeforeground=FOREGROUND, borderwidth=0, command=pressedcancelbutton)
cancelbutton.grid(row=3, column=0, padx=20, pady=10)

generatebutton = tk.Button(addpanel, font=("Arial Bold", 20), text=" [ Generate A Password ]", bg=LIGHT_ONE, activebackground=LIGHT_ONE, fg='#6190FF', activeforeground=FOREGROUND, 
borderwidth=0, padx=10, pady=10, command=pressedgeneratebutton)
generatebutton.grid(row=3, column=1)

removebutton = tk.Button(addpanel, font=("Arial Bold", 20), text="[ Remove Entry ]", bg=LIGHT_ONE, activebackground=LIGHT_ONE, fg=LIGHT_FOUR, activeforeground=FOREGROUND, borderwidth=0, command=pressedremovebutton)

createbutton = tk.Button(addpanel, font=("Arial Bold", 20), text="[ Create ]", bg=LIGHT_ONE, activebackground=LIGHT_ONE, fg='#1ED760', activeforeground=FOREGROUND, borderwidth=0, command=pressedcreatebutton)
createbutton.grid(row=3, column=2, padx=20, pady=10)

# --------------------------------------------------------------- | RUN

window.mainloop()
