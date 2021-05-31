from tkinter import Menu
from sys import argv

from packages.extras import globals
from packages.extras.utilities import toPath
from packages.extras.file_operations import openFile

from packages.managers.builder_manager import SubBuilder

from packages.menus.menuroutes import createEditMenu, createFileMenu, createFormatMenu, createOptionsMenu

'''
try:
    windowMasterWidgets = WindowBuilder()
    janela = windowMasterWidgets.janela
    Caixa = windowMasterWidgets.Caixa
    Bloco = windowMasterWidgets.Bloco
    Side = windowMasterWidgets.Side

    try:
        abrirArquivo(janela, Caixa, toPath(argv[1]))
        globals.dirDeTrabalhoAtual = toPath(argv[1])
    except:
        pass
        
    menu = Menu(janela)
    criarMenuArquivo(janela, Caixa, menu)
    editar = criarMenuEditar(janela, Caixa, menu)
    menuFormatar = criarMenuFormatar(janela, Caixa, menu)
    menuRapido = MenuRapido(janela, Caixa, editar).coresPreDefinidas
    criarMenuOpcoes(janela, Bloco, Side, Caixa, menu, menuFormatar, menuRapido)
    janela.mainloop()
except Exception as e:
    print("Unexpected Error:"+str(e))
'''
widgetBuilder = SubBuilder()
root = widgetBuilder.root
text = widgetBuilder.text

try:
    openFile(root, text, toPath(argv[1]))
    globals.currentWorkingDirectory = toPath(argv[1])
except:
    pass
menu = Menu(root)
createFileMenu(root, text, menu)
createEditMenu(root, text, menu)
createFormatMenu(root, text, menu)
createOptionsMenu(root, menu)
root.mainloop()