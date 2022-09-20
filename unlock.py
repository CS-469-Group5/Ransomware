import os
from cryptography.fernet import Fernet


extensions = ["encryptedpdf", "encryptedtxt", "encryptedmp3",
              "encryptedjpg", "encryptedpptx", "encrypteddocx"]

#DECRYPT FILES
with open("key.key", 'rb') as f:
        key = f.read()
        f.close()
fernet = Fernet(key)
for root, dirs, files in os.walk("./TestDirectories", topdown=False):
    for name in files:
        ext = name.rsplit('.', 1)
        if (len(ext) > 1):
            ext = ext[1]
            if(ext in extensions):
                curFile = os.path.join(root,name)
                with open(curFile, 'r+b') as f:
                    data = f.read()
                    decrypted = fernet.decrypt(data)
                    f.seek(0)
                    oldExt = decrypted[:5]
                    print(oldExt)
                    f.seek(0)
                    decrypted = fernet.decrypt(data)
                    f.seek(0)
                    decrypted = decrypted[5:]
                    f.write(decrypted)
                    f.truncate()
                    f.close()

                newName = curFile.rsplit('.', 1)
                newName[0] = newName[0] + "." + oldExt.decode('utf-8')
                os.rename(curFile, newName[0])