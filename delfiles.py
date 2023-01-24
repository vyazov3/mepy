import os

files = os.listdir()
ignore_types = ["git", "py", "md", "txt"]

for file in files:
    if file.split(".")[-1] not in ignore_types:
        os.remove(file)