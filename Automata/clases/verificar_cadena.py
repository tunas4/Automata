class Automata:
    def __init__(self):
        self.cadena = ""

    def validar(cadena):
        cadena = cadena  # Almacena la cadena en la instancia
        estado = 0
        n = len(cadena)

        impar = ["1", "3", "5", "7", "9"]
        par = ["0", "2", "4", "6", "8"]
        consMay = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
        simbolo = ["@", "#", "&", "%", "$"]

        for i in range(n):
            c = cadena[i]
            match estado:
                case 0:
                    if c in impar:
                        estado = 1
                    else:
                        return "Cadena Inválida0"
                case 1:
                    if c in consMay:
                        estado = 2
                    else:
                        return "Cadena Inválida1"
                case 2:
                    if c in impar:
                        estado = 3
                    elif c in par:
                        estado = 6
                    else:
                        return "Cadena Inválida2"
                case 3:
                    if c in impar:
                        estado = 4
                    else:
                        return "Cadena Inválida3"
                case 4:
                    if c in par:
                        estado = 5
                    if c in impar:
                        estado = 4
                    else:
                        return "Cadena Inválida4"
                case 5:
                    if c in simbolo:
                        estado = 8
                    else:
                        return "Cadena Inválida5"
                case 6:
                    if c in impar:
                        estado = 7
                    if c in par:
                        estado = 6
                    else:
                        return "Cadena Inválida6"
                case 7:
                    if c in simbolo:
                        estado = 8
                    else:
                        return "Cadena Inválida7"
                case 8:
                    if i == n - 1:
                        return "Cadena Válida8"
                    else:
                        return "Cadena Inválida9"