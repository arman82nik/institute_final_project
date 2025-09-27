from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk


from controller.register_controller import RegisterController
from model.entity.register import Register
from view.component.label_with_text import LabelWithText



class RegisterView:
    def reset_form(self):
        self.person_id.set(0)
        self.name.set("")
        self.family.set("")
        self.phone_number.set(0)
        self.course_number.set(0)

        status, register_list = self.register_controller.find_all()
        if status:
            self.show_data_on_table(register_list)

    def show_data_on_table(self, register_list):
        for item in self.table.register():
            self.table.delete(item)


        if register_list:
            for register in register_list:
                self.table.insert("", 'end', values = register.to_tuple())


    def select_register(self):
        selected_register= self.table.item(self.table.focus())["values"]
        if selected_register:
            register =Register(*selected_register[1:])
            register.register_id = selected_register[0]
            self.person_id.set(register.person_id)
            self.name.set(register.name)
            self.family.set(register.family)
            self.phone_number.set(register.phone_number)
            self.course_number(register.course_number)



    def search(self):
        status , register_list= self.register_controller.find_by_id(self.search_course_number.get())

        if status:
            self.show_data_on_table(register_list)


    def save_click(self):
        status, message = self.register_controller.save(self.person_id.get(),self.name.get(),
                                                      self.family.get(),self.phone_number.get(),self.course_number.get())

        if status:
            msg.showinfo("Success", f"{message}Register Saved Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}Register Saved Error")

    def edit_click(self):
        status, message = self.register_controller.edit(self.person_id.get(), self.name.get(),
                                                      self.family.get(), self.phone_number.get(), self.course_number.get())

        if status:
            msg.showinfo("Success", f"{message}Register edit Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}Register edit Error")

    def delete_click(self):
        status, message = self.register_controller.delete(self.person_id.get())
        if status:
            msg.showinfo("Success", f"{message}register delete Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}register delete Error")


    def __init__(self):
        self.register_controller = RegisterController()
        self.win=Tk()
        self.win.title("Register profile")
        self.win.geometry("900x450")

        self.person_id = IntVar()
        LabelWithText(self.win, "Person ID:", self.person_id ,20,20,state="readonly")


        self.name = StringVar()
        LabelWithText(self.win, "name:", self.name ,20,60)

        self.family = StringVar()
        LabelWithText(self.win, "family:", self.family ,20,100)

        self.phone_number = IntVar()
        LabelWithText(self.win, "Phone number:", self.phone_number ,20,140)


        self.course_number = IntVar()
        LabelWithText(self.win, "course number:", self.course_number ,20,200)




        self.table= ttk.Treeview(self.win,columns=[1,2,3,4,5],show='headings')
        self.table.heading(1, text='Person ID')
        self.table.heading(2, text='Name')
        self.table.heading(3, text='Family')
        self.table.heading(4, text='Phone number')
        self.table.heading(5, text='Course id')




        self.table.column(1, width=70)
        self.table.column(2, width=70)
        self.table.column(3, width=70)
        self.table.column(4, width=70)
        self.table.column(5, width=70)


        self.table.bind("<<TreeviewSelect>>", self.select_register())
        self.table.place(x=220,y=60)

        Button(self.win, text="New Person", command=self.reset_form).place(x=220,y=390)
        Button(self.win, text="Save", command=self.save_click).place(x=300, y=390)
        Button(self.win, text="edit", command=self.edit_click).place(x=340, y=390)
        Button(self.win, text="delete", command=self.delete_click).place(x=380, y=390)

        self.reset_form()
        self.win.mainloop()

        #finished