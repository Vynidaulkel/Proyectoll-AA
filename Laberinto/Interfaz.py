from tkinter import *
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image,ImageTk
from Fitness import Crear_poblacion
import numpy
from PIL import Image
 
from tkinter import ttk

#........................Ventana.Principal.................................

vPrincipal = tk.Tk()
vPrincipal.title("Laberinto")
vPrincipal.geometry("1200x920")

imgFondo = Image.open('fondo.jpeg')
imgFondo = imgFondo.resize((1205, 925), Image.ANTIALIAS) # Redimension (Alto, Ancho)
imgFondo = ImageTk.PhotoImage(imgFondo)
fondo= Label(vPrincipal,image=imgFondo).place(x=-5,y=-5)

imgFondoboton = Image.open('rojo.jpg')
imgFondoboton = imgFondoboton.resize((1205, 925), Image.ANTIALIAS) # Redimension (Alto, Ancho)
imgFondoboton = ImageTk.PhotoImage(imgFondoboton)

#Obtener la imagen para saber color de los pixeles 
def get_image(image_path):
    """Get a numpy array of an image so that one can access values[x][y]."""
    image = Image.open('laberinto.png', "r")
    width, height = image.size
    pixel_values = list(image.getdata())
    if image.mode == "RGB":
        channels = 3
    elif image.mode == "L":
        channels = 1
    else:
        print("Unknown mode: %s" % image.mode)
        return None
    pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
    return pixel_values

imgLab = Image.open('laberinto.png')
imgLab = imgLab.resize((400, 400), Image.ANTIALIAS) # Redimension (Alto, Ancho)
imgLab = ImageTk.PhotoImage(imgLab)
fondo= Label(vPrincipal,image=imgLab).place(x=450,y=100)

image = get_image('laberinto.jpg')

#clase marcador para las señales en el mapa
class Markers:
    def Markers(self,posx,posy,individuo):
        marker= tk.Button(vPrincipal,width=2 ,height=2,bg = "red", image=imgFondoboton, command=lambda: Markers.OpenWindow(individuo)).place(x=posx ,y=posy)
    def OpenWindow(individuo):
        newWindow = Toplevel(vPrincipal)
        newWindow.title("Información")
        newWindow.geometry("270x260")
        #fondo= Label(newWindow,image=imgFondoPokebola).place(x=0,y=0)
        #newWindow.iconbitmap('pIcon.ico')
        label= Label(newWindow,fg="black",font=("Arial",13,"bold"),text="Informacion").place(x=75,y=4)
        label= Label(newWindow,fg="black",font=("Arial",13,"bold"),text="Individuo #"+str(individuo[4])).place(x=20,y=40)
        label= Label(newWindow,fg="black",font=("Arial",13,"bold"),text="Posicion= x:"+ str(individuo[1]) +"  "+ "y:"+str(individuo[0])).place(x=20,y=80)
        label= Label(newWindow,fg="black",font=("Arial",13,"bold"),text="Nota="+str(individuo[2])).place(x=20,y=120)
        label= Label(newWindow,fg="black",font=("Arial",13,"bold"),text="Padres=").place(x=20,y=160)
        label= Label(newWindow,fg="black",font=("Arial",13,"bold"),text=str(individuo[3])).place(x=20,y=180)
        


# Combobox creation
n = tk.StringVar()
monthchoosen = ttk.Combobox(vPrincipal, width = 27, textvariable = n)
  
# Adding combobox drop down list
 
  
monthchoosen.grid(column = 1, row = 5)
monthchoosen.current()
monthchoosen.place(relx="0.46",rely="0.07")

def seleccion():
    fondo= Label(vPrincipal,image=imgLab).place(x=450,y=100)
    crearMarcadores(datos,monthchoosen.current())
    


btn = ttk.Button(vPrincipal, text="Ver poblacion",command=seleccion)
btn.place(relx="0.45",rely="0.8")

#Pone los marcadores en el mapa
def crearMarcadores(marcadores,indice):
    
    for punto in marcadores[indice]:
        marcador = Markers()
        marcador.Markers(punto[1]*8.05+451, punto[0]*8.05+101,punto)




m = tk.StringVar()
porcentaje = ttk.Combobox(vPrincipal, width = 27, textvariable = m)
# Adding combobox drop down list
porcentaje['values'] = (' 100%', ' 90%', 
                          ' 80%',
                          ' 70%',
                          ' 60%',
                          ' 50%',
                          ' 40%',
                          ' 30%',
                          ' 20%',
                          ' 10%',
                          ' 0%',)
  
porcentaje.grid(column = 1, row = 5)
porcentaje.current()
porcentaje.place(relx="0.46",rely="0.6")


# Crear caja de texto.
txtcantidad = ttk.Entry(vPrincipal)
# Posicionarla en la ventana.
txtcantidad.place(relx="0.55",rely="0.7")


# Crear caja de texto.
txtpoblacion = ttk.Entry(vPrincipal)
# Posicionarla en la ventana.
txtpoblacion.place(relx="0.43",rely="0.7")


def crearPoblacion():
    global datos
    datos=Crear_poblacion(int(txtpoblacion.get()),image,int(txtcantidad.get()),porcentaje.current())

    lista=[]
    for n in range (int(txtcantidad.get())):
        lista.append(str(n))
    monthchoosen['values']= lista



btn2 = ttk.Button(vPrincipal, text="Crear poblacion",command=crearPoblacion)
btn2.place(relx="0.56",rely="0.8")


vPrincipal.mainloop()





