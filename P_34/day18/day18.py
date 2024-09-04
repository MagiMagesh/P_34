import tkinter

root = tkinter.Tk()
root.title("Calculator")
root.geometry("400x450")

label1 = tkinter.Label(root,text='HH:MM:SS')
label1.pack()

def start(seconds):
    old_data = label1.cget('text')
    new_data  = old_data.split(':') # ['HH','MM','SS']
    new_data[-1] = str(seconds) # ['HH','MM','23']
    label1.config(text=':'.join(new_data))
    seconds = seconds + 1

    root.after(1000,start,seconds) # recursive

tkinter.Button(root,text=f"Start",command=lambda seconds = 0 : start(seconds)).pack()




def stop():
    print('Button Clicked!!!')

button2 = tkinter.Button(root,text="Stop",command=stop)
button2.pack()

def reset():
    print('Button Clicked!!!')

button4 = tkinter.Button(root,text="Reset",command=reset)
button4.pack()




root.mainloop()