import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTkf

def abrir_imagen():
    # Abrir el explorador de archivos para seleccionar la imagen
    ruta = filedialog.askopenfilename(
        title="Seleccionar imagen",
        filetypes=[("Archivos de imagen", "*.jpg *.png *.jpeg *.gif *.bmp")]
    )
    if ruta:
        # Abrir la imagen y redimensionar si es necesario
        img = Image.open(ruta)
        img = img.resize((400, 300))  # ajusta tamaño si quieres
        img_tk = ImageTk.PhotoImage(img)
        
        # Mostrar la imagen en un Label
        label_imagen.config(image=img_tk)
        label_imagen.image = img_tk  # guardar referencia

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Visor de Imágenes")
ventana.geometry("500x400")

# Botón para abrir imagen
boton = tk.Button(ventana, text="Abrir Imagen", command=abrir_imagen)
boton.pack(pady=10)

# Etiqueta donde se mostrará la imagen
label_imagen = tk.Label(ventana)
label_imagen.pack()

# Ejecutar la aplicación
ventana.mainloop()
