import os
import getpass

try:
  import tkinter
except ModuleNotFoundError:
  os.system("pip install tkinter")
from tkinter import *

root = Tk()
root.title("Ari Antivirus Setup")
