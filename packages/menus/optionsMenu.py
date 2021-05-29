from ..menusclasses.options_window import OptionsWindow
      
def createOptionsMenu(janela, Bloco, Side, Caixa, menu):
    menu.add_command(label = "Options", command = lambda rootMain = janela: OptionsWindow(rootMain))
