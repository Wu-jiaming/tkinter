import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry("500x250")

l = tk.Label(window,
             text='this is tk',
             bg='green',
             font=('Arial',12),
             width=25,height=5)

var = tk.StringVar()#这是文字变量存储器
l2 = tk.Label(window,
              textvariable=var,#使用textvariable替换，因为这个可以变化
              bg='blue',font=('Arial',12), width=35, height=7)
l2.pack()

on_click= False
s1 = "you click successful"
def click(s1):
    global on_click
    if on_click == False:
        on_click = True
        var.set(s1)
    else:
        on_click = False
        var.set('')

#button
b = tk.Button(window,
              text='click',
              width=15,height=5,
              #command传递参数，不能直接放参数,command=click(s1),如果这样，会直接执行该方法，不会等待触发
              command=lambda :click(s1))
b.pack()



window.mainloop()