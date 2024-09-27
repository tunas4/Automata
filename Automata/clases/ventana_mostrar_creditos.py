import tkinter as tk

class MostrarCreditos:
    def mostrar_creditos(self, root):
        creditos_ventana = tk.Toplevel(root)
        creditos_ventana.geometry("300x150")
        creditos_ventana.title("Créditos")
        
        label1 = tk.Label(creditos_ventana, text="Jonathan Ivan Castro Saenz")
        label1.pack(pady=30)

        label2 = tk.Label(creditos_ventana, text="Noe Abel Vargas López")
        label2.pack()
