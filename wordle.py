import numpy as np

# Función para el uso de colores (BLANCO, AMARILLO, VERDE) en la salida por pantalla
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)



# Explicación de los colores del juego y su número que lo identifica en el código
'''
0 --> VERDE    ---> Existe esa letra en la palabra y está justo en esa posición
1 --> AMARILLO ---> Existe esa letra en la palabra pero no está en esa posición 
2 --> BLANCO   ---> No existe esa letra en la palabra
'''

# Clase con array de tamaño 5 de atributo para gestionar el color que ocupa cada letra en una jugada/intento.
class Info:

    def __init__(self):
        self.a = [2, 2, 2, 2, 2] # Inicializamos a valores por defecto (todo en BLANCO)

    def print(self, guess):

        for i in range (5):

            if self.a[i] == 0:
                color1 = 0    #
                color2 = 255  # Color verde
                color3 = 0    #

            elif self.a[i] == 1:
                color1 = 255  #
                color2 = 255  # Color amarillo
                color3 = 0    #

            elif self.a[i] == 2:
                color1 = 255  #
                color2 = 255  # Color blanco
                color3 = 255  # 

            else:
                assert(False) # Error!
            
            print(colored(color1, color2, color3, guess[i]), end= "") # Sacamos por pantalla la letra con su respectivo color


# Función que comprueba la coincidencia (en cuanto a letras se refiere) de dos palabras (devuelve un objeto de la clase Info)
def match(hidden, guess):

    info = Info()
    used = np.array([False, False, False, False, False])
    
    for i in range (5):
        #info.a[i] == 2 
        if guess[i] == hidden[i]: # Si tienen la misma letra en la misma posición...
            used[i] = True
            info.a[i] = 0 # ... pintamos de verde esa letra

    for i in range (5):
        if info.a[i] == 2: # Solo nos interesan las que no eran iguales (las que están en BLANCO)
            for j in range (5):
                if not used[j] and ( guess[i] == hidden[j] ): # Comprobamos si hay alguna letra igual en distintas posiciones...
                    used[j] = True
                    info.a[i] = 1 # ... la pintamos de amarillo
                    break

    return info
            
''' PROCESO PRINCIPAL '''

info = Info()
info = match('CIVIL', 'SILLA')
info.print('SILLA')