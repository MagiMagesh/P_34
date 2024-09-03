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

checkbx = tkinter.Button(root,text="checkbox check",command=checkbutton)
checkbx.pack()

var = tkinter.StringVar()
# var.set('Option3')

radiobutton1 = tkinter.Radiobutton(root,text='Option1',variable=var,value='Option1')
radiobutton2 = tkinter.Radiobutton(root,text='Option2',variable=var,value='Option2')
radiobutton3 = tkinter.Radiobutton(root,text='Option3',variable=var,value='Option3')
radiobutton4 = tkinter.Radiobutton(root,text='Option4',variable=var,value='Option4')
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
radiobutton4.pack()

def radiobutton():
    print('the user entered multi line data is')
    print(var.get())

radiobtn = tkinter.Button(root,text="checkbox check",command=radiobutton)
radiobtn.pack()

root.mainloop()