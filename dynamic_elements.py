from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.geometry("900x600")
root.title("Classes")
class CreateElements:
    def __init__(self):
        print("This is CreateElements class")
    def createNewElement(self):
        text=text_dropdown.get()
        if(text=="Label"):
            label=Label(root,text="A new label is been created using class",fg="red")
            label.pack()
        elif(text=="Button"):
            btn=Button(root,text="Button",command=self.message)
            btn.pack(padx=20,pady=20)
        elif(text=="Dropdown"):
            dropdown_sub=ttk.Combobox(values=[1,2,3,4],state="readonly")
            dropdown_sub.pack()
        elif(text=="Entry"):
            Enter=Entry(root)
            Enter.pack()
        else:
            messagebox.showerror("Error","Please select the element from the dropdown")
    def message(self):
        messagebox.showinfo("showinfo","You clicked the button created using class")

obj_of_CreateElements=CreateElements()
text_dropdown=StringVar()
dropdown=ttk.Combobox(textvariable=text_dropdown,values=["Label","Button","Dropdown","Entry"],state="readonly")
dropdown.pack()
btn=Button(root,text="Create Element",command=obj_of_CreateElements.createNewElement)
btn.pack(padx=10,pady=10)
root.mainloop()
