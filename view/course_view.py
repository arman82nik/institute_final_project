from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk


from controller.course_controller import CourseController
from model.entity.course import Course
from view.component.label_with_text import LabelWithText



class CourseView:
    def reset_form(self):
        self.course_id.set(0)
        self.name.set("")
        self.teacher.set("")
        self.start_date.set("")
        self.end_date.set("")
        self.start_time.set("")
        self.end_time.set("")
        self.type_class.set("")
        status, course_list = self.course_controller.find_all()
        if status:
            self.show_data_on_table(course_list)

    def show_data_on_table(self, course_list):
        for item in self.table.get_children():
            self.table.delete(item)


        if course_list:
            for course in course_list:
                self.table.insert("", 'end', values = course.to_tuple())


    def select_course(self):
        focus_item = self.table.focus()
        if not focus_item:
            return
        selected_course= self.table.item(self.table.focus())["values"]
        if selected_course:
            course =Course(*selected_course[1:])
            course.course_id = selected_course[0]
            self.course_id.set(course.course_id)
            self.name.set(course.name)
            self.teacher.set(course.teacher)
            self.start_date.set(course.start_date)
            self.end_date.set(course.end_date)
            self.start_time.set(course.start_time)
            self.end_time.set(course.end_time)
            self.type_class.set(course.type_class)

    def search(self):
        status , course_list= self.course_controller.find_by_id(self.search_course_id.get())

        if status:
            self.show_data_on_table(course_list)

    def save_click(self):
        status, message = self.course_controller.save(
            self.course_id.get(), self.name.get(), self.teacher.get(),
            self.start_date.get(), self.end_date.get(),
            self.start_time.get(), self.end_time.get(),
            self.type_class.get()
        )
        if status:
            msg.showinfo("Success", f"{message}Course Saved Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}Course Saved Error")

    def edit_click(self):
        status, message = self.course_controller.edit(self.course_id.get(), self.name.get(),
                                                      self.teacher.get(), self.start_date.get(), self.end_date.get(),
                                                      self.start_time.get(), self.end_time.get())
        if status:
            msg.showinfo("Success", f"{message}Course edit Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}Course edit Error")

    def delete_click(self):
        status, message = self.course_controller.delete(self.course_id.get())
        if status:
            msg.showinfo("Success", f"{message}Course delete Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}Course delete Error")


    def __init__(self):
        self.course_controller = CourseController()
        self.win=Tk()
        self.win.title("Course profile")
        self.win.geometry("900x450")

        self.course_id = IntVar()
        LabelWithText(self.win, "Course ID:", self.course_id ,20,20,state="readonly")


        self.name = StringVar()
        LabelWithText(self.win, "name:", self.name ,20,60)

        self.teacher = StringVar()
        LabelWithText(self.win, "teacher:", self.teacher ,20,100)

        self.start_date = StringVar()
        LabelWithText(self.win, "start_date:", self.start_date ,20,140)

        self.end_date = StringVar()
        LabelWithText(self.win, "end_date:", self.end_date ,20,200)

        self.start_time = StringVar()
        LabelWithText(self.win, "start_time:", self.start_time ,20,240)

        self.end_time = StringVar()
        LabelWithText(self.win, "end_time:", self.end_time ,20,300)

        self.type_class = StringVar()
        LabelWithText(self.win, "type_class:", self.type_class ,20,340)

        self.search_course_id = IntVar()
        LabelWithText(self.win, "search course id:", self.search_course_id ,220,20)


        self.table= ttk.Treeview(self.win,columns=[1,2,3,4,5,6,7,8],show='headings')
        self.table.heading(1, text='Course ID')
        self.table.heading(2, text='Name')
        self.table.heading(3, text='Teacher')
        self.table.heading(4, text='Start Date')
        self.table.heading(5, text='End Date')
        self.table.heading(6, text='Start Time')
        self.table.heading(7, text='End Time')
        self.table.heading(8, text='Type')


        self.table.column(1, width=70)
        self.table.column(2, width=70)
        self.table.column(3, width=70)
        self.table.column(4, width=70)
        self.table.column(5, width=70)
        self.table.column(6, width=70)
        self.table.column(7, width=70)
        self.table.column(8, width=70)

        self.table.bind("<<TreeviewSelect>>", self.select_course())
        self.table.place(x=220,y=60)

        Button(self.win, text="New Person", command=self.reset_form).place(x=220,y=390)
        Button(self.win, text="Save", command=self.save_click).place(x=300, y=390)
        Button(self.win, text="edit", command=self.edit_click).place(x=340, y=390)
        Button(self.win, text="delete", command=self.delete_click).place(x=380, y=390)

        self.reset_form()
        self.win.mainloop()




