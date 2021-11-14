from tkinter import *
from tkinter.messagebox import *
import math as m
from audio_helper import PlayAudio
import threading

#some useful variables
font = ('verdana',18,'italic  bold')
ob=PlayAudio()
#------

#important functions
def clear():
    ex=textField.get()
    ex=ex[0:len(ex)-1]
    textField.delete(0,END)
    textField.insert(0,ex)


def all_clear():
    textField.delete(0,END)


def click_btn_function(event):
    print("btn clicked")
    b=event.widget
    text=b['text']
    print(text)
    t=threading.Thread(target=ob.speak,args=(text,))
    t.start()

    if text=='x':
        textField.insert(END,"*")
        return

    if text=='=':
        try:
            ex=textField.get()
            answer=eval(ex)
            textField.delete(0,END)
            textField.insert(0,answer)
        except Exception as e:
            print("Error....",e)
            showerror("Error...",e)
        return

    textField.insert(END,text)


# creating a window
window=Tk()
window.title('My Calculator')
window.geometry('390x650')

#picture label
pic=PhotoImage(file='img/cal2.png')
headingLabel=Label(window,image=pic)
headingLabel.pack(side=TOP,pady=10)

#heading label
heading = Label(window,text='My Calculator',font=font, underline=0)
heading.pack(side=TOP)

#text filled
textField = Entry(window, font=font, justify=CENTER)
textField.pack(side=TOP,pady=10,fill=X,padx=10)

#button
buttonFrame = Frame(window)
buttonFrame.pack(side=TOP,padx=10)

#adding button
# btn1=Button(buttonFrame, text="1",font=font)
# btn1.grid(row =0,column=0)
#
# btn2=Button(buttonFrame, text="2",font=font)
# btn2.grid(row=0,column=1)
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn = Button(buttonFrame,text=str(temp), font=font,width=4,relief='ridge',activebackground='orange',activeforeground='white')
        btn.grid(row=i,column=j)
        temp = temp + 1
        btn.bind('<Button-1>',click_btn_function)

zeroBtn=  Button(buttonFrame,text='0', font=font,width=4,relief='ridge',activebackground='orange',activeforeground='white')
zeroBtn.grid(row=3,column=0)

doBtn=  Button(buttonFrame,text='.', font=font,width=4,relief='ridge',activebackground='orange',activeforeground='white')
doBtn.grid(row=3,column=1)

equalBtn=  Button(buttonFrame,text='=', font=font,width=4,relief='ridge',activebackground='orange',activeforeground='white')
equalBtn.grid(row=3,column=2)

plusBtn=  Button(buttonFrame,text='+', font=font,width=4,relief='ridge',activebackground='orange',activeforeground='white')
plusBtn.grid(row=0,column=3)

minusBtn=  Button(buttonFrame,text='-', font=font,width=4,relief='ridge',activebackground='orange',activeforeground='white')
minusBtn.grid(row=1,column=3)

multBtn=  Button(buttonFrame,text='x', font=font,width=4,relief='ridge',activebackground='orange',activeforeground='white')
multBtn.grid(row=2,column=3)

divideBtn=  Button(buttonFrame,text='/', font=font,width=4,relief='ridge',activebackground='orange',activeforeground='white')
divideBtn.grid(row=3,column=3)

clearBtn=  Button(buttonFrame,text='<--', font=font,width=9,relief='ridge',activebackground='orange',
                  activeforeground='white',command=clear)
clearBtn.grid(row=4,column=0, columnspan=2)

allclearBtn=  Button(buttonFrame,text='AC', font=font,width=9,relief='ridge',activebackground='orange',
                     activeforeground='white',command=all_clear)
allclearBtn.grid(row=4,column=2, columnspan=2)

#binding all btns
plusBtn.bind('<Button-1>', click_btn_function)
minusBtn.bind('<Button-1>', click_btn_function)
multBtn.bind('<Button-1>', click_btn_function)
divideBtn.bind('<Button-1>', click_btn_function)
zeroBtn.bind('<Button-1>', click_btn_function)
doBtn.bind('<Button-1>', click_btn_function)
equalBtn.bind('<Button-1>', click_btn_function)

