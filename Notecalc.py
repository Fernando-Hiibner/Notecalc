#Notecalc#
#Renan Kawamoto | Fernando Hiibner#

''' Pra cada 12 de width e 27 de height aumenta 1 no width e 1 no height do bloco '''
#Importação as bibliotecas necessárias do Tkinter#
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
#Importação das bibliotecas do sistema para salvar e abrir arquivos#
import os
#Importação das bibliotecas criada por nós, necessárias para algumas funções do programa#
#from Pomodoro import *
import keyboard
#Inicio da clase do programa#
class wordcalc():
    #Def __init__, ela inicia assim que a classe é chamada#
    def __init__(self):
        global lock, saindo, janela, xj, yj, wid, heig
        lock = False
        saindo = False
        #define a janela tk e as suas propriedades#
        self.janela = Tk() #declara a janela#
        self.janela.title("Notecalc") #define o titulo pra janela#
        self.janela.geometry("450x575") #define as dimensões da janela#
        self.janela.resizable(False,False)#impede que a janela seja redimensionada pelo usuario(sujeito a mudança)#
        #Define o sistemas de guias(abas) e as abas#
        self.Guia_Blocouia_Controle = ttk.Notebook(self.janela) #---- Define um sistema de guias(abas) ----#
        self.Bloco = Frame(self.Guia_Blocouia_Controle) #---- Define efetivamente que a guia e quadrada e o seu espaço a ABA ----#
        self.Calc = Frame(self.Guia_Blocouia_Controle) #---- Define efetivamente que a guia e quadrada e o seu espaço a ABA ----#
        self.Guia_Blocouia_Controle.add(self.Bloco, text = 'Bloco de Notas') #---- Adciona a ABA no controle junto com seu nome ----#
        self.Guia_Blocouia_Controle.add(self.Calc, text = 'Calculadora') #---- Adciona a ABA no controle junto com seu nome ----#
        self.Guia_Blocouia_Controle.grid(column = 0, row = 0) #---- Define a posição do sistema de guias ----#
        self.bloco()
        self.calculadora()
        def on_closing():
            sair = messagebox.askyesnocancel("Sair", "Você deseja salvar antes de sair?")
            if sair == True:
                saindo = True
                salvar()
                self.janela.destroy()
            elif sair ==  False:
                self.janela.destroy()
            else:
                pass
        self.janela.protocol("WM_DELETE_WINDOW", on_closing)
        self.janela.iconbitmap('Notecalc.ico')
        self.janela.mainloop()#NÃO ESQUEÇA O MAINLOOP, SEU PROGRAMA PODE ATE RODAR MAS LA NA FRENTE SO VAI DAR RUIM#
    def bloco(self):
        global salvar
        #comeca a criação do sistema de bloco de notas#
        self.Caixa = Text(self.Bloco, width = "37", height = "21", selectbackground = "#303030", tabs = ('1c'))#declara a caixa de texto do bloco de notas#
        self.Caixa.grid(column = 0, row = 2)#posiciona a caixa de texto#
        self.Caixa.configure(font="Arial 16")#configura a fonte da caixa de texto#
        #inicia a definição responsavel pelo código de abrir arquivos de texto no bloco de notas#
        global localabrir
        localabrir = ''
        def novo():
            global localabrir
            self.Caixa.delete('1.0','end')
            localabrir = ''
        def abrir():
            #torna a variavel que vai conter o diretório do arquivo que você vai abrir global#
            global localabrir
            #Com esse código abrirá uma janela do explorer para o usuario selecionar o arquivo que quer abrir#
            localabrir = filedialog.askopenfilename(parent=self.janela,title='Selecione o arquivo que você quer abrir',filetypes = (("Documentos de Texto (*.txt)","*.txt"),("Todos Arquivos","*.*")))
            #Código responsavel por pegar o diretório obtido no código de cima, ler o arquivo de texto, limpar a caixa atual e passar o novo texto para ela#
            with open(localabrir, 'r') as aberto:
                self.Caixa.delete('1.0','end')
                texto = aberto.read()
                self.Caixa.insert('1.0',texto)
                aberto.close()
        #Inicia a definição responsavel pelo salvamento rápido de um documento de texto sendo feito no Notecalc#
        def salvar():
            global localabrir
            #Código que tenta salvar o arquivo rapidamente no local que ele ja conhece(proveniente tanto do Salvar como, quanto do Abrir)#
            if localabrir == '':
                saveas()
            else:
                try:
                    texto = self.Caixa.get('1.0', 'end-1c')
                    with open(localabrir, 'a+') as salvar:
                        salvar.truncate(0)
                        salvar.write(texto)
                        salvar.close()
                #Código que ele executa caso não consiga, ele automaticamente executa o código de salvar como#
                except NameError:
                    localabrir = None
                    saveas()
            
        #inicia a definição responsável pelo salvar como#
        def saveas():
            global localabrir, saindo, janela
            #Com esse código abrirá uma janela do explorer para o usuario selecionar o diretorio onde quer salvar o arquivo e o nome dele#
            self.saveas = filedialog.asksaveasfilename(parent=self.janela, title='Selecione o local onde quer salvar o arquivo', defaultextension = ("*.txt"),filetypes = (("Documentos de Texto (*.txt)","*.txt"),("Todos Arquivos","*.*")))
            texto = self.Caixa.get('1.0', 'end-1c')
            localabrir = self.saveas
            #Código responsavel por pegar o diretório obtido no código de cima e salvar o arquivo nele, com o nome especificado#
            with open(self.saveas, 'a+') as saveas:
                saveas.truncate(0)
                saveas.write(texto)
                saveas.close()
        switchbt = [0,1]
        switchtit = [0,1]
        switchstit = [0,1]
        switchit = [0,1]
        def removbold():
            self.Caixa.tag_remove("bt", "sel.first", "sel.last")
        def removtit():
            self.Caixa.tag_remove("tit", "sel.first", "sel.last")
        def removstit():
            self.Caixa.tag_remove("stit", "sel.first", "sel.last")
        def removit():
            self.Caixa.tag_remove("it", "sel.first", "sel.last")
        def bold():
            switchtit = [0,1]
            switchstit = [0,1]
            switchit = [0,1]            
            if switchbt[0] == 0:
                self.Caixa.tag_add("bt", "sel.first", "sel.last")
                self.Caixa.tag_config("bt", font=('Arial', '16', 'bold'))
            elif switchbt[0] == 1:
                removbold()
            switchbt.reverse()
        def italic():
            switchtit = [0,1]
            switchstit = [0,1]
            switchbt = [0,1]  
            if switchit[0] == 0:
                self.Caixa.tag_add("it", "sel.first", "sel.last")
                self.Caixa.tag_config("it", font=("Arial", "16", "italic"))
            elif switchit[0] == 1:
                removit()
            switchit.reverse()
        def titulo():
            switchit = [0,1]
            switchstit = [0,1]
            switchbt = [0,1] 
            if switchtit[0] == 0:
                self.Caixa.tag_add("tit", "sel.first", "sel.last")
                self.Caixa.tag_config("tit", font=("Arial", "22", "bold"))
            elif switchtit[0] == 1:
                removtit()
            switchtit.reverse()
        def subtit():
            switchtit = [0,1]
            switchit = [0,1]
            switchbt = [0,1] 
            if switchstit[0] == 0:
                self.Caixa.tag_add("stit", "sel.first", "sel.last")
                self.Caixa.tag_config("stit", font=("Arial", "18", "italic"))
            elif switchstit[0] == 1:
                removstit()
            switchstit.reverse()
        #Define os botões que executarão as funções de Abrir, Salvar e Salvar como#
        self.Guia_Bloco = Frame(self.Bloco, width = 450, height = 25)
        self.Guia_Bloco.grid(column = 0, row = 1, sticky = 'w')
        self.novob = Button(self.Guia_Bloco, text= 'Novo', command = novo, relief = FLAT)
        self.novob.place(x=3,y=0)
        self.Abrir = Button(self.Guia_Bloco, text= 'Abrir', command = abrir, relief = FLAT) #Perceba que a definição abrir e atribuida como comando desse botão, assim como outros comandos são atribuidos aos outros botões#
        self.Abrir.place(x=39,y=0)
        self.Salvar = Button(self.Guia_Bloco, text= 'Salvar', command = salvar, relief = FLAT)
        self.Salvar.place(x=72,y=0)
        self.Saveas = Button(self.Guia_Bloco, text = 'Salvar como', command = saveas, relief = FLAT)
        self.Saveas.place(x=110,y=0)
        
        #Define os botões de formatação#
        self.titulob = Button(self.Guia_Bloco, text = 'T', command = titulo, relief = FLAT)
        self.titulob.place(x=370,y=0)
        self.subtitb = Button(self.Guia_Bloco, text = 'Sub', command = subtit, relief = FLAT)
        self.subtitb.place(x=385,y=0)
        self.boldb = Button(self.Guia_Bloco, text = 'N', font = 'Arial 10 bold', command = bold, relief = FLAT)
        self.boldb.place(x=410,y=-2)
        self.italicb = Button(self.Guia_Bloco, text = 'i', font = 'Arial 10 italic', command = italic, relief = FLAT)
        self.italicb.place(x=430,y=-2)
    def calculadora(self):
        #Nesse ponto começa os códigos relacionados a calculadora#
        #------------------------------------------------------------#
        #Aqui definimos um visor pra calculadora, ele mostrara os números dos calculos feitos nela#
        self.Resultado = Label(self.Calc, width = 15, height = 3, text = '0', foreground='#303030', relief = GROOVE)
        self.Resultado.configure(font = 'Arial 36')
        self.Resultado['bg'] = 'white'
        self.Resultado.grid(column = 0, row = 0, padx = 10, pady = 10)
        #------------------------------------------------------------#
        #Aqui criamos as definições que terão os códigos dos botões das calculadoras(desde os números ate os operadores)#
        def zero():
            if self.Resultado['text'] == '0':
                self.Resultado['text'] = "0"
            else:
                self.Resultado['text'] = (self.Resultado['text']) + "0"
        def um():
            self.Calc.focus_set()
            if self.Resultado['text'] == '0':
                self.Resultado['text'] = "1"
            else:
                self.Resultado['text'] = (self.Resultado['text']) + "1"
        def dois():
            if self.Resultado['text'] == '0':
                self.Resultado['text'] = "2"
            else:
                self.Resultado['text'] = (self.Resultado['text']) + "2"
        def tres():
            if self.Resultado['text'] == '0':
                self.Resultado['text'] = "3"
            else:
                self.Resultado['text'] = (self.Resultado['text']) + "3"
        def quatro():
            if self.Resultado['text'] == '0':
                self.Resultado['text'] = "4"
            else:
                self.Resultado['text'] = (self.Resultado['text']) + "4"
        def cinco():
            if self.Resultado['text'] == '0':
                self.Resultado['text'] = "5"

            else:
                self.Resultado['text'] = (self.Resultado['text']) + "5"
        def seis():
            if self.Resultado['text'] == '0':
                self.Resultado['text'] = "6"
            else:
                self.Resultado['text'] = (self.Resultado['text']) + "6"
        def sete():
            if self.Resultado['text'] == '0':
                self.Resultado['text'] = "7"
            else:
                self.Resultado['text'] = (self.Resultado['text']) + "7"
        def oito():
            if self.Resultado['text'] == '0':
                self.Resultado['text'] = "8"
            else:
                self.Resultado['text'] = (self.Resultado['text']) + "8"
        def nove():
            if self.Resultado['text'] == '0':
                self.Resultado['text'] = "9"
            else:
                self.Resultado['text'] = (self.Resultado['text']) + "9"
        def ponto():
            if '.' not in self.Resultado['text']:
                self.Resultado['text'] = self.Resultado['text'] + '.'
            elif '.' in self.Resultado['text']:
                pass
        def cls():
            self.Resultado['text'] = '0'
        def back():
            self.Resultado['text'] = self.Resultado['text'][0:-1]
        #Aqui começam as definições responsaveis pelo calculo#
        def somar():
            global x1, operando
            x1 = float(self.Resultado['text'])
            self.Resultado['text'] = '0'
            operando = 1
        def sub():
            global x1, operando
            x1 = float(self.Resultado['text'])
            self.Resultado['text'] = '0'
            operando = 2
        def mult():
            global x1, operando
            x1 = float(self.Resultado['text'])
            self.Resultado['text'] = '0'
            operando = 3
        def div():
            global x1, operando
            x1 = float(self.Resultado['text'])
            self.Resultado['text'] = '0'
            operando = 4
        def por():
            global x1, operando
            x1 = float(self.Resultado['text'])
            self.Resultado['text'] = '0'
            operando = 5
        def igual():
            if operando == 1:
                x2 = float(self.Resultado['text'])
                resp = x1+x2
            elif operando == 2:
                x2 = float(self.Resultado['text'])
                resp = x1-x2
            elif operando == 3:
                x2 = float(self.Resultado['text'])
                resp = x1*x2
                resp = str(f'{resp:.2f}')
                resp = float(resp)
            elif operando == 4:
                x2 = float(self.Resultado['text'])
                resp = x1/x2
                resp = str(f'{resp:.2f}')
                resp = float(resp)
            elif operando == 5:
                x2 = float(self.Resultado['text'])
                resp = x1*(x2/100)
                resp = str(f'{resp:.2f}')
                resp = float(resp)
            self.Resultado['text'] = resp
            self.Resultado['text'] = str(self.Resultado['text'])
        
        #------------------------------------------------------------#
        #Aqui começa a criação dos botões da calculadora#
        self.cls = Button(self.Calc, text = "7", relief = GROOVE, command = sete)
        self.cls['bg'] = '#fefefe'
        self.cls.place(height = 80, width = 80,x = 13,y=190)
        
        
        self.vazio = Button(self.Calc, text = "8", relief = GROOVE, command = oito)
        self.vazio['bg'] = '#fefefe'
        self.vazio.place(height = 80, width = 80,x = 98,y=190)
        
        self.cls = Button(self.Calc, text = "9", relief = GROOVE, command = nove)
        self.cls['bg'] = '#fefefe'
        self.cls.place(height = 80, width = 80,x = 183,y=190)
        
        self.cls = Button(self.Calc, text = "CLS", relief = GROOVE, command = cls)
        self.cls['bg'] = '#fefefe'
        self.cls.place(height = 80, width = 80,x = 268,y=190)

        self.cls = Button(self.Calc, text = "<<", relief = GROOVE, command = back)
        self.cls['bg'] = '#fefefe'
        self.cls.place(height = 80, width = 80,x = 353,y=190)
        #-----------------------------------------------------------#
        self.cls = Button(self.Calc, text = "4", relief = GROOVE, command = quatro)
        self.cls['bg'] = '#fefefe'
        self.cls.place(height = 80, width = 80,x = 13,y=275)
        
        self.vazio = Button(self.Calc, text = "5", relief = GROOVE, command = cinco)
        self.vazio['bg'] = '#fefefe'
        self.vazio.place(height = 80, width = 80,x = 98,y=275)
        
        self.cls = Button(self.Calc, text = "6", relief = GROOVE, command = seis)
        self.cls['bg'] = '#fefefe'
        self.cls.place(height = 80, width = 80,x = 183,y=275)
        
        self.cls = Button(self.Calc, text = "/", relief = GROOVE, command = div)
        self.cls['bg'] = '#fefefe'
        self.cls.place(height = 80, width = 80,x = 268,y=275)

        self.cls = Button(self.Calc, text = "X", relief = GROOVE, command = mult)
        self.cls['bg'] = '#fefefe'
        self.cls.place(height = 80, width = 80,x = 353,y=275)
        #-----------------------------------------------------------#
        self.cls = Button(self.Calc, text = "1", relief = GROOVE, command = um)
        self.cls['bg'] = '#fefefe'
        self.cls.place(height = 80, width = 80,x = 13,y=360)
        
        self.vazio = Button(self.Calc, text = "2", relief = GROOVE, command = dois)
        self.vazio['bg'] = '#fefefe'
        self.vazio.place(height = 80, width = 80,x = 98,y=360)
        
        self.cls = Button(self.Calc, text = "3", relief = GROOVE, command = tres)
        self.cls['bg'] = '#fefefe'
        self.cls.place(height = 80, width = 80,x = 183,y=360)
        
        self.cls = Button(self.Calc, text = "-", relief = GROOVE, command = sub)
        self.cls['bg'] = '#fefefe'
        self.cls.place(height = 80, width = 80,x = 268,y=360)

        self.cls = Button(self.Calc, text = "+", relief = GROOVE, command = somar)
        self.cls['bg'] = '#fefefe'
        self.cls.place(height = 80, width = 80,x = 353,y=360)
        #----------------------------------------------------------#
        #definição que carrega o código do pomodoro#
        def load_pomo():
            pomodoro()
        def numlock():
            global lock
            if lock == False:
                #Atalhos Numeros#
                keyboard.add_hotkey("0", lambda: zero())
                keyboard.add_hotkey("1", lambda: um())
                keyboard.add_hotkey("2", lambda: dois())
                keyboard.add_hotkey("3", lambda: tres())
                keyboard.add_hotkey("4", lambda: quatro())
                keyboard.add_hotkey("5", lambda: cinco())
                keyboard.add_hotkey("6", lambda: seis())
                keyboard.add_hotkey("7", lambda: sete())
                keyboard.add_hotkey("8", lambda: oito())
                keyboard.add_hotkey("9", lambda: nove())
                #Atalhos operaçoes#
                keyboard.add_hotkey("+", lambda: somar())
                keyboard.add_hotkey("-", lambda: sub())
                keyboard.add_hotkey("/", lambda: div())
                keyboard.add_hotkey("*", lambda: mult())
                keyboard.add_hotkey("shift+5", lambda: por())
                keyboard.add_hotkey(".", lambda: ponto())
                keyboard.add_hotkey("shift+backspace", lambda: cls())
                keyboard.add_hotkey("backspace", lambda: back())
                keyboard.add_hotkey("return", lambda: igual())
                lock = True
                print("Num Lock OFF")
            elif lock == True:
                #Atalhos Numeros#
                keyboard.remove_hotkey("0")
                keyboard.remove_hotkey("1")
                keyboard.remove_hotkey("2")
                keyboard.remove_hotkey("3")
                keyboard.remove_hotkey("4")
                keyboard.remove_hotkey("5")
                keyboard.remove_hotkey("6")
                keyboard.remove_hotkey("7")
                keyboard.remove_hotkey("8")
                keyboard.remove_hotkey("9")
                #Atalhos operaçoes#
                keyboard.remove_hotkey("+")
                keyboard.remove_hotkey("-")
                keyboard.remove_hotkey("/")
                keyboard.remove_hotkey("*")
                keyboard.remove_hotkey("shift+5")
                keyboard.remove_hotkey(".")
                keyboard.remove_hotkey("shift+backspace")
                keyboard.remove_hotkey("backspace")
                keyboard.remove_hotkey("return")
                lock = False
                print("Num Lock ON")
        #NumLock#
        keyboard.add_hotkey("ctrl+l", lambda: numlock())
        
        self.cls = Button(self.Calc, text = ".", relief = GROOVE, command = ponto)
        self.cls['bg'] = '#fefefe'
        self.cls.place(height = 80, width = 80,x = 13,y=445)
        
        self.vazio = Button(self.Calc, text = "0", relief = GROOVE, command = zero)
        self.vazio['bg'] = '#fefefe'
        self.vazio.place(height = 80, width = 80,x = 98,y=445)
        
        self.cls = Button(self.janela, text = "Pomo", relief = GROOVE, command = load_pomo) #botão que chama o pomodoro(sujeito a mudanças)#
        self.cls['bg'] = '#fefefe'
        self.cls.place(height = 19, width = 40,x = 410,y=2)

        self.cls = Button(self.Calc, text = "Num\nLock", relief = GROOVE, command = numlock) #botao num lock#
        self.cls['bg'] = '#fefefe'
        self.cls.place(height = 80, width = 80,x = 183,y=445)
        
        self.cls = Button(self.Calc, text = "%", relief = GROOVE, command = por)
        self.cls['bg'] = '#fefefe'
        self.cls.place(height = 80, width = 80,x = 268,y=445)

        self.cls = Button(self.Calc, text = "=", relief = GROOVE, command = igual)
        self.cls['bg'] = '#fefefe'
        self.cls.place(height = 80, width = 80,x = 353,y=445)
        #----------------------------------------------------------#
        
            
        
        
c = wordcalc()
