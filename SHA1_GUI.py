import tkinter as tk
from hashlib import sha1
from getpass import getpass
import pyperclip
def copyclip():
    passwordcopy=result_box["text"]
    pyperclip.copy(passwordcopy)
def generate():
    result_box["text"]=" "
    text_copy=message_space.get()
    hash_code=sha1(text_copy.encode('utf-8'))
    hash_code=str(hash_code.hexdigest())
    result_box['text']=hash_code
#----------------window-----------
window=tk.Tk()
window.title("SHA-1 Hash Generator")
window.geometry("500x400")
window.grid_columnconfigure((0,1),weight=1)

message_prompt=tk.Label(
    text="Enter message in the textbox below (max limit=255)",
    font=("Times New Roman", 14,"bold"),
    padx=20,
    pady=20,
    )
message_space=tk.Entry(
    #height=10,
    width=100,
    selectborderwidth=5,
    font=15
   # padx=20,
    #pady=20
)
encrypt_button=tk.Button(
    text="Generate Hash Code",
    underline=True,
    padx=30,
    pady=30,
    command=generate,
    borderwidth=5,
    font=("Arial",12)
)
copy=tk.Button(
    text="Copy To Clipboard",
    width=20,
    command=copyclip,
    padx=20,
    pady=20
    )
result_box=tk.Label(
    text="                                     ",
    padx=40,
    pady=20,
    font=("Times New Roman",13,"italic"),
    bg="black",
    fg="white",
)
about=tk.Label(
    text='''
    This is a SHA-1 Hash Generator created by Darsh Jain. 
    Suggestions are welcome.Contact-9867476582
    ''',
    fg="grey",
    height=2,)
message_prompt.pack()
message_space.pack()
encrypt_button.pack()
result_box.pack()
copy.pack()
about.pack()
window.mainloop()