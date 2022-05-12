import os
import sys
from tkinter.filedialog import Open

from cloudinary.api import delete_resources_by_tag, resources_by_tag
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import cloudinary
""" 
# config
os.chdir(os.path.join(os.path.dirname(sys.argv[0]), '.'))
if os.path.exists('settings.py'):
    exec(open('settings.py').read())

cloudinary.config( 
  cloud_name = "doh7eom1j", 
  api_key = "218576176667494", 
  api_secret = "XIIe3Gl9T6f11Ei4jUcgLX8hrlI",
)

DEFAULT_TAG = "python_sample_basic"


def dump_response(response):
    print("Upload response:")
    for key in sorted(response.keys()):
        print("  %s: %s" % (key, response[key]))


def upload_files():

    print("--- Upload a local file with custom public ID")

    response = upload( "pizza.jpg",
        tags=DEFAULT_TAG,
    )
    dump_response(response)
    url, options = cloudinary_url(
        response['public_id'],
        format=response['format'],
        width=200,
        height=150,
        crop="fit"
    )
    print("Fit into 200x150 url: " + url)
    print("")
 """

################# GUI    
""" import tkinter as tk
import tkinter.filedialog
import requests
import json

ventana = tk.Tk()
imagen = None

def abrirArchivo():
    global imagen
    archivo_abierto = tk.filedialog.askopenfilename(initialdir="/", 
                      title="Seleccione archivo", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
    print(archivo_abierto)
    if (archivo_abierto):
        imagen = tk.PhotoImage(file=archivo_abierto)
        lbImagen = tk.Label(ventana, image=imagen).place(relx=.5, rely=.1,relwidth=.4,relheight=.5)


ventana.geometry("500x500")
tk.Button(text="Abrir archivo", bg="pale green", command=abrirArchivo).place(relx=.10, rely=.10, relheight=.1, relwidth=.3)

ventana.mainloop() """





######################## bigjpg
""" import requests
import json

data = {
        'style': 'art',
        'noise': '3',
        'x2': '1',
        'input': 'url'
        
}

r = requests.post(
        url='https://bigjpg.com/api/task/',
        headers={'X-API-KEY': '21eb74b866894ad9b751cbfe09e2ddd3'},
        data={'conf': json.dumps(data)}
    )
print(r.json())


r = requests.get(url='https://bigjpg.com/api/task/#########')
print(r.json()) 
#devulve un url para descargar la imagen
"""