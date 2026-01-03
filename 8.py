import tkinter as tk
from tkinter import messagebox

def calculate():

    cash =int( ent_bill.get())
    num = int(ent_num.get())

    messagebox.showinfo("information",f"every one should pay : {cash/num}")

root = tk.Tk()
root.title("login")
root.geometry("300x200")

lbl_bill = tk.Label(root, text = "Total Bill :")
lbl_bill.grid(row=0, column=0, padx=10, pady=20)

ent_bill = tk.Entry(root)
ent_bill.grid(row=0, column=1, padx=10, pady=20)

lbl_num = tk.Label(root, text="Number of People :")
lbl_num.grid(row=1, column=0, padx=10, pady=20)

ent_num = tk.Entry(root)
ent_num.grid(row=1, column=1, padx=10, pady=20)

btn_cal = tk.Button(root, text = "Calculate", command=calculate)
btn_cal.grid(row=2, column=0, columnspan=2, pady=10)


root.mainloop()



