from ctypes import windll
import string
import time
import os

os.system("cls")

# ----------------------------------------------------------------

with open("conf.txt","r") as f:
    data = f.read()

if data.find("refresh_delay")==-1:
    refresh_delay = 1      # seconds
else:
    refresh_delay = float(data[data.find("refresh_delay")+16:].split("\n")[0])

if data.find("pass_disks")==-1:
    pass_disks = ["C:"]  # dont foget to add column at the end
else:
    pass_disks = data[data.find("pass_disks")+13:].split("\n")[0].split(" ")


backup_path = 'C:\\Users\\'+os.getlogin()+'\\Saved Games\\Backup'
# check if backup folder exists
if not os.path.exists(backup_path):
    # create backup folder
    os.mkdir(backup_path)
    print('Backup folder created at '+backup_path)

def walk(path):
    os.chdir(path+'\\')
    lis=[]
    for root, dirs, files in os.walk(path):
        for i in files:
            lis.append(os.path.join(root, i))
    return(sorted(list(set(lis))))

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter+':')
        bitmask >>= 1
    return(sorted(drives))

def get_extra_drives():
    extra_disks = []
    for i in get_drives():
        if not (i in pass_disks):
            extra_disks.append(i)
    return extra_disks

# ----------------------------------------------------------------

print("checking drives...")
last_drives = sorted(list(set(get_extra_drives())))

while True:
    os.system("cls")
    print("checking drives...\n")
    drivers = sorted(list(set(get_extra_drives())))
    if not (drivers == last_drives):
        if len(drivers) < len(last_drives):
            print("removed\n")
        else:
            print("extra drive found")
        last_drives = drivers  
    else:
        time.sleep(refresh_delay)
        continue  

    for disk in list(last_drives):
        print('Backuping -> '+disk)
        files_in_backup_path = os.listdir(backup_path)
        bpname="reset"
        for num in range(10000):
            num_str = "bp"+"0"*(4-len(list(str(num))))+str(num)
            if not (num_str in files_in_backup_path):
                bpname=num_str
                os.mkdir(os.path.join(backup_path, bpname))
                break
        if bpname=="reset":
            print("\nbackup folder is full! (10 000 files)")
            exit(0)
        os.system('xcopy /E /Y /I /Q /D "'+disk+'" "'+os.path.join(backup_path,bpname)+'"')
        print(disk+' Backuped\n')
