import tkinter as tk
from tkinter import scrolledtext as st
import googletrans

ventana = tk.Tk()
ventana.title("Traductor de Idiomas")
ventana.geometry("800x500")
ventana.resizable(width=False, height=False)

fondo= tk.PhotoImage(file="fondo.png")
fondo1= tk.Label(ventana, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)

traductor = googletrans.Translator()

#fondo
boton_fondo= "#004AAD"
lista_fondo= "#e2e2e2"

caja = st.ScrolledText(ventana, width=37, height=7, relief="flat", font=("Califri Light", 12))
caja.place(x=20, y=170)

caja2 = tk.Text(ventana, width=37, height=7, relief="flat", font=("Califri Light", 12))
caja2.place(x=410, y=170)

def traducir():
    datos = caja.get("1.0", tk.END)
    traduccion = traductor.translate(datos, dest=idioma2.get())
    caja2.insert(tk.END, traduccion.text)
def borrar():
    caja2.delete("1.0", tk.END)

idioma = tk.StringVar(ventana)
idioma2 = tk.StringVar(ventana)
list1 = googletrans.LANGUAGES
list2 = list1.values()
list3 = list(list2)
idiomas= []
for i in list3:
    idiomas.append(i)

#droplist = tk.OptionMenu(ventana, idioma, *idiomas)
#idioma.set("Seleccione el idioma a traducir")
#droplist.config(width=30, cursor="hand2", relief="flat", bg=lista_fondo, font=("Arial", 12, "bold"))
#droplist.place(x=74, y=110)

droplist2= tk.OptionMenu(ventana, idioma2, *idiomas)
idioma2.set("Seleccione el idioma a traducir")
droplist2.config(width=30, cursor="hand2", relief="flat", bg=lista_fondo, font=("Arial", 12, "bold"))
droplist2.place(x=425, y=110)

#botones
boton2 = tk.Button(ventana, text="Traducir", command=traducir, relief="flat", cursor="hand2", bg=boton_fondo,
height=2, width=14, font=("Arial", 12, "bold"))
boton2.place(x=99, y=343)

boton3 = tk.Button(ventana, text="Borrar", command=borrar, relief="flat", cursor="hand2", bg=boton_fondo,
height=2, width=14, font=("Arial", 12, "bold"))
boton3.place(x=582, y=344)


ventana.mainloop()







