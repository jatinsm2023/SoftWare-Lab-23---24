import tkinter as tk
from tkinter import messagebox
import re
from tkinter import ttk
import json


class Person:
    def __init__(self, userid, password):
        self.userid = userid
        self.password = password
        self.count = 0


class Teacher(Person):

    def __init__(self, userid, password, name):
        super().__init__(userid, password)
        self.name = name
        self.role = "Teacher"


class Student(Person):

    def __init__(self, userid, password, name):
        super().__init__(userid, password)
        self.name = name


class PGStudent(Student):

    def __init__(self, userid, password, name, specialization):
        super().__init__(userid, password, name)
        self.specialization = specialization
        self.role = "PGStudent"


class UGStudent(Student):

    def __init__(self, userid, password, name, dept):
        super().__init__(userid, password, name)
        self.dept = dept
        self.role = "UGStudent"


def write_json(data, fname="data.json"):
    with open(fname, "w") as f:
        json.dump(data, f, indent=4)


with open("data.json") as f:
    data = json.load(f)

Teacher_Collection = data["Teacher"]
UGStudent_Collection = data["UGStudent"]
PGStudent_Collection = data["PGStudent"]


def User_Registration(user, role):
    if role == "Teacher":
        Teacher_Collection.append(user)
    elif role == "PGStudent":
        PGStudent_Collection.append(user)
    elif role == "UGStudent":
        UGStudent_Collection.append(user)
    write_json(data)


def Sign_into_System(userid, password):
    for user in Teacher_Collection:
        if user["userid"] == userid and user["password"] == password:
            return user
    for user in PGStudent_Collection:
        if user["userid"] == userid and user["password"] == password:
            return user
    for user in UGStudent_Collection:
        if user["userid"] == userid and user["password"] == password:
            return user
    return None


def Teacher_Update(userid, password, new_userid, new_password, name):
    for user in Teacher_Collection:
        if user["userid"] == userid and user["password"] == password:
            user["userid"] = new_userid
            user["password"] = new_password
            user["name"] = name
            write_json(data)
            messagebox.showinfo("Success", "Successfully Updated")
            return
    messagebox.showerror("Error", "User Not Found")


def PGStudent_Update(userid, password, new_userid, new_password, name, specialization):
    for user in PGStudent_Collection:
        if user["userid"] == userid and user["password"] == password:
            user["userid"] = new_userid
            user["password"] = new_password
            user["name"] = name
            user["specialization"] = specialization
            write_json(data)
            messagebox.showinfo("Success", "Successfully Updated")
            return
    messagebox.showerror("Error", "User Not Found")


def UGStudent_Update(userid, password, new_userid, new_password, name, dept):
    for user in UGStudent_Collection:
        if user["userid"] == userid and user["password"] == password:
            user["userid"] = new_userid
            user["password"] = new_password
            user["name"] = name
            user["dept"] = dept
            write_json(data)
            messagebox.showinfo("Success", "Successfully Updated")
            return
    messagebox.showerror("Error", "User Not Found")


def exist(userid, password):
    for user in Teacher_Collection:
        if user["userid"] == userid and user["password"] == password:
            return True
    for user in PGStudent_Collection:
        if user["userid"] == userid and user["password"] == password:
            return True
    for user in UGStudent_Collection:
        if user["userid"] == userid and user["password"] == password:
            return True
    return False


def Deactivate_User_Account(userid, password, role):
    if role == "Teacher":
        for user in Teacher_Collection:
            if user["userid"] == userid and user["password"] == password:
                Teacher_Collection.remove(user)
                write_json(data)
                messagebox.showinfo("Success", "Successfully Deactivated")
                return
    elif role == "PGStudent":
        for user in PGStudent_Collection:
            if user["userid"] == userid and user["password"] == password:
                PGStudent_Collection.remove(user)
                write_json(data)
                messagebox.showinfo("Success", "Successfully Deactivated")
                return
    elif role == "UGStudent":
        for user in UGStudent_Collection:
            if user["userid"] == userid and user["password"] == password:
                UGStudent_Collection.remove(user)
                write_json(data)
                messagebox.showinfo("Success", "Successfully Deactivated")
                return
    messagebox.showerror("Error", "User Not Found")


