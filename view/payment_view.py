from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk


from controller.payment_controller import PaymentController
from model.entity.payment import Payment
from view.component.label_with_text import LabelWithText



class PaymentView:
    def reset_form(self):
        self.person_id.set(0)
        self.amount.set(0)
        self.title.set("")
        self.payment_type.set("")
        self.pay_date.set("")
        self.description.set("")

        status, payment_list = self.payment_controller.find_all()
        if status:
            self.show_data_on_table(payment_list)

    def show_data_on_table(self, payment_list):
        for item in self.table.get_children():
            self.table.delete(item)


        if payment_list:
            for payment in payment_list:
                self.table.insert("", 'end', values = payment.to_tuple())


    def select_payment(self):
        focus_item = self.table.focus()
        if not focus_item:
            return
        selected_payment= self.table.item(self.table.focus())["values"]
        if selected_payment:
            payment =Payment(*selected_payment[1:])
            payment.person_id = selected_payment[0]
            self.person_id.set(payment.person_id)
            self.amount.set(payment.amount)
            self.title.set(payment.title)
            self.payment_type.set(payment.payment_type)
            self.pay_date.set(payment.pay_date)
            self.description.set(payment.description)


    def search(self):
        status , payment_list= self.payment_controller.find_by_id(self.search_person_id.get())

        if status:
            self.show_data_on_table(payment_list)

    def save_click(self):
        status, message = self.payment_controller.save(
            self.person_id.get(), self.title.get(), self.amount.get(),
            self.payment_type.get(), self.pay_date.get(),
            self.description.get()
        )
        if status:
            msg.showinfo("Success", f"{message}payment Saved Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}payment Saved Error")

    def edit_click(self):
        status, message = self.payment_controller.edit(self.person_id.get(), self.title.get(), self.amount.get(),
            self.payment_type.get(), self.pay_date.get(),
            self.description.get())
        if status:
            msg.showinfo("Success", f"{message}payment edit Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}payment edit Error")

    def delete_click(self):
        status, message = self.payment_controller.delete(self.person_id.get())
        if status:
            msg.showinfo("Success", f"{message}payment delete Successfully")
            self.reset_form()

        else:
            msg.showerror("Error", f"{message}payment delete Error")


    def __init__(self):
        self.payment_controller = PaymentController()
        self.win=Tk()
        self.win.title("payment profile")
        self.win.geometry("900x450")

        self.person_id = IntVar()
        LabelWithText(self.win, "person_id:", self.person_id ,20,20,state="readonly")


        self.amount = StringVar()
        LabelWithText(self.win, "amount:", self.amount ,20,60)

        self.teacher = StringVar()
        LabelWithText(self.win, "teacher:", self.teacher ,20,100)

        self.title = StringVar()
        LabelWithText(self.win, "title:", self.title ,20,140)

        self.pay_date = StringVar()
        LabelWithText(self.win, "pay_date:", self.pay_date ,20,200)

        self.description = StringVar()
        LabelWithText(self.win, "description:", self.description ,20,240)

        self.payment_type = StringVar()
        LabelWithText(self.win, "payment_type:", self.payment_type, 20, 240)




        self.table= ttk.Treeview(self.win,columns=[1,2,3,4,5,6],show='headings')
        self.table.heading(1, text='person ID')
        self.table.heading(2, text='amount')
        self.table.heading(3, text='title')
        self.table.heading(4, text='payment type')
        self.table.heading(5, text='pay_date Date')
        self.table.heading(6, text='description')



        self.table.column(1, width=70)
        self.table.column(2, width=70)
        self.table.column(3, width=70)
        self.table.column(4, width=70)
        self.table.column(5, width=70)
        self.table.column(6, width=70)


        self.table.bind("<<TreeviewSelect>>", self.select_payment())
        self.table.place(x=220,y=60)

        Button(self.win, text="New Payment", command=self.reset_form).place(x=220,y=390)
        Button(self.win, text="Save", command=self.save_click).place(x=300, y=390)
        Button(self.win, text="edit", command=self.edit_click).place(x=340, y=390)
        Button(self.win, text="delete", command=self.delete_click).place(x=380, y=390)

        self.reset_form()
        self.win.mainloop()




