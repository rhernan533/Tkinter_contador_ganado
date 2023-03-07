from tkinter import *
from tkinter import scrolledtext as st
from tkinter import filedialog as fd
import datetime as dt
import os


raiz = Tk()

raiz.iconbitmap('icono.ico')
raiz.title('Contador de Ganado')

frame = Frame(raiz, width= 1200, height= 1000, bg= '#fac560').pack(fill='both', expand= True)

'''------------------------------------------------Ventana info------------------------------------------------------'''
ventana_info = Toplevel(frame) 

ventana_info.iconbitmap('icono.ico')

Label(ventana_info, text= 'Puede agregar la información que deseé recordar:', font= 'Calibri 12').pack(anchor= 'w',pady= 10)

info_user = st.ScrolledText(ventana_info, width= 35, height=12)
info_user.pack(anchor= 'center')

ventana_info.geometry('400x380+100+100')
ventana_info.transient(raiz)
ventana_info.resizable(0,0)

#NOMBRE DEL ENCARGADO DEL CONTEO:

etiq_autor = Label(ventana_info, text= 'Anotador: ', font= 'Calibri 12').place(x= 100, y=250)

nombre_autor = StringVar()
autor = Entry(ventana_info, textvariable= nombre_autor).place(x= 170, y=252)


#FECHA DE TRABAJO:

dia_horario = dt.datetime.now()

etiq_estatica_dia_hor = Label(ventana_info, text= 'Fecha y horario de trabajo:', font= 'Calibri 12', height= 1)
etiq_estatica_dia_hor.place(x=115, y=290)

etiq_dia_hor = Label(ventana_info, text= dt.datetime.strftime(dia_horario, '%d/%m/%Y %H:%M'), relief= 'groove')
etiq_dia_hor.place(x=160, y=315)

#BOTON GUARDAR info extra:

info_extra = StringVar()

def guardar_info():
    global info_extra, nombre_autor        
    info_extra = info_user.get("0.0", END)
    nombre_autor = nombre_autor.get() 
    ventana_info.destroy()
    


guardar = Button(ventana_info, text= '  Guardar  ', command= guardar_info)
guardar.place(x=170, y= 350)

def valores_defaul():
    global info_extra, nombre_autor
    if info_extra.strip() == '':
        info_extra = '**No se ha añadido información'

    if nombre_autor.strip() == '':
        nombre_autor= '**No se ha especificado el autor'


'''-------------------------------------------Objeto contadores------------------------------------------------------'''

class Contador:
    def __init__(self, texto, x, y):
    
        self.tipografia = 'Georgia 25'
        self.color_n = '#6ea1bf'
        
        self.relx = x 
        self.rely = y

        self.etiqueta = Label(frame, text= texto, font= self.tipografia, bg= self.color_n, anchor="n")
        self.etiqueta.place(relx= self.relx, rely= self.rely, relheight= 0.2, relwidth= 0.17)

        self.cont = 0
        self.color_a = '#f2efaa'

        self.etiqueta_cont = Label(frame, text= self.cont,bg= self.color_a,relief="sunken")
        self.etiqueta_cont.place(relx= self.relx + 0.055, rely= self.rely + 0.10, relwidth=0.06, relheight= 0.1)

        self.boton1 = Button(self.etiqueta, text= "-1", command= self.decrementar)
        self.boton1.place(relx= 0.005 , rely= 0.6, relheight= 0.4 , relwidth=0.25)

        self.boton2 = Button(self.etiqueta, text= "+1", command= self.incrementar)
        self.boton2.place(relx= 0.745, rely= 0.6, relheight= 0.4 , relwidth=0.25)
    
    def incrementar(self):
        self.cont = self.cont + 1
        self.etiqueta_cont.config(text= self.cont)

        global cont_total 
        global total
        cont_total = cont_total + 1
        total.config(text= f'TOTAL = {cont_total}')
         

    def decrementar(self):
        self.cont = self.cont - 1
        self.etiqueta_cont.config(text= self.cont)

        global cont_total 
        global total
        cont_total = cont_total - 1
        total.config(text= f'TOTAL = {cont_total}')

        