def is_strong_password(password):
    errors = []

    if len(password) < 8:
        errors.append("Password should be at least 8 characters long.")

    if not any(c.isupper() for c in password):
        errors.append("Password should contain at least one uppercase letter.")

    if not any(c.islower() for c in password):
        errors.append("Password should contain at least one lowercase letter.")

    if not any(c.isdigit() for c in password):
        errors.append("Password should contain at least one digit.")

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        errors.append(
            'Password should contain at least one special character (!@#$%^&*(),.?":{}|<>).'
        )

    if errors:
        messagebox.showerror("Password Strength Error", "\n".join(errors))
        return False
    return True


regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"


def checkmail(email):
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def user_by_id(userid):
    for user in Teacher_Collection:
        if user["userid"] == userid:
            return user
    for user in PGStudent_Collection:
        if user["userid"] == userid:
            return user
    for user in UGStudent_Collection:
        if user["userid"] == userid:
            return user
    return None


def Register(frame, role):
    frame.destroy()
    frame = ttk.Frame(root)
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    label_user_id = tk.Label(frame, text="User ID:")
    label_user_id.pack()
    entry_user_id = tk.Entry(frame)
    entry_user_id.pack()

    label_password = tk.Label(frame, text="Password:")
    label_password.pack()

    entry_password = tk.Entry(frame, show="*")  # Show '*' for password
    entry_password.pack()

    def register_users():
        if not checkmail(entry_user_id.get()):
            messagebox.showerror("Error", "User ID is not an email. Please try again.")
            return
        if not is_strong_password(entry_password.get()):
            messagebox.showerror(
                "Error", "Password is not strong. Please follow the password criteria."
            )
            return
        elif exist(entry_user_id.get(), entry_password.get()) == True:
            messagebox.showerror("Error", "This Account already Exists")
        else:
            if role == "Teacher":
                user = {
                    "userid": entry_user_id.get(),
                    "password": entry_password.get(),
                    "name": "",
                    "role": "Teacher",
                    "count": 0,
                }
            elif role == "PGStudent":
                user = {
                    "userid": entry_user_id.get(),
                    "password": entry_password.get(),
                    "name": "",
                    "specialization": "",
                    "role": "PGStudent",
                    "count": 0,
                }
            elif role == "UGStudent":
                user = {
                    "userid": entry_user_id.get(),
                    "password": entry_password.get(),
                    "name": "",
                    "dept": "",
                    "role": "UGStudent",
                    "count": 0,
                }
            User_Registration(user, role)
            messagebox.showinfo("Success", "User registered successfully!")
            if role == "Teacher":
                register_button.destroy()
                label_name = tk.Label(frame, text="Name:")
                label_name.pack()

                entry_name = tk.Entry(frame)
                entry_name.pack()

                update_button = tk.Button(
                    frame,
                    text="Update Details",
                    command=lambda: Teacher_Update(
                        user["userid"],
                        user["password"],
                        entry_user_id.get(),
                        entry_password.get(),
                        entry_name.get(),
                    ),
                )
                update_button.pack(pady=10)

                deactivate_button = tk.Button(
                    frame,
                    text="Deactivate User",
                    command=lambda: Deactivate_User_Account(
                        entry_user_id.get(), entry_password.get(), role
                    ),
                )
                deactivate_button.pack(pady=10)

                sign_button = tk.Button(
                    frame, text="Sign In Page", command=lambda: Sign_window(frame)
                )
                sign_button.pack(pady=10)

            elif role == "PGStudent":
                register_button.destroy()
                label_name = tk.Label(frame, text="Name:")
                label_name.pack()

                entry_name = tk.Entry(frame)
                entry_name.pack()

                label_specialization = tk.Label(frame, text="Specialization:")
                label_specialization.pack()

                entry_specialization = tk.Entry(frame)
                entry_specialization.pack()

                update_button = tk.Button(
                    frame,
                    text="Update Details",
                    command=lambda: PGStudent_Update(
                        user["userid"],
                        user["password"],
                        entry_user_id.get(),
                        entry_password.get(),
                        entry_name.get(),
                        entry_specialization.get(),
                    ),
                )
                update_button.pack(pady=10)

                deactivate_button = tk.Button(
                    frame,
                    text="Deactivate User",
                    command=lambda: Deactivate_User_Account(
                        entry_user_id.get(), entry_password.get(), role
                    ),
                )
                deactivate_button.pack(pady=10)

                sign_button = tk.Button(
                    frame, text="Sign In Page", command=lambda: Sign_window(frame)
                )
                sign_button.pack(pady=10)

            elif role == "UGStudent":
                register_button.destroy()
                label_name = tk.Label(frame, text="Name:")
                label_name.pack()

                entry_name = tk.Entry(frame)
                entry_name.pack()

                label_dept = tk.Label(frame, text="Department:")
                label_dept.pack()

                entry_dept = tk.Entry(frame)
                entry_dept.pack()

                update_button = tk.Button(
                    frame,
                    text="Update Details",
                    command=lambda: UGStudent_Update(
                        user["userid"],
                        user["password"],
                        entry_user_id.get(),
                        entry_password.get(),
                        entry_name.get(),
                        entry_dept.get(),
                    ),
                )
                update_button.pack(pady=10)

                deactivate_button = tk.Button(
                    frame,
                    text="Deactivate User",
                    command=lambda: Deactivate_User_Account(
                        entry_user_id.get(), entry_password.get(), role
                    ),
                )
                deactivate_button.pack(pady=10)

                sign_button = tk.Button(
                    frame, text="Sign In Page", command=lambda: Sign_window(frame)
                )
                sign_button.pack(pady=10)

    register_button = tk.Button(frame, text="Register", command=register_users)
    register_button.pack(pady=10)


