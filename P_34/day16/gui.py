# GUI - Graphical User Interface


import tkinter

root = tkinter.Tk()

root.title("GUVI P34")
root.geometry("500x550")

# widgets:

# 1. label
# 2. button
# 3. entry    - single line input
# 4. text     - multi line input
# 5. checkboxbutton
# 6. radio
# 7. list

label1 = tkinter.Label(root,text='P34 Folder')
label1.pack()

label2 = tkinter.Label(root,text='Enter your name')
label2.pack()


entry1 = tkinter.Entry(root,width=30)
entry1.pack()


text1 = tkinter.Text(root,height=5,width=30)
text1.pack()


button1 = tkinter.Button(root,text="Submit")
button1.pack()

def trigger():
    print('Button Clicked!!!')

button2 = tkinter.Button(root,text="Command",command=trigger)
button2.pack()

print('text present in label 1')
print(label1.cget('text'))

label2.config(text='Hello P34!.')


def pushbutton():
    # label1.config(text='Hello Magesh')
    user_input = input("Enter any input to get displayed: ")
    label1.config(text=user_input)

button2 = tkinter.Button(root,text="Push",command=pushbutton)
button2.pack()

def enter():
    inp = entry1.get()
    print('the user entered data is')
    print(inp)

button3 = tkinter.Button(root,text="Enter",command=enter)
button3.pack()

def entertext():
    multi_lin_inp = text1.get('1.0',tkinter.END)
    print('the user entered multi line data is')
    print(multi_lin_inp)

button4 = tkinter.Button(root,text="Enter Text",command=entertext)
button4.pack()

def insertentry():
    multi_lin_inp = entry1.insert(0,'Some thing which is Good')
    print('the user entered multi line data is')
    print(multi_lin_inp)

button5 = tkinter.Button(root,text="Insert Entry",command=insertentry)
button5.pack()

def inserttext():
    multi_lin_inp = text1.insert("1.0",'Some thing which is Good\n')
    print('the user entered multi line data is')
    print(multi_lin_inp)

button6 = tkinter.Button(root,text="Insert Text",command=inserttext)
button6.pack()

def deleteentry():
    multi_lin_inp = entry1.delete(0,tkinter.END)
    print('the user entered multi line data is')
    print(multi_lin_inp)

button7 = tkinter.Button(root,text="Delete Entry",command=deleteentry)
button7.pack()

root.mainloop()




















