#importing the modoule
from tkinter import*
import ttkbootstrap as ttk
#making the window 
x = ttk.Window(themename = 'vapor')
x.geometry('1120x300')
x.title('Binary visualizer and binary converter by Dihad(max: 4095)')
#s vareables
s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0
s7 = 0
s8 = 0
s9 = 0
s10 = 0
s11 = 0
s12 = 0
#n vareabl
n1 =0
n2 =0
n3 =0
n4 =0
n5 =0
n6 =0
n7 =0
n8 =0
n9 =0
n10 =0
n11 =0
n12 =0
def c():

    num = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12
    vew_label.config(text=num)
#c
def c1():
    global s1
    global n1
    if s1 == 0:
        b1.config(text="1")
        l1.config(text="1")
        n1 = 1
        s1 = 1
        c()
    else:
        b1.config(text="0")
        l1.config(text="0")
        n1 = 0
        s1 = 0
        c()
def c2():
    global s2
    global n2
    if s2 == 0:
        b2.config(text="1")
        l2.config(text="2")
        n2 = 2
        s2 = 1
        c()
    else:
        b2.config(text="0")
        l2.config(text="0")
        n2 = 0
        s2 = 0
        c()
def c3():
    global s3
    global n3
    if s3 == 0:
        b3.config(text="1")
        l3.config(text="4")
        n3 = 4
        s3 = 1
        c()
    else:
        b3.config(text="0")
        l3.config(text="0")
        n3 = 0
        s3 = 0
        c()
def c4():
    global s4
    global n4
    if s4 == 0:
        b4.config(text="1")
        l4.config(text="8")
        n4 = 8
        s4 = 1
        c()
    else:
        b4.config(text="0")
        l4.config(text="0")
        n4 = 0
        s4 = 0
        c()
def c5():
    global s5
    global n5
    if s5 == 0:
        b5.config(text="1")
        l5.config(text="16")
        n5 = 16
        s5 = 1
        c()
    else:
        b5.config(text="0")
        l5.config(text="0")
        n5 = 0
        s5 = 0
        c()
def c6():
    global s6
    global n6
    if s6 == 0:
        b6.config(text="1")
        l6.config(text="32")
        n6 = 32
        s6 = 1
        c()
    else:
        b6.config(text="0")
        l6.config(text="0")
        n6 = 0
        s6 = 0
        c()
def c7():
    global s7
    global n7
    if s7 == 0:
        b7.config(text="1")
        l7.config(text="64")
        n7 = 64
        s7 = 1
        c()
    else:
        b7.config(text="0")
        l7.config(text="0")
        n7 = 0
        s7 = 0
        c()
def c8():
    global s8
    global n8
    if s8 == 0:
        b8.config(text="1")
        l8.config(text="128")
        n8 = 128
        s8 = 1
        c()
    else:
        b8.config(text="0")
        l8.config(text="0")
        n8 = 0
        s8 = 0
        c()
def c9():
    global s9
    global n9
    if s9 == 0:
        b9.config(text="1")
        l9.config(text="256")
        n9 = 256
        s9 = 1
        c()
    else:
        b9.config(text="0")
        l9.config(text="0")
        n9 = 0
        s9 = 0
        c()
def c10():
    global s10
    global n10
    if s10 == 0:
        b10.config(text="1")
        l10.config(text="512")
        n10 = 512
        s10 = 1
        c()
    else:
        b10.config(text="0")
        l10.config(text="0")
        n10 = 0
        s10 = 0
        c()
def c11():
    global s11
    global n11
    if s11 == 0:
        b11.config(text="1")
        l11.config(text="1024")
        n11 = 1024
        s11 = 1
        c()
    else:
        b11.config(text="0")
        l11.config(text="0")
        n11 = 0
        s11 = 0
        c()
