from tkinter import *
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image,ImageTk
from Fitness import Crear_poblacion
import numpy
from PIL import Image

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
    image = Image.open('laberinto.jpg', "r")
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

imgLab = Image.open('laberinto.jpg')
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
        label= Label(newWindow,fg="black",font=("Arial",13,"bold"),text="Posicion= x:"+ str(individuo[1]) +"  "+ "y:"+str(individuo[0])+ "nota:"+str(individuo[2])).place(x=20,y=40)

#Pone los marcadores en el mapa
def crearMarcadores(marcadores):
    for punto in marcadores:
        marcador = Markers()
        marcador.Markers(punto[0]*8.05+451, punto[1]*8.05+101,punto)

crearMarcadores(Crear_poblacion(50,image))

vPrincipal.mainloop()





