from tkinter import *
import random
import string
from tkinter import Button
from tkinter import messagebox
from tkinter import END

window = Tk()
window.title("Password Manager")
window.configure(padx=20, pady=20, bg="white")
# Website
Label(text="Website:", bg="white").grid(row=1, column=0)
entry = Entry(width=35)
entry.grid(row=1, column=1, columnspan=2)
entry.focus()
# generate password fn
def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    password = ''.join(random.choice(letters + numbers + symbols) for _ in range(12))
    entry3.delete(0, END)
    entry3.insert(0, password)

# Save Function with Messagebox
def email_value():
    website_name = entry.get()
    emails = entry2.get()
    passwords = entry3.get()

    save = messagebox.askyesno(title='Save', message='Do you want to save this?')
    if save:
        if website_name == "" or passwords == "":
            messagebox.showwarning(title="Oops", message="Please don't leave fields empty!")
            return
        with open("emails.txt", "a") as file:
            file.write(f"Website name : {website_name} | Email id : {emails} | Password : {passwords}\n")
        entry.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry.focus()


# Email
Label(text="Email/Username:", bg="white").grid(row=2, column=0)
entry2 = Entry(width=35)
entry2.grid(row=2, column=1, columnspan=2)

# Password
Label(text="Password:", bg="white").grid(row=3, column=0)
entry3 = Entry(width=21, show="*")
entry3.grid(row=3, column=1)
# Generate Password Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
window.mainloop()