#import tkinter for creating GUI apps
import tkinter as tk

from tkinter import filedialog, messagebox

#main window code
root=tk.Tk()
root.title("my text editor")
root.geometry("500x500")

#creating text area
text= tk.Text (root, wrap=tk.WORD,font=("Helvetica", 12))
text.pack(expand=True, fill=tk.BOTH)

#main logic starts now

#funtion 1 - to create new file
def new_file():
    text.delete("1.0",tk.END)

#funtion 2 - to open a file
def open_file():
    file_path=filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text files","*.txt")]
        )
    
    if file_path:
        #open selevted file
        with open(file_path,"r") as file:
            text.delete("1.0",tk.END)
            text.insert(tk.END,file.read())

#function 3 - save the file
def save_file():
    #open save file dialogue
    file_path=filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files","*.txt")]
        )
    
    if file_path:
        #save the file
        with open(file_path,"w") as file:
            file.write(text.get("1.0",tk.END))
    
        messagebox.showinfo("info","File saved successfully")

#menu
menu=tk.Menu(root)
root.config(menu=menu)

#file menu
file_menu=tk.Menu(menu)

# new file open file save file exit file

#add file menu to menu bar
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Exit",command=root.quit)
file_menu.add_separator()


#starts and keeps the window open
root.mainloop()


