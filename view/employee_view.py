from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk


from controller.employee_controller  import EmployeeController
from model.entity.employee import Employee
from view.component.label_with_text import LabelWithText



class EmployeeView:
    def reset_form(self):
        self.first_name.set("")
        self.last_name.set("")
        self.national_id.set(0)
        self.birthday.set("")
        self.email.set("")
        self.job_title.set("")
        self.department.set("")
        self.hire_date.set(0)
        self.salary.set(0)

        status, employee_list = self.employee_controller.find_all()
        if status:
            self.show_data_on_table(employee_list)

    def show_data_on_table(self, employee_list):
        for item in self.table.get_children():
            self.table.delete(item)


        if employee_list:
            for employee in employee_list:
                self.table.insert("", 'end', values = employee.to_tuple())


    def select_employee(self):
        focus_item = self.table.focus()
        if not focus_item:
            return
        selected_employee= self.table.item(self.table.focus())["values"]
        if selected_employee:
            employee =Employee(*selected_employee[1:])
            employee.employee_id = selected_employee[0]
            self.first_name.set(employee.first_name)
            self.last_name.set(employee.last_name)
            self.national_id.set(employee.national_id)
            self.national_id.set(employee.birthday)
            self.email.set(employee.email)
            self.job_title.set(employee.job_title)
            self.department.set(employee.department)
            self.hire_date.set(employee.hire_date)
            self.salary.set(employee.salary)

    def search(self):
        status , employee_list= self.employee_controller.find_by_id(self.search_employee_id.get())

        if status:
            self.show_data_on_table(employee_list)

    def save_click(self):
        status, message = self.employee_controller.save(
            self.first_name.get(), self.last_name.get(), self.national_id.get(),
            self.birthday.get(), self.email.get(),
            self.job_title.get(), self.department.get(),
            self.hire_date.get(),self.salary.get())

        if status:
            msg.showinfo("Success", f"{message}employee Saved Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}employee Saved Error")

    def edit_click(self):
        status, message = self.employee_controller.edit(self.first_name.get(), self.last_name.get(), self.national_id.get(),
             self.email.get(),
            self.job_title.get(), self.department.get(),
            self.hire_date.get(),self.salary.get())
        if status:
            msg.showinfo("Success", f"{message}employee edit Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}employee edit Error")

    def delete_click(self):
        status, message = self.employee_controller.delete(self.employee_id.get())
        if status:
            msg.showinfo("Success", f"{message}employee delete Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}employee delete Error")


    def __init__(self):
        self.employee_controller = EmployeeController()
        self.win=Tk()
        self.win.title("employee profile")
        self.win.geometry("900x450")

        self.first_name = IntVar()
        LabelWithText(self.win, "first_name:", self.first_name ,20,20,state="readonly")


        self.last_name = StringVar()
        LabelWithText(self.win, "last_name:", self.last_name ,20,60)

        self.national_id = StringVar()
        LabelWithText(self.win, "national_id:", self.national_id ,20,100)

        self.birthday = StringVar()
        LabelWithText(self.win, "birthday:", self.birthday ,20,140)

        self.email = StringVar()
        LabelWithText(self.win, "email:", self.email,20,200)

        self.job_title = StringVar()
        LabelWithText(self.win, "job_title:", self.job_title ,20,240)

        self.department = StringVar()
        LabelWithText(self.win, "department:", self.department ,20,300)

        self.hire_date = StringVar()
        LabelWithText(self.win, "hire_date:", self.hire_date ,20,340)

        self.salary = StringVar()
        LabelWithText(self.win, "salary:", self.salary ,20,400)

        self.search_employee_id = IntVar()
        LabelWithText(self.win, "search employee id:", self.search_employee_id ,220,20)


        self.table= ttk.Treeview(self.win,columns=[1,2,3,4,5,6,7,8,9],show='headings')
        self.table.heading(1, text='name')
        self.table.heading(2, text='last name')
        self.table.heading(3, text='national id')
        self.table.heading(4, text='email')
        self.table.heading(5, text='job title')
        self.table.heading(6, text='department')
        self.table.heading(7, text='hire_date')
        self.table.heading(8, text='salary')
        self.table.heading(9, text='Department')


        self.table.column(1, width=70)
        self.table.column(2, width=70)
        self.table.column(3, width=70)
        self.table.column(4, width=70)
        self.table.column(5, width=70)
        self.table.column(6, width=70)
        self.table.column(7, width=70)
        self.table.column(8, width=70)
        self.table.column(9, width=70)

        self.table.bind("<<TreeviewSelect>>", self.select_employee())
        self.table.place(x=220,y=60)

        Button(self.win, text="New Employee", command=self.reset_form).place(x=220,y=390)
        Button(self.win, text="Save", command=self.save_click).place(x=300, y=390)
        Button(self.win, text="edit", command=self.edit_click).place(x=340, y=390)
        Button(self.win, text="delete", command=self.delete_click).place(x=380, y=390)

        self.reset_form()
        self.win.mainloop()