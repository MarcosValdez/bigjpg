#Librerias de python
import os
from PIL import ImageTk,Image

#Librerias de tkinter
import tkinter as tk
from tkinter import filedialog       #Obtenga la ruta completa del archivo
from tkinter import ttk

#Librerias del cloudinary
from cloudinary.api import delete_resources_by_tag, resources_by_tag
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import cloudinary

import requests
import json

def main():

    ventana=tk.Tk() 

    ventana.title('UNMSM-FISI | Software-Inteligente')
    ventana.iconbitmap('img/artificialintelligence.ico')
    ventana.resizable(0,0)

    ancho_ventana = 900
    alto_ventana = 600

    x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    ventana.geometry(posicion)
    
    frame = tk.Frame()
    frame.pack()      

    frame.config(bg="lightblue")     
    frame.config(width=ancho_ventana / 2 - 20,height=alto_ventana - 60)
    frame.place(x=ancho_ventana / 2 + 10,y= 50)

    l=tk.Label(frame,text='', image=None)   #Crea una etiqueta
    l.pack()

    # ruta_image = ""

    def openpicture():
        global img
        global ruta_image
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),filetypes=[("jpg files", "*.jpg")])     #Obtenga la ruta completa del archivo
        ruta_image=filename
        img=ImageTk.PhotoImage(Image.open(filename))   #tkinter solo puede abrir archivos gif, aquí use la biblioteca PIL
        print(filename)
        l.config(image=img)    #Utilice el método de configuración para colocar la imagen en la etiqueta

    
    lblTitulo=tk.Label(ventana,text='Trabajo Semanal 1', font=("Helvetica", 24))   #Crea una etiqueta
    lblTitulo.pack(pady=20)

    lblTitulo=tk.Label(ventana,text='Seleccione la imagen')   #Crea una etiqueta
    lblTitulo.place(x=100,y=70)

    b=tk.Button(ventana,text='Seleccione una imagen', command=openpicture)  # Configure el botón y dele el comando openpicture
    b.place(x=100, y=100)

    lblTitulo=tk.Label(ventana,text='Seleccione el estilo')   #Crea una etiqueta
    lblTitulo.place(x=100,y=130)

    comboStyle = ttk.Combobox(state="readonly", values=["Art", "Photo"])
    comboStyle.place(x=100, y=160)

    lblTitulo=tk.Label(ventana,text='Seleccione el ruido')   #Crea una etiqueta
    lblTitulo.place(x=100,y=190)

    comboNoise = ttk.Combobox(state="readonly", values=["-1", "0", "1", "2", "3"])
    comboNoise.place(x=100, y=220)

    lblTitulo=tk.Label(ventana,text='Seleccione el X2')   #Crea una etiqueta
    lblTitulo.place(x=100,y=250)

    comboX2 = ttk.Combobox(state="readonly", values=["1", "2", "3", "4"])
    comboX2.place(x=100, y=280)


    def dump_response(response):
        print("Upload response:")
        for key in sorted(response.keys()):
            print("  %s: %s" % (key, response[key]))

    def guardar_imagen():
        cloudinary.config( 
            cloud_name = "doh7eom1j", 
            api_key = "218576176667494", 
            api_secret = "XIIe3Gl9T6f11Ei4jUcgLX8hrlI",
        )

        DEFAULT_TAG = "python_sample_basic"
        response = upload( ruta_image, tags=DEFAULT_TAG)
        # dump_response(response)
        url, options = cloudinary_url(
            response['public_id'],
            format=response['format'],
            width=200,
            height=150,
            crop="fit"
        )
        #print("Fit into 200x150 url: " + url)
        return url

    def enviar_imagen():
        link_image = guardar_imagen()
        # print(f"{comboStyle.get()}\n{comboNoise.get()}\n{comboX2.get()}\n{ruta_image}\n{link_image}")

        data = {
            'style': f"{comboStyle.get()}",
            'noise': f"{comboNoise.get()}",
            'x2': f"{comboX2.get()}",
            'input': f"{link_image}"
        }

        r = requests.post(
            url='https://bigjpg.com/api/task/',
            headers={'X-API-KEY': '21eb74b866894ad9b751cbfe09e2ddd3'},
            data={'conf': json.dumps(data)}
        )
        print(r.json())


        #r = requests.get(url='https://bigjpg.com/api/task/#########')
        #print(r.json()) 


        
    button = ttk.Button(text="Convertir imagen", command=enviar_imagen)
    button.place(x=100, y=310)

    lblTitulo=tk.Label(ventana,text='Integrantes:\n- Marcos Valdez Alexander 18200089\n- Navarro Ortiz Eduardo 18200279\n- Quinteros Peralta Rodrigo 18200316\n- Tirado Julca Juan Jose 18200117\n- Valentin Ricaldi David 18200103', font=("Helvetica", 12))   #Crea una etiqueta
    lblTitulo.place(x=50,y=alto_ventana - 200)

    ventana.mainloop()

if __name__ == '__main__':
    main()