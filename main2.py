#coding: utf-8
'''
Calculadora de equacao do segundo grau
'''
import tkinter as tk
import math as m
def CalcularRaizes2grau(a,b,c): 
	Delta = b**2-4*a*c
	x1 =0
	x2 = 0
	#Verifica se tem raizes reais ou complexas: 
	if (Delta<0):
		real_Z = -b/(2*a)
		imag_Z = m.sqrt(-Delta)/(2*a)
		x1 = complex(real_Z, imag_Z) #Tipo complex
		x2 = complex(real_Z, -imag_Z)
	elif (Delta>0): 
		x1 = -b/(2*a)-m.sqrt(Delta)/(2*a)
		x2 = -b/(2*a)+m.sqrt(Delta)/(2*a)
	else: 
		x1 = x2 = -b/(2*a)
	return x1,x2,Delta			

def _command_Button_Calc2Grau(): 
	try: 
		a = float(Entry_Coef_a.get())
		b = float(Entry_Coef_b.get())
		c = float(Entry_Coef_c.get())
		x1,x2,Delta = CalcularRaizes2grau(a,b,c)
		if isinstance(x1, complex): 
			Res.set(f"Raizes complexas: x1 = {x1:.2f} e x2 = {x2:.2f} ")
		elif (x1==x2): 
			Res.set(f"Raizes reais iguais: x1 = {x1:.2f} e x2 = {x2:.2f} ")
		else :
			Res.set(f"Raizes reais distintas: x1 = {x1:.2f} e x2 = {x2:.2f} ")
	except 	ValueError: 
		Res.set("Bizonho(a), digite numeros")	

janela=tk.Tk()
janela.title("Calculadora de equacao de 2 grau")
janela.geometry("400x350")
#Criação dos widgets para a interface
#Linha 1
Label_Coef_a = tk.Label(janela, text = "Coeficiente a: ")
Label_Coef_a.grid(row=0, column = 0)
Entry_Coef_a = tk.Entry(janela)
Entry_Coef_a.grid(row=0, column = 1)
#Linha 2
Label_Coef_b = tk.Label(janela, text = "Coeficiente b: ")
Label_Coef_b.grid(row=1, column = 0)
Entry_Coef_b = tk.Entry(janela)
Entry_Coef_b.grid(row=1, column = 1)
#Linha 3
Label_Coef_c = tk.Label(janela, text = "Coeficiente c: ")
Label_Coef_c.grid(row=2, column = 0)
Entry_Coef_c = tk.Entry(janela)
Entry_Coef_c.grid(row=2, column = 1)
#Botao para fazer os comandos 
Button_Calc2Grau=tk.Button(janela, text = "Calcular Raizes", command=_command_Button_Calc2Grau)
Button_Calc2Grau.grid(row = 3, column = 0, columnspan=2)
#Label para exibir resultado
Res = tk.StringVar()
Res.set("")
Resultado_Label = tk.Label(janela, textvariable= Res)
Resultado_Label.grid(row=4, column = 0, columnspan= 2)




janela.mainloop()
