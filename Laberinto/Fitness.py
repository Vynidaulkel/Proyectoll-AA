import random
global pesos, colores 
poblacion=[]
pesos=()
pesos2=()

def Crear_poblacion(cantidad,imagen,tamanho,porcentaje):
    
    global colores, pesos2, pesos
   
    poblacion=[]
    pesos=()
    pesos2=()

    individuos=[]
    colores= imagen

    #Crea la cantidad de la poblacion que el usuario ingresa
    numero_individuo=0
    for _ in range(cantidad):
        x= random.randint(0,49)
        y= random.randint(0,49)
        nota= fitness([x,y],imagen)
        individuos.append([x,y,nota,"Primera generacion",numero_individuo])
        numero_individuo+=1
    
    pesos=pesos2
    pesos2=()
    poblacion.append(individuos)
    
    
    dato=seleccion(poblacion,pesos,cantidad,porcentaje)
    poblacion.append(dato)
    
    #Crea todas las poblaciones que el usuario ingresa 
    for l in range(tamanho):
        pesos=pesos2
        pesos2=()
        dato=seleccion([dato],pesos,cantidad,porcentaje)
        poblacion.append(dato)
        
    pesos2=()
   
    return poblacion



def fitness(individuo,imagen):
    global pesos2 
    peso = 0
    color= []

    color.append(imagen[individuo[0]][individuo[1]]) 


    if 235 < color[0][0] and 235 < color[0][1] and 235 < color[0][2]:
        peso += 300 

    for n in range(2):
        try:
            #Guarda los datos de los pixeles cerca del punto, en horizontal
            # y vertical
            color.append(imagen[individuo[0]-n][individuo[1]])
            color.append(imagen[individuo[0]+n][individuo[1]])
            color.append(imagen[individuo[0]][individuo[1]-n])
            color.append(imagen[individuo[0]][individuo[1]-n])

            #Guarda las coordenadas de los pixeles cerca del punto en
            #diagonal 
            color.append(imagen[individuo[0]+n][individuo[1]+n])
            color.append(imagen[individuo[0]+n][individuo[1]-n])
            color.append(imagen[individuo[0]-n][individuo[1]+n])
            color.append(imagen[individuo[0]-n][individuo[1]+n])
        except:
            #En caso que no choque con un borde y no tenga datos cerca 
            color.append(imagen[individuo[0]][individuo[1]])
       

   
    #Pone la nota dependiendo del color 
    for n in color:
        #negro
        if n[0]<8 and n[1]<8 and n[2]<8:
            peso -=50

        #blanco
        elif 235 < n[0] and 235 < n[1] and 235 < n[2]:
            peso += 100

        #Colores de la entrada y salida 
        else:
            peso += 100

    #En caso que sea un punto negro sin nada cerca 
    if peso<0:
        peso=1
    pesos2+=(peso,)
    return peso 

#Selecciona 2 padres entre los mejores candidatos y realiza
#un cruce entre ambos dando como resultado un miembro de la
#nueva generacion
def seleccion(poblacion,pesos,cantidad,porcentaje):
    global colores

    indice=len(poblacion)-1
    resultado=[]
    mejores=[]
    numero_individuo=0
    #Crea una nueva poblacion con la misma cantidad que la anterior 
    for hijos in range(cantidad):
        mejores=[]
        
        
        mejores= (random.choices(poblacion[indice], weights=pesos, k=2))
        
        lista_hijos=[]
        cromosoma=""
        
        #Pasa los datos de ambos padres a binario
        x1=format(mejores[0][0], '08b')
        x2=format(mejores[1][0], '08b')

        y1=format(mejores[0][1], '08b')
        y2=format(mejores[1][1], '08b')

        #Crea los valores aleatorios para que mute
        if random.randint(0,10) >porcentaje:
            #Cromosoma que muta en X y en Y
            x= random.randint(0,7) 
            y= random.randint(0,1)
        else:
            #En caso que no haya mutacion
            x=-1
            y=-1

        #Combina los valores de ambos padres para x
        for letra in range(8):
            if y==0 and x == letra:
                cromosoma+=str(random.randint(0,1))

            elif letra<4:
                cromosoma+=x1[letra]
            else:
                cromosoma+=x2[letra]

        if binario_a_decimal(cromosoma)>=50:
            x3=random.randint(0,49)
        else:
            x3=binario_a_decimal(cromosoma)

        cromosoma=""
        
        #Combina los valores de ambos padres para y
        for letra in range(8):
            if y==1 and x == letra:
                cromosoma+=str(random.randint(0,1))

            if letra<4:
                cromosoma+=y1[letra]
            else:
                cromosoma+=y2[letra]
        

        if binario_a_decimal(cromosoma)>=50:
            y4=random.randint(0,49)
           
        else:
            y4=binario_a_decimal(cromosoma)
            

        notas=fitness([x3,y4],colores)
        lista_hijos.append(mejores)
        resultado.append([x3,y4, notas,"#"+str(mejores[0][4])+ ": " +"("+str(mejores[0][0])+ ","+str(mejores[0][1]) +")  #"+str(mejores[1][4])+": ("+str(mejores[1][0])+ ","+str(mejores[1][1])+")",numero_individuo ])
        lista_hijos=[]
        numero_individuo+=1
  
    return resultado
    

#Convierte el numero binario a decimal      
def binario_a_decimal(numero_binario):
	numero_decimal = 0 

	for posicion, digito_string in enumerate(numero_binario[::-1]):
		numero_decimal += int(digito_string) * 2 ** posicion

	return numero_decimal

