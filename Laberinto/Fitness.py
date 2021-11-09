import random
global pesos 
poblacion=[]
pesos=()

def Crear_poblacion(cantidad,imagen):
    print(len(poblacion))
    if len(poblacion)==0:
        Crear_otra_poblacion()
    for _ in range(cantidad):
        x= random.randint(0,49)
        y= random.randint(0,49)
        nota= fitness([x,y],imagen)
        poblacion.append([x,y,nota])
    
    seleccion(poblacion,pesos)

    return poblacion


def Crear_otra_poblacion():
    return


def fitness(individuo,imagen):
    global pesos 
    color= imagen[individuo[0]][individuo[1]]
    binario = format(individuo[0], "b")
    print(individuo)
    print(binario)
    print(binario[0],"primero")

    
    if color[0]<5 and color[1]<5 and color[2]<5:
        pesos+=(0,)
        return 0
    elif 240 < color[0] and 240 < color[1] and 240 < color[2]:
        pesos+=(50,)
        return 50
    else:
        pesos+=(100,)
        return 100


def seleccion(poblacion,pesos):
    
     
    print(random.choices(poblacion, weights=pesos, k=50))
    return 

    
     


