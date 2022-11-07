from tkinter import *
import random

root=Tk()
root.title("Generador de numeros random")
root.geometry("850x400")

random_number_list = Label(root)
random_number_sorted_list = Label(root)

def randomlist():
    randomlist = random.sample(range(0,100),25)
    random_number_list["text"] = "Lista aleatoria: " + str(randomlist)
    randomlist.sort()
    random_number_sorted_list["text"] = "Números aleatorios ordenados: " + str(randomlist)

def salir():
    root.destroy()

def eliminar():
    randomlist = random.sample(range(0,0),0)
    random_number_list["text"] = ""
    randomlist.sort()
    random_number_sorted_list["text"] = ""

btn=Button(root,text="Generar lista",command=randomlist)
btn.place(relx=0.5,rely=0.2,anchor=CENTER)

btn=Button(root,text="Eliminar lista",command=eliminar)
btn.place(relx=0.5,rely=0.3,anchor=CENTER)

random_number_list.place(relx=0.5,rely=0.5,anchor=CENTER)
random_number_sorted_list.place(relx=0.5,rely=0.6,anchor=CENTER)

btn=Button(root,text="SALIR",command=salir)
btn.place(relx=0.5,rely=0.8,anchor=CENTER)

root.mainloop()
