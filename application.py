#-*- coding: utf-8 -*-
#Importamos nuestras Librerias
import smtplib, getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import time
import sys

#Declaramos nuestro Diccionario
PAISES = {}
TODOORDENADO = {}

#1. Ingeso de Datos
def ingresoPaises(): #Se ingresan los paises y capitales
    print "                         ***** Ingreso Paises *****\n"

    RESPUESTA3 = "si"
    RESPUESTA = True
    PAI = ""
    CAPI = ""


    while RESPUESTA3 != "no": #Se ejecuta mientras respuesta sea si

        while len(PAI) <=2 or PAI != "Usa": #Ingreso del País
            PAI = raw_input("Ingrese País: ")
            PAI = PAI.title()
            try:
                PAI = float(PAI)
                PAI = int(PAI)
                print u"Debe ingresar un País válido\n"
            except(RuntimeError, NameError, ValueError):
                if (len(PAI) <= 2):
                    print u"Debe ingresar un País válido\n"
                else:
                    PAI = PAI
                    break

        while len(CAPI) <= 3: #Ingreso de la Capital
            CAPI = raw_input("Ingrese la Capítal: ")
            CAPI = CAPI.title()
            try:
                CAPI = float(CAPI)
                CAPI = int(CAPI)
                print u"Debe ingresar una Capital válida\n"
            except(RuntimeError, NameError, ValueError):
                if len(CAPI) <= 3:
                    print u"Debe ingresar una Capital válida\n"
                else:
                    PAISES[PAI] = CAPI
                    break

        while RESPUESTA3 != "no":
            RESPUESTA3 = raw_input("Desea Ingresar otro País si/no: \n")
            RESPUESTA3 = RESPUESTA3.lower()

            try:
                RESPUESTA3 = float(RESPUESTA3)
                RESPUESTA3 = int(RESPUESTA3)
                print "Error Desea Ingresar otro País si/no: \n"
            except(RuntimeError, NameError, ValueError):
                RESPUESTA3 = RESPUESTA3

            if RESPUESTA3 == "si":
                PAI = ""
                CAPI = ""
                break

            elif RESPUESTA3 == "no":
                break
                break

            else:
                print"\n  Error debe ingresar una opción válida\n"

    raw_input("Presione Enter para continuar ... ")
    os.system("clear")
    return 

#2. Lista de Paises
def listaPaises(): #Imprime lista de Paises
    print "Lista Paises ...\n"

    print "                             ***** Lista de Paises *****        \n"
    print "     Pais :\n"

    for X in PAISES:
        print "     "+ X +"\n"

    raw_input("Presione Enter para continuar ... ")
    os.system("clear")
    return

#3. Lista de Capitales
def listaCapitales():#Imprime la lista de Capitales
    print "Lista Capitales ...\n"

    print "                              ***** Lista de Capitales *****        \n"
    print "     Capital :\n"

    for X in PAISES:
        print "     "+ str(PAISES[X]) + "\n"


    raw_input("Presione Enter para continuar ... ")
    os.system("clear")
    return

#4. Ver Todo
def vertodo():
    print "Ver Todo ...\n"

    print "                         ***** Lista de Paises y Capitales *****        \n"
    print "     Pais        **/**        Capital     \n"

    for X in PAISES:
        print "     "+ X + "    ****    " + str(PAISES[X]) + "\n"

    raw_input("Presione Enter para continuar ... ")
    os.system("clear")
    return

#5. Todo Ordenado
def todoOrdenado():# Se imprimen las Capitales en orden alfabetico

    ORDEN = []
    PAISES2 = []
    
    print "                 ***** Todo Ordenado Paises ***** \n\n"

    ORDEN = PAISES.items()
    ORDEN.sort()
    print " Pais    **/**    Capital     \n"
    for i in ORDEN:
        print "    ****   ".join(i)
    print "\n"
    raw_input("Presione Enter para continuar ... ")
    print "\n                 ***** Todo Ordenado Capitales ***** \n\n"
    print u" Capital    **/**    País     \n"

    for PAIS, CAPITAL in PAISES.items():
    	TODOORDENADO[CAPITAL]=PAIS

    PAISES2 = TODOORDENADO.items()
    PAISES2.sort()
    for x in PAISES2:
        print "    ****   ".join(x)
    print "\n"
    raw_input("Presione Enter para continuar ... ")
    os.system("clear")
    return

def correo(PAISES):
    CORREO2 = " Pais    **/**    Capital     \n"
    CORREO1 = PAISES.items()
    CORREO1.sort()
    for i in CORREO1:
        CORREO2 += "    ****   ".join(i)+"\n"

    return CORREO2