'''---------------------------------------------Etiqueta total-------------------------------------------------------'''
cont_total = 0 
total= Label(frame, text= f'TOTAL = {cont_total}', bg= '#f2efaa', font='Times 25', bd= 8, relief= 'raised')
total.place(relheight= 0.1 ,relwidth= 0.25 ,relx=0.725, rely=0.85)
'''------------------------------------------------------------------------------------------------------------------'''

vacas = Contador('Vacas', 0.081667, 0.2) 
toros = Contador('Toros', 0.418335, 0.2)
terneros = Contador('Terneros', 0.748333, 0.2)

novillos = Contador('Novillos', 0.248332, 0.5)
vaquillas = Contador('Vaquillas', 0.581665, 0.5)


raiz.mainloop()

'''-------------------------------------Crar blog de notas con la información---------------------------------------'''
DIRECTORIO = 'C:/Users/Usuario/Desktop/Registro del conteo del ganado/'
fin_ejecuccion = dt.datetime.now()


if not os.path.exists(DIRECTORIO):    #Comprueba si existe la direccion de DIRECTORIO
    os.makedirs(DIRECTORIO)           #En caso de no existir, la crea por esta linea de codigo

valores_defaul()  

with open(DIRECTORIO + 'Registro del día '+ dt.datetime.strftime(dia_horario, '%d-%m-%Y- %H %M')+ '.txt', 'w') as archivo:
    try:
        archivo.write('INFORMACIÓN DEL CONTEO:\n\n' + info_extra + 
        '\n\n\n-------------------------------------------------------------------------'
        '\n\nRegistro de conteo:\n'
        'Vacas:  '+ str(vacas.cont) +'\n'
        'Toros:  '+ str(toros.cont) +'\n'
        'Terneros:  '+ str(terneros.cont) +'\n'
        'Novillos:  '+ str(novillos.cont) +'\n'
        'Vaquillas:  '+ str(vaquillas.cont) +'\n\n'
        'TOTAL DEL GANADO:  '+ str(cont_total) + '\n\n\n'
        '\n\n\n-------------------------------------------------------------------------\n\n'
        'FECHA DE TRABAJO:   ' + dt.datetime.strftime(dia_horario, '%d/%m/%Y') + '\n'
        'HORA DE INICIO:   ' + dt.datetime.strftime(dia_horario, '%H:%M') + '\n'
        'HORA DE FINALIZACIÓN:   ' + dt.datetime.strftime(fin_ejecuccion, '%H:%M') + '\n'
        'AUTOR:   ' + nombre_autor + '\n') 

    except TypeError:
        archivo.write('INFORMACIÓN DEL CONTEO:\n\n**No se ha añadido información' 
        '\n\n\n-------------------------------------------------------------------------'
        '\n\nRegistro de conteo:\n'
        'Vacas:  '+ str(vacas.cont) +'\n'
        'Toros:  '+ str(toros.cont) +'\n'
        'Terneros:  '+ str(terneros.cont) +'\n'
        'Novillos:  '+ str(novillos.cont) +'\n'
        'Vaquillas:  '+ str(vaquillas.cont) +'\n\n'
        'TOTAL DEL GANADO:  '+ str(cont_total) + '\n\n\n'
        '\n\n\n-------------------------------------------------------------------------\n\n'
        'FECHA DE TRABAJO:   ' + dt.datetime.strftime(dia_horario, '%d/%m/%Y') + '\n'
        'HORA DE INICIO:   ' + dt.datetime.strftime(dia_horario, '%H:%M') + '\n'
        'HORA DE FINALIZACIÓN:   ' + dt.datetime.strftime(fin_ejecuccion, '%H:%M') + '\n'
        'AUTOR:   **No se ha especificado el autor\n')

    





