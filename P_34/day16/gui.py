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




root.mainloop()




















