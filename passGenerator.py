from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import string

root=Tk()
root.geometry("300x250")
root.title("PasswordGenerator")
def show_info(head,body):
    messagebox.showinfo(head, body)
def about_us():
    show_info("Password Generator","This is an simple application to generate a password.It uses a random function")
menubar = Menu(root)
root.config(menu=menubar)
subMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="Exit",command=root.destroy)

subMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=subMenu)
subMenu.add_command(label="App Info",command=about_us)



                          
def util_gen_password(pass_length=10):
    return "".join(random.choice(string.ascii_uppercase + string.digits+string.ascii_lowercase) for _ in range(pass_length))
    
def copy_password():
    password=entry.get()        
    root.clipboard_clear()
    root.clipboard_append(password)  
    show_info("Copied","Your Copied Password :" +password)
    


label=ttk.Label(root,text="Generated Password")
label.pack()

entry=ttk.Entry(root)
entry.pack(padx=10,pady=10)

pass_label=ttk.Label(root,text="Specify Password Length")
pass_label.pack(padx=10,pady=10)

spinbox= Spinbox(root, from_=10, to=100,state='readonly',width=5)
spinbox.pack(padx=10,pady=10)
def spinbox_val():
    return spinbox.get()

def gen_password():
    
    password=util_gen_password(int(spinbox_val()))
    entry.config(state='enabled')
    entry['width']=len(password)+5
    entry.delete(0, END)
    entry.insert(0,password)
    entry.config(state='readonly')
    return password

gen_password()

copy_btn=ttk.Button(root,text="Copy Password",command=copy_password)
copy_btn.pack(padx=10,pady=10)

create_password=ttk.Button(root,text="Generate Password",command=gen_password)
create_password.pack(padx=10,pady=10)

mainloop()
