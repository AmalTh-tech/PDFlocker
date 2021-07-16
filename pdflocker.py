from PyPDF2 import PdfFileWriter,PdfFileReader
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
style = Style(theme="darkly")
from tkinter import messagebox as msg
from tkinter import filedialog
import time
def browseFiles():                                              # for the file explorer
    global filename
    filename = filedialog.askopenfilename(initialdir = "/", 
										title = "Select a File", 
										filetypes = (("Text files", 
														"*.txt*"), 
													("all files", 
														"*.*")))
    ttk.Label(win,text = "You have chosen: "+filename).grid(column = 4,row = 5)
def secure_pdf(file,password):                                 # locking the file
    parser = PdfFileWriter()
    pdf = PdfFileReader(file)

    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))
    parser.encrypt(password)

    with open(filename+"encrypted.pdf","wb") as f:
        parser.write(f)
        f.close()
    print("encrypted file created....")

def confirm():                                   # confirmation message
    secure_pdf(filename,passwd.get())
    msg.showinfo("PDF locker says","Password protected file successfully created in the same folder as the original file.")
    time.sleep(5)
    win.destroy()

if __name__ == "__main__":
    win  = style.master
    win.geometry("500x200")
    win.title("PDF Locker")
    ttk.Label(win,text = "Choose file location:").grid(column = 0,row = 0)
    ttk.Button(win,text="Choose",style="primary.TButton",command = browseFiles).grid(column = 1,row = 0)
    passwd = tk.StringVar()
    passwd_confirm = tk.StringVar()
    ttk.Label(win,text="Enter password:").grid(column=0,row=1,pady=3)
    passwd_entered = ttk.Entry(win,width = 15,textvariable = passwd)
    passwd_entered.grid(column=1,row=1,padx = 2,pady=15)
    passwd_entered_confirm = ttk.Entry(win,width=15,textvariable=passwd_confirm)
    ttk.Button(win,text = "Confirm",style="success.TButton",command = confirm).grid(column=0,row = 3,pady = 5)
    win.mainloop()
    
    
