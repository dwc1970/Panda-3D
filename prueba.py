#Funcion para dibujar un cuadrado
#def dibujar_triangulo(tamaño):
 #   for i in range(1, tamaño, 1):
  #      print('*' * i)
    
# Ejemplo de uso
#tamaño = int(input("ingrese el tramaño del triangulo: "))
#dibujar_triangulo(tamaño)

# crear un circulo
import math

# Funcion par dibujar un ciculo
def dibujar_circulo(radio):
    # Recorrer los puntos en una cuadricula
    for i in range((radio * 2) + 1):
        for i in range((radio * 2) +1):
            #Calcular la distancia al centro del circulo 
            distancia = math.sqrt((i - radio) ** 2 +(j -radio) **2)
            
            # Si la distancio esta cerca del radio , imprime un asterisco
            if distancia < radio + 0.5 and distancia > radio - 0.5:
                print("*", end="")
            else:
                print(" ", end="")
        print()
        