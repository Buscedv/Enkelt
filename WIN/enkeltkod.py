import os
action = True
file = ""
tmp = ""
while action == True:
    filename = input("Filnamn eller tomt: ")
    if filename == "" and file == "":
        continue
    elif filename == "" and file != "":
        cmd = "python K:\\Omat\\enkelt.py K:\Omat\\"+file
        os.system(cmd)
        tmp = input(">>>: ")
        if tmp == "":
            action = True
        else:
            action = False
    elif filename != "":
        file = filename
        cmd = "python K:\\Omat\\enkelt.py K:\Omat\\"+file
        os.system(cmd)
        tmp = input(">>>: ")
        if tmp == "":
            action = True
        else:
            action = False
