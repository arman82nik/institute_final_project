from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk


from controller.student_controller import StudentController
from model.entity.student import Student
from view.component.label_with_text import LabelWithText

class StudentView:
    def reset_form(self):
        self.student_id.set(0)
        self.name.set("")
        self.family.set("")
        self.age.set(0)
        self.gender.set("")
        self.birthay.set("")
        self.email.set("")

        status, student_list = self.student_controller.find_all()
        if status:
            self.show_data_on_table(student_list)

    def show_data_on_table(self, student_list):
        for item in self.table.student.get():
            self.table.delete(item)


        if student_list:
            for student in student_list:
                self.table.insert("", 'end', values = student.to_tuple())


    def select_student(self):
        selected_student= self.table.item(self.table.focus())["values"]
        if selected_student:
            student =Student(*selected_student[1:])
            student.student_id = selected_student[0]
            self.student_id.set(student.student_id)
            self.name.set(student.name)
            self.family.set(student.family)
            self.student_id.set(student.student_id)
            self.age.set(student.age)
            self.gender.set(student.gender)
            self.birthay.set(student.birthday)


    def search(self):
        status , student_list= self.student_controller.find_by_id(self.search_student_id.get())

        if status:
            self.show_data_on_table(student_list)

    def save_click(self):
        status, message = self.student_controller.save(self.student_id.get(),self.name.get(),self.age.get(),
                                                      self.gender.get(),self.birthay.get(),self.email.get())

        if status:
            msg.showinfo("Success", f"{message}Student Saved Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}Student Saved Error")

    def edit_click(self):
        status, message = self.student_controller.edit(self.student_id.get(),self.name.get(),self.age.get(),
                                                      self.gender.get(),self.birthay.get(),self.email.get())
        if status:
            msg.showinfo("Success", f"{message}Student edit Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}Student edit Error")

    def delete_click(self):
        status, message = self.student_controller.delete(self.student_id.get())
        if status:
            msg.showinfo("Success", f"{message}Student delete Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}Student delete Error")


    def __init__(self):
        self.student_controller = StudentController()
        self.win=Tk()
        self.win.title("Student profile")
        self.win.geometry("900x450")

        self.student_id = IntVar()
        LabelWithText(self.win, "Student ID:", self.student_id ,20,20,state="readonly")


        self.name = StringVar()
        LabelWithText(self.win, "name:", self.name ,20,60)

        self.family = StringVar()
        LabelWithText(self.win, "family:", self.family ,20,100)

        self.age = IntVar()
        LabelWithText(self.win, "age:", self.age ,20,140)

        self.gender = StringVar()
        LabelWithText(self.win, "gender:", self.gender ,20,200)

        self.birthay = StringVar()
        LabelWithText(self.win, "birthay:", self.birthay ,20,240)

        self.email = StringVar()
        LabelWithText(self.win, "email:", self.email ,20,300)



        self.search_student_id = IntVar()
        LabelWithText(self.win, "search student id:", self.search_student_id ,220,20)


        self.table= ttk.Treeview(self.win,columns=[1,2,3,4,5,6,7],show="headings")
        self.table.heading(1, text='Student ID')
        self.table.heading(2, text="Name")
        self.table.heading(3, text="Family")
        self.table.heading(4, text="Age")
        self.table.heading(5, text="Gender")
        self.table.heading(6, text="birthay")
        self.table.heading(7, text="Email")



        self.table.column(1, width=70)
        self.table.column(2, width=70)
        self.table.column(3, width=70)
        self.table.column(4, width=70)
        self.table.column(5, width=70)
        self.table.column(6, width=70)
        self.table.column(7, width=70)


        self.table.bind("<<TreeviewSelect>>", self.select_student())
        self.table.place(x=220,y=60)

        Button(self.win, text="New Student", command=self.reset_form).place(x=220,y=390)
        Button(self.win, text="Save", command=self.save_click).place(x=300, y=390)
        Button(self.win, text="edit", command=self.edit_click).place(x=340, y=390)
        Button(self.win, text="delete", command=self.delete_click).place(x=380, y=390)

        self.reset_form()
        self.win.mainloop()




