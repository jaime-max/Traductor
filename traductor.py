import tkinter as tk
from  tkinter import ttk
from googletrans import Translator

translator = Translator()
ventana = tk.Tk()
ventana.configure(bg="blue")
ventana.geometry("700x200")
#funcion para realizar la traduccion
def con_tra():
    datos= entrada.get()
    if datos!="":
        variable_src = combo.get()
        variable_dest= combo2.get()
        resultado = translator.translate(datos, src=variable_src, dest=variable_dest)
        resultado=tk.Label(ventana,text=resultado.text)
        respuesta.grid(row=5,column=1)
Etiqueta=tk.Label(ventana, text="Traductor Conect")
Etiqueta.grid(row=2,column=1)
entrada=tk.Entry(ventana)
entrada.grid(row=3,column=1)

combo=ttk.Combobox(ventana,values=['en','es','ru','fr','ca'])
combo.current(0)
combo.grid(row=1,column=3)

combo2=ttk.Combobox(ventana,values=['en','es','ru','fr','ca'])
combo2.current(1)
combo2.grid(row=1,column=6)

boton=tk.Button(ventana,text="aceptar",command=con_tra)
boton.grid(row=1,column=1)

ventana.mainloop()