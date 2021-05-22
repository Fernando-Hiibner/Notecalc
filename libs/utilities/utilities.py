from sys import argv
from os.path import dirname, join
from pathlib import Path

def toPath(path):
    try:
        path = Path(path)
        return path
    except TypeError:
        return path

def getIcon(iconName = "Notecalc.ico"):
    icon = toPath(join("./libs/img/", iconName))
    return icon

def replaceSubstring(string, oldSubstring, newSubstring, optionalIndex = None):
    if optionalIndex == None:
        string.replace(oldSubstring, newSubstring)
        return string
    elif optionalIndex != None:
        if string.find(oldSubstring, optionalIndex) != -1:
            oldSubstringWidth = len(oldSubstring)
            newString = string[0:optionalIndex]+newSubstring+string[optionalIndex+oldSubstringWidth::]
            return newString
    return string
