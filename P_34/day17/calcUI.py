import tkinter

root = tkinter.Tk()
root.title("Calculator")
root.geometry("400x450")

label1 = tkinter.Label(root,text='')
label1.grid(row=0,columnspan=5)

operators = ['C','AC','+','-','*','/','%','//']

def button_pressed(x):
    old_label_data = label1.cget('text') # str
    if str(x) in operators:
        oldl_data_last_ele = old_label_data[-1]
        if oldl_data_last_ele in operators:
            new_data = list(old_label_data)
            new_data[-1] = x
            label1.config(text=''.join(new_data))
            return True
        
    new_data = str(old_label_data) + str(x)
    label1.config(text=new_data)

    
btn = 1
for i in range(1,4): # 1,2,3
    for j in range(3): # 0,1,2
        tkinter.Button(root,text=f"{btn}",command=lambda x = btn : button_pressed(x)).grid(row=i,column=j)
        btn = btn + 1  # btn +=1
        print(i,j)
print(10*'-')
btn = 0
for i in range(3,5): # 3,4
    for j in range(1,5): # 1,2,3,4
        tkinter.Button(root,text=f"{operators[btn]}",command=lambda x = operators[btn] : button_pressed(x)).grid(column=i,row=j)
        print(j,i)
        btn = btn + 1  # btn +=1

root.mainloop()


def hi(a):
    print('hello',a)

a1 = lambda a = 10 : hi(a)

a1()



