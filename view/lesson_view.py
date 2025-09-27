from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk


from controller.lesson_controller import LessonController
from model.entity.lesson import Lesson
from view.component.label_with_text import LabelWithText



class LessonView:
    def reset_form(self):
        self.person_id.set(0)
        self.title.set("")
        self.code.set(0)
        self.teacher.set("")
        self.units.set(0)
        status, lesson_list = self.lesson_controller.find_all()
        if status:
            self.show_data_on_table(lesson_list)

    def show_data_on_table(self, lesson_list):
        for item in self.table.get_children():
            self.table.delete(item)


        if lesson_list:
            for lesson in lesson_list:
                self.table.insert("", 'end', values = lesson.to_tuple())


    def select_lesson(self):
        focus_item = self.table.focus()
        if not focus_item:
            return
        selected_lesson= self.table.item(self.table.focus())["values"]
        if selected_lesson:
            lesson =Lesson(*selected_lesson[1:])
            lesson.person_id = selected_lesson[0]
            self.person_id.set(lesson.person_id)
            self.title.set(lesson.title)
            self.code.set(lesson.code)
            self.teacher.set(lesson.teacher)
            self.units.set(lesson.units)


    def search(self):
        status , lesson_list= self.lesson_controller.find_by_id(self.search_person_id.get())

        if status:
            self.show_data_on_table(lesson_list)

    def save_click(self):
        status, message = self.lesson_controller.save(
            self.person_id.get(), self.title.get(), self.code.get(),
            self.teacher.get(), self.units.get())

        if status:
            msg.showinfo("Success", f"{message}Lesson Saved Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}Lesson Saved Error")

    def edit_click(self):
        status, message = self.lesson_controller.edit(self.person_id.get(), self.title.get(),
                                                      self.code.get(), self.teacher.get(), self.units.get())

        if status:
            msg.showinfo("Success", f"{message}Lesson edit Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}Lesson edit Error")

    def delete_click(self):
        status, message = self.lesson_controller.delete(self.person_id.get())
        if status:
            msg.showinfo("Success", f"{message}lesson delete Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}Lesson delete Error")


    def __init__(self):
        self.lesson_controller = LessonController()
        self.win=Tk()
        self.win.title("Lesson profile")
        self.win.geometry("900x450")

        self.person_id = IntVar()
        LabelWithText(self.win, "Person ID:", self.person_id ,20,20,state="readonly")


        self.title = StringVar()
        LabelWithText(self.win, "title:", self.title ,20,60)

        self.code = IntVar()
        LabelWithText(self.win, "code:", self.code ,20,100)

        self.teacher = StringVar()
        LabelWithText(self.win, "teacher:", self.teacher ,20,140)

        units = IntVar()
        LabelWithText(self.win, "units:", self.units ,20,200)




        self.table= ttk.Treeview(self.win,columns=[1,2,3,4,5],show='headings')
        self.table.heading(1, text='Person ID')
        self.table.heading(2, text='Title')
        self.table.heading(3, text='Code')
        self.table.heading(4, text='teacher')
        self.table.heading(5, text='Units')



        self.table.column(1, width=70)
        self.table.column(2, width=70)
        self.table.column(3, width=70)
        self.table.column(4, width=70)
        self.table.column(5, width=70)


        self.table.bind("<<TreeviewSelect>>", self.select_lesson())
        self.table.place(x=220,y=60)

        Button(self.win, text="New Lesson", command=self.reset_form).place(x=220,y=390)
        Button(self.win, text="Save", command=self.save_click).place(x=300, y=390)
        Button(self.win, text="edit", command=self.edit_click).place(x=340, y=390)
        Button(self.win, text="delete", command=self.delete_click).place(x=380, y=390)

        self.reset_form()
        self.win.mainloop()




