import tkinter 
import sys
import subprocess

def update_text():
    cmd = "speedtest-cli"
    speed = subprocess.call(cmd, shell=True)
    return(cmd)
    
root = tkinter.Tk()
root.title("VELOCIMETER")
root.geometry("300x300")
button = tkinter.Button(root, text="Get Speed", width=30, command=update_text)
button.pack()
down_label = tkinter.Label(root, text="")
down_label.pack()
up_label = tkinter.Label(root, text="")
up_label.pack()



root.mainloop()