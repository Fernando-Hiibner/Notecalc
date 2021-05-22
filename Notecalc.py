#Notecalc#
#Renan Kawamoto | Fernando Hiibner#

#Importação as bibliotecas necessárias do Tkinter#
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.scrolledtext import *
#Importação bibliotecas adcionais#
import ast
import time
from winsound import *
#Importação das bibliotecas do sistema para salvar e abrir arquivos#
import os
#Importação das bibliotecas criada por nós, necessárias para algumas funções do programa#

#Inicio da clase do programa#

class wordcalc():
    #Def __init__, ela inicia assim que a classe é chamada#
    def __init__(self):
        global lock, saindo, janela, xj, yj, wid, heig, switchbt, switchit, switchtit, switchstit, switchnum, switchcaix, switchdark, vsctheme, darktheme, dark_mode
        lock = False
        saindo = False
        #Define Baozi#
        #define a janela tk e as suas propriedades#
        self.janela = Tk() #declara a janela#
        self.janela.title("Notecalc") #define o titulo pra janela#
        self.janela.minsize(450, 575) #define as dimensões da janela#
        self.janela.geometry("450x575")
        #Define o sistemas de guias(abas) e as abas#
        self.Guia_Controle = ttk.Notebook(self.janela) #---- Define um sistema de guias(abas) ----#
        self.Bloco = ttk.Frame(self.janela) #---- Define efetivamente que a guia e quadrada e o seu espaço a ABA ----#
        self.Calc = ttk.Frame(self.janela) #---- Define efetivamente que a guia e quadrada e o seu espaço a ABA ----#
        self.Guia_Controle.add(self.Bloco, text = 'Bloco de Notas') #---- Adciona a ABA no controle junto com seu nome ----#
        self.Guia_Controle.add(self.Calc, text = 'Calculadora') #---- Adciona a ABA no controle junto com seu nome ----#
        self.Guia_Controle.grid(column = 0, row = 0) #---- Define a posição do sistema de guias ----#
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
        global salvar
        #comeca a criação do sistema de bloco de notas#
        self.Caixa = Text(self.Bloco, tabs = ('1c'), selectbackground = "#264f78", selectforeground = "#cccccc", relief = FLAT, undo = True, autoseparators = True)#declara a caixa de texto do bloco de notas#
        self.Scroll = ttk.Scrollbar(self.Bloco, orient = 'vertical', command = self.Caixa.yview)
        self.Caixa.configure(yscrollcommand=self.Scroll.set)
        self.Caixa.grid(column = 0, row = 2,sticky = 'w')#posiciona a caixa de texto#
        self.Scroll.grid(columns = 1, row = 2,sticky = "nse")
        self.Caixa.configure(font="Calibri  18")#configura a fonte da caixa de texto#
        def bloco_criar():
            self.janela.update()
            if self.janela.winfo_width() < 1220:
                self.Caixa.configure(width = int(self.janela.winfo_width()/12.26), height = int(self.janela.winfo_height()/31.38))
            elif self.janela.winfo_width() >= 1220:
                self.Caixa.configure(width = int(self.janela.winfo_width()/12.05), height = int(self.janela.winfo_height()/31.38))
            self.janela.after(500, bloco_criar)
        bloco_criar()
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
            localabrir = filedialog.askopenfilename(parent=self.janela,title='Selecione o arquivo que você quer abrir',filetypes = (("Documentos Notecalc (*.nxc)","*.nxc"),("Documentos de Texto (*.txt)","*.txt"),("Todos Arquivos","*.*")))
            #Código responsavel por pegar o diretório obtido no código de cima, ler o arquivo de texto, limpar a caixa atual e passar o novo texto para ela#
            with open(localabrir, 'r') as aberto:
                self.Caixa.delete('1.0','end')
                texto = aberto.read()
                if localabrir[-4:] == ".nxc":
                    textop1 = ast.literal_eval(texto)
                    final = ""
                    for (key, value, index) in textop1:
                        if key == "text":
                            final += value
                    self.Caixa.insert('1.0',final)
                    for (key, value, index) in textop1:
                        if key == "tagon":
                            indexcomecodetag = index
                        elif key == "tagoff":
                            if value == "bt":
                                self.Caixa.tag_add("bt", f"{indexcomecodetag}", f"{index}")
                                self.Caixa.tag_config("bt", font=('Arial', '16', 'bold'))
                            elif value == "it":
                                self.Caixa.tag_add("it", f"{indexcomecodetag}", f"{index}")
                                self.Caixa.tag_config("it", font=("Arial", "16", "italic"))
                            elif value == "tit":
                                self.Caixa.tag_add("tit", f"{indexcomecodetag}", f"{index}")
                                self.Caixa.tag_config("tit", font=("Arial", "22", "bold"))
                            elif value == "stit":
                                self.Caixa.tag_add("stit", f"{indexcomecodetag}", f"{index}")
                                self.Caixa.tag_config("stit", font=("Arial", "18", "italic"))
                else:
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
                    textonormal = self.Caixa.get('1.0', 'end-1c')
                    texto = str(self.Caixa.dump("1.0", "end"))
                    with open(localabrir, 'a+') as salvar:
                        salvar.truncate(0)
                        if localabrir[-4:] == ".nxc":
                            salvar.write(texto)
                        else:
                            salvar.write(textonormal)
                        salvar.close()
                #Código que ele executa caso não consiga, ele automaticamente executa o código de salvar como#
                except NameError:
                    localabrir = None
                    saveas()
            
        #inicia a definição responsável pelo salvar como#
        def saveas():
            global localabrir, saindo, janela
            #Com esse código abrirá uma janela do explorer para o usuario selecionar o diretorio onde quer salvar o arquivo e o nome dele#
            self.saveas = filedialog.asksaveasfilename(parent=self.janela, title='Selecione o local onde quer salvar o arquivo', defaultextension = ("*.nxc"),filetypes = (("Documentos Notecalc (*.nxc)","*.nxc"),("Documentos de Texto (*.txt)","*.txt"),("Todos Arquivos","*.*")))
            texto = str(self.Caixa.dump("1.0", "end"))
            textonormal = self.Caixa.get('1.0', 'end-1c')
            localabrir = self.saveas
            #Código responsavel por pegar o diretório obtido no código de cima e salvar o arquivo nele, com o nome especificado#
            with open(self.saveas, 'a+') as saveas:
                saveas.truncate(0)
                if localabrir[-4:] == ".nxc":
                    saveas.write(texto)
                else:
                    saveas.write(textonormal)
                saveas.close()
        switchbt = False
        switchtit = False
        switchstit = False
        switchit = False
        def removbold():
            self.Caixa.tag_remove("bt", "sel.first", "sel.last")
        def removtit():
            self.Caixa.tag_remove("tit", "sel.first", "sel.last")
        def removstit():
            self.Caixa.tag_remove("stit", "sel.first", "sel.last")
        def removit():
            self.Caixa.tag_remove("it", "sel.first", "sel.last")
        def bold():
            global switchbt, switchit, switchtit, switchstit
            switchtit = False
            switchstit = False
            switchit = False
            removtit()
            removstit()
            removit()           
            if switchbt == False:
                self.Caixa.tag_add("bt", "sel.first", "sel.last")
                self.Caixa.tag_config("bt", font=('Arial', '16', 'bold'))
            elif switchbt == True:
                removbold()
            switchbt = not switchbt
        def italic():
            global switchbt, switchit, switchtit, switchstit
            switchbt = False
            switchtit = False
            switchstit = False
            removbold()
            removtit()
            removstit()
            if switchit == False:
                self.Caixa.tag_add("it", "sel.first", "sel.last")
                self.Caixa.tag_config("it", font=("Arial", "16", "italic"))
            elif switchit == True:
                removit()
            switchit = not switchit
        def titulo():
            global switchbt, switchit, switchtit, switchstit
            switchbt = False
            switchit = False
            switchstit = False
            removbold()
            removit()
            removstit()
            if switchtit == False:
                self.Caixa.tag_add("tit", "sel.first", "sel.last")
                self.Caixa.tag_config("tit", font=("Arial", "22", "bold"))
            elif switchtit == True:
                removtit()
            switchtit = not switchtit
        def subtit():
            global switchbt, switchit, switchtit, switchstit
            switchbt = False
            switchit = False
            switchtit = False
            removbold()
            removit()
            removtit()
            if switchstit == False:
                self.Caixa.tag_add("stit", "sel.first", "sel.last")
                self.Caixa.tag_config("stit", font=("Arial", "18", "italic"))
            elif switchstit == True:
                removstit()
            switchstit = not switchstit
        #Atalhos bloco de notas#
        self.Caixa.bind("<Control-s>", lambda event: salvar())
        self.Caixa.bind("<Alt-s>", lambda event: saveas())
        self.Caixa.bind("<Control-n>", lambda event: novo())
        self.Caixa.bind("<Control-o>", lambda event: abrir())
        self.Caixa.bind("<Control-Key-1>", lambda event: titulo())
        self.Caixa.bind("<Control-Key-2>", lambda event: subtit())
        self.Caixa.bind("<Control-Key-3>", lambda event: bold())
        self.Caixa.bind("<Control-Key-4>", lambda event: italic())
        #Define os botões que executarão as funções de Abrir, Salvar e Salvar como#
        self.Guia_Bloco = Frame(self.Bloco, width = 450, height = 25)
        self.Guia_Bloco.grid(column = 0, row = 1, sticky = 'w')
        def Guia():
            self.janela.update()
            self.Guia_Bloco.configure(width = self.janela.winfo_width())
            self.janela.after(500, Guia)
        Guia()
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
        self.titulob.place(x = int(self.Guia_Bloco.winfo_width()-80),y=0)
        self.subtitb = Button(self.Guia_Bloco, text = 'Sub', command = subtit, relief = FLAT)
        self.subtitb.place(x = int(self.Guia_Bloco.winfo_width()-65),y=0)
        self.boldb = Button(self.Guia_Bloco, text = 'N', font = 'Arial 10 bold', command = bold, relief = FLAT)
        self.boldb.place(x = int(self.Guia_Bloco.winfo_width()-40), y=-2)
        self.italicb = Button(self.Guia_Bloco, text = 'i', font = 'Arial 10 italic', command = italic, relief = FLAT)
        self.italicb.place(x = int(self.Guia_Bloco.winfo_width()-20), y=-2)
        def brue_respon():
            self.janela.update()
            self.titulob.place(x = int(self.Guia_Bloco.winfo_width()-80))
            self.subtitb.place(x = int(self.Guia_Bloco.winfo_width()-65))
            self.boldb.place(x = int(self.Guia_Bloco.winfo_width()-40))
            self.italicb.place(x = int(self.Guia_Bloco.winfo_width()-20))
            self.janela.after(500, brue_respon)
        brue_respon()
        #Nesse ponto começa os códigos relacionados a calculadora#
        #------------------------------------------------------------#
        #Aqui definimos um visor pra calculadora, ele mostrara os números dos calculos feitos nela#
        self.Resultado = Label(self.Calc, text = '0', width = "15", height = "3", foreground='#303030', relief = GROOVE)
        self.Resultado.configure(font = 'Arial 36')
        self.Resultado['bg'] = 'white'
        self.Resultado.grid(column = 0, row = 0)
        def calc_visor():
            self.janela.update()
            self.Resultado.configure(width = int(self.janela.winfo_width()/30), height = int(self.janela.winfo_height()/190.6666666666667))
            self.Resultado.grid(column = 0, row = 0, padx = int(self.janela.winfo_width()/32), pady = int(self.janela.winfo_height()/45))
            self.janela.after(500, calc_visor)
        calc_visor()
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
        switchnum = False
        def baozi():
            global switchnum
            if switchnum == False:
                #Atalhos Numeros#
                self.janela.bind("0", lambda event: zero())
                self.janela.bind("1", lambda event: um())
                self.janela.bind("2", lambda event: dois())
                self.janela.bind("3", lambda event: tres())
                self.janela.bind("4", lambda event: quatro())
                self.janela.bind("5", lambda event: cinco())
                self.janela.bind("6", lambda event: seis())
                self.janela.bind("7", lambda event: sete())
                self.janela.bind("8", lambda event: oito())
                self.janela.bind("9", lambda event: nove())
                #Atalhos operaçoes#
                self.janela.bind("+", lambda event: somar())
                self.janela.bind("-", lambda event: sub())
                self.janela.bind("/", lambda event: div())
                self.janela.bind("*", lambda event: mult())
                self.janela.bind("%", lambda event: por())
                self.janela.bind(".", lambda event: ponto())
                self.janela.bind("<Shift-BackSpace>", lambda event: cls())
                self.janela.bind("<BackSpace>", lambda event: back())
                self.janela.bind("<Return>", lambda event: igual())
            elif switchnum == True:
                #Atalhos Numeros#
                self.janela.unbind("0")
                self.janela.unbind("1")
                self.janela.unbind("2")
                self.janela.unbind("3")
                self.janela.unbind("4")
                self.janela.unbind("5")
                self.janela.unbind("6")
                self.janela.unbind("8")
                self.janela.unbind("7")
                self.janela.unbind("9")
                #Atalhos operaçoes#
                self.janela.unbind("+")
                self.janela.unbind("-")
                self.janela.unbind("/")
                self.janela.unbind("*")
                self.janela.unbind("%")
                self.janela.unbind(".")
                self.janela.unbind("<Shift-BackSpace>")
                self.janela.unbind("<BackSpace>")
                self.janela.unbind("<Return>")
            switchnum = not switchnum
        self.janela.bind("<<NotebookTabChanged>>", lambda event: baozi())
        #-----------------------------------------------------------#
        self.seteb = Button(self.Calc, text = "7", relief = GROOVE, command = sete)
        self.seteb.configure(font = ("bold"))
        self.seteb['bg'] = '#fefefe'
        
        self.oitob = Button(self.Calc, text = "8", relief = GROOVE, command = oito)
        self.oitob.configure(font = ("bold"))
        self.oitob['bg'] = '#fefefe'        
        
        self.noveb = Button(self.Calc, text = "9", relief = GROOVE, command = nove)
        self.noveb.configure(font = ("bold"))
        self.noveb['bg'] = '#fefefe'        
        
        self.cls = Button(self.Calc, text = "CLS", relief = GROOVE, command = cls)
        self.cls.configure(font = ("bold"))
        self.cls['bg'] = '#fefefe'        

        self.backb = Button(self.Calc, text = "<<", relief = GROOVE, command = back)
        self.backb.configure(font = ("bold"))
        self.backb['bg'] = '#fefefe'       
        #-----------------------------------------------------------#
        self.quatrob = Button(self.Calc, text = "4", relief = GROOVE, command = quatro)
        self.quatrob.configure(font = ("bold"))
        self.quatrob['bg'] = '#fefefe'        
        
        self.cincob = Button(self.Calc, text = "5", relief = GROOVE, command = cinco)
        self.cincob.configure(font = ("bold"))
        self.cincob['bg'] = '#fefefe'        
        
        self.seisb = Button(self.Calc, text = "6", relief = GROOVE, command = seis)
        self.seisb.configure(font = ("bold"))
        self.seisb['bg'] = '#fefefe'        
        
        self.barrab = Button(self.Calc, text = "/", relief = GROOVE, command = div)
        self.barrab.configure(font = ("bold"))
        self.barrab['bg'] = '#fefefe'        

        self.vezesb = Button(self.Calc, text = "X", relief = GROOVE, command = mult)
        self.vezesb.configure(font = ("bold"))
        self.vezesb['bg'] = '#fefefe'        
        #-----------------------------------------------------------#
        self.umb = Button(self.Calc, text = "1", relief = GROOVE, command = um)
        self.umb.configure(font = ("bold"))
        self.umb['bg'] = '#fefefe'        
        
        self.doisb = Button(self.Calc, text = "2", relief = GROOVE, command = dois)
        self.doisb.configure(font = ("bold"))
        self.doisb['bg'] = '#fefefe'        
        
        self.tresb = Button(self.Calc, text = "3", relief = GROOVE, command = tres)
        self.tresb.configure(font = ("bold"))
        self.tresb['bg'] = '#fefefe'        
        
        self.menosb = Button(self.Calc, text = "-", relief = GROOVE, command = sub)
        self.menosb.configure(font = ("bold"))
        self.menosb['bg'] = '#fefefe'        

        self.maisb = Button(self.Calc, text = "+", relief = GROOVE, command = somar)
        self.maisb.configure(font = ("bold"))
        self.maisb['bg'] = '#fefefe'        
        #----------------------------------------------------------#
        #definição que carrega o código do pomodoro#
        def load_pomo():
            pomodoro()
        self.pontob = Button(self.Calc, text = ".", relief = GROOVE, command = ponto)
        self.pontob.configure(font = ("bold"))
        self.pontob['bg'] = '#fefefe'
        
        self.zerob = Button(self.Calc, text = "0", relief = GROOVE, command = zero)
        self.zerob.configure(font = ("bold"))
        self.zerob['bg'] = '#fefefe'
        
        self.pomobu = Button(self.janela, text = "Pomo", relief = GROOVE, command = load_pomo) #botão que chama o pomodoro(sujeito a mudanças)#
        self.pomobu['bg'] = '#fefefe'
        self.pomobu.place(height = 15, width = 40,x = 410,y=2)
        def pomo_respon():
            self.janela.update()
            self.pomobu.place(x = self.janela.winfo_width()-45)
            self.janela.after(500, pomo_respon)
        pomo_respon()
        self.janela.bind("<Control-p>", lambda event: load_pomo())
        
        self.porb = Button(self.Calc, text = "%", relief = GROOVE, command = por)
        self.porb.configure(font = ("bold"))
        self.porb['bg'] = '#fefefe'

        self.igualb = Button(self.Calc, text = "=", relief = GROOVE, command = igual)
        self.igualb.configure(font = ("bold"))
        self.igualb['bg'] = '#fefefe'
        #----------------------------------------------------------#
        def resp_butt():
            self.janela.update()
            self.seteb.place(height = int(self.janela.winfo_height()/7.16), width = int(self.janela.winfo_width()/5.62),x = int(self.janela.winfo_width()/34.61538461538462),y=int(self.janela.winfo_height()/3.026315789473684))
            self.oitob.place(height = int(self.janela.winfo_height()/7.16), width = int(self.janela.winfo_width()/5.62),x = int(self.janela.winfo_width()/4.591836734693878),y=int(self.janela.winfo_height()/3.026315789473684))
            self.noveb.place(height = int(self.janela.winfo_height()/7.16), width = int(self.janela.winfo_width()/5.62),x = int(self.janela.winfo_width()/2.459016393442623),y=int(self.janela.winfo_height()/3.026315789473684))
            self.cls.place(height = int(self.janela.winfo_height()/7.16), width = int(self.janela.winfo_width()/5.62),x = int(self.janela.winfo_width()/1.67910447761194),y=int(self.janela.winfo_height()/3.026315789473684))
            self.backb.place(height = int(self.janela.winfo_height()/7.16), width = int(self.janela.winfo_width()/5.62),x = int(self.janela.winfo_width()/1.274787535410765),y=int(self.janela.winfo_height()/3.026315789473684))
            self.quatrob.place(height = int(self.janela.winfo_height()/7.16), width = int(self.janela.winfo_width()/5.62),x = int(self.janela.winfo_width()/34.61538461538462),y=int(self.janela.winfo_height()/2.090909090909091))
            self.cincob.place(height = int(self.janela.winfo_height()/7.16), width = int(self.janela.winfo_width()/5.62),x = int(self.janela.winfo_width()/4.591836734693878),y=int(self.janela.winfo_height()/2.090909090909091))
            self.seisb.place(height = int(self.janela.winfo_height()/7.16), width = int(self.janela.winfo_width()/5.62),x = int(self.janela.winfo_width()/2.459016393442623),y=int(self.janela.winfo_height()/2.090909090909091))
            self.barrab.place(height = int(self.janela.winfo_height()/7.16), width = int(self.janela.winfo_width()/5.62),x = int(self.janela.winfo_width()/1.67910447761194),y=int(self.janela.winfo_height()/2.090909090909091))
            self.vezesb.place(height = int(self.janela.winfo_height()/7.16), width = int(self.janela.winfo_width()/5.62),x = int(self.janela.winfo_width()/1.274787535410765),y=int(self.janela.winfo_height()/2.090909090909091))
            self.umb.place(height = int(self.janela.winfo_height()/7.16), width = int(self.janela.winfo_width()/5.62),x = int(self.janela.winfo_width()/34.61538461538462),y=int(self.janela.winfo_height()/1.597222222222222))
            self.doisb.place(height = int(self.janela.winfo_height()/7.16), width = int(self.janela.winfo_width()/5.62),x = int(self.janela.winfo_width()/4.591836734693878),y=int(self.janela.winfo_height()/1.597222222222222))
            self.tresb.place(height = int(self.janela.winfo_height()/7.16), width = int(self.janela.winfo_width()/5.62),x = int(self.janela.winfo_width()/2.459016393442623),y=int(self.janela.winfo_height()/1.597222222222222))
            self.menosb.place(height = int(self.janela.winfo_height()/7.16), width = int(self.janela.winfo_width()/5.62),x = int(self.janela.winfo_width()/1.67910447761194),y=int(self.janela.winfo_height()/1.597222222222222))
            self.maisb.place(height = int(self.janela.winfo_height()/7.16), width = int(self.janela.winfo_width()/5.62),x = int(self.janela.winfo_width()/1.274787535410765),y=int(self.janela.winfo_height()/1.597222222222222))
            self.zerob.place(height = int(self.janela.winfo_height()/7.16), width = int(self.janela.winfo_width()/5.62),x = int(self.janela.winfo_width()/4.591836734693878),y=int(self.janela.winfo_height()/1.292134831460674))
            self.pontob.place(height = int(self.janela.winfo_height()/7.16), width = int(self.janela.winfo_width()/5.62),x = int(self.janela.winfo_width()/34.61538461538462),y=int(self.janela.winfo_height()/1.292134831460674))
            self.porb.place(height = int(self.janela.winfo_height()/7.16), width = int(self.janela.winfo_width()/5.62),x = int(self.janela.winfo_width()/1.67910447761194),y=int(self.janela.winfo_height()/1.292134831460674))
            self.igualb.place(height = int(self.janela.winfo_height()/7.16), width = int(self.janela.winfo_width()/5.62),x = int(self.janela.winfo_width()/1.274787535410765),y=int(self.janela.winfo_height()/1.292134831460674))
            self.janela.after(500, resp_butt)
        resp_butt()
        #Modo Escuro#
        switchdark = False
        defaultgrey = self.novob.cget("background")
        self.darkttk = ttk.Style()
        self.darkttk.theme_create("DarkTab", parent = 'alt', settings = {
            "TNotebook": {"configure": {"background": "#323232", "foreground": "#cccccc"}},
            "TNotebook.Tab": {"configure": {"background": "#323232", "foreground": "#cccccc"},
                              "map": {"background": [("selected", "#464646")]}},
            "TFrame": {"configure": {"background": "#464646", "foreground": "#cccccc"}},
            "Vertical.TScrollbar": {"configure": {"background": "#464646", "troughcolor": "#323232", "arrowcolor": "#cccccc", "relief":"flat"}}})
        self.original = ttk.Style()
        self.original.theme_create("Original", parent = 'alt', settings = {
            "TNotebook": {"configure": {"background": defaultgrey, "foreground": "#000000"}},
            "TNotebook.Tab": {"configure": {"background": defaultgrey, "foreground": "#000000"},
                              "map": {"background": [("selected", "#ffffff")]}},
            "TFrame": {"configure": {"background": defaultgrey, "foreground": "#000000"}},
            "Vertical.TScrollbar": {"configure": {"background": defaultgrey, "troughcolor": "#cccccc", "arrowcolor": "#323232", "relief":"flat"}}})
        def dark_mode():
            global switchdark, darktheme, originaltheme, vsctheme
            switchdark = not switchdark
            if switchdark == True:
                self.darkttk.theme_use("DarkTab")
                self.janela['bg'] = '#464646'
                self.Caixa['bg'] = '#1e1e1e'
                self.Caixa.configure(foreground = '#cccccc', insertbackground = "#cccccc")
                self.Guia_Bloco['bg'] = '#464646'
                #Botões#
                self.novob['bg'] = "#464646"
                self.novob.configure(foreground = "#cccccc")
                self.Abrir['bg'] = "#464646"
                self.Abrir.configure(foreground = "#cccccc")
                self.Salvar['bg'] = "#464646"
                self.Salvar.configure(foreground = "#cccccc")
                self.Saveas['bg'] = "#464646"
                self.Saveas.configure(foreground = "#cccccc")
                self.titulob['bg'] = "#464646"
                self.titulob.configure(foreground = "#cccccc")
                self.subtitb['bg'] = "#464646"
                self.subtitb.configure(foreground = "#cccccc")
                self.boldb['bg'] = "#464646"
                self.boldb.configure(foreground = "#cccccc")
                self.italicb['bg'] = "#464646"
                self.italicb.configure(foreground = "#cccccc")
                self.pomobu['bg'] = "#323232"
                self.pomobu.configure(foreground = "#cccccc", relief = FLAT)
                #Botões Calculadora#
                self.Resultado['bg'] = "#323232"
                self.Resultado.configure(foreground = "#cccccc")
                self.umb['bg'] = "#323232"
                self.umb.configure(foreground = "#cccccc")
                self.doisb['bg'] = "#323232"
                self.doisb.configure(foreground = "#cccccc")
                self.tresb['bg'] = "#323232"
                self.tresb.configure(foreground = "#cccccc")
                self.quatrob['bg'] = "#323232"
                self.quatrob.configure(foreground = "#cccccc")
                self.cincob['bg'] = "#323232"
                self.cincob.configure(foreground = "#cccccc")
                self.seisb['bg'] = "#323232"
                self.seisb.configure(foreground = "#cccccc")
                self.seteb['bg'] = "#323232"
                self.seteb.configure(foreground = "#cccccc")
                self.oitob['bg'] = "#323232"
                self.oitob.configure(foreground = "#cccccc")
                self.noveb['bg'] = "#323232"
                self.noveb.configure(foreground = "#cccccc")
                self.zerob['bg'] = "#323232"
                self.zerob.configure(foreground = "#cccccc")
                #Funcões Calculadora#
                self.maisb['bg'] = "#323232"
                self.maisb.configure(foreground = "#cccccc")
                self.pontob['bg'] = "#323232"
                self.pontob.configure(foreground = "#cccccc")
                self.menosb['bg'] = "#323232"
                self.menosb.configure(foreground = "#cccccc")
                self.vezesb['bg'] = "#323232"
                self.vezesb.configure(foreground = "#cccccc")
                self.barrab['bg'] = "#323232"
                self.barrab.configure(foreground = "#cccccc")
                self.porb['bg'] = "#323232"
                self.porb.configure(foreground = "#cccccc")
                self.cls['bg'] = "#323232"
                self.cls.configure(foreground = "#cccccc")
                self.backb['bg'] = "#323232"
                self.backb.configure(foreground = "#cccccc")
                self.darkb['bg'] = "#323232"
                self.darkb.configure(foreground = "#cccccc")
                self.igualb['bg'] = "#323232"
                self.igualb.configure(foreground = "#cccccc")
                self.Caixa.tag_config("tit", foreground = "#cccccc", selectbackground = "#264f78", selectforeground = "#cccccc")
                self.Caixa.tag_config("stit", foreground = "#cccccc", selectbackground = "#264f78", selectforeground = "#cccccc")
                self.Caixa.tag_config("bt", foreground = "#cccccc", selectbackground = "#264f78", selectforeground = "#cccccc")
                self.Caixa.tag_config("it", foreground = "#cccccc", selectbackground = "#264f78", selectforeground = "#cccccc")
                self.vscmanual['bg'] = '#323232'
                self.vscmanual.configure(foreground = "#cccccc", relief = FLAT)
                global vsc_p
                def vsc_p():
                    self.Caixa.tag_config("tit", foreground = "#b96fb4", selectbackground = "#264f78", selectforeground = "#cccccc")
                    self.Caixa.tag_config("stit", foreground = "#499cb3", selectbackground = "#264f78", selectforeground = "#cccccc")
                    self.Caixa.tag_config("bt", foreground = "#ce8349", selectbackground = "#264f78", selectforeground = "#cccccc")
                    self.Caixa.tag_config("it", foreground = "#6a9955", selectbackground = "#264f78", selectforeground = "#cccccc")
                if vsctheme == True:
                    vsc_p()
                #Brue#
                self.Caixa.configure(selectbackground = "#264f78", selectforeground = "#cccccc")
                darktheme = True
            elif switchdark == False:
                self.darkttk.theme_use("Original")
                self.janela['bg'] = defaultgrey
                self.Caixa['bg'] = '#ffffff'
                self.Caixa.configure(foreground = '#000000', insertbackground = "#000000")
                self.Guia_Bloco['bg'] = defaultgrey
                #Botões#
                self.novob['bg'] = defaultgrey
                self.novob.configure(foreground = '#000000')
                self.Abrir['bg'] = defaultgrey
                self.Abrir.configure(foreground = '#000000')
                self.Salvar['bg'] = defaultgrey
                self.Salvar.configure(foreground = '#000000')
                self.Saveas['bg'] = defaultgrey
                self.Saveas.configure(foreground = '#000000')
                self.titulob['bg'] = defaultgrey
                self.titulob.configure(foreground = '#000000')
                self.subtitb['bg'] = defaultgrey
                self.subtitb.configure(foreground = '#000000')
                self.boldb['bg'] = defaultgrey
                self.boldb.configure(foreground = '#000000')
                self.italicb['bg'] = defaultgrey
                self.italicb.configure(foreground = '#000000')
                self.pomobu['bg'] = '#fefefe'
                self.pomobu.configure(foreground = '#000000', relief = GROOVE)
                #Botões Calculadora#
                self.Resultado['bg'] = "#ffffff"
                self.Resultado.configure(foreground = "#000000")
                self.umb['bg'] = "#ffffff"
                self.umb.configure(foreground = "#000000")
                self.doisb['bg'] = "#ffffff"
                self.doisb.configure(foreground = "#000000")
                self.tresb['bg'] = "#ffffff"
                self.tresb.configure(foreground = "#000000")
                self.quatrob['bg'] = "#ffffff"
                self.quatrob.configure(foreground = "#000000")
                self.cincob['bg'] = "#ffffff"
                self.cincob.configure(foreground = "#000000")
                self.seisb['bg'] = "#ffffff"
                self.seisb.configure(foreground = "#000000")
                self.seteb['bg'] = "#ffffff"
                self.seteb.configure(foreground = "#000000")
                self.oitob['bg'] = "#ffffff"
                self.oitob.configure(foreground = "#000000")
                self.noveb['bg'] = "#ffffff"
                self.noveb.configure(foreground = "#000000")
                self.zerob['bg'] = "#ffffff"
                self.zerob.configure(foreground = "#000000")
                #Funcões Calculadora#
                self.maisb['bg'] = "#ffffff"
                self.maisb.configure(foreground = "#000000")
                self.pontob['bg'] = "#ffffff"
                self.pontob.configure(foreground = "#000000")
                self.menosb['bg'] = "#ffffff"
                self.menosb.configure(foreground = "#000000")
                self.vezesb['bg'] = "#ffffff"
                self.vezesb.configure(foreground = "#000000")
                self.barrab['bg'] = "#ffffff"
                self.barrab.configure(foreground = "#000000")
                self.porb['bg'] = "#ffffff"
                self.porb.configure(foreground = "#000000")
                self.cls['bg'] = "#ffffff"
                self.cls.configure(foreground = "#000000")
                self.backb['bg'] = "#ffffff"
                self.backb.configure(foreground = "#000000")
                self.darkb['bg'] = "#ffffff"
                self.darkb.configure(foreground = "#000000")
                self.igualb['bg'] = "#ffffff"
                self.igualb.configure(foreground = "#000000")
                self.vscmanual['bg'] = '#fefefe'
                self.vscmanual.configure(foreground = "#000000", relief = GROOVE)
                #Brue#
                self.Caixa.configure(selectbackground = "#264f78", selectforeground = "#cccccc")
                self.Caixa.tag_config("tit", foreground = "#000000", selectbackground = "#264f78", selectforeground = "#cccccc")
                self.Caixa.tag_config("stit", foreground = "#000000", selectbackground = "#264f78", selectforeground = "#cccccc")
                self.Caixa.tag_config("bt", foreground = "#000000", selectbackground = "#264f78", selectforeground = "#cccccc")
                self.Caixa.tag_config("it", foreground = "#000000", selectbackground = "#264f78", selectforeground = "#cccccc")
                darktheme = False
            return darktheme
        self.janela.bind("<Control-Key-5>", lambda event: dark_mode())
        vsctheme = False
        darktheme = False
        def vsc_man():
            global vsctheme, switchdark, darktheme, vsc_p
            vsctheme = not vsctheme
            if vsctheme == True and darktheme == True:
                vsc_p()
            elif vsctheme == False and darktheme == True:
                switchdark = False
                dark_mode()
        self.vscmanual = Button(self.janela, text = "VSC", relief = GROOVE, command = vsc_man)
        self.vscmanual['bg'] = '#fefefe'
        self.vscmanual.place(height = 15, width = 40, x = 360, y = 2)
        self.darkb = Button(self.Calc, text = "Dark", relief = GROOVE, command = dark_mode) #botao num lock#
        self.darkb.configure(font = ("bold"))
        self.darkb['bg'] = '#fefefe'
        def vscdark_respon():
            self.janela.update()
            self.vscmanual.place(x = self.janela.winfo_width()-90)
            self.darkb.place(height = int(self.janela.winfo_height()/7.16), width = int(self.janela.winfo_width()/5.62),x = int(self.janela.winfo_width()/2.459016393442623),y=int(self.janela.winfo_height()/1.292134831460674))
            self.janela.after(500, vscdark_respon)
        vscdark_respon()
        self.janela.mainloop()#NÃO ESQUEÇA O MAINLOOP, SEU PROGRAMA PODE ATE RODAR MAS LA NA FRENTE SO VAI DAR RUIM#

