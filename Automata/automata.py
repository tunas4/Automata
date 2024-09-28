class Automata:
    def __init__(self, cadena):
        self.cadena = cadena

# Alfabeto
impar = ["1","3","5","7","9"]
par = ["0","2","4","6","8"]
consMay = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
simbolo = ["@","#","&","%","$"]

# Recibir la cadena por el input
cadena_input = input("Introduce una cadena: ")

# Descomponer cadena y guardar en una lista de elementos
cadena_elementos = list(cadena_input)

# Crear el automata y asignarle la cadena
automata = Automata(cadena_elementos)

def validar(automata):
    # Variables de la funcion
    estado = i = 0
    n = len(automata.cadena)
    seguir = True

    while i < n and seguir:
        c = automata.cadena[i]
        match estado:
            case 0:
                if c in impar:
                    estado = 1
                    i += 1
                else:
                    seguir = False
            case 1:
                if c in consMay:
                    i += 1
                    estado = 2
                else:
                    seguir = False
            case 2:
                if c in impar:
                    i += 1
                    estado = 3
                elif c in par:
                    estado = 6
                    i += 1
                else:
                    seguir = False
            case 3:
                if c in impar:
                    i += 1
                    estado = 4
                else:
                    seguir = False
            case 4:
                    if c in impar:
                        i += 1
                    elif c in par:
                        estado = 5
                        i += 1
                    else:
                        seguir = False
            case 5:
                if c in simbolo:
                    estado = 8
                    i += 1
                else:
                    seguir = False
            case 6:
                    if c in par:
                        i += 1
                    elif c in impar:
                        estado = 7
                        i += 1
                    else:
                        seguir = False
            case 7:
                if c in simbolo:
                    i += 1
                    estado = 8
                else:
                    seguir = False

    if estado == 8:
        seguir = True
    else:
        seguir = False

    return seguir

if(validar(automata)):
    print("Cadena Valida")
else:
    print("Cadena Invalida")
