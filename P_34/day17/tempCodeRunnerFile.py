btn = 1
for i in range(1,4): # 1,2,3
    for j in range(1,4): # 1,2,3
        # tkinter.Button(root,text=f"{btn}",command=lambda x = btn : button_pressed(x)).grid(row=i,column=j)
        btn = btn + 1  # btn +=1
        print(i,j)
print(10*'-')
btn = 0
for i in range(3,5): # 1,2,3
    for j in range(1,5): # 1,2,3
        # tkinter.Button(root,text=f"{operators[btn]}",command=lambda x = operators[btn] : button_pressed(x)).grid(column=i,row=j)
        print(j,i)
        btn = btn + 1 