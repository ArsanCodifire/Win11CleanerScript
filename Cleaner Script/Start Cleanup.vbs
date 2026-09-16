Set shell = CreateObject("Shell.Application")
Set ws = CreateObject("WScript.Shell")

pythonw = ws.ExpandEnvironmentStrings("%LocalAppData%") & "\Programs\Python\Python314\pythonw.exe"
script = ws.SpecialFolders("Desktop") & "\Cleaner Script\cleaner.py"

shell.ShellExecute pythonw, """" & script & """", "", "runas", 0
