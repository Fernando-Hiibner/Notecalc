import tkinter as tk
import tkinter.scrolledtext as tkST

from ..menusclasses.menu_classes import Format

from ..menus.fastMenu import FastMenu

class LabelButton(tk.Label):
    def __init__(self, master, highlightbackground = None, highlightforeground = None, command = None, **kw):
        tk.Label.__init__(self, master = master, **kw)
        self.bind("<Enter>", self.onEnter)
        self.bind("<Leave>", self.onLeave)
        self.command = command

        self.defaultBackground = self['background']
        self.defaultForeground = self['foreground']

        if highlightbackground == None:
            self.highlightbackground = self['background']
        else:
            self.highlightbackground = highlightbackground
        if highlightforeground == None:
            self.highlightforeground = self['foreground']
        else:
            self.highlightforeground = highlightforeground

    def onEnter(self, e):
        if self.command != None:
            self.bind("<Button-1>", lambda event: self.command())
        self['background'] = self.highlightbackground
        self['foreground'] = self.highlightforeground

    def onLeave(self, e):
        if self.command != None:
            self.unbind("<Button-1>")
        self['background'] = self.defaultBackground
        self['foreground'] = self.defaultForeground

    def configure(self, *args, **kw):
        if 'highlightbackground' in kw.keys():
            self.highlightbackground = kw.pop('highlightbackground')
        if 'highlightforeground' in kw.keys():
            self.highlightforeground = kw.pop('highlightforeground')
        if 'bg' in kw.keys() or 'background' in kw.keys():
            try:
                self.defaultBackground = kw['bg']
            except:
                self.defaultBackground = kw['background']
        if 'fg' in kw.keys() or 'foreground' in kw.keys():
            try:
                self.defaultForeground = kw['fg']
            except:
                self.defaultForeground = kw['foreground']
        if 'command' in kw.keys():
            self.command = kw.pop('command')
        super().config(*args, **kw)
    def config(self, *args, **kw):
        self.configure(*args, **kw)

class myScrolledText(tkST.ScrolledText):
    def __init__(self, master, richText = False, **kw):
        tkST.ScrolledText.__init__(self, master = master, **kw)
        self.master = master
        self.richText = richText
        if 'inactiveselect' not in kw.keys():
            self['inactiveselect'] = self['selectbackground']
        if 'exportselection' not in kw.keys():
            self['exportselection'] = False
        if self.richText == True:
            self.format = Format(self, self)
            self.fastMenu = FastMenu(self, self)

    def configure(self, *args, **kw):
        if 'richText' in kw.keys():
            richText = kw.pop('richText')
            if richText == True and richText != self.richText:
                self.format = Format(self, self)
                self.fastMenu = FastMenu(self, self)
            elif richText == False and richText != self.richText:
                del(self.format)
                del(self.fastMenu)
        if 'inactiveselect' in kw.keys():
            self['inactiveselect'] = kw.pop('inactiveselect')
        super().config(*args, **kw)
    def config(self, *args, **kw):
        self.configure(*args, **kw)
    def tag_add(self, *args, **kw):
        super().tag_add(*args, **kw)
        self.event_generate("<<TagAdd>>", when = "now")
    def tag_remove(self, *args, **kw):
        super().tag_remove(*args, **kw)
        self.event_generate("<<TagRemove>>", when = "now")
    def tag_delete(self, *args, **kw):
        super().tag_delete(*args, **kw)
        self.event_generate("<<TagDelete>>", when = "now")
    def tag_indexes(self, index1, index2 = None, tagName = "all"):
        if index2 == None:
            self.tag_add("endTag", "end")
            index2 = str(self.tag_ranges("endTag")[0])
            self.tag_delete("endTag", "end")
        sample = self.dump(index1, index2)
        tagNames = list()
        if tagName == "all":
            for key, value, index in sample:
                if key == "tagon" and value != "sel" and value not in tagNames:
                    tagNames.append(value)
        elif tagName != "all":
            tagNames.append(tagName)
        tagsIndexes = dict()
        for tagInAnalylis in tagNames:
            tagsIndexOn = list()
            tagsIndexOff = list()
            tagsTupleList = list()
            for (key, value, index) in sample:
                if key == "tagon" and value == tagInAnalylis:
                    tagsIndexOn.append(index)
                elif key == "tagoff" and value == tagInAnalylis:
                    tagsIndexOff.append(index)
            tagsIndexOn.sort()
            tagsIndexOff.sort()
            if len(tagsIndexOn) >= len(tagsIndexOff):
                for i in range(len(tagsIndexOn)):
                    try:
                        if tagsIndexOn[i] < tagsIndexOff[i]:
                            tagsTupleList.append((tagsIndexOn[i], tagsIndexOff[i]))
                        elif tagsIndexOn[i] > tagsIndexOff[i]:
                            tagsTupleList.append((index1, tagsIndexOff[i]))
                    except IndexError:
                        tagsTupleList.append((tagsIndexOn[i], index2))
            else:
                for i in range(len(tagsIndexOff)):
                    try:
                        if tagsIndexOn[i] < tagsIndexOff[i]:
                            tagsTupleList.append((tagsIndexOn[i], tagsIndexOff[i]))
                        elif tagsIndexOn[i] > tagsIndexOff[i]:
                            tagsTupleList.append((index1, tagsIndexOff[i]))
                    except IndexError:
                        tagsTupleList.append((index1, tagsIndexOff[i]))
            tagsIndexes[tagInAnalylis] = tagsTupleList
        
        if "sel" in self.tag_names():
            tagsNotInSample = self.tag_names("sel.first")
            for tag in tagsNotInSample:
                if tag != "sel" and tag not in tagsIndexes.keys():
                    tagsIndexes[tag] = [(str(self.tag_ranges("sel")[0]), str(self.tag_ranges("sel")[1]))]
        return tagsIndexes

    def tagsInSelection(self):
        tagsInSel = self.tag_indexes(str(self.tag_ranges("sel")[0]), str(self.tag_ranges("sel")[1]))
        return tagsInSel

