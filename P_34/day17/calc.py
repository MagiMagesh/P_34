import tkinter

root = tkinter.Tk()
root.title("Calculator")
root.geometry("400x450")

label1 = tkinter.Label(root,text='')
label1.pack()

def button_pressed(x):
    old_label_data = label1.cget('text') # str
    new_data = old_label_data + str(x)
    label1.config(text=new_data)
    # print(f'button {x} is pressed')

for i in range(10):
    tkinter.Button(root,text=f"{i}",command=lambda x = i : button_pressed(x)).pack()


for i in ['+','-','*','/','=']:
    tkinter.Button(root,text=f"{i}").pack()


# 1. when we press the button
# 2. get the data in the label add new entry

root.mainloop()

def hi(a):
    print('hello',a)

a1 = lambda a = 10 : hi(a)

a1()