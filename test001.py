# python 3.6.5
import os, re, glob, pathlib, shutil, time, datetime
from pathlib import Path

os.chdir("./20180520a")
print(os.getcwd())
print(os.listdir())

print("-"*36)
print("抽出")
a = os.listdir("./")
c = []
for b in a:
    if re.search("test", b):
        c.append(b)
print(c)

print("-"*36)
print("番号付与")

step = 1
for i, o in enumerate(c, 1):
    print("{:02}_{}".format(i * step, o))