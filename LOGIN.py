from tkinter import *
from tkinter import messagebox
import mysql.connector
def check_db():
    user_input = user_value.get()
    paswd = password_value.get()
    my_db = mysql.connector.connect(host="localhost", user="root", password="@whisper301", database="carpool")
    cursor = my_db.cursor()
    sql_query="select email_id,phone_num,user_password from new_table where (email_id=%s or phone_num=%s) and (user_password=%s)"
    cursor.execute(sql_query, (user_input,user_input,paswd))
    row=cursor.fetchone()
    if row is None:
        messagebox.showinfo("Invalid user","Either username or password is incorrect")
    else:
        messagebox.showinfo("user found","successful login")

root = Tk()
root.title("LOGIN PAGE")
root.resizable(True, True)
user_value = StringVar()
password_value = StringVar()
input_label = Label(root, text="username/mobile no").pack()
input_val = Entry(root, textvariable=user_value)
input_val.pack()
pswd_label = Label(root, text="Password").pack()
pswd_val = Entry(root, textvariable=password_value)
pswd_val.pack()
Button(root, text="signup", bg="orange", fg="white", width=20, command=check_db).pack()
root.mainloop()
