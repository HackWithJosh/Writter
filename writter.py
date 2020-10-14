from tkinter import *
import pyautogui
import time
root = Tk()
root.title('Type Writter')
e =Entry(root, width= 50, bg="black", fg="white", borderwidth= 10)
e.pack()
e.insert(0, "")

def myClick():
    try:
        info = e.get()
        time.sleep(5)
        pyautogui.write(info)
        e.delete(0,END)
    except:
        e.delete(0,END)

myButton = Button(root, text="Done", command=myClick)
myButton.pack()
myLabel = Label(root, text="Click a location to type in 5 sec")
myLabel.pack()
root.mainloop()
