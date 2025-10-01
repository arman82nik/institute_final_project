from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk

from controller.exercise_controller import ExerciseController
from model.entity.exercise import Exercise
from view.component.label_with_text import LabelWithText


class ExerciseView:
    def reset_form(self):
        self.id.set(0)
        self.student_id.set(0)
        self.lesson_id.set(0)
        self.score.set(0)

        status, exercise_list = self.exercise_controller.find_all()
        if status:
            self.show_data_on_table(exercise_list)

    def show_data_on_table(self, exercise_list):
        for item in self.table.get_children():
            self.table.delete(item)

        if exercise_list:
            for ex in exercise_list:
                self.table.insert("", 'end', values=ex.to_tuple())

    def select_exercise(self, event=None):
        focus_item = self.table.focus()
        if not focus_item:
            return
        selected = self.table.item(focus_item)["values"]
        if selected:
            ex = Exercise(*selected[1:])
            ex.id = selected[0]
            self.id.set(ex.id)
            self.student_id.set(ex.student_id)
            self.lesson_id.set(ex.lesson_id)
            self.score.set(ex.score)

    def search(self):
        status, ex = self.exercise_controller.find_by_id(self.search_id.get())
        if status:
            self.show_data_on_table([ex])

    def save_click(self):
        status, message = self.exercise_controller.save(
            self.student_id.get(), self.lesson_id.get(), self.score.get()
        )
        if status:
            msg.showinfo("Success", "Exercise Saved Successfully")
            self.reset_form()
        else:
            msg.showerror("Error", f"{message} Exercise Save Error")

    def edit_click(self):
        status, message = self.exercise_controller.edit(
            self.id.get(), self.student_id.get(), self.lesson_id.get(), self.score.get()
        )
        if status:
            msg.showinfo("Success", "Exercise Edited Successfully")
            self.reset_form()
        else:
            msg.showerror("Error", f"{message} Exercise Edit Error")

    def delete_click(self):
        status, message = self.exercise_controller.delete(self.id.get())
        if status:
            msg.showinfo("Success", "Exercise Deleted Successfully")
            self.reset_form()
        else:
            msg.showerror("Error", f"{message} Exercise Delete Error")

    def __init__(self):
        self.exercise_controller = ExerciseController()
        self.win = Tk()
        self.win.title("Exercise Management")
        self.win.geometry("900x450")

        self.id = IntVar()
        LabelWithText(self.win, "ID:", self.id, 20, 20, state="readonly")

        self.student_id = IntVar()
        LabelWithText(self.win, "Student ID:", self.student_id, 20, 60)

        self.lesson_id = IntVar()
        LabelWithText(self.win, "Lesson ID:", self.lesson_id, 20, 100)

        self.score = IntVar()
        LabelWithText(self.win, "Score:", self.score, 20, 140)

        self.table = ttk.Treeview(self.win, columns=[1, 2, 3, 4], show='headings')
        self.table.heading(1, text='ID')
        self.table.heading(2, text='Student ID')
        self.table.heading(3, text='Lesson ID')
        self.table.heading(4, text='Score')

        for col in range(1, 5):
            self.table.column(col, width=100)

        self.table.bind("<<TreeviewSelect>>", self.select_exercise)
        self.table.place(x=220, y=60)

        Button(self.win, text="New", command=self.reset_form).place(x=220, y=390)
        Button(self.win, text="Save", command=self.save_click).place(x=270, y=390)
        Button(self.win, text="Edit", command=self.edit_click).place(x=320, y=390)
        Button(self.win, text="Delete", command=self.delete_click).place(x=370, y=390)

        self.reset_form()
        self.win.mainloop()
