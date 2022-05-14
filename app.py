#Librerias de python
import os
from PIL import ImageTk,Image

#Librerias de tkinter
import tkinter as tk
from tkinter import filedialog #Obtenga la ruta completa del archivo
from tkinter import ttk
from tkinter import Label

#Librerias del cloudinary
from cloudinary.api import delete_resources_by_tag, resources_by_tag
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import cloudinary

import requests
from io import BytesIO
import json
import time
import urllib.request


""" class WebImage:
    def __init__(self,url):
        u = requests.get(url)
        self.image = ImageTk.PhotoImage(Image.open(BytesIO(u.content)))
        
    def get(self):
        return self.image """

def guardar_imagen():
    # cloudinary.config( 
    #     cloud_name = "dfvalentin", 
    #     api_key = "897557139935321", 
    #     api_secret = "aIbNmOBA99y6kXhAjqd4T-9wGIA",
    # )
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

def main():
    
    ventana=tk.Tk() 

    ventana.title('UNMSM-FISI | Software-Inteligente')
    ventana.iconbitmap('img/artificialintelligence.ico')
    ventana.resizable(0,0)

    ancho_ventana = 900
    alto_ventana = 410

    frame = tk.Frame()
    frame.pack()   

    frame.config(width=ancho_ventana,height=alto_ventana+alto_ventana-30, bg="lightblue")

    lblTitulo=tk.Label(frame,text='Trabajo Semanal 1 | Disminución del ruido en imágenes', font=("Helvetica", 24))   #Crea una etiqueta
    lblTitulo.config(bg="lightblue")
    lblTitulo.place(x=50,y=20)

    img = ImageTk.PhotoImage(Image.open('./img/Fisi.jpg').resize((512,225)))
    lbl_img = Label(frame, image=img)
    lbl_img.place(x=30,y=80)

    lblTitulo=tk.Label(frame,text='Software Inteligente', font=("Helvetica", 24))   #Crea una etiqueta
    lblTitulo.config(bg="lightblue")
    lblTitulo.place(x=578,y=95)
    lblTitulo=tk.Label(frame,text='Integrantes:', font=("Helvetica", 16))   #Crea una etiqueta
    lblTitulo.config(bg="lightblue")
    lblTitulo.place(x=580,y=150)
    lblTitulo=tk.Label(frame,text='- Marcos Valdez Alexander   18200089', font=("Helvetica", 12))   #Crea una etiqueta
    lblTitulo.config(bg="lightblue")
    lblTitulo.place(x=580,y=180)
    lblTitulo=tk.Label(frame,text='- Navarro Ortiz Eduardo        18200279', font=("Helvetica", 12))   #Crea una etiqueta
    lblTitulo.config(bg="lightblue")
    lblTitulo.place(x=580,y=205)
    lblTitulo=tk.Label(frame,text='- Quinteros Peralta Rodrigo  18200316', font=("Helvetica", 12))   #Crea una etiqueta
    lblTitulo.config(bg="lightblue")
    lblTitulo.place(x=580,y=230)
    lblTitulo=tk.Label(frame,text='- Tirado Julca Juan Jose       18200117', font=("Helvetica", 12))   #Crea una etiqueta
    lblTitulo.config(bg="lightblue")
    lblTitulo.place(x=580,y=255)
    lblTitulo=tk.Label(frame,text='- Valentin Ricaldi David         18200103', font=("Helvetica", 12))   #Crea una etiqueta
    lblTitulo.config(bg="lightblue")
    lblTitulo.place(x=580,y=280)

    l=tk.Label(frame,text='', image=None)   #Crea una etiqueta
    l.config(bg="lightblue")
    l.place(x=70,y=alto_ventana + 40)

    descarga_imagen = False

    #ruta_image = ""

    def openpicture():
        global img
        global ruta_image
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),filetypes=[("jpg files", "*.jpg")])     #Obtenga la ruta completa del archivo
        ruta_image=filename
        img=ImageTk.PhotoImage(Image.open(filename).resize((300,300)))   #tkinter solo puede abrir archivos gif, aquí use la biblioteca PIL
        print(filename)
        l.config(image=img)    #Utilice el método de configuración para colocar la imagen en la etiqueta


    def dump_response(response):
        print("Upload response:")
        for key in sorted(response.keys()):
            print("  %s: %s" % (key, response[key]))

    
    imagenGenerada = ''
    def enviar_imagen():

        global imagenGenerada 
        global descarga_imagen       
        tid = ""

        link_image = guardar_imagen()
        print(link_image)
        # print(f"{comboStyle.get()}\n{comboNoise.get()}\n{comboX2.get()}\n{ruta_image}\n{link_image}")

        data = {
            'style': f"{comboStyle.get()}".lower(),
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
        tid = r.json().get('tid')
        print(tid)

        time.sleep(15)

        r = requests.get(url='https://bigjpg.com/api/task/{}'.format(tid))
        print(r.json())

        rpta_api = r.json().get(tid)
        url_img_procesada = rpta_api.get('url')
        print(url_img_procesada)
        imagenGenerada = url_img_procesada
        urllib.request.urlretrieve(imagenGenerada, "test.jpg")
        descarga_imagen = True

        #img2 = ImageTk.PhotoImage(Image.open('./test.jpg').resize((512,225)))
        #lbl_img2 = Label(frame, image=img2)
        #lbl_img2.place(x=350,y=alto_ventana + 40)
        lblTitulo=tk.Label(frame,text='La imagen se ha descargado')   #Crea una etiqueta
        lblTitulo.config(bg="lightblue")
        lblTitulo.place(x=400,y=alto_ventana + 100)

    #Datos de Entrada
    lblTitulo=tk.Label(frame,text='Seleccione la imagen')   #Crea una etiqueta
    lblTitulo.config(bg="lightblue")
    lblTitulo.place(x=50,y=325)

    b=tk.Button(frame,text='Seleccione una imagen', command=openpicture)  # Configure el botón y dele el comando openpicture
    b.place(x=50, y=355)

    lblTitulo=tk.Label(frame,text='Seleccione el estilo')   #Crea una etiqueta
    lblTitulo.config(bg="lightblue")
    lblTitulo.place(x=250,y=325)

    comboStyle = ttk.Combobox(frame, state="readonly", values=["Art", "Photo"])
    lblTitulo.config(bg="lightblue")
    comboStyle.place(x=250, y=355)

    lblTitulo=tk.Label(frame,text='Seleccione el ruido')   #Crea una etiqueta
    lblTitulo.config(bg="lightblue")
    lblTitulo.place(x=450,y=325)

    comboNoise = ttk.Combobox(frame, state="readonly", values=["-1", "0", "1", "2", "3"])
    lblTitulo.config(bg="lightblue")
    comboNoise.place(x=450, y=355)

    lblTitulo=tk.Label(frame,text='Seleccione el X2')   #Crea una etiqueta
    lblTitulo.config(bg="lightblue")
    lblTitulo.place(x=650,y=325)

    comboX2 = ttk.Combobox(frame, state="readonly", values=["1", "2"])
    lblTitulo.config(bg="lightblue")
    comboX2.place(x=650, y=355)

    lbltexto=tk.Label(frame,text=' Imagen Ingresada:', font=("Helvetica", 14))   #Crea una etiqueta
    lbltexto.config(bg="lightblue")
    lbltexto.place(x=130,y=alto_ventana)

    button = ttk.Button(text="Convertir imagen", command=enviar_imagen)
    button.place(x=550, y=alto_ventana)

    lblTitulo=tk.Label(frame,text='Espere por favor')   #Crea una etiqueta
    lblTitulo.config(bg="lightblue")
    lblTitulo.place(x=400,y=alto_ventana + 40)

    ventana.mainloop()

if __name__ == '__main__':
    main()