#importamos las librerias
import tkinter as tk
from  tkinter import ttk
from googletrans import Translator

translator = Translator()
ventana = tk.Tk()
ventana.configure(bg="blue")
ventana.geometry("700x200")
#funcion para realizar la traduccion
def traducir():
    datos= entrada.get()
    if datos!="":
    	#idioma de entrada
        variable_src = combo.get()
        #idioma de salida
        variable_dest= combo2.get()
        #traducimos los datos que ingresa el usuario
        resultado = translator.translate(datos, src=variable_src, dest=variable_dest)
        #en una ventana vemos el resultado
        resultado=tk.Label(ventana,text=resultado.text)
        respuesta.grid(row=5,column=1)
Etiqueta=tk.Label(ventana, text="Traductor Conect")
Etiqueta.grid(row=2,column=1)
entrada=tk.Entry(ventana)
entrada.grid(row=3,column=1)
#seleccionamos el origen del idioma en el cual estamos escribiendo
combo=ttk.Combobox(ventana,values=['en','es','ru','fr','ca'])
combo.current(0)
combo.grid(row=1,column=3)
#seleccionamos el idioma en el cual queremos que nos tradusca
combo2=ttk.Combobox(ventana,values=['en','es','ru','fr','ca'])
combo2.current(1)
combo2.grid(row=1,column=6)

