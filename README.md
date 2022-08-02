# ubsCopy (windows)
copy storage devices in a sneaky way 😈

first, run start.exe and see how it works

note: if the start.exe file didn't work on your pc then you should compile yourself as below

windows might block the program and ask your permission, in this case, you should allow it

if it sounds suspicious to you, you can compile that main.py and make a exe file, it's very straightforward
1) first install python if you haven't
2) type "pip install pyinstaller" to the cmd (but before that you need to set python and pip as an environment variable, there are lots of tutorials out there)
3) type "pyinstaller --onefile main.py"
4) you are all set



to use all you need to do is run start.exe, but if dont want a terminal to pop up
then you need to run runScript.vbs and it won't show anything to the user

TIP: if you want to run it automatically you can make a shortcut and move it to the startup path then it would start as the pc boots up

startup path => C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
