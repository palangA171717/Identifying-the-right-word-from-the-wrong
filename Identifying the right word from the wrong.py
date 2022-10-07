
from tkinter import *
def a():
    Q=e.get()
    m=str(Q).lower()

    nnnnnnnnnnnnnnnnnn="wrong"
    n=open('h:/words.txt','r')
    nn=(n.readlines())
    nnnnn=len(nn)
    for i in range((-1),nnnnn):
     nn[i]=nn[i].lower() 
    if((m+'\n') in nn):
        nnnnnnnnnnnnnnnnnn="right"
 
    ww=Toplevel()
    Label(ww,text=str(nnnnnnnnnnnnnnnnnn)).pack()
    
    n.close()

W=Tk()
W.title("Identifying the right word from the wrong")
#W.geometry('450x300')
e=Entry(W,width=65)
e.pack()
b=Button(W,width=20,command=a).pack()
W.mainloop()
