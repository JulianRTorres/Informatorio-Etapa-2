import tkinter as tk

ventana = tk.Tk()
ventana.title('Mi primer ventana con Tkinter')
ventana.geometry('400x600')

etiqueta = tk.Label(ventana, text='Hola Mundo', font=('Console', 20))
etiqueta.pack()

etiqueta_2 = tk.Label(ventana, text='Etiqueta 2', font=('Arial', 30))
etiqueta_2.place(height=300)

ventana.mainloop()