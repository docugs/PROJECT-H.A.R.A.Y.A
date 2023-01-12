import subprocess

program = "C:\\Users\\Gianne Bacay\\Desktop\\Messenger.exe.lnk"

subprocess.Popen(f'start /b /wait /min /high "Running messenger as Administrator" "{program}"', shell=True)


#Run command: python open_program.py