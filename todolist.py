from tkinter import *
from tkinter import ttk
root=Tk()
root.title("To do list")
root.geometry("1000x1000")

def insertitem():
    listbox.insert(END,content.get())
def deleteitem():
    selected_index = listbox.curselection()
    if selected_index:  # Check if any item is selected
        listbox.delete(selected_index)


l=Label(root,text="List-To-Do",font=("cursive", 25, "bold"),borderwidth=2,relief="raised",height=2,bg="pink",fg="black",bd=10)
l.pack(fill=BOTH,side="top")
Label(root,height=2).pack()

l1=Label(root,text="Your Task",font=("cursive", 25, "bold"),width=60,bg="cyan",height=2,borderwidth=2,relief="raised",fg="black",bd=5)
l1.pack(padx=20,side="top")

listbox=Listbox(root,height=14,width=50,bg="white",font=("cursive", 25, "bold"))
listbox.pack(side="top",pady=8)

content=StringVar()
e1=Entry(root,bd=4,textvariable=content,width=35)
e1.pack()

add_but=Button(root,text="Add Task",bg="cyan",activebackground="pink",fg="black",height=2,width=20,command=insertitem,font=("cursive", 25, "bold"))
add_but.pack(padx=10,pady=10)
#add_but.grid(row=0,column=0)

del_but=Button(root,text="del Task",bg="red",activebackground="pink",fg="black",height=2,width=20,command=deleteitem,font=("cursive", 25, "bold"))
del_but.pack(padx=10,pady=10)
#del_but.grid(row=0,column=1)
root.mainloop()