import tkinter as tk
from clases.ventana_capturar_cadena import CapturarCadena
from clases.ventana_mostrar_creditos import MostrarCreditos
from clases.salir import Salir

root = tk.Tk()
root.title("Ventana Principal")
root.geometry("300x150")

cc = CapturarCadena()
mc = MostrarCreditos()
s = Salir()

boton_captura = tk.Button(root, text="Capturar Cadena de Entrada", command=lambda: cc.capturar_cadena(root))
boton_captura.pack(pady=10)

boton_creditos = tk.Button(root, text="Créditos", command=lambda: mc.mostrar_creditos(root))
boton_creditos.pack(pady=10)

boton_salir = tk.Button(root, text="Salir", command=lambda: s.salir(root))
boton_salir.pack(pady=10)

root.mainloop()
