#!/usr/bin/python3
def introdution():
    from pathlib import Path
    path1 = Path("intro.txt")
    print(path1.read_text())
