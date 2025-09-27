from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk


from controller.project_controller import ProjectController
from model.entity.project import Project
from view.component.label_with_text import LabelWithText



class ProjectView:
    def reset_form(self):
        self.project_id.set(0)
        self.project_name.set("")
        self.file_url.set("")
        self.date_time.set("")
        self.score.set("")

        status, project_list = self.project_controller.find_all()
        if status:
            self.show_data_on_table(project_list)

    def show_data_on_table(self, project_list):
        for item in self.table.get_children():
            self.table.delete(item)


        if project_list:
            for project in project_list:
                self.table.insert("", 'end', values = project.to_tuple())


    def select_project(self):
        focus_item = self.table.focus()
        if not focus_item:
            return
        selected_project= self.table.item(self.table.focus())["values"]
        if selected_project:
            project =Project(*selected_project[1:])
            project.project_id = selected_project[0]
            self.project_id.set(project.project_id)
            self.project_name.set(project.project_name)
            self.file_url.set(project.file_url)
            self.date_time.set(project.date_time)
            self.score.set(project.score)


    def search(self):
        status , project_list= self.project_controller.find_by_id(self.search_project_id.get())

        if status:
            self.show_data_on_table(project_list)

    def save_click(self):
        status, message = self.project_controller.save(
            self.project_id.get(), self.project_name.get(), self.file_url.get(),
            self.date_time.get(), self.score.get(),

        )
        if status:
            msg.showinfo("Success", f"{message}project Saved Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}project Saved Error")

    def edit_click(self):
        status, message = self.project_controller.edit(self.project_id.get(), self.project_name.get(),
                                                      self.file_url.get(), self.date_time.get(), self.score.get())
        if status:
            msg.showinfo("Success", f"{message}project edit Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}project edit Error")

    def delete_click(self):
        status, message = self.project_controller.delete(self.project_id.get())
        if status:
            msg.showinfo("Success", f"{message}project delete Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}project delete Error")


    def __init__(self):
        self.project_controller = ProjectController()
        self.win=Tk()
        self.win.title("project profile")
        self.win.geometry("700x350")

        self.project_id = IntVar()
        LabelWithText(self.win, "project ID:", self.project_id ,20,20,state="readonly")


        self.project_name = StringVar()
        LabelWithText(self.win, "name:", self.project_name ,20,60)

        self.file_url = StringVar()
        LabelWithText(self.win, "file_url:", self.file_url ,20,100)

        self.date_time = StringVar()
        LabelWithText(self.win, "start_date:", self.date_time ,20,140)

        self.score = StringVar()
        LabelWithText(self.win, "end_date:", self.score ,20,200)


        self.search_project_id = IntVar()
        LabelWithText(self.win, "search project id:", self.search_project_id ,220,20)


        self.table= ttk.Treeview(self.win,columns=[1,2,3,4,5],show='headings')
        self.table.heading(1, text='project ID')
        self.table.heading(2, text='project nam')
        self.table.heading(3, text='file url')
        self.table.heading(4, text='date time')
        self.table.heading(5, text='score')



        self.table.column(1, width=70)
        self.table.column(2, width=80)
        self.table.column(3, width=110)
        self.table.column(4, width=70)
        self.table.column(5, width=70)


        self.table.bind("<<TreeviewSelect>>", self.select_project())
        self.table.place(x=220,y=60)

        Button(self.win, text="New Person", command=self.reset_form).place(x=220,y=290)
        Button(self.win, text="Save", command=self.save_click).place(x=300, y=290)
        Button(self.win, text="edit", command=self.edit_click).place(x=340, y=290)
        Button(self.win, text="delete", command=self.delete_click).place(x=380, y=290)

        self.reset_form()
        self.win.mainloop()




