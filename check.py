import subprocess

try:
  res = subprocess.run(["powershell.exe", "ps", "|", "wsl", "grep", "\"A Game Name\"", "|", "wsl", "wc", "-l"], stdout=subprocess.PIPE)
except:
  print(__file__ + "errored")

if(res.stdout == "1\n".encode('utf-8')):
  exec(open("./warn.py").read())
else:
  print("going well.")
