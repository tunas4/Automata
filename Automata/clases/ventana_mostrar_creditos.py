import tkinter as tk

class MostrarCreditos:
    def mostrar_creditos(self, root):
        creditos_ventana = tk.Toplevel(root)
        creditos_ventana.geometry("300x150")
        creditos_ventana.title("Créditos")

        label = tk.Label(creditos_ventana, text="Grado: 4 | Sección: A")
        label.pack()

        label0 = tk.Label(creditos_ventana, text="Asignatura: Estructura de Datos y Aplicadas")
        label0.pack()
        
        label1 = tk.Label(creditos_ventana, text="Jonathan Ivan Castro Saenz | 23170035")
        label1.pack(pady=30)

        label2 = tk.Label(creditos_ventana, text="Noe Abel Vargas López | 23170106")
        label2.pack()