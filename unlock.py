import os
import time
from cryptography.fernet import Fernet


#extensions = ["encryptedpdf", "encryptedtxt", "encryptedmp3",
#              "encryptedjpg", "encryptedpptx", "encrypteddocx"]
extensions = ["encryptedpdf"]

#DECRYPT FILES
startTime = time.time()
with open("key.key", 'rb') as f:
        key = f.read()
        f.close()
fernet = Fernet(key)
fileCounter = 0
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
                    oldExt = decrypted[:5]
                    decrypted = fernet.decrypt(data)
                    f.seek(0)
                    decrypted = decrypted[5:]
                    f.write(decrypted)
                    f.truncate()
                    print(curFile)
                    f.close()

                newName = curFile.rsplit('.', 1)
                newName[0] = newName[0] + "." + oldExt.decode('utf-8')
                os.rename(curFile, newName[0])
                fileCounter = fileCounter + 1

endTime = time.time()
execTime = endTime-startTime
print(f'{fileCounter}, file(s) have been decrypted in, {execTime} seconds')
