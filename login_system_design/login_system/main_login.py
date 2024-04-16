from tkinter import *
from PIL import ImageTk #pip install pillow
from tkinter import messagebox

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+350+200")
        self.root.resizable(False, False)

        # Background Image
        self.bg = ImageTk.PhotoImage(file="image/maxresdefault.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0 ,y=0, relwidth=1, relheight=1)

        # Login Frame
        Frame_login = Frame(self.root, bg="white", highlightthickness=1, highlightbackground="black")
        Frame_login.place(x=380 , y=150, width=450, height=400)

        # Title & Subtitle
        title = Label(Frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=110, y=40)
        subtitle = Label(Frame_login, text="Members Login Area", font=("Goudy old Style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=110, y=110)

        # Username
        lbl_username = Label(Frame_login, text="Username", font=("Goudy old Style", 15, "bold"), fg="grey", bg="white").place(x=110, y=150)
        self.username = Entry(Frame_login, font=("Goudy old Style", 15), bg="#E7E6E6")
        self.username.place(x=110, y=180, width=240, height=30)

        # Password
        lbl_password = Label(Frame_login, text="Password", font=("Goudy old Style", 15, "bold"), fg="grey", bg="white").place(x=110, y=210)
        self.password = Entry(Frame_login, font=("Goudy old Style", 15), bg="#E7E6E6")
        self.password.place(x=110, y=240, width=240, height=30)

        # Button
        forget = Button(Frame_login, text="forget password?", bd=0, font=("Goudy old Style", 12), fg="#6162FF", bg="white").place(x=110, y=280)
        submit = Button(Frame_login,command=self.check_function, text="Login", bd=0, font=("Goudy old Style", 15), bg="#6162FF", fg="white").place(x=110, y=320, height=40)

    def check_function(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        elif self.username.get()!="hao666" or self.password.get()!="880630":
            messagebox.showerror("Error", "Invalid Username or Password",parent=self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome{self.username.get()}")


root = Tk()
obj = Login(root)
root.mainloop()