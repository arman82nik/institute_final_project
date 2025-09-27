from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk


from controller.teacher_controller import TeacherController
from model.entity.teacher import Teacher
from view.component.label_with_text import LabelWithText



class TeacherView:
    def reset_form(self):
        self.teacher_id.set(0)
        self.first_name.set("")
        self.last_name.set("")
        self.email.set("")
        self.department.set("")
        self.national_id.set(0)
        self.phone_number.set(0)


        status, teacher_list = self.teacher_controller.find_all()
        if status:
            self.show_data_on_table(teacher_list)

    def show_data_on_table(self, teacher_list):
        for item in self.table.get_children():
            self.table.delete(item)


        if teacher_list:
            for teacher in teacher_list:
                self.table.insert("", 'end', values = teacher.to_tuple())


    def select_teacher(self):
        selected_teacher= self.table.item(self.table.focus())["values"]
        if selected_teacher:
            teacher =Teacher(*selected_teacher[1:])
            teacher.teacher_id = selected_teacher[0]
            self.teacher_id.set(teacher.teacher_id)
            self.first_name.set(teacher.first_name)
            self.last_name.set(teacher.last_name)
            self.email.set(teacher.email)
            self.department.set(teacher.department)
            self.national_id.set(teacher.national_id)
            self.phone_number.set(teacher.phone_number)


    def search(self):
        status , teacher_list= self.teacher_controller.find_by_id(self.search_teacher_id.get())

        if status:
            self.show_data_on_table(teacher_list)

    def save_click(self):
        status, message = self.teacher_controller.save(self.teacher_id.get(),self.first_name.get(),
                                                      self.last_name.get(),self.email.get(),self.department.get(),
                                                      self.national_id.get(),self.phone_number.get())
        if status:
            msg.showinfo("Success", f"{message}Teacher Saved Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}Teacher Saved Error")

    def edit_click(self):
        status , message = self.teacher_controller.edit(self.teacher_id.get(), self.first_name.get(),
                                                      self.last_name.get(), self.email.get(), self.department.get(),
                                                      self.national_id.get(), self.phone_number.get())
        if status:
            msg.showinfo("Success", f"{message}Teacher edit Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}Teacher edit Error")

    def delete_click(self):
        status, message = self.teacher_controller.delete(self.teacher_id.get())
        if status:
            msg.showinfo("Success", f"{message}Teacher delete Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}Teacher delete Error")


    def __init__(self):
        self.teacher_controller = TeacherController()
        self.win=Tk()
        self.win.title("Teacher profile")
        self.win.geometry("900x450")

        self.teacher_id = IntVar()
        LabelWithText(self.win, "Teacher ID:", self.teacher_id ,20,20,state="readonly")


        self.first_name = StringVar()
        LabelWithText(self.win, "first name:", self.first_name ,20,60)

        self.last_name = StringVar()
        LabelWithText(self.win, "last name:", self.last_name ,20,100)

        self.email = StringVar()
        LabelWithText(self.win, "email:", self.email ,20,140)

        self.department = StringVar()
        LabelWithText(self.win, "department:", self.department ,20,200)

        self.national_id = IntVar()
        LabelWithText(self.win, "national_id:", self.national_id ,20,240)

        self.phone_number = IntVar()
        LabelWithText(self.win, "phone_number:", self.phone_number ,20,300)



        self.search_teacher_id = IntVar()
        LabelWithText(self.win, "search teacher id:", self.search_teacher_id ,220,20)


        self.table= ttk.Treeview(self.win,columns=[1,2,3,4,5,6],show='headings')
        self.table.heading(1, text='Teacher ID')
        self.table.heading(2, text='Name')
        self.table.heading(3, text='last name')
        self.table.heading(4, text='email')
        self.table.heading(5, text='department')
        self.table.heading(6, text='phone number')



        self.table.column(1, width=70)
        self.table.column(2, width=70)
        self.table.column(3, width=70)
        self.table.column(4, width=70)
        self.table.column(5, width=70)
        self.table.column(6, width=70)


        self.table.bind("<<TreeviewSelect>>", self.select_teacher())
        self.table.place(x=220,y=60)

        Button(self.win, text="New Person", command=self.reset_form).place(x=220,y=390)
        Button(self.win, text="Save", command=self.save_click).place(x=300, y=390)
        Button(self.win, text="edit", command=self.edit_click).place(x=340, y=390)
        Button(self.win, text="delete", command=self.delete_click).place(x=380, y=390)

        self.reset_form()
        self.win.mainloop()