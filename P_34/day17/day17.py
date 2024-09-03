import tkinter

root = tkinter.Tk()
root.title("GUVI P34")
root.geometry("400x450")

var1 = tkinter.BooleanVar()
var2 = tkinter.BooleanVar()
var3 = tkinter.BooleanVar()
var4 = tkinter.BooleanVar()

checkbutton1 = tkinter.Checkbutton(root,text='Option1',variable=var1)
checkbutton2 = tkinter.Checkbutton(root,text='Option2',variable=var2)
checkbutton3 = tkinter.Checkbutton(root,text='Option3',variable=var3)
checkbutton4 = tkinter.Checkbutton(root,text='Option4',variable=var4)
checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()
checkbutton4.pack()


def checkbutton():
    print('the user entered multi line data is')
    print(var1.get())
    print(var2.get())
    print(var3.get())
    print(var4.get())

button6 = tkinter.Button(root,text="checkbox check",command=checkbutton)
button6.pack()

root.mainloop()