def c12():
    global s12
    global n12
    if s12 == 0:
        b12.config(text="1")
        l12.config(text="2048")
        n12 = 2048
        s12 = 1
        c()
    else:
        b12.config(text="0")
        l12.config(text="0")
        n12 = 0
        s12 = 0
        c()
#dbnt
def dntb():
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    global s7
    global s8
    global s9
    global s10
    global s11
    global s12
    num  = int(num_entry.get())
    if num <4096:
     eror_label.config(text="intger to binary(under:4096)")
     num = bin(num)[2:]
     len1 = len(num)
     rnum = num[::-1]
     for i in range(12-len1):
        rnum = rnum+'0'
     lnum= rnum[::-1]
     nl1=lnum[-1]
     nl2=lnum[-2]
     nl3=lnum[-3]
     nl4=lnum[-4]
     nl5=lnum[-5]
     nl6=lnum[-6]
     nl7=lnum[-7]
     nl8=lnum[-8]
     nl9=lnum[-9]
     nl10=lnum[2]
     nl11=lnum[1]
     nl12=lnum[-0]
     if nl1 == "0":
        if s1 == 1:
            c1()
     if nl1 == "1":
        if s1 == 0:
            c1()
     if nl2 == "0":
        if s2 == 1:
            c2()
     if nl2 == "1":
        if s2 == 0:
            c2()
     if nl3 == "0":
        if s3 == 1:
            c3()
     if nl3 == "1":
        if s3 == 0:
            c3()
     if nl4 == "0":
        if s4 == 1:
            c4()
     if nl4 == "1":
        if s4 == 0:
            c4()
     if nl5 == "0":
        if s5 == 1:
            c5()
     if nl5 == "1":
        if s5 == 0:
            c5()
     if nl6 == "0":
        if s6 == 1:
            c6()
     if nl6 == "1":
        if s6 == 0:
            c6()
     if nl7 == "0":
        if s7 == 1:
            c7()
     if nl7 == "1":
        if s7 == 0:
            c7()
     if nl8 == "0":
        if s8 == 1:
            c8()
     if nl8 == "1":
        if s8 == 0:
            c8()
     if nl9 == "0":
        if s9 == 1:
            c9()
     if nl9 == "1":
        if s9 == 0:
            c9()
     if nl10 == "0":
        if s10 == 1:
            c10()
     if nl10 == "1":
        if s10 == 0:
            c10()
     if nl11 == "0":
        if s11 == 1:
            c11()
     if nl11 == "1":
        if s11 == 0:
            c11()
     if nl12 == "0":
        if s12 == 1:
            c12()
     if nl12 == "1":
        if s12 == 0:
            c12()
    else:
        eror_label.config(text="you have put over 4096")
