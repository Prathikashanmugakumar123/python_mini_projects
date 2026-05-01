from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

# -------- DB CONNECTION --------
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ps@123",
    database="ps"
)
cursor = con.cursor()
# -------- COLORS --------
bg_color = "#6A0DAD"
fg_color = "white"

# -------- LOGIN WINDOW --------
login = Tk()
login.title("Livewire Employee Smart Management System")
login.geometry("1500x1300")

# -------- Background --------
img = Image.open("C:\\Users\\ELCOT\\Downloads\\em4.jpg")
img = img.resize((1300, 1200))
bg = ImageTk.PhotoImage(img)

Label(login, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

# -------- LOGIN FRAME --------
frame = Frame(login, bg=bg_color)
frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=500, height=400)

Label(frame, text="Livewire Employee\nSmart Management System",
      bg=bg_color, fg=fg_color, font=("Arial", 20, "bold")).place(x=50, y=40)

Label(frame, text="Username", bg=bg_color, fg=fg_color,
      font=("Arial", 14)).place(x=50, y=150)
user_entry = Entry(frame, font=("Arial", 14), width=25)
user_entry.place(x=180, y=150)

Label(frame, text="Password", bg=bg_color, fg=fg_color,
      font=("Arial", 14)).place(x=50, y=200)
pass_entry = Entry(frame, show="*", font=("Arial", 14), width=25)
pass_entry.place(x=180, y=200)

# -------- ADMIN DASHBOARD --------
def open_admin():
    root = Toplevel()
    root.title("Admin Dashboard")
    root.geometry("1500x1300")

    img2 = Image.open("C:\\Users\\ELCOT\\Downloads\\em3.jpg")
    img2 = img2.resize((1300, 1300))
    bg2 = ImageTk.PhotoImage(img2)

    Label(root, image=bg2).place(x=0, y=0, relwidth=1, relheight=1)

    frame = Frame(root, bg=bg_color)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=900, height=900)

    labels = ["ID", "Name", "Salary", "Address", "Domain", "Leave Days"]
    entries = []

    start_y = 100
    for i, text in enumerate(labels):
        y = start_y + i * 60

        Label(frame, text=text, bg=bg_color, fg=fg_color,
              font=("Arial", 16, "bold")).place(x=200, y=y)

        e = Entry(frame, font=("Arial", 16), width=20)
        e.place(x=400, y=y)

        entries.append(e)

    e1, e2, e3, e4, e5, e6 = entries

    # -------- TEXT BOX --------
    text_box = Text(frame, width=60, height=10, font=("Arial", 12))
    text_box.place(x=200, y=500)

    # -------- FUNCTIONS --------
    def insert():
        cursor.execute("INSERT INTO employee VALUES (%s,%s,%s,%s,%s,%s)",
                       (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get()))
        con.commit()
        messagebox.showinfo("Success", "Inserted")

    def update():
        cursor.execute("UPDATE employee SET name=%s,salary=%s,address=%s,domain=%s,leave_days=%s WHERE id=%s",
                       (e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e1.get()))
        con.commit()
        messagebox.showinfo("Success", "Updated")

    def delete():
        cursor.execute("DELETE FROM employee WHERE id=%s", (e1.get(),))
        con.commit()
        messagebox.showinfo("Success", "Deleted")

    def view():
        cursor.execute("SELECT * FROM employee")
        rows = cursor.fetchall()
        text_box.delete("1.0", END)
        for r in rows:
            text_box.insert(END, str(r) + "\n")

    # -------- BUTTONS --------
    Button(frame, text="Insert", bg="white", fg=bg_color,
           font=("Arial", 14), width=12, command=insert).place(x=200, y=440)

    Button(frame, text="Update", bg="white", fg=bg_color,
           font=("Arial", 14), width=12, command=update).place(x=350, y=440)

    Button(frame, text="Delete", bg="white", fg=bg_color,
           font=("Arial", 14), width=12, command=delete).place(x=500, y=440)

    Button(frame, text="View", bg="white", fg=bg_color,
           font=("Arial", 14), width=12, command=view).place(x=650, y=440)

    root.mainloop()


# -------- EMPLOYEE DASHBOARD --------
def open_employee():
    root = Toplevel()
    root.title("Employee Dashboard")
    root.geometry("1500x1300")

    img3 = Image.open("C:\\Users\\ELCOT\\Downloads\\em3.jpg")
    img3 = img3.resize((1500, 1300))
    bg3 = ImageTk.PhotoImage(img3)

    Label(root, image=bg3).place(x=0, y=0, relwidth=1, relheight=1)

    frame = Frame(root, bg=bg_color)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=800, height=700)

    text_box = Text(frame, width=70, height=20, font=("Arial", 12))
    text_box.place(x=50, y=50)

    def view():
        cursor.execute("SELECT * FROM employee")
        rows = cursor.fetchall()
        text_box.delete("1.0", END)
        for r in rows:
            text_box.insert(END, str(r) + "\n")

    Button(frame, text="View Data", bg="white", fg=bg_color,
           font=("Arial", 14), width=15, command=view).place(x=250, y=500)

    root.mainloop()


# -------- LOGIN FUNCTION --------
def login_check():
    username = user_entry.get()
    password = pass_entry.get()

    if username == "livewire" and password == "123":
        messagebox.showinfo("Login", "Admin Login Success")
        open_admin()

    elif username == "employee" and password == "123":
        messagebox.showinfo("Login", "Employee Login Success")
        open_employee()

    else:
        messagebox.showerror("Error", "Invalid Login")


Button(frame, text="Login", bg="white", fg=bg_color,
       font=("Arial", 14), width=15, command=login_check).place(x=170, y=260)

login.mainloop()