class pomodoro():
    #Criando a def principal#
    def __init__(self):
        #Declarando as Vars#
        global rodando, resetar, darktheme
        rodando = False
        resetar = False
        self.mainmins = 25
        self.mainseg = 0
        self.desmins = 5
        self.desseg = 0
        #Declarando a janela#
        self.janela_p = Tk()
        self.janela_p.title("Pomodoro")
        self.janela_p.resizable(False, False)
        self.janela_p.geometry('444x280')
        self.janela_p.iconbitmap("Notecalc.ico")
        #Criando o Label que mostrara o tempo do pomodoro#
        self.telapomo = Label(self.janela_p, width = 15, height = 3, text = '00:00', foreground='#303030', relief = GROOVE)
        self.telapomo.configure(font = 'Arial 36')
        self.telapomo['bg'] = 'white'
        self.telapomo.grid(column = 0, row = 0, padx = 10, pady = 10)
        #fazendo a def que chama o timer#
        def comecar():
            global rodando, resetar
            rodando = True
        def pausar():
            global rodando, resetar
            rodando = False
        def reset():
            global resetar, rodando
            resetar = True
        #Atalhos#
        self.janela_p.bind("<Return>", lambda event: comecar())
        self.janela_p.bind("<Shift_R>", lambda event: pausar())
        self.janela_p.bind("<BackSpace>", lambda event: reset())
        #fazendo o botao que chama o timer#
        self.botao_start = Button(self.janela_p, text = 'Começar', foreground = 'white', command = comecar, relief = FLAT)
        self.botao_start.configure(font = 'impact 24')
        self.botao_start['bg'] = '#66ef66'
        self.botao_start.place(height=60,width=160,x=10,y=196)
        #fazendo o botão Pause#
        self.botao_pause = Button(self.janela_p, text = 'Pause', foreground = 'white', command = pausar, relief = FLAT)
        self.botao_pause.configure(font = 'impact 18')
        self.botao_pause['bg'] = '#ef6666'
        self.botao_pause.place(height=60,width=80,x=183,y=196)
        #fazendo o botão Reset#
        self.botao_reset = Button(self.janela_p, text = 'Resetar', foreground = 'white', command = reset, relief = FLAT)
        self.botao_reset.configure(font = 'impact 24')
        self.botao_reset['bg'] = '#6666ef'
        self.botao_reset.place(height=60,width=160,x=275,y=196)
        #Chamando a janela#
        self.timer_pomodoro()
        defaultgrey = self.janela_p.cget("background")
        def theme():
            if darktheme == False:
                self.janela_p['bg'] = defaultgrey
                self.telapomo['bg'] = "#ffffff"
                self.telapomo.configure(foreground = "#303030")
            if darktheme == True:
                self.janela_p['bg'] = "#464646"
                self.telapomo['bg'] = "#323232"
                self.telapomo.configure(foreground = "#cccccc")
            self.janela_p.after(200, theme)
        theme()
        self.janela_p.mainloop()#MAINLOOP#
    #Criando a def do timer#
    def timer_pomodoro(self):
        global rodando, resetar
        #Criando a logíca que fará sempre diminuir 1 segundo a medida que passa um segundo na vida real#
        #Criando os if's para o tempo de descanso#
        self.telapomo.configure(foreground = '#303030')
        if self.mainmins < 0 and rodando == True:
            self.desseg -= 1
            if self.desmins >= 0 and self.desseg >= 10:
                self.telapomo['text'] = f'{self.desmins}:{self.desseg}'
            elif self.desseg <= 9 and self.desseg > 0:
                self.telapomo['text'] = f'{self.desmins}:0{self.desseg}'
            elif self.desseg <= 0:
                self.desmins -= 1
                self.desseg = 59
                if self.desmins >= 0:
                    self.telapomo['text'] = f'{self.desmins}:{self.desseg}'
                elif self.desmins < 0:
                    self.telapomo['text'] = '00:00'
                    self.telapomo.configure(foreground = "red")
            #Criando o if que resetará os minutos do timer pra mais um ciclo de pomodoro#
        if self.desmins < 0 or resetar == True:
            self.mainseg = 0
            self.mainmins = 25
            self.desseg = 0
            self.desmins = 5
            self.telapomo['text'] = f'{self.mainmins}:0{self.mainseg}'
            resetar = False
        #Ifs responsaveis pelo tempo de trabalho#
        elif self.mainmins >= 0 and self.mainseg >= 0 and rodando == True:
            self.mainseg -= 1
            if self.mainmins >= 0 and self.mainseg >= 10:
                self.telapomo['text'] = f'{self.mainmins}:{self.mainseg}'
            #Criando os ifs que fazem os calculos corretos de tempo#
            elif self.mainseg <= 9 and self.mainseg > 0:
                self.telapomo['text'] = f'{self.mainmins}:0{self.mainseg}'
            elif self.mainseg <= 0:
                self.mainmins -= 1
                self.mainseg = 59
                if self.mainmins >= 0:
                    self.telapomo['text'] = f'{self.mainmins}:{self.mainseg}'
                elif self.mainmins < 0:
                    self.telapomo['text'] = '00:00'
                    self.telapomo.configure(foreground = "red")
                    Beep(2000, 500)
                    
        #loop pra ficar chamando o timer dnvo e atualizando o timer#
        self.janela_p.after(1000, self.timer_pomodoro)
                
            
        
        
c = wordcalc()