#6. Envia E-mail
class todoMail(object):
    def __init__ (self):
        pass

    def enviarMail(self):
        print "Enviar E-mail ...\n"
        print "             **** Enviar E-Mail con Gmail **** \n\n"

        #Datos usuario
        usser = raw_input("Ingrese Cuenta de G-mail: ")
        password = getpass.getpass("Password: ")

        #Cabezeras del e-mail

        remitente = raw_input("From, ejemplo: administrador: <admin@gmail.com>: ")
        destinatario = raw_input("To, amigo: <amigo@gmail.com >: ")
        asunto = raw_input("Subject, Asunto del Mensaje: ") 
        mensaje = str(correo(PAISES))

        #Declaracion de variables publicas
        self.usser = usser
        self.password = password
        self.remitente = remitente
        self.de = destinatario
        self.asunto = asunto 
        self.mensaje = mensaje 

        #modulo y host SMTP DE GMAIL
        gmail = smtplib.SMTP('smtp.gmail.com:587')

        #Cifrado de datos de gmail
        gmail.ehlo()
        gmail.starttls()
        gmail.ehlo()

        #Credenciales
        gmail.login(usser, password)

        #Depuracion de envio
        gmail.set_debuglevel(1)

        #Cabezeras
        header = MIMEMultipart()
        header['Subject'] = asunto
        header['From'] = remitente
        header['To'] = destinatario

        mensaje = MIMEText(mensaje,'plain') # Conect- type:text/plain

        header.attach(mensaje)

        smtplib.SMTPAuthenticationError(534, '5.7.14')

        #Enviar
        print "Enviando... \n"
        gmail.sendmail(remitente, destinatario, header.as_string())

        #Se cierra la conexion
        gmail.quit()
        os.system("reset")

        print " Mensaje Enviado... "
        raw_input("Presione Enter para continuar ... ")
        os.system("clear")
        return


#Menu
def menu():
    OP = 0
    RESTRICCION = 0

    while True:

        while (OP != 1) or (OP != 2) or (OP != 3) or (OP != 4) or (OP != 5) or (OP != 6) or (OP != 7):
            print U"\n                         **** Desplegador de Paises © ****"
            print "1. Ingresar Paises "
            print "2. Lista de Paises "
            print "3. Lista de Capitales"
            print "4. Ver Todo"
            print "5. Ver Todo Ordenado"
            print "6. Enviar E-mail"
            print "7. Salir\n"

            OP = raw_input("Ingresa una opción: ")

            try:
                OP = int(OP)
                if OP > 0 and OP <= 7:
                    break
                else:
                    print "Ingrese opción válida\n"
                    time.sleep(2)
                    os.system("clear")
            except(RuntimeError, TypeError, NameError, ValueError):
                print "Ingrese opción válida\n"
                time.sleep(2)
                os.system("clear")
                pass

        if OP == 1:
            ingresoPaises()
            RESTRICCION = 1

        elif OP == 2 and RESTRICCION != 1:
            print "Error Ingreso de Datos Fallido\n"
            time.sleep(1)
            os.system("clear")
        elif OP == 2 and RESTRICCION == 1:
            listaPaises()

        elif OP == 3 and RESTRICCION != 1:
            print "Error Ingreso de Datos Fallido\n"
            time.sleep(1)
            os.system("clear")
        elif OP == 3 and RESTRICCION == 1:
            listaCapitales()

        elif OP == 4 and RESTRICCION != 1:
            print "Error Ingreso de Datos Fallido\n"
            time.sleep(1)
            os.system("clear")
        elif OP == 4 and RESTRICCION == 1:
            vertodo()

        elif OP == 5 and RESTRICCION != 1:
            print "Error Ingreso de Datos Fallido\n"
            time.sleep(1)
            os.system("clear")
        elif OP == 5 and RESTRICCION == 1:
            todoOrdenado()

        elif OP == 6 and RESTRICCION != 1:
            print "Error Ingreso de Datos Fallido\n"
            time.sleep(1)
            os.system("clear")
        elif OP == 6 and RESTRICCION == 1:
            enviar = todoMail()
            enviar.enviarMail()
        elif OP == 7 :
            print "Gracias por usar nuestro Programa ...\n"
            time.sleep(1)
            os.system("clear")
            print
            print u"                 **** Desplegador de Paises Full Pro 2.0 © **** "
            print u"                              ***** Cognits *****"
            print u"                         Third Generation Grupo: KAR-FER :\n"
            print u"                                  Fernando López"
            print u"                                   Kevin Herrera\n"
            print u"                          KAR_KO,INDUSTRIS Copyright ®"
            time.sleep(2)
            sys.exit()
    OP = 0
    return
menu() #Llamo a mi funcion menu