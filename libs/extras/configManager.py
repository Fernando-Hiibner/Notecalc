from tkinter import *
from tkinter.font import Font
from configparser import ConfigParser
from os import mkdir
from os.path import expanduser, isdir, exists, join

from ..utilities import globals
from ..utilities.utilities import toPath

class ConfigManager():
    def __init__(self):
        self.configFolder = toPath(expanduser("~/Documents/Notecalc"))
        if isdir(self.configFolder):
            self.configDir = toPath(join(self.configFolder, "config.ini"))
            if exists(self.configDir):
                self.readConfig(self.configDir)
            elif not exists(self.configDir):
                self.createConfig(self.configDir)

        elif not isdir(self.configFolder):
            try:
                mkdir(self.configFolder)
                self.createConfig(join(self.configFolder, "config.ini"))
            except:
                pass

    def createConfig(self, configDir):
        configDir = toPath(configDir)
        config = ConfigParser()
        config.add_section("general")
        config["general"]["theme"] = "default"
        config["general"]["fontFamily"] = "Calibri"
        config["general"]["fontSize"] = "18"
        config["general"]["side"] = "off" 
        config["general"]["sidePrefix"] = "SidePrefix1"
        config["general"]["vsc"] = "off"
        config.add_section("SidePrefix1")
        config["SidePrefix1"]["upperFolder"] = "\"^\""
        config["SidePrefix1"]["actualFolder"] = "\"v \""
        config["SidePrefix1"]["folder"] = "\"   >\""
        config["SidePrefix1"]["file"] = "\"    \""
        config.add_section("SidePrefix2")
        config["SidePrefix2"]["upperFolder"] = "\"   Voltar pasta\""
        config["SidePrefix2"]["actualFolder"] = "\"   \""
        config["SidePrefix2"]["folder"] = "\"    \""
        config["SidePrefix2"]["file"] = "\"     \""
        config.add_section("default")
        config["default"]["configCaixa"] = str(globals.textConfig)
        config["default"]["configSide"] = str(globals.sideConfig)
        config["default"]["configBloco"] = str(globals.pannedWindowBGConfig)
        config["default"]["configCores"] = str(globals.colorConfig)
        config.add_section("dark")
        config["dark"]["configCaixa"] = str(globals.darkTextConfig)
        config["dark"]["configSide"] = str(globals.darkSideConfig)
        config["dark"]["configBloco"] = str(globals.darkPannedWindowBGConfig)
        config["dark"]["configCores"] = str(globals.darkColorConfig)
        with open(configDir, 'w', encoding='utf-8') as cfg:
            config.write(cfg)
        self.readConfig(configDir)

    def readConfig(self, configDir, globalRead = True, **kw):
        #Variables:

        configDir = toPath(configDir)
        config = ConfigParser()
        config.read(configDir, encoding="utf-8")
        if "font" not in kw.keys():
            font = Font(family=config.get("general", "fontFamily"), size=config.get("general", "fontSize"))
        else:
            font = kw.pop("font")
        if "side" not in kw.keys():
            side = config.getboolean("general", "side")
        else:
            side = kw.pop("side")
        if "vsc" not in kw.keys():
            vsc = config.getboolean("general", "vsc")
        else:
            vsc = kw.pop("vsc")
        if "sidePrefix" not in kw.keys():
            sidePrefix = config.get("general", "sidePrefix")
        else:
            sidePrefix = kw.pop("sidePrefix")

        for section in config.sections():
            if section == sidePrefix:
                configSideUpperFolderPrefix = config.get(section, "upperFolder", raw = True).strip("\"")
                configSideActualFolderPrefix = config.get(section, "actualFolder", raw = True).strip("\"")
                configSideFolderPrefix = config.get(section, "folder", raw = True).strip("\"")
                configSideFilePrefix = config.get(section, "file", raw = True).strip("\"")

        if "theme" not in kw.keys():
            theme = config.get("general", "theme")
        else:
            theme = kw.pop("theme")

        for section in config.sections():
            if section == theme:
                textConfig = eval(
                    config.get(section, "configCaixa"))
                sideConfig = eval(
                    config.get(section, "configSide"))
                pannedWindowBGConfig = config.get(section, "configBloco")
                colorConfig = eval(config.get(section, "configCores"))

        if globalRead == True:
            globals.font = font
            globals.side = side
            globals.vsc = vsc

            globals.sidePrefix = sidePrefix
            globals.configSideUpperFolderPrefix = configSideUpperFolderPrefix
            globals.configSideActualFolderPrefix = configSideActualFolderPrefix
            globals.configSideFolderPrefix = configSideFolderPrefix
            globals.configSideFilePrefix = configSideFilePrefix

            globals.theme = theme

            globals.textConfig = textConfig
            globals.sideConfig = sideConfig
            globals.pannedWindowBGConfig = pannedWindowBGConfig
            globals.colorConfig = colorConfig
        else:
            return {"font": font, "side" : side, "vsc" : vsc, "sidePrefix" : sidePrefix,
                    "cfgSideUpper" : configSideUpperFolderPrefix, "cfgSideActual" : configSideActualFolderPrefix, "cfgSideFolder" : configSideFolderPrefix, "cfgSideFile" : configSideFilePrefix, 
                    "theme" : theme, "textConfig" : textConfig, "sideConfig" : sideConfig, "pannedWindowBGConfig" : pannedWindowBGConfig, "colorConfig" : colorConfig}

    
    def modifyConfig(self, section, key, value):
        configDir = toPath(join(expanduser("~/Documents/Notecalc"), "config.ini"))
        config = ConfigParser()
        config.read(configDir, encoding="utf-8")
        config[section][key] = value;
        with open(configDir, 'w', encoding='utf-8') as cfg:
            config.write(cfg)
            cfg.close()
        return