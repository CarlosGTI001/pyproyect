import os
from tkinter import Tk, Label, Button, filedialog, ttk, Frame, Scrollbar, Listbox
from moviepy.editor import *
from ttkthemes import ThemedStyle

def seleccionar_carpeta_entrada():
    global carpeta_entrada
    carpeta_entrada = filedialog.askdirectory()
    label_carpeta_entrada.config(text=f"Carpeta de entrada: {carpeta_entrada}")
    actualizar_lista_archivos(lista_izquierda, carpeta_entrada)

def seleccionar_carpeta_salida():
    global carpeta_salida
    carpeta_salida = filedialog.askdirectory()
    label_carpeta_salida.config(text=f"Carpeta de salida: {carpeta_salida}")
    actualizar_lista_archivos(lista_derecha, carpeta_salida)

def convertir_a_mp3():
    archivos = os.listdir(carpeta_entrada)
    cantidad_archivos = len([archivo for archivo in archivos if os.path.isfile(os.path.join(carpeta_entrada, archivo))
                             and (archivo.endswith(".mp4") or archivo.endswith(".avi") or archivo.endswith(".wav")
                             or archivo.endswith(".opus") or archivo.endswith(".m4a"))])

    progreso['maximum'] = cantidad_archivos
    progreso['value'] = 0

    for archivo in archivos:
        ruta_completa = os.path.join(carpeta_entrada, archivo)
        if os.path.isfile(ruta_completa) and (archivo.endswith(".mp4") or archivo.endswith(".avi") or archivo.endswith(".wav")
                             or archivo.endswith(".opus") or archivo.endswith(".m4a")):
            clip = AudioFileClip(ruta_completa)
            nombre_mp3 = os.path.splitext(archivo)[0] + ".mp3"
            ruta_mp3 = os.path.join(carpeta_salida, nombre_mp3)
            clip.write_audiofile(ruta_mp3)
            clip.close()

            progreso['value'] += 1
            root.update_idletasks()
            lista_derecha.insert("end", nombre_mp3)

def actualizar_lista_archivos(lista, carpeta):
    lista.delete(0, "end")
    archivos = os.listdir(carpeta)
    for archivo in archivos:
        lista.insert("end", archivo)

# Configuración de la ventana
root = Tk()
root.title("Conversor de Audio/Video a MP3")
root.geometry("800x400")  # Tamaño de la ventana

# Estilo Material Design
style = ThemedStyle(root)
style.set_theme("equilux")

# Frames para organizar la interfaz
frame_izquierda = Frame(root, padx=10, pady=10)
frame_izquierda.pack(side="left", fill="both", expand=True)

frame_centro = Frame(root, padx=10, pady=10)
frame_centro.pack(side="left", fill="both", expand=True)

frame_derecha = Frame(root, padx=10, pady=10)
frame_derecha.pack(side="left", fill="both", expand=True)

# Lista de archivos en la carpeta de entrada
label_lista_izquierda = Label(frame_izquierda, text="Archivos en la carpeta de entrada")
label_lista_izquierda.pack()

scroll_izquierda = Scrollbar(frame_izquierda, orient="vertical")
scroll_izquierda.pack(side="right", fill="y")

lista_izquierda = Listbox(frame_izquierda, yscrollcommand=scroll_izquierda.set)
lista_izquierda.pack(fill="both", expand=True)
scroll_izquierda.config(command=lista_izquierda.yview)

# Botones para seleccionar carpetas de entrada y salida
boton_carpeta_entrada = Button(frame_centro, text="Seleccionar carpeta de entrada", command=seleccionar_carpeta_entrada)
boton_carpeta_entrada.pack()

boton_carpeta_salida = Button(frame_centro, text="Seleccionar carpeta de salida", command=seleccionar_carpeta_salida)
boton_carpeta_salida.pack()

boton_convertir = Button(frame_centro, text="Convertir a MP3", command=convertir_a_mp3)
boton_convertir.pack()

# Etiquetas para mostrar las carpetas seleccionadas
label_carpeta_entrada = Label(frame_centro, text="Carpeta de entrada: ")
label_carpeta_entrada.pack()

label_carpeta_salida = Label(frame_centro, text="Carpeta de salida: ")
label_carpeta_salida.pack()

# Barra de progreso
progreso = ttk.Progressbar(frame_centro, orient='horizontal', mode='determinate')
progreso.pack()

# Lista de archivos convertidos en la carpeta de salida
label_lista_derecha = Label(frame_derecha, text="Archivos convertidos en la carpeta de salida")
label_lista_derecha.pack()

scroll_derecha = Scrollbar(frame_derecha, orient="vertical")
scroll_derecha.pack(side="right", fill="y")

lista_derecha = Listbox(frame_derecha, yscrollcommand=scroll_derecha.set)
lista_derecha.pack(fill="both", expand=True)
scroll_derecha.config(command=lista_derecha.yview)

root.mainloop()
