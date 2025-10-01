from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk

from controller.attendance_controller import AttendanceController
from model.entity.attendance import Attendance
from view.component.label_with_text import LabelWithText


class AttendanceView:
    def reset_form(self):
        self.id.set(0)
        self.student_id.set(0)
        self.status.set("")
        self.date.set("")

        status, attendance_list = self.attendance_controller.find_all()
        if status:
            self.show_data_on_table(attendance_list)

    def show_data_on_table(self, attendance_list):
        for item in self.table.get_children():
            self.table.delete(item)

        if attendance_list:
            for attendance in attendance_list:
                self.table.insert("", 'end', values=attendance.to_tuple())

    def select_attendance(self, event=None):
        focus_item = self.table.focus()
        if not focus_item:
            return
        selected = self.table.item(focus_item)["values"]
        if selected:
            att = Attendance(*selected[1:])
            att.id = selected[0]
            self.id.set(att.id)
            self.student_id.set(att.student_id)
            self.status.set(att.status)
            self.date.set(att.date)

    def search(self):
        status, att = self.attendance_controller.find_by_id(self.search_id.get())
        if status:
            self.show_data_on_table([att])

    def save_click(self):
        status, message = self.attendance_controller.save(
            self.student_id.get(), self.status.get(), self.date.get()
        )
        if status:
            msg.showinfo("Success", "Attendance Saved Successfully")
            self.reset_form()
        else:
            msg.showerror("Error", f"{message} Attendance Save Error")

    def edit_click(self):
        status, message = self.attendance_controller.edit(
            self.id.get(), self.student_id.get(), self.status.get(), self.date.get()
        )
        if status:
            msg.showinfo("Success", "Attendance Edited Successfully")
            self.reset_form()
        else:
            msg.showerror("Error", f"{message} Attendance Edit Error")

    def delete_click(self):
        status, message = self.attendance_controller.delete(self.id.get())
        if status:
            msg.showinfo("Success", "Attendance Deleted Successfully")
            self.reset_form()
        else:
            msg.showerror("Error", f"{message} Attendance Delete Error")

    def __init__(self):
        self.attendance_controller = AttendanceController()
        self.win = Tk()
        self.win.title("Attendance Management")
        self.win.geometry("900x450")

        self.id = IntVar()
        LabelWithText(self.win, "ID:", self.id, 20, 20, state="readonly")

        self.student_id = IntVar()
        LabelWithText(self.win, "Student ID:", self.student_id, 20, 60)

        self.status = StringVar()
        LabelWithText(self.win, "Status:", self.status, 20, 100)

        self.date = StringVar()
        LabelWithText(self.win, "Date:", self.date, 20, 140)

        self.table = ttk.Treeview(self.win, columns=[1, 2, 3, 4], show='headings')
        self.table.heading(1, text='ID')
        self.table.heading(2, text='Student ID')
        self.table.heading(3, text='Status')
        self.table.heading(4, text='Date')

        for col in range(1, 5):
            self.table.column(col, width=100)

        self.table.bind("<<TreeviewSelect>>", self.select_attendance)
        self.table.place(x=220, y=60)

        Button(self.win, text="New", command=self.reset_form).place(x=220, y=390)
        Button(self.win, text="Save", command=self.save_click).place(x=270, y=390)
        Button(self.win, text="Edit", command=self.edit_click).place(x=320, y=390)
        Button(self.win, text="Delete", command=self.delete_click).place(x=370, y=390)

        self.reset_form()
        self.win.mainloop()
