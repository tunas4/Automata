import tkinter as tk
from clases.verificar_cadena import VerificarCadena

vc = VerificarCadena()

class CapturarCadena:
    def capturar_cadena(self, root):
        captura_ventana = tk.Toplevel(root)
        captura_ventana.geometry("300x150")
        captura_ventana.title("Capturar cadena de entrada")
        
        label = tk.Label(captura_ventana, text="Introduce una cadena:")
        label.pack(pady=10)
        
        textbox = tk.Entry(captura_ventana, width=40)
        textbox.pack(pady=10)
        
        def capturar():
            cadena = textbox.get()
            resultado = vc.verificar_cadena(cadena)
            resultado_label = tk.Label(captura_ventana, text=resultado)
            resultado_label.pack(pady=10)
        
        boton = tk.Button(captura_ventana, text="Capturar", command=capturar)
        boton.pack()