def User_Register_window(frame):
    frame.destroy()
    frame = ttk.Frame(root)
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    label_role = tk.Label(frame, text="Register As: ")
    label_role.pack()

    button1 = tk.Button(
        frame, text="Teacher", command=lambda: Register(frame, "Teacher")
    )
    button1.pack(pady=10)

    button2 = tk.Button(
        frame, text="PG-Student", command=lambda: Register(frame, "PGStudent")
    )
    button2.pack(pady=10)

    button3 = tk.Button(
        frame, text="UG-Student", command=lambda: Register(frame, "UGStudent")
    )
    button3.pack(pady=10)


def Sign_window(frame):
    frame.destroy()
    frame = ttk.Frame(root)
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    label_user_id = tk.Label(frame, text="User ID:")
    label_user_id.pack()

    entry_user_id = tk.Entry(frame)
    entry_user_id.pack()

    label_password = tk.Label(frame, text="Password:")
    label_password.pack()

    entry_password = tk.Entry(frame, show="*")  # Show '*' for password
    entry_password.pack()

    def submit_form():
        user_id = entry_user_id.get()
        password = entry_password.get()
        if Sign_into_System(user_id, password) == None:
            messagebox.showerror(
                "Error", "User ID or Password is incorrect. Please try again."
            )
            if user_by_id(user_id) != None:
                user = user_by_id(user_id)
                user["count"] += 1
                write_json(data)
                if user["count"] >= 3:
                    if user["role"] == "Teacher":
                        Teacher_Collection.remove(user)
                    elif user["role"] == "PGStudent":
                        PGStudent_Collection.remove(user)
                    elif user["role"] == "UGStudent":
                        UGStudent_Collection.remove(user)
                    write_json(data)
                    messagebox.showerror(
                        "Error",
                        "You have exceeded the maximum number of attempts. Your account has been deactivated.",
                    )
                    messagebox.showinfo(
                        "Info", f"{user_id}'s account has been deactivated."
                    )
            return
        else:
            messagebox.showinfo("Success", "Login Successful!")
            user = Sign_into_System(user_id, password)
            if user["role"] == "Teacher":
                submit_button.destroy()
                label_name = tk.Label(frame, text="Name:")
                label_name.pack()
                entry_name = tk.Entry(frame, textvariable="Enter New Name")
                entry_name.pack()

                update_button = tk.Button(
                    frame,
                    text="Update Details",
                    command=lambda: Teacher_Update(
                        user["userid"],
                        user["password"],
                        entry_user_id.get(),
                        entry_password.get(),
                        entry_name.get(),
                    ),
                )
                update_button.pack(pady=10)

                deactivate_button = tk.Button(
                    frame,
                    text="Deactivate User",
                    command=lambda: Deactivate_User_Account(
                        entry_user_id.get(), entry_password.get(), "Teacher"
                    ),
                )
                deactivate_button.pack(pady=10)

                sign_button = tk.Button(
                    frame, text="Sign In Page", command=lambda: Sign_window(frame)
                )
                sign_button.pack(pady=10)

            elif user["role"] == "PGStudent":
                submit_button.destroy()
                label_name = tk.Label(frame, text="Name:")
                label_name.pack()

                entry_name = tk.Entry(frame, textvariable="Enter New Name")
                entry_name.pack()

                label_specialization = tk.Label(frame, text="Specialization:")
                label_specialization.pack()

                entry_specialization = tk.Entry(frame)
                entry_specialization.pack()

                update_button = tk.Button(
                    frame,
                    text="Update Details",
                    command=lambda: PGStudent_Update(
                        user["userid"],
                        user["password"],
                        entry_user_id.get(),
                        entry_password.get(),
                        entry_name.get(),
                        entry_specialization.get(),
                    ),
                )
                update_button.pack(pady=10)

                deactivate_button = tk.Button(
                    frame,
                    text="Deactivate User",
                    command=lambda: Deactivate_User_Account(
                        entry_user_id.get(), entry_password.get(), "PGStudent"
                    ),
                )
                deactivate_button.pack(pady=10)

                sign_button = tk.Button(
                    frame, text="Sign In Page", command=lambda: Sign_window(frame)
                )
                sign_button.pack(pady=10)

            elif user["role"] == "UGStudent":
                submit_button.destroy()
                label_name = tk.Label(frame, text="Name:")
                label_name.pack()

                entry_name = tk.Entry(frame, textvariable="Enter New Name")
                entry_name.pack()

                label_dept = tk.Label(frame, text="Department:")
                label_dept.pack()

                entry_dept = tk.Entry(frame)
                entry_dept.pack()

                update_button = tk.Button(
                    frame,
                    text="Update Details",
                    command=lambda: UGStudent_Update(
                        user["user"],
                        user["password"],
                        entry_user_id.get(),
                        entry_password.get(),
                        entry_name.get(),
                        entry_dept.get(),
                    ),
                )
                update_button.pack(pady=10)

                deactivate_button = tk.Button(
                    frame,
                    text="Deactivate User",
                    command=lambda: Deactivate_User_Account(
                        entry_user_id.get(), entry_password.get(), "UGStudent"
                    ),
                )
                deactivate_button.pack(pady=10)

                sign_button = tk.Button(
                    frame, text="Sign In Page", command=lambda: Sign_window(frame)
                )
                sign_button.pack(pady=10)

    submit_button = tk.Button(frame, text="Submit", command=submit_form)
    submit_button.pack(pady=10)


# Main window
root = tk.Tk()
root.title("Academic Unit System")
root.geometry("400x400")

# Frame to hold the content
main_frame = ttk.Frame(root)
main_frame.pack(expand=True, fill="both", padx=10, pady=10)

# Buttons
button1 = tk.Button(
    main_frame, text="Register User", command=lambda: User_Register_window(main_frame)
)
button1.pack(pady=10)

button2 = tk.Button(main_frame, text="Sign In", command=lambda: Sign_window(main_frame))
button2.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
