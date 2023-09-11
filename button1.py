from tkinter import *

window =Tk()

# 공백 넣기
bl1 = Label(window, text=" ")
bl1.grid(row=1, column=0)  
bl2 = Label(window, text=" ")
bl2.grid(row=1, column=2)  
bl3 = Label(window, text=" ")
bl3.grid(row=1, column=4)  
bl4 = Label(window, text=" ")
bl4.grid(row=0, column=0) 
bl5 = Label(window, text=" ")
bl5.grid(row=2, column=4) 

# 문자 넣기
b1 = Button(window, text="Shin heeyoun")
b2 = Button(window, text="60172166")
# 위치 고정
b1.grid(row=1, column=1)
b2.grid(row=1, column=3)

window.mainloop()

