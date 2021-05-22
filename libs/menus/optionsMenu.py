from ..extras.optionsWindow import optionsWindow
      
def createOptionsMenu(janela, Bloco, Side, Caixa, menu):
    menu.add_command(label = "Options", command = lambda rootMain = janela: optionsWindow(rootMain))
