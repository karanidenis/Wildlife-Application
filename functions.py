#!/usr/bin/python3
def introduction():
    from pathlib import Path
    path1 = Path("intro.txt")
    print(path1.read_text())



def importance():
    from pathlib import Path
    path2 = Path("important.txt")
    print(path2.read_text())


def involve():
    from pathlib import Path
    path3 = Path("involve.txt")
    print(path3.read_text())
