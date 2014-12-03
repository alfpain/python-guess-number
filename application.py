#coding:utf-8
def comprobadornumero():
	numero = False
	while (numero==False):
		try:
			numusuario = int(raw_input("Adivine numero: "))
			if (str(numusuario).isdigit()==True):
				if (numusuario<=0):
					print "Su numero no puede ser menor o igual que cero"
				elif(numusuario>1000):
					print "Su numero no puede ser mayor que 1000"
				else:
					numero=True
					return int(numusuario)
		except ValueError:
			print "Ingreso incorrecto. Solo se permiten numeros."
			numero=False

def menu():
	print "/"*80
	print "//\t\tBienvenido a Adivinator 3000 Version 2.1Beta           \t      //"
	print "/"*80
	print ""
	print """          ***********************************************************
          * INSTRUCCIONES: Usted debe adivinar un numero del 1 al   *
          *     1000. Si tu numero no acierta te dara una pista     *
          ***********************************************************
"""
def volverintentar():
	respuestavalida= False
	while (respuestavalida==False):	
		respuesta = raw_input("Desea volver a intentarlo? (Si/no)\n")
		respuesta = respuesta.lower()
		if (respuesta.isalpha()==True):
			if respuesta=="si":
				var=1
				respuestavalida = True
				return var
			elif (respuesta =="no"):
				var=0
				respuestavalida=True
				return var
			else:
				print "Solo se permite si o no"
				respuestavalida = False
import random
import time
menu()

numazar = random.randint(1,1000)
#print numazar
juegoterminado = False
vidas = 5
while (juegoterminado==False or vidas>=0):
	numusuario = comprobadornumero()
	if (numusuario>numazar and vidas!=0):
		print "Su numero es mayor que el numero buscado"
		vidas-=1
		print vidas
	elif (numusuario<numazar and vidas!=0):
		print "Su numero es menor que el numero buscado"
		vidas-=1
		print vidas
	elif (vidas==0):
		print """
      ___           ___           ___           ___     
     /\__\         /\  \         /\  \         /\__\    
    /:/ _/_       /::\  \       |::\  \       /:/ _/_   
   /:/ /\  \     /:/\:\  \      |:|:\  \     /:/ /\__\  
  /:/ /::\  \   /:/ /::\  \   __|:|\:\  \   /:/ /:/ _/_ 
 /:/__\/\:\__\ /:/_/:/\:\__\ /::::|_\:\__\ /:/_/:/ /\__\ 
 \:\  \ /:/  / \:\/:/  \/__/ \:\~~\  \/__/ \:\/:/ /:/  /
  \:\  /:/  /   \::/__/       \:\  \        \::/_/:/  / 
   \:\/:/  /     \:\  \        \:\  \        \:\/:/  /  
    \::/  /       \:\__\        \:\__\        \::/  /   
     \/__/         \/__/         \/__/         \/__/    
       ___                         ___           ___     
      /\  \          ___          /\__\         /\  \    
     /::\  \        /\  \        /:/ _/_       /::\  \   
    /:/\:\  \       \:\  \      /:/ /\__\     /:/\:\__\  
   /:/  \:\  \       \:\  \    /:/ /:/ _/_   /:/ /:/  /  
  /:/__/ \:\__\  ___  \:\__\  /:/_/:/ /\__\ /:/_/:/__/___
  \:\  \ /:/  / /\  \ |:|  |  \:\/:/ /:/  / \:\/:::::/  /
   \:\  /:/  /  \:\  \|:|  |   \::/_/:/  /   \::/~~/~~~~ 
    \:\/:/  /    \:\__|:|__|    \:\/:/  /     \:\~~\     
     \::/  /      \::::/__/      \::/  /       \:\__\    
      \/__/        ~~~~           \/__/         \/__/    
"""
		if volverintentar() == 0:
			print "Gracias por participar"
			time.sleep(1)
			break
		else:
			juegoterminado = False
			print "si"
			vidas = 5
	else:
		print """
░░░░░░░░░░░░▄▄
░░░░░░░░░░░█░░█
░░░░░░░░░░░█░░█
░░░░░░░░░░█░░░█
░░░░░░░░░█░░░░█
███████▄▄█░░░░░██████▄
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█░LE ATINASTE░░█
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█████░░░░░░░░░█
██████▀░░░░▀▀██████▀
"""
		if volverintentar() == 0:
			print "Gracias por participar"
			time.sleep(1)
		else:
			print "Recargando vidas..."
			vidas = 5



