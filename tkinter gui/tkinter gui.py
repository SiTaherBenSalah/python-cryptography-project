
from tkinter import *
from caesarCipherEncrypt import *
from AESEncrypt import *
from caesarcipherDecrypt import *
root=Tk()
root.title("kikou")
bg=PhotoImage(file="cryptography.png")
mylab=Label(root,image=bg)
mylab.place(x=0,y=0,relwidth=1,relheight=1)
e=Text(root,height=5,width=20)
e.grid(row=1,column=20,columnspan=10)
def clickcipher() :
	k=e.get("1.0","end")
	d=ci(k)
	Y.delete(0,END)
	Y.insert(0,d)
def clickaes() :
	k=e.get("1.0","end")
	d=ae(k)
	Y.delete(0,END)
	Y.insert(0,d) 
mybut1=Button(root, padx="30",text=" crypt cipher",command=clickcipher)
mybut2=Button(root,padx="30",text=" crypt AES",command=clickaes)
mybut1.grid(row=3,column=30)
mybut2.grid(row=6,column=30)
Y=Entry(root,borderwidth=30)
Y.grid(row=7,column=20,columnspan=5)
#decryptage
p=Entry(root,borderwidth=0)
p.grid(row=7,column=100,columnspan=5)
c=Text(root,height=5,borderwidth=0,width=20)
c.grid(row=1,column=100,columnspan=10)
def decryptcipher() :
	k=c.get("1.0","end")
	d=di(k)
	p.delete(0,END)
	p.insert(0,d)
#def decryptaes(KEY,k) :
#	d=decae(KEY,k)
#	Y.delete(0,END)
#	Y.insert(0,d) 
mybut3=Button(root, padx="30",text=" decrypt cipher",command=decryptcipher)
mybut3.grid(row=5,column=50)
#mybut3=Button(root, padx="20",text=" decrypt cipher",command=decryptaes(ae(k)[0],k))
#mybut3.grid(row=3,column=8)


root.mainloop()