#buttons
b1 =ttk.Button(x, text = '    0',command=c1)
b2 =ttk.Button(x, text = '    0',command=c2)
b3 =ttk.Button(x, text = '    0',command=c3)
b4 =ttk.Button(x, text = '    0',command=c4)
b5 =ttk.Button(x, text = '    0',command=c5)
b6 =ttk.Button(x, text = '    0',command=c6)
b7 =ttk.Button(x, text = '    0',command=c7)
b8 =ttk.Button(x, text = '    0',command=c8)
b9 =ttk.Button(x, text = '    0',command=c9)
b10 =ttk.Button(x, text = '    0',command=c10)
b11 =ttk.Button(x, text = '    0',command=c11)
b12 =ttk.Button(x, text = '    0',command=c12)
#other widget
dntb_button =ttk.Button(x, text = 'Display\nin\nbinary',command=dntb)
eror_label = ttk.Label(x, text = 'intger to binary(under:4096)')
line_label = ttk.Label(x, text = '|\n|\n|\n|\n|\n|')
vew_label =ttk.Label(x, text = '0',font="Arial 42")
number_label =ttk.Label(x, text = 'number:',font="Arial 42")
num_entry = Entry(x)
#byte label
byte1_label = ttk.Label(x, text = '    1.5 byte',font="Arial 32")
byte2_label = ttk.Label(x, text = '    1.0 byte',font="Arial 32")
byte3_label = ttk.Label(x, text = '    0.5 byte',font="Arial 32")
#labels
l1 =ttk.Label(x, text = '0')
l2 =ttk.Label(x, text = '0')
l3 =ttk.Label(x, text = '0')
l4 =ttk.Label(x, text = '0')
l5 =ttk.Label(x, text = '0')
l6 =ttk.Label(x, text = '0')
l7 =ttk.Label(x, text = '0')
l8 =ttk.Label(x, text = '0')
l9 =ttk.Label(x, text = '0')
l10 =ttk.Label(x, text = '0')
l11 =ttk.Label(x, text = '0')
l12 =ttk.Label(x, text = '0')
#bit label
bit1 =ttk.Label(x, text = '-bits-',font="Arial 22")
bit2 =ttk.Label(x, text = '-bits-',font="Arial 22")
#normal label
n1_label =ttk.Label(x, text = '-normal-',font="Arial 11")
n2_label =ttk.Label(x, text = '-normal-',font="Arial 11")
#configure grid
x.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13), weight = 1, uniform = 'a')
x.rowconfigure((0,1,2,3), weight = 2, uniform = 'a')
#placeing buttons on grid
b1.grid(row = 1, column = 13, sticky = 'nsew')
b2.grid(row = 1, column = 12, sticky = 'nsew')
b3.grid(row = 1, column = 11, sticky = 'nsew')
b4.grid(row = 1, column = 10, sticky = 'nsew')
b5.grid(row = 1, column = 8, sticky = 'nsew')
b6.grid(row = 1, column = 7, sticky = 'nsew')
b7.grid(row = 1, column = 6, sticky = 'nsew')
b8.grid(row = 1, column = 5, sticky = 'nsew')
b9.grid(row = 1, column = 3, sticky = 'nsew')
b10.grid(row = 1, column = 2, sticky = 'nsew')
b11.grid(row = 1, column = 1, sticky = 'nsew')
b12.grid(row = 1, column = 0, sticky = 'nsew')
#placeing labels on grid
l1.grid(row = 2, column = 13, sticky = 'nsew')
l2.grid(row = 2, column = 12, sticky = 'nsew')
l3.grid(row = 2, column = 11, sticky = 'nsew')
l4.grid(row = 2, column = 10, sticky = 'nsew')
l5.grid(row = 2, column = 8, sticky = 'nsew')
l6.grid(row = 2, column = 7, sticky = 'nsew')
l7.grid(row = 2, column = 6, sticky = 'nsew')
l8.grid(row = 2, column = 5, sticky = 'nsew')
l9.grid(row = 2, column = 3, sticky = 'nsew')
l10.grid(row = 2, column = 2, sticky = 'nsew')
l11.grid(row = 2, column = 1, sticky = 'nsew')
l12.grid(row = 2, column = 0, sticky = 'nsew')
#placeing bit labels on grid
bit1.grid(row = 1, column = 9, sticky = 'nsew')
bit2.grid(row = 1, column = 4, sticky = 'nsew')
#placeing normal labels on grid
n1_label.grid(row = 2, column = 4, sticky = 'nsew')
n2_label.grid(row = 2, column = 9, sticky = 'nsew')
#placeing byte labels on grid
byte1_label.grid(row = 0, column = 0, sticky = 'nsew',columnspan=4)
byte2_label.grid(row = 0, column = 5, sticky = 'nsew',columnspan=4)
byte3_label.grid(row = 0, column = 10, sticky = 'nsew',columnspan=4)
#placeing other buttons
dntb_button.grid(row = 3, column = 8, sticky = 'nsew')
vew_label.place(x=260,y=220)
number_label.place(x=0,y=220)
num_entry.place(x=445,y=260)
eror_label.place(x=445,y=229)
line_label.place(x=425,y=230)
#mainloop
x.mainloop()