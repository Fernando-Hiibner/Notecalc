import globais
from tkinter import *
class pomodoro():
	#Criando a def principal#
	def __init__(self):
		#Declarando as Vars#
		global rodando, resetar
		rodando = False
		resetar = False
		globais.abertopomo = True
		def fechando():
			globais.abertopomo = False
			self.janela_p.destroy()
		self.mainmins = 25
		self.mainseg = 0
		self.desmins = 5
		self.desseg = 0
		#Declarando a janela#
		self.janela_p = Tk()
		self.janela_p.title("Pomodoro")
		self.janela_p.resizable(False, False)
		self.janela_p.geometry('444x280')
		self.janela_p.iconbitmap(globais.icon)
		self.janela_p.protocol("WM_DELETE_WINDOW", fechando)
		#Criando o Label que mostrara o tempo do pomodoro#
		self.telapomo = Label(self.janela_p, width = 15, height = 3, text = '00:00', foreground='#323232', relief = GROOVE)
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
		self.botao_start = Button(self.janela_p, text = 'Começar', foreground = 'black', command = comecar, relief = GROOVE)
		self.botao_start.configure(font = 'impact 24')
		self.botao_start['bg'] = 'white'
		self.botao_start.place(height=60,width=160,x=10,y=196)
		#fazendo o botão Pause#
		self.botao_pause = Button(self.janela_p, text = 'Pause', foreground = 'black', command = pausar, relief = GROOVE)
		self.botao_pause.configure(font = 'impact 18')
		self.botao_pause['bg'] = 'white'
		self.botao_pause.place(height=60,width=80,x=183,y=196)
		#fazendo o botão Reset#
		self.botao_reset = Button(self.janela_p, text = 'Resetar', foreground = 'black', command = reset, relief = GROOVE)
		self.botao_reset.configure(font = 'impact 24')
		self.botao_reset['bg'] = 'white'
		self.botao_reset.place(height=60,width=160,x=275,y=196)
		#Chamando a janela#
		self.timer_pomodoro()
		def darkmpomo():
			if globais.darkmode == False and globais.darkmode != globais.anterior:
				self.janela_p['bg'] = "SystemButtonFace"
				self.telapomo['bg'] = "white"
				self.telapomo.configure(foreground = "#323232")
			if globais.darkmode == True and globais.darkmode != globais.anterior:
				self.janela_p['bg'] = "#1e1e1e"
				self.telapomo['bg'] = "#323232"
				self.telapomo.configure(foreground = "#cccccc")
			else:
				pass
			if globais.vsc == False and globais.darkmode == True:
				self.botao_start.configure(bg = '#323232', fg = '#cccccc')
				self.botao_pause.configure(bg = '#323232', fg = '#cccccc')
				self.botao_reset.configure(bg = '#323232', fg = '#cccccc')
			elif globais.vsc == True and globais.darkmode == True:
				self.botao_start.configure(bg = '#323232', fg = '#6a9955')
				self.botao_pause.configure(bg = '#323232', fg = '#ce8349')
				self.botao_reset.configure(bg = '#323232', fg = '#499cb3')

			if globais.vsc == False and globais.darkmode == False:
				self.botao_start.configure(bg = 'white', fg = '#323232')
				self.botao_pause.configure(bg = 'white', fg = '#323232')
				self.botao_reset.configure(bg = 'white', fg = '#323232')
			if globais.vsc == True and globais.darkmode == False:
				self.botao_start.configure(bg = 'white', fg = '#6a9955')
				self.botao_pause.configure(bg = 'white', fg = '#ce8349')
				self.botao_reset.configure(bg = 'white', fg = '#499cb3')
			globais.anterior = globais.darkmode
			self.janela_p.after(200, darkmpomo)
		darkmpomo()
		#MAINLOOP#
		self.janela_p.mainloop()
	#Criando a def do timer#
	def timer_pomodoro(self):
		global rodando, resetar
		#Criando a logíca que fará sempre diminuir 1 segundo a medida que passa um segundo na vida real#
		#Criando os if's para o tempo de descanso#
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