def enterclick(event):
    print('hi')
    e=Event()
    e.widget=equalBtn
    click_btn_function(e)

textField.bind('<Return>',enterclick)

######################################################################################
#function scientific

scFrame=Frame(window)
sqrtBtn=  Button(scFrame,text='√', font=font,width=4,relief='ridge',activebackground='orange',
                     activeforeground='white',command=all_clear)
sqrtBtn.grid(row=0,column=0)
powBtn=  Button(scFrame,text='‸', font=font,width=4,relief='ridge',activebackground='orange',
                     activeforeground='white',command=all_clear)
powBtn.grid(row=0,column=1)
factBtn=  Button(scFrame,text='x!', font=font,width=4,relief='ridge',activebackground='orange',
                     activeforeground='white',command=all_clear)
factBtn.grid(row=0,column=2)
radBtn=  Button(scFrame,text='toRad', font=font,width=4,relief='ridge',activebackground='orange',
                     activeforeground='white',command=all_clear)
radBtn.grid(row=0,column=3)
degBtn=  Button(scFrame,text='toDeg', font=font,width=4,relief='ridge',activebackground='orange',
                     activeforeground='white',command=all_clear)
degBtn.grid(row=1,column=0)
sinBtn=  Button(scFrame,text='sinΘ', font=font,width=4,relief='ridge',activebackground='orange',
                     activeforeground='white',command=all_clear)
sinBtn.grid(row=1,column=1)
cosBtn=  Button(scFrame,text='cosΘ', font=font,width=4,relief='ridge',activebackground='orange',
                     activeforeground='white',command=all_clear)
cosBtn.grid(row=1,column=2)
tanBtn=  Button(scFrame,text='tanΘ', font=font,width=4,relief='ridge',activebackground='orange',
                     activeforeground='white',command=all_clear)
tanBtn.grid(row=1,column=3)


normalcalc=True

def calculate_sc(event):
    print('btn...')
    btn=event.widget
    text=btn['text']
    print(text)
    ex=textField.get()
    answer=''
    if text=='todeg':
        print("cal degree")
        answer=str(m.degrees(float(ex)))

    elif text=='toRad':
        print("radian")
        answer=str(m.radians(float(ex)))

    elif text=='x!':
        print("cal factoria")
        answer=str(m.factorial(int(ex)))

    elif text=='sinΘ':
        print("cal sinΘ")
        answer=str(m.sin(m.radians(int(ex))))

    elif text=='cosΘ':
        print("cal cosΘ")
        answer = str(m.cos(m.radians(int(ex))))

    elif text=='tanΘ':
        print("cal tanΘ")
        answer = str(m.tan(m.radians(int(ex))))

    elif text=='√':
        print('sqrt')
        answer=m.sqrt(int(ex))

    elif text=='‸':
        print('pow')
        base, pow = ex.split(',')
        print(base)
        print(pow)
        answer= m.pow(int(base),int(pow))

    textField.delete(0,END)
    textField.insert(0,answer)


def sc_click():
    global normalcalc
    if normalcalc:
        #sc..
        buttonFrame.pack_forget()
        #add sc frame
        scFrame.pack(side=TOP,padx=10)
        buttonFrame.pack(side=TOP,pady=10)
        window.geometry('400x750')

        print("show sc")
        normalcalc=False
    else:
        print('show normal')
        scFrame.pack_forget()
        window.geometry('390x650')
        normalcalc = True



#end function
#binding sc button
sqrtBtn.bind("<Button-1>",calculate_sc)
powBtn.bind("<Button-1>",calculate_sc)
factBtn.bind("<Button-1>",calculate_sc)
radBtn.bind("<Button-1>",calculate_sc)
degBtn.bind("<Button-1>",calculate_sc)
sinBtn.bind("<Button-1>",calculate_sc)
cosBtn.bind("<Button-1>",calculate_sc)
tanBtn.bind("<Button-1>",calculate_sc)

fontMenu=('',15)
menubar=Menu(window,font=fontMenu)

mode=Menu(menubar,font=fontMenu, tearoff=0)
mode.add_command(label="scientific calculator",command=sc_click)

menubar.add_cascade(label="Mode",menu=mode)

window.config(menu=menubar)


window.mainloop()