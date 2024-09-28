class Automata:
    def __init__(self, cadena):
        self.cadena = cadena

# Alfabeto
impar = ["1", "3", "5", "7", "9"]
par = ["0", "2", "4", "6", "8"]
consMay = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
simbolo = ["@", "#", "&", "%", "$"]

# Recibir la cadena por el input
cadena_input = input("Introduce una cadena: ")

# Descomponer cadena y guardar en una lista de elementos
cadena_elementos = list(cadena_input)

# Crear el automata y asignarle la cadena
automata = Automata(cadena_elementos)

def validar(automata):
    # Variables
    simbolo_count = 0
    estado = 0  
    i = 0      
    n = len(automata.cadena)  
    
    while i < n: 
        c = automata.cadena[i]  
        match estado:
            case 0:
                if c in impar:
                    estado = 1
                else:
                    return False
            case 1:
                if c in consMay:
                    estado = 2
                else:
                    return False
            case 2:
                if c in impar:
                    estado = 3
                elif c in par:
                    estado = 6
                else:
                    return False
            case 3:
                if c in impar:
                    estado = 4
                else:
                    return False
            case 4:
                if c in impar:
                    estado = 4 
                elif c in par:
                    estado = 5
                else:
                    return False
            case 5:
                if c in simbolo and i == n - 1:
                    estado = 8
                else:
                    return False
            case 6:
                if c in par:
                    estado = 6  
                elif c in impar:
                    estado = 7
                else:
                    return False
            case 7:
                if c in simbolo and i == n - 1:
                    estado = 8
                else:
                    return False
            case 8:
                return True
        i += 1  
    
    # Si el automata se encuentra en el estado 8, la cadena es valida
    return estado == 8

# Validar la cadena ingresada
if validar(automata):
    print("Cadena Válida")
else:
    print("Cadena Inválida")
