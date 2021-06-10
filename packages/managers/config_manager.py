from tkinter import *
from tkinter.font import Font
from configparser import ConfigParser
from os import get_exec_path, mkdir, listdir
from os.path import expanduser, isdir, exists, join

from ..extras import globals
from ..extras.utilities import toPath

from json import load, dump

class ConfigManager():
    def __init__(self):
        self.configFolder = toPath(expanduser("~/Documents/Notecalc"))
        self.configDir = toPath(join(self.configFolder, "config.json"))
        self.themesFolder = toPath(join(self.configFolder, "themes"))
        if isdir(self.configFolder):
            if not isdir(self.themesFolder):
                mkdir(self.themesFolder)
                self.createThemes()
            if exists(self.configDir):
                self.readConfig()
            else:
                self.createConfig()
                self.readConfig()

        else:
            try:
                mkdir(self.configFolder)
                mkdir(join(self.configFolder, "themes"))
                self.createConfig()
                self.createThemes()
                self.readConfig()
            except Exception as e:
                print("Erro:", str(e), "\nFunção: ConfigManager.__init__()\nCódigo: config_manager.py")
    def createConfig(self):
        config = {
            "general" :
            {
                "themeName" : "Default Light",
                "fontFamily" : "Calibri",
                "fontSize" : 18,
                "showSide" : False,
                "sidePrefix" : "sidePrefix1",
                "vsc" : False
            },
            "sidePrefix1" :
            {
                "name" : "Classic Side Prefix",
                "upperFolder" : "^ Voltar pasta",
                "actualFolder" : "v ",
                "folder" : "    >",
                "file" : "    ",
            },
            "sidePrefix2" :
            {
                "name" : "Nerd Fonts Side Prefix",
                "upperFolder" : "   Voltar pasta",
                "actualFolder" : "   ",
                "folder" : "    ",
                "file" : "     "
            }
        }
        with open(self.configDir, "w", encoding="utf-8") as generalConfig:
            dump(config, generalConfig, indent=4)
            generalConfig.close()
    def createThemes(self):
        defaultLight = {
            "textConfig" : {"tab": '1c', "bg": 'SystemWindow', "fg": 'black',
                   "selectbackground": '#dddddd', "selectforeground": 'black', "insertbackground": 'black'},
            "sideConfig" : {"family": "Courier New", "size": "10", "bg": '#f3f3f3',
                  "fg": '#333333', "selectbackground": '#dddddd', "selectforeground": 'black', "highlightbackground" : "#dddddd", "highlightforeground" : "#333333"},
            "pannedWindowBGConfig" : "#f3f3f3",
            "colorConfig" : {"default": "#000000", "title": "#af00db", "subtitle": "#0000ff",
                    "bold": "#ce8349", "italic": "#008000", "underline": "#267e99", "overstrike": "#a31515"}
        }
        defaultDark = {
            "textConfig" : {"tab": '1c', "bg": '#1e1e1e', "fg": '#cccccc',
                   "selectbackground": '#264f78', "selectforeground": '#cccccc', "insertbackground": '#cccccc'},
            "sideConfig" : {"family": "Courier New", "size": "10", "bg": '#252526',
                  "fg": '#cccccc', "selectbackground": '#3e3e3e', "selectforeground": '#cccccc', "highlightbackground" : "#3e3e3e", "highlightforeground" : "#cccccc"},
            "pannedWindowBGConfig" : "#1e1e1e",
            "colorConfig" : {"default": "#cccccc", "title": "#b96fb4", "subtitle": "#499cb3",
                    "bold": "#ce8349", "italic": "#6a9955", "underline": "#3ac9a3", "overstrike": "#dcdcaa"}
        }
        with open(toPath(join(self.themesFolder, "Default Light"+".json")), "w", encoding="utf-8") as themes:
            dump(defaultLight, themes, indent=4)
            themes.close()
        with open(toPath(join(self.themesFolder, "Default Dark"+".json")), "w", encoding="utf-8") as themes:
            dump(defaultDark, themes, indent=4)
            themes.close()

    def readConfig(self):
        with open(self.configDir, 'r', encoding="utf-8") as generalConfig:
            gConfig = load(generalConfig)
            generalConfig.close()
        with open(toPath(join(self.themesFolder, gConfig["general"]["themeName"]+".json")), 'r', encoding="utf-8") as themeConfig:
            tConfig = load(themeConfig)
            themeConfig.close()

        globals.font = Font(family=gConfig["general"]["fontFamily"], size=gConfig["general"]["fontSize"])
        globals.side = gConfig["general"]["showSide"]
        globals.vsc  = gConfig["general"]["vsc"]

        globals.theme = gConfig["general"]["themeName"]

        sidePrefix = gConfig["general"]["sidePrefix"]
        globals.sidePrefix = gConfig[sidePrefix]["name"]
        globals.configSideUpperFolderPrefix = gConfig[sidePrefix]["upperFolder"]
        globals.configSideActualFolderPrefix = gConfig[sidePrefix]["actualFolder"]
        globals.configSideFolderPrefix = gConfig[sidePrefix]["folder"]
        globals.configSideFilePrefix = gConfig[sidePrefix]["file"]

        globals.textConfig = tConfig["textConfig"]
        globals.sideConfig = tConfig["sideConfig"]
        globals.pannedWindowBGConfig = tConfig["pannedWindowBGConfig"]
        globals.colorConfig = tConfig["colorConfig"]

    def modifyConfig(self, sectionKeyValueDict):
        with open(self.configDir, "r", encoding="utf-8") as getConfig:
            gConfig = load(getConfig)
            getConfig.close()
        for section in sectionKeyValueDict.keys():
            for key, value in sectionKeyValueDict[section].items():
                gConfig[section][key] = value
        with open(self.configDir, "w") as newConfig:
            dump(gConfig, newConfig, indent=4)
            newConfig.close()
    def modifyTheme(self, keyValueDict, themeName):
        with open(toPath(join(self.themesFolder, themeName+".json")), "r", encoding="utf-8") as getTheme:
            tConfig = load(getTheme)
            getTheme.close()
        for key, value in keyValueDict.items():
            tConfig[key] = value
        with open(toPath(join(self.themesFolder, themeName+".json")), "w", encoding="utf-8") as newTheme:
            dump(tConfig, newTheme, indent=4)
            newTheme.close()
    def newTheme(self, themeDict, themeName):
        with open(join(self.themesFolder, themeName+".json"), "w", encoding="utf-8") as newTheme:
            dump(themeDict, newTheme, indent=4)
            newTheme.close()
    def getThemes(self):
        themes = [themeFile[0:-5] for themeFile in listdir(self.themesFolder)]
        return themes
    def getSidePrefix(self):
        with open(self.configDir, 'r', encoding="utf-8") as getConfig:
            config = load(getConfig)
            getConfig.close()
        prefix = [config[section]["name"] for section in config.keys() if "sidePrefix" in section]
        return prefix