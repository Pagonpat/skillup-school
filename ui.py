from tkinter import *
from tkinter import messagebox
import settings

def main():
    root = Tk()
    root.title(settings.APP_FULL_NAME)
    root.geometry("300x200")

    def show_message():
        messagebox.showinfo("asdw", "Hi")
        king = open(settings.DATA_PATH,"a")
        king.write("yay duolingo")
        king.close()

    button = Button(root, text="Click Me", command=show_message)
    button.pack(pady=20)

    root.mainloop()