class HighlightListBox(tk.Listbox):
    def __init__(self, master, highlightbackground = None, highlightforeground = None, **kw):
        tk.Listbox.__init__(self, master = master, **kw)
        self.bind("<Enter>", self.onEnter)
        self.bind("<Leave>", self.onLeave)
        self.bind("<<ListboxSelect>>", self.selectValidation)
        self.deactivatedIndex = []
        self.lastHighlighted = None
        if highlightbackground == None:
            self.highlightbackground = self['selectbackground']
        elif highlightbackground != None:
            self.highlightbackground = highlightbackground
        if highlightforeground == None:
            self.highlightforeground = self['foreground']
        elif highlightforeground != None:
            self.highlightforeground = highlightforeground
            
    def configure(self, *args, **kw):
        if 'highlightbackground' in kw.keys():
            self.highlightbackground = kw.pop('highlightbackground')
                
        if 'highlightforeground' in kw.keys():
            self.highlightforeground = kw.pop('highlightforeground')
        
        super().config(*args, **kw)

        for _ in range(self.size()):
            self.itemconfig(_, bg = self['background'])
            self.itemconfig(_, fg = self['foreground'])

    def config(self, *args, **kw):
        self.configure(*args, **kw)
    def insert(self, index, element, active = True):
        super().insert(index, element)
        if index == 'end':
            index = self.size()-1
        self.deactivatedIndex = list(map(lambda newIndex: newIndex+1 if newIndex > index else (newIndex+1 if newIndex == index else newIndex), self.deactivatedIndex))
        if active == False:
            self.deactivatedIndex.append(index)
    def delete(self, index, index2 = None):
        if index == 'end':
            index = self.size()-1
        if index2 == 'end':
            index2 = self.size()-1
        if index2 == None:
            super().delete(index)
            self.deactivatedIndex = list(map(lambda newIndex: newIndex-1 if newIndex > index else newIndex, self.deactivatedIndex))
        elif index2 != None:
            super().delete(index, index2)
            self.deactivatedIndex = list(map(lambda newIndex: newIndex-(index2 - index)-1 if newIndex > index else newIndex, self.deactivatedIndex))
    def selectValidation(self, e):
        index = int(self.curselection()[0])
        if index in self.deactivatedIndex:
            self.selection_clear(index)
            return False
        return True
    def onEnter(self, e):
        self.focus_set()
        self.bind("<Motion>", self.onHover)
        self.bind("<MouseWheel>", lambda e: self.event_generate("<Motion>", when="tail", x = e.x, y=e.y))
    def onLeave(self, e):
        if self.lastHighlighted != None:
            self.itemconfig(self.lastHighlighted, bg = self['background'])
            self.itemconfig(self.lastHighlighted, fg = self['foreground'])
        self.unbind("<Motion>")
    def onHover(self, e):
        if self.lastHighlighted != None and self.lastHighlighted != self.nearest(e.y):
            self.itemconfig(self.lastHighlighted, bg = self['background'])
            self.itemconfig(self.lastHighlighted, fg = self['foreground'])
        if self.nearest(e.y) not in self.deactivatedIndex:
            self.itemconfig(self.nearest(e.y), bg = self.highlightbackground)
            self.itemconfig(self.nearest(e.y), fg = self.highlightforeground)
            self.lastHighlighted = self.nearest(e.y)
