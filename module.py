import os


while True:
    ent=input("choose operation:q ip / wi-fi / shutdown / reload / ver / tasklist / time / date / exit: \n")
    if ent == "wi-fi":
        wifi=os.system('cmd /c "netsh wlan show networks"')
        continue
    
    elif ent == "ip":
        ip=os.system('cmd /c "ipconfig"')
        continue

    elif ent  == "shutdown":
        ch1=input("Are you sure?  yes / no : \n")
        if ch1 == "yes":
            ip=os.system('cmd /c "shutdown"')
        elif ch1 == "no":
            continue

    elif ent  == "reload":
        ch1=input("Are you sure?  ryes / no : \n")
        if ch1 == "yes":
            ip=os.system('cmd /c "reload"')
        elif ch1 == "no":
            continue

    elif ent  == "ver":
        ver=os.system('cmd /c "ver"')
        continue

    elif ent == "tasklist":
        ver=os.system('cmd /c "tasklist"')
        continue

    elif ent == "time":
        ver=os.system('cmd /c "time"')
        continue
            
    elif ent  == "date":
        ver=os.system('cmd /c "date"')
        continue



    elif ent  == "exit":
        break




    else:
        print("system: Try again!")
        continue


