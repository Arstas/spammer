import os
if os.name == "nt":
  pass
else:
  os.system("apt update -y")
  os.system("apt upgrade -y")
  os.system("pkg install python")
  os.system("pkg install git")
os.system("pip3 install colorama")
os.system("pip3 install pysocks")
os.system("pip3 install wheel")
os.system("pip3 install fastapi")
os.system("pip3 install uvicorn")
os.system("pip3 install aiofiles")
os.system("pip3 install pydantic")
os.system("pip3 install jinja2")
os.system("pip3 install httpx")
os.system("pip3 install phonenumbers")
os.system("pip3 install click")
os.system("pip3 install sentry-sdk")
os.system("pip3 install loguru")
os.system("pip3 install random_user_agent")
os.system("pip3 install urllib.request")
os.system("pip3 install zipfile")
os.system("pip3 install b0mb3r -U")
if os.name == "nt":
  pass
else:
  os.system("cd")
  os.system("cd spammer")
  os.system("python3 spammer.py")