import tkinter as tk
import os
from PIL import ImageTk,Image
from tkinter import filedialog       #Obtenga la ruta completa del archivo
from tkinter import ttk

ventana=tk.Tk()   #Crear objeto

ancho_ventana = 900
alto_ventana = 600

x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)

ventana.title('UNMSM-FISI | Software-Inteligente')
ventana.iconbitmap('img/artificialintelligence.ico')
ventana.resizable(0,0)

# l=tk.Label(ventana,text='Imagen en baja calidad para procesar', image=None)   #Crea una etiqueta
# l.place(x=50,y=10)

comboStyle = ttk.Combobox(state="readonly", values=["Art", "Photo"])
comboStyle.place(x=50, y=50)

comboNoise = ttk.Combobox(state="readonly", values=["-1", "0", "1", "2", "3"])
comboNoise.place(x=50, y=150)

comboX2 = ttk.Combobox(state="readonly", values=["1", "2", "3", "4"])
comboX2.place(x=50, y=250)

frame = tk.Frame()
frame.pack()      

# Como no tenemos ningún elemento dentro del frame, 
# no tiene tamaño y aparece ocupando lo mínimo posible, 0*0 px

# Color de fondo, background
frame.config(bg="lightblue")     

# Podemos establecer un tamaño,
# la raíz se adapta al frame que contiene
frame.config(width=480,height=320) 
l=tk.Label(frame,text='Imagen en baja calidad para procesar', image=None)   #Crea una etiqueta
l.place(x=50,y=10)

def openpicture():
    global img
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),filetypes=[("jpg files", "*.jpg")])     #Obtenga la ruta completa del archivo
    img=ImageTk.PhotoImage(Image.open(filename))   #tkinter solo puede abrir archivos gif, aquí use la biblioteca PIL
    print(filename)
    l.config(image=img)    #Utilice el método de configuración para colocar la imagen en la etiqueta
 


b=tk.Button(ventana,text='Seleccione una imagen', command=openpicture)  # Configure el botón y dele el comando openpicture
b.place(x=50, y=100)

tk.mainloop()

