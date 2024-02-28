from tkinter import *
from tktooltip import ToolTip
from modules import backend as bk, superadmin as sp, admin as ad, faculty, student
from tkinter import messagebox as mb, simpledialog as sd
from tkcalendar import DateEntry


class Login():
    def __init__(self, win):
        self.win = win
        # self.win.geometry("500x700+500+300")  # Change the geometry of the wind
        self.center_window()  # Call the function to center the window
        self.login_gui()

    def center_window(self):
        # Get the width and height of the screen
        screen_width = self.win.winfo_screenwidth()
        screen_height = self.win.winfo_screenheight()

        # Calculate the x and y coordinates to place the window at the center of the screen
        x = (screen_width - 500) // 2  # 500 is the width of the window
        y = (screen_height - 500) // 2  # 700 is the height of the window

        # Set the geometry of the window to place it at the center
        self.win.geometry(f"500x500+{x}+{y}")

    def login_gui(self):
        self.username = StringVar()
        self.password = StringVar()

        self.login_frame = Frame(self.win)

        Label(self.login_frame, text="LOGIN", font=("Segoe UI Black", 25),
              ).place(x=160, y=10)
        Label(self.login_frame, text="Username :", font=("Century", 15),
              ).place(x=10, y=100)
        self.uname_txt = Entry(self.login_frame, font=(
            "Cambria", 27), background="white", width=20, bd=1, relief="solid", textvariable=self.username)
        self.uname_txt.place(x=15, y=145)
        Label(self.login_frame, text="Password :", font=("Century", 15),
              ).place(x=10, y=220)
        self.pass_txt = Entry(self.login_frame, font=("Cambria", 27),
                              background="white", show="•", width=20, bd=1, relief="solid", textvariable=self.password)
        self.pass_txt.place(x=15, y=270)
        self.reset_btn = Button(
            self.login_frame, text="Reset", font=(15),
               relief="ridge", bd=2, command=self.reset_field)
        self.reset_btn.place(x=150, y=390)
        Button(self.login_frame, text="Login", font=(15),
               relief="ridge", bd=2, command=self.login).place(x=20, y=390)
        self.count = IntVar()
        self.show_pass = Checkbutton(self.login_frame, text="Show Password", variable=self.count,
                                     font=("Calibri", 14, "bold"), command=self.show_password).place(x=16, y=330)
        ToolTip(self.reset_btn, msg="Reset the field", follow=True)
        self.forgot = Label(self.login_frame, text="Forgot Username/Password ?",
                            foreground="blue", font=("Calibri", 12, "bold", "underline"))
        self.forgot.place(x=260, y=330)
        self.forgot.bind("<Button-1>", self.__forgot_frame)

        self.login_frame.pack(expand=True, fill=BOTH)

    def reset_field(self):
        self.username.set("")
        self.password.set("")

    def __forgot_frame(self, e):
        self.login_frame.pack_forget()
        self.forgot_frame = Frame(self.win)
        self.forgot_frame.pack(expand=True, fill="both")
        self.backlogin_frame = Label(self.forgot_frame, text="Back to Login",
                                     foreground="blue", font=("Calibri", 14, "bold", "underline"))
        self.backlogin_frame.place(x=10, y=560)
        self.backlogin_frame.bind("<Button-1>", lambda e: self.login_gui())
        Label(self.forgot_frame, text="Forgot Username/Password", font=("lucida",
              18, "bold")).place(x=100, y=10)
        self.id = StringVar()
        Label(self.forgot_frame, text="Enter Your ID :", font=(
            "Century", 13)).place(x=10, y=70)
        Label(self.forgot_frame, text="Enter Your Date Of Birth : (mm/dd/yyyy) format",
              font=("Century", 13)).place(x=10, y=140)
        Entry(self.forgot_frame, textvariable=self.id, font=(
            "Cambria", 19), relief="solid", bd=2).place(x=10, y=100)
        self.dob = DateEntry(self.forgot_frame, selectmode="day", font=(
            "Cambria", 16), bd=2, relief="solid")
        self.dob.place(x=10, y=170)
        Button(self.forgot_frame, text="Get Username", font=(15),
               relief="ridge", bd=2, command=self.__get_username).place(x=100, y=240)
        Button(self.forgot_frame, text="Forgot Password", font=(15),
               relief="ridge", bd=2, command=self.__set_password).place(x=270, y=240)

    def validation(self):
        query = '''select uname,typeofuser from login_details where id=%s'''
        data = bk.fetch_details(query, (self.id.get(),))
        if len(data) == 0:
            mb.showinfo("No User", f"No User Found with ID {self.id.get()}")
        elif data[0][1] == "student":
            mb.showinfo(
                "Access Denied", "Hello You are Student\nContact to Admin Office to set your username or password")
            self.login_gui()
        elif data[0][1] == "faculty":
            facultydob = 'select dob from faculty where id=%s;'
            data1 = bk.fetch_details(facultydob, (self.id.get(),))
            if data1[0][0] != self.dob.get_date():
                mb.showinfo("Error", "Incorrect Date of birth")
            else:
                return True
        elif data[0][1] == "admin":
            return True

    def __get_username(self):
        if self.validation():
            uname = bk.fetch_details(
                '''select uname from login_details where id=%s''', (self.id.get(),))[0][0]
            mb.showinfo("Username", f"Your Username is {uname}")

    def __set_password(self):
        if self.validation():
            self.password_label = Label(
                self.forgot_frame, bg="#4bf542", height=14, width=70)
            self.password_label.place(x=0, y=310)
            self.new_password = StringVar()
            self.reenter_password = StringVar()
            self.new_password_txt = Entry(self.password_label, font=(
                "Cambria", 15), background="white", show="•", width=25, bd=1, relief="solid", textvariable=self.new_password)
            self.new_password_txt.place(x=10, y=30)
            self.reenter_pass_txt = Entry(self.password_label, font=(
                "Cambria", 15), background="white", show="•", width=25, bd=1, relief="solid", textvariable=self.reenter_password)
            self.reenter_pass_txt.place(x=10, y=100)
            Label(self.password_label, text="Enter New Password :", font=(
                "Century", 13)).place(x=10, y=0)
            Label(self.password_label, text="Re-enter Password :",
                  font=("Century", 13)).place(x=10, y=70)
            Button(self.password_label, text="UPDATE", font=("Verdana", 16), bg="#ecfc05",
                   relief="raised", bd=2, command=self.__change_password).place(x=30, y=140)
            self.show_pass = Checkbutton(self.password_label, text="Show Password", variable=self.count,
                                         font=("Calibri", 13), command=self.show_password1).place(x=280, y=60)

    def show_password1(self):
        if self.count.get() == 1:
            self.new_password_txt.configure(show="")
            self.reenter_pass_txt.configure(show="")
        else:
            self.new_password_txt.configure(show="•")
            self.reenter_pass_txt.configure(show="•")

    def __change_password(self):
        if self.new_password.get() != self.reenter_password.get():
            mb.showerror("Error", "The Passwords are Not matching")
        else:
            query = 'update login_details set password=sha(%s) where id=%s'
            val = (self.new_password.get(), self.id.get())
            if bk.execute_query(query, val):
                mb.showinfo("Success", "successfully changed the password")
                self.login_gui()
            else:
                mb.showerror("Server Error", "Some Error Occured")

    def show_password(self):
        if self.count.get() == 1:
            self.pass_txt.configure(show="")
        else:
            self.pass_txt.configure(show="•")

    def login(self):
        self.user_name = self.username.get()
        self.pass_word = self.password.get()
        query = "select * from login_details where uname=%s and password=sha1(%s);"
        val = (self.user_name, self.pass_word)
        result = bk.fetch_details(query, val)
        if len(result) == 0:
            mb.showerror(
                "No User", "No Username or Password Found\nPlease Check Your Username or password")
        else:
            result = result[0]
            typeofuser = result[3]
            id = result[0]
            self.change_frame(typeofuser, result)

    def change_frame(self, type, user_tuple):

        if type == "superadmin":
            self.login_frame.pack_forget()
            sp.SA(self.win, user_tuple)
        elif type == "admin":
            self.login_frame.pack_forget()
            ad.admin(self.win, user_tuple)
        elif type == "faculty":
            self.login_frame.pack_forget()
            faculty.Faculty(self.win, user_tuple)
        elif type == "student":
            self.login_frame.pack_forget()
            student.Student(self.win, user_tuple)
