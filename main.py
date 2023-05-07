from tkinter import *
import tkinter.messagebox
root=Tk()
root.iconbitmap('C:\\Users\\Dhanwanth R Gowda\\Desktop\\tic tac toe\\tic icon.ico')
root.title("tic tac toe by dhanwanth")
root.resizable(False,False)
click=True
count=0
btn1 =StringVar()
btn2 =StringVar()
btn3 =StringVar()
btn4 =StringVar()
btn5 =StringVar()
btn6 =StringVar()
btn7 =StringVar()
btn8 =StringVar()
btn9 =StringVar()
xphoto = PhotoImage(file='C:\\Users\\Dhanwanth R Gowda\\Desktop\\tic tac toe\\x.png')
ophoto=PhotoImage(file='C:\\Users\\Dhanwanth R Gowda\\Desktop\\tic tac toe\\o.png')
def play():
    but1=Button(root,height=9,width=19,relief='groove',textvariable=btn1,background="#000000",command=lambda :press(1,0,0))
    but1.grid(row=0,column=0)
    but2 = Button(root, height=9, width=19, relief='groove', textvariable=btn2, background="#000000",
                  command=lambda: press(2, 0, 1))
    but2.grid(row=0, column=1)
    but3 = Button(root, height=9, width=19, relief='groove', textvariable=btn3, background="#000000",
                  command=lambda: press(3, 0, 2))
    but3.grid(row=0, column=2)
    but4 = Button(root, height=9, width=19, relief='groove', textvariable=btn4, background="#000000",
                  command=lambda: press(4, 1, 0))
    but4.grid(row=1, column=0)
    but5 = Button(root, height=9, width=19, relief='groove', textvariable=btn5, background="#000000",
                  command=lambda: press(5, 1, 1))
    but5.grid(row=1, column=1)
    but6 = Button(root, height=9, width=19, relief='groove', textvariable=btn6, background="#000000",
                  command=lambda: press(6, 1, 2))
    but6.grid(row=1, column=2)
    but7 = Button(root, height=9, width=19, relief='groove', textvariable=btn7, background="#000000",
                  command=lambda: press(7, 2, 0))
    but7.grid(row=2, column=0)
    but8= Button(root, height=9, width=19, relief='groove', textvariable=btn8, background="#000000",
                  command=lambda: press(8, 2, 1))
    but8.grid(row=2, column=1)
    but9 = Button(root, height=9, width=19, relief='groove', textvariable=btn9, background="#000000",
                 command=lambda: press(9, 2, 2))
    but9.grid(row=2, column=2)




def press(num,r,c):
    global click,count
    if click==True:
        label1=Label(root,image=xphoto)
        label1.grid(row=r,column=c)

        if num==1:
            btn1.set('x')
        elif num==2:
            btn2.set("x")
        elif num==3:
            btn3.set("x")
        elif num==4:
            btn4.set("x")
        elif num==5:
            btn5.set("x")
        elif num==6:
            btn6.set("x")
        elif num==7:
            btn7.set("x")
        elif num==8:
            btn8.set("x")
        else:
            btn9.set("x")


        count+=1
        checkwin()
        click=False
    else:
        label2=Label(root,image=ophoto)
        label2.grid(row=r,column=c)
        if num==1:
            btn1.set("o")
        elif num==2:
            btn2.set("o")
        elif num==3:
            btn3.set("o")
        elif num==4:
            btn4.set("o")
        elif num==5:
            btn5.set("0")
        click=True
        count+=1
        checkwin()



def checkwin():
    global  count,click
    if(btn1.get()=="x"and btn2.get()=='x 'and btn3.get()=='x' or
    btn4.get()=='x'and btn5.get()=='x'and btn6.get()=='x' or
    btn7.get()=='x'and btn9.get()== 'x'and btn8.get()=='x' or
    btn1.get()=='x' and btn4.get()=='x' and btn7.get()=='x' or
    btn5.get()=='x' and btn2.get()=='x' and btn8.get()=='x' or
    btn3.get()=='x' and btn6.get()=='x' and btn9.get()=='x' or
    btn9.get()=='x' and btn5.get()=='x' and btn1.get()=='x' or
    btn3.get()=='x' and btn5.get()=='x' and btn7.get()=='x'):
     tkinter.messagebox.showinfo("tic tac toe",'player x wins')
     click=True
     count=0
     play()
     clear()
    elif (btn1.get()=="o" and btn2.get()=='o ' and btn3.get()=='o' or
        btn4.get()=='o' and btn5.get()=='o' and btn6.get()=='o' or
        btn7.get()=='o' and btn9.get()=='o' and btn8.get()=='o' or
        btn1.get()=='o' and btn4.get()=='o' and btn7.get()=='o' or
        btn5.get()=='o' and btn2.get()=='o' and btn8.get()=='o' or
        btn3.get()=='o' and btn6.get()=='o' and btn9.get()=='o' or
        btn9.get()=='o' and btn5.get()=='o' and btn1.get()=='o' or
        btn3.get()=='o' and btn5.get()=='o' and btn7.get()=='o' ):
          tkinter.messagebox.showinfo("tic tac toe",'player o wins')
          count=0
          click=False
          play()
          clear()


    elif(count ==9):
        tkinter.messagebox.showinfo("tictactoe",'tie')

        count=0
        click=True
        clear()
        play()
def clear():
    btn2.set('')
    btn3.set('')
    btn4.set('')
    btn5.set('')
    btn6.set('')
    btn7.set('')
    btn8.set('')
    btn9.set('')
    btn1.set('')

play()
root.mainloop()

