import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_name_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found")
    else:
        if website in data:
            messagebox.showinfo(website, "The username is " + data[website]["username"] + " and the password is " + data[website]["password"])
            website_name_entry.delete(0, END)
        else:
            messagebox.showerror("Error", "No data found")
   

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """
    Generates a random password.
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """
    Saves the password to a file.
    """
    webiste = website_name_entry.get()
    username = user_name_entry.get()
    password = password_entry.get()
    new_data = {
        webiste:{
            "username": username,
            "password": password
        }
    }

    if webiste == "" or username == "" or password == "":
        messagebox.showerror("Error", "Please fill in all fields")
    else:
        is_ok = messagebox.askokcancel("Save", "The Username for " + webiste +
                                       " is " + username + " and the password is " + password + "\n\n" + "Would you like to save it?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file)
            finally:
                website_name_entry.delete(0, END)
                password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=20)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)


website_name = Label(text="Website:")
website_name.grid(row=1, column=0)
user_name = Label(text="Email/Username:")
user_name.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

website_name_entry = Entry(width=30)
website_name_entry.grid(row=1, column=1)
website_name_entry.focus()
user_name_entry = Entry(width=48)
user_name_entry.grid(row=2, column=1, columnspan=2)
user_name_entry.insert(0, "jonyjas@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2)
add = Button(text="Add", width=35, command=save)
add.grid(row=4, column=1, columnspan=2)
search = Button(text="Search", width=13, command=find_password)
search.grid(row=1, column=2)


window.mainloop()