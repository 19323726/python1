#login page
from tkinter import*
import tkinter.messagebox as messagebox

root=Tk()
root.title("Registration")
root.geometry("800x600")
myfra=LabelFrame(root,text="Registration",padx=50,pady=60)
myfra.pack()
name=Label(myfra,text="name :")
name.grid(row=0,column=0)
ent=Entry(myfra,fg="black",bg="white")
ent.grid(row=0,column=1)


name=Label(myfra,text="Mother's name:")
name.grid(row=1,column=0)
ent=Entry(myfra,fg="black",bg="white")
ent.grid(row=1,column=1)


name=Label(myfra,text="ERP ID :")
name.grid(row=2,column=0)
ent=Entry(myfra,fg="black",bg="white")
ent.grid(row=2,column=1)

name=Label(myfra,text="Father's name :")
name.grid(row=3,column=0)
ent=Entry(myfra,fg="black",bg="white")
ent.grid(row=3,column=1)

name=Label(myfra,text="Roll.no :")
name.grid(row=4,column=0)
ent=Entry(myfra,fg="black",bg="white")
ent.grid(row=4,column=1)


name=Label(myfra,text="Branch:")
name.grid(row=5,column=0)
lb=Listbox(myfra)
lb.insert(1,"CSE")
lb.insert(2,"AI")
lb.insert(3,"DS")
lb.insert(1,"ECE")
lb.insert(5,"IT")
lb.grid(row=5,column=1)
radio_var=StringVar()
sem=Label(myfra,text="Semester:")
sem.grid(row=6,column=0)
ep=Radiobutton(myfra,text="1",variable=radio_var, value="1")
ep.grid(row=6,column=1)
ep=Radiobutton(myfra,text="2",variable=radio_var, value="2")
ep.grid(row=6,column=2)


branch=Label(myfra,text="Branch")
branch.grid(row=7,column=0)
ep=Radiobutton(myfra,text="CSE",variable=radio_var, value="1")
ep.grid(row=7,column=1)
ep=Radiobutton(myfra,text="AI",variable=radio_var, value="2")
ep.grid(row=7,column=2)
ep=Radiobutton(myfra,text="DS",variable=radio_var, value="3")
ep.grid(row=7,column=3)
ep=Radiobutton(myfra,text="ECE",variable=radio_var, value="4")
ep.grid(row=7,column=4)
ep=Radiobutton(myfra,text="IT",variable=radio_var, value="5")
ep.grid(row=7,column=5)



def show():
    messagebox.showinfo("Fill Again")
button=Button(myfra,text="Cancel",command=show)
button.grid(row=8,column=0)


def click():
    messagebox.showinfo("Warning","you have successfully registered")
    myfra.destroy()
button=Button(myfra,text="SUBMIT",command=click
              )
button.grid(row=8,column=2)
root.mainloop()
