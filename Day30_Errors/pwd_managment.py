from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# YELLOW = "#f7f5dd" 

# ---------------------------- SEARCH FUCNTION ------------------------------- #

def find_password():
    
    site_word = input_web.get()
    encontrado = False
    try:
        with open("pwd_data.json", "r") as data_file:
                    #Reading data
                    data = json.load(data_file)
        
        for key, value in data.items():
            if site_word in key:
                checked_email = value.get("email")
                checked_password = value.get("password")
                messagebox.showinfo(
                     title= site_word, 
                     message= f"Email: {checked_email} \nPassword:{checked_password}"
                      )
                encontrado = True
            
        if not encontrado:
            messagebox.showinfo(title="Error", message= "Data Not Found")            



    except FileNotFoundError:
         messagebox.showerror(title="Error", message="Archivo no encontrado")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # x = [new_item for item in list]      "EXPRESION"

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    input_password.insert(0, password)
    pyperclip.copy(password)
    


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = input_web.get()
    email = input_user.get()
    password = input_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
     
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title= "ATTENTION!", message="Please don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Comfirm the details? \nEmail: {email} \nWebsite: {website} \nPassword: {password}")
        if is_ok: 
            try: 
                with open("pwd_data.json", "r") as data_file:
                    #Reading data
                    data = json.load(data_file)
            except FileNotFoundError:
                    with open("pwd_data.json", "w") as data_file:
                        json.dump(new_data, data_file, indent=4)

            else:                        
                #Updating data
                data.update(new_data)
                with open("pwd_data.json", "w") as data_file:
                    #Saving updated data
                    json.dump(data, data_file, indent=4)

            finally:
                input_web.delete(0, END)
                input_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(column=1, row=0)

# ---------- WEBSITE ROW SETTINGS ------------
web_label = Label(text="Website: ")
web_label.config(padx=5, pady=5)
web_label.grid(column=0, row=1)

input_web = Entry(width=21)
input_web.grid(column=1, row=1)
input_web.focus()

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

# ---------- USER/EMAIL SETTINGS ------------

user_label = Label(text="Email/Username: ")
user_label.config(padx=5, pady=5)
user_label.grid(column=0, row=2)

input_user = Entry(width=40)
input_user.grid(column=1, row=2, columnspan=2)
input_user.insert(0, "dmaximus80@yahoo.com")

# ---------- PASSWORD ROW SETTINGS ------------

password_label = Label(text="Password: ")
password_label.config(padx=5, pady=5)
password_label.grid(column=0, row=3)
input_password = Entry(width=21)
input_password.grid(column=1, row=3)

button = Button(text="Generate Password", width=15, command=generate_password)
button.grid(column=2, row=3)

# ---------- BUTTON ADD SETTINGS ------------

add_button = Button(text="Add", width=32, command=save)
add_button.config(pady=2)
add_button.grid(column=1, row=5, columnspan=2)


#---------------------------------
space_label = Label(text=" ")
space_label.grid(column=1, row=4)

window.mainloop()

