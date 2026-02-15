import tkinter as tk

root = tk.Tk()
root.title("Varun GUI Test")
root.geometry("300x200")

label = tk.Label(root, text="GUI is working 🎉", font=("Arial", 16))
label.pack(pady=50)

root.mainloop()
