from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    # print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())            
        scvalue.set(value)    
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("320x580")
root.title("Calculator - MR")
# root.wm_iconbitmap("calc.ico")

# String varable 
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 35 bold")
screen.pack(fill=X, ipadx=8, padx=10, pady=10 )

# Binding buttons in the frame 
f = Frame(root, bg="grey")
f.pack()
b = Button(f, text="9", padx=22, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=22, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=22, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f = Frame(root, bg="grey")
f.pack()
b = Button(f, text="6", padx=22, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=22, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=22, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f = Frame(root, bg="grey")
f.pack()
b = Button(f, text="3", padx=22, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=22, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=22, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f = Frame(root, bg="grey")
f.pack()
b = Button(f, text="0", padx=22, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=22, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=22, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f = Frame(root, bg="grey")
f.pack()
b = Button(f, text="*", padx=22, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=22, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="C", padx=22, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f = Frame(root, bg="grey")
f.pack()
b = Button(f, text="-", padx=22, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=22, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=22, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

root.mainloop()