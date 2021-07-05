import tkinter as tk
from typing import Dict

class WinButton(tk.Button):
    """### AJUDA  
           ---  
            self.Border -> Borda (Feita usando um tk.LabelFrame)  
                * self.borderCfg      -> configs padrões dele, um dict com as chaves e os valores normais de um LabelFrame, modifique ele pra mudar as configs  
                    * Ex.: WinButton.borderCfg["bg"] = "#adadad  
                * self.borderHLCfg    -> configs que ele assume automaticamente quando o mouse estiver acima dele (hover), modifique da mesma forma que o de cima  
                    * Ex.: WinButton.borderHLCfg["bg"] = "#0076d7"  
                * self.borderPressCfg -> configs que ele assume automaticamente quando o usuario clicar nele, modifique ad amesma forma que o de cima:
                    * WinButton.borderPressCfg["bg"] = "#005499"
            ---  
            WinButton   -> Botão (Feito usando um tk.Button)  
                * self.buttonCfg   -> configs padrões dele, um dict com as chaves e os valores normais de um Button, modifique ele para mudar as configs  
                    * Ex.: WinButton.buttonCfg["bg"] = "SystemButtonFace"  
                * self.buttonHLCfg -> configs que ele assume automaticamente quando o mouse estiver acima dele (hover), modifique da mesma forma que o de cima  
                    * Ex.: WinButton.buttonHLCfg["bg"] = "#e5f1fb"  
            ---
            Para configurar o layout tem que fazer o mesmo, dar um pack no WinButton e um na borda igual
    """
    def __init__(self, master, borderCfg = None, borderHLCfg = None, borderPressCfg = None, buttonCfg = None, buttonHLCfg = None, buttonPressCfg = None, **kw):
        self.master = master
        if borderCfg == None:
            self.borderCfg = {
                    "bd" : 1,
                    "bg" : "#adadad",
                    "relief": "flat"
                }
        else:
            self.borderCfg = borderCfg
        if buttonCfg == None:
            self.buttonCfg = {
                    "bg" : "SystemButtonFace",
                    "fg" : "black",
                    "relief" : "flat"
                }
        else:
            self.buttonCfg = buttonCfg
        if borderHLCfg == None:
            self.borderHLCfg = {
                    "bg" : "#0076d7"
                }
        else:
            self.borderHLCfg = borderHLCfg
        if buttonHLCfg == None:
            self.buttonHLCfg = {
                    "bg" : "#e5f1fb"
                }
        else:
            self.buttonHLCfg = buttonHLCfg
        if borderPressCfg == None:
            self.borderPressCfg = {
                "bg" : "#005499"
            }
        else:
            self.borderPressCfg = borderPressCfg
        if buttonPressCfg == None:
            self.buttonPressCfg = {
                "bg" : "#cce4f7"
            }
        else:
            self.buttonPressCfg = buttonPressCfg
        self.Border = tk.LabelFrame(self.master, self.borderCfg)
        self.Border.pack()

        tk.Button.__init__(self, self.Border, self.buttonCfg, **kw)

        self.bind("<Enter>", self.onHover)
        self.bind("<Leave>", self.onLeave)
        self.bind("<ButtonPress-1>", lambda event: self.customCommandPress(event))
        self.bind("<ButtonRelease-1>", lambda event: self.customCommandRelease(event))
    def onHover(self, event):
        self.Border.config(self.borderHLCfg)
        self.config(self.buttonHLCfg)
    def onLeave(self, event):
        self.Border.config(self.borderCfg)
        self.config(self.buttonCfg)
    def customCommandPress(self, event):
        self.Border.config(self.borderPressCfg)
        self.config(self.buttonPressCfg)
        self.invoke()
        return "break"
    def customCommandRelease(self, event):
        self.master.update_idletasks()
        self.Border.config(self.borderCfg)
        self.config(self.buttonCfg)
        return "break"