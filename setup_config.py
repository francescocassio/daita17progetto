# setup_config.py
import os
import shutil

if not os.path.exists("config.py"):
    shutil.copyfile("config.py.example", "config.py")
    print("config.py created from config.py.example")
else:
    print("config.py already exists")