from tkinter import *
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image,ImageTk



#........................Ventana.Principal.................................

vPrincipal = tk.Tk()
vPrincipal.title("Laberinto")
vPrincipal.geometry("1200x920")

imgFondo = Image.open('fondo.jpeg')
imgFondo = imgFondo.resize((1205, 925), Image.ANTIALIAS) # Redimension (Alto, Ancho)
imgFondo = ImageTk.PhotoImage(imgFondo)
fondo= Label(vPrincipal,image=imgFondo).place(x=-5,y=-5)




imgLab = Image.open('laberinto.jpg')
imgLab = imgLab.resize((400, 400), Image.ANTIALIAS) # Redimension (Alto, Ancho)
imgLab = ImageTk.PhotoImage(imgLab)
fondo= Label(vPrincipal,image=imgLab).place(x=450,y=100)

#clase marcador para las señales en el mapa
class Markers:
    
    def Markers(self,posx,posy):
        marker= tk.Button(vPrincipal,width=2 ,height=2, image=imgFondo, command=lambda: Markers.OpenWindow()).place(x=posx ,y=posy)
    def OpenWindow():
        newWindow = Toplevel(vPrincipal)
        
        newWindow.title("Información")
        newWindow.geometry("270x260")
        #fondo= Label(newWindow,image=imgFondoPokebola).place(x=0,y=0)
        #newWindow.iconbitmap('pIcon.ico')
        label= Label(newWindow,fg="black",font=("Arial",13,"bold"),text="Informacion").place(x=50,y=4)
        

#Pone los marcadores en el mapa
def crearMarcadores():

    marcador = Markers()
    marcador.Markers(650,270)
    

crearMarcadores()

vPrincipal.mainloop()
