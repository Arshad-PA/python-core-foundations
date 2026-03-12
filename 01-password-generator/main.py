from tkinter import *

window = Tk()
window.title("Password Manager")
window.configure(padx=20, pady=20, bg="white")
# Website
Label(text="Website:", bg="white").grid(row=1, column=0)
entry = Entry(width=35)
entry.grid(row=1, column=1, columnspan=2)
entry.focus()

# Email
Label(text="Email/Username:", bg="white").grid(row=2, column=0)
entry2 = Entry(width=35)
entry2.grid(row=2, column=1, columnspan=2)

# Password
Label(text="Password:", bg="white").grid(row=3, column=0)
entry3 = Entry(width=21, show="*")
entry3.grid(row=3, column=1)
window.mainloop()