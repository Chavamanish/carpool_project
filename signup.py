from tkinter import *
from tkinter import messagebox
import mysql.connector
def add_to_db():
    fn=f_n.get()
    ln=l_n.get()
    pswd=p_swd.get()
    email_id=e_id.get()
    phone_num=phone.get()
    mysql_db=mysql.connector.connect(host="localhost",user="root",password="@whisper301",database="carpool")
    mycursor=mysql_db.cursor()
    sql="INSERT INTO CUSTOMERS(first_name,last_name,email_id,phone_num,password,cust_id) VALUES(%s, %s, %s, %s, %s, %s)"
    data=(fn,ln,email_id,phone_num,pswd,0)
    try:
        mycursor.execute(sql,data)
        mysql_db.commit()
        messagebox.showinfo("data inserted")
    except:
        mysql_db.rollback()
main_window=Tk()
main_window.title("SIGNUP PAGE")
main_window.resizable(True,True)
f_n=StringVar()
l_n=StringVar()
u_n=StringVar()
p_swd=StringVar()
e_id=StringVar()
phone=StringVar()
first_name_label=Label(main_window,text="First Name").pack()
first_name=Entry(main_window,textvariable=f_n)
first_name.pack()
last_name_label=Label(main_window,text="Last Name").pack()
last_name=Entry(main_window,textvariable=l_n)
last_name.pack()
email_label=Label(main_window,text="E-mail").pack()
email=Entry(main_window,textvariable=e_id)
email.pack()
phone_no_label=Label(main_window,text="Phone no").pack()
phone_no=Entry(main_window,textvariable=phone)
phone_no.pack()
password_label=Label(main_window,text="Password").pack()
password=Entry(main_window,textvariable=p_swd)
password.pack()

Button(main_window,text="signup",bg="orange",fg="white",width=20,command=add_to_db).pack()
main_window.mainloop()

