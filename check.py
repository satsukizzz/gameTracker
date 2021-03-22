import subprocess

# local files
import settings as env

try:
  res = subprocess.run(["powershell.exe", "ps", "|", "wsl", "grep", env.a_game_name, "|", "wsl", "wc", "-l"], stdout=subprocess.PIPE)

  if(res.stdout == "1\n".encode('utf-8')):
    exec(open("./warn.py").read())
  else:
    print("going well.")

except:
  print(__file__ + " errored")
