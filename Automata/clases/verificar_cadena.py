class Automata:
    def validar(cadena):
        # Alfabeto
        impar = ["1", "3", "5", "7", "9"]
        par = ["0", "2", "4", "6", "8"]
        consMay = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
        simbolo = ["@", "#", "&", "%", "$"]

        # Variables
        estado = 0  
        i = 0      
        n = len(cadena)  
        
        while i < n: 
            c = cadena[i]  
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
        
        return estado == 8