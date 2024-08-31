#Save this project as: TV for my grandma, done by Shadows of war, (Luna González)

import tkinter as tk
import webbrowser

# Función para abrir un enlace en el navegador
def abrir_enlace(url):
    webbrowser.open(url)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Televisión para la Yaya")
ventana.configure(bg='black')  # Cambiar el color de fondo a negro

# Definir el tamaño de la ventana
ancho_ventana = 600
alto_ventana = 400

# Obtener el tamaño de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Calcular la posición para centrar la ventana
pos_x = (ancho_pantalla - ancho_ventana) // 2
pos_y = (alto_pantalla - alto_ventana) // 2

# Establecer la geometría de la ventana con la posición centrada
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

# Lista de nombres de los botones y sus URLs correspondientes
canales = {
    "La 1": "https://www.rtve.es/play/videos/directo/canales-lineales/la-1/",
    "La 2": "https://www.rtve.es/play/videos/directo/canales-lineales/la-2/",
    "Antena 3": "https://www.atresplayer.com/directos/antena3/",
    "La Cuatro": "https://www.mitele.es/directo/cuatro/",
    "Telecinco": "https://www.mitele.es/directo/telecinco/",
    "La Sexta": "https://www.atresplayer.com/directos/lasexta/"
}

# Crear y agregar botones a la ventana con tamaño grande
for nombre, url in canales.items():
    boton = tk.Button(
        ventana, 
        text=nombre, 
        command=lambda u=url: abrir_enlace(u), 
        bg='gray', 
        fg='white', 
        width=20,     # Ajusta el ancho del botón
        height=2,     # Ajusta la altura del botón
        font=('Arial', 16, 'bold')  # Ajusta el tamaño de la fuente
    )
    boton.pack(pady=10)  # Incrementa el espacio vertical entre botones

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
