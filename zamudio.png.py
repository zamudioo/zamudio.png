import os
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 500, 500
FONT_PATH = "path to your font. just to the ttf file"
WHERE_TO_SAVE = "where do you want it to save your png file"

def ajustar_texto_a_imagen(dibujo, texto, fuente, max_width):
    palabras = texto.split(' ')
    lineas = []
    linea_actual = ""

    for palabra in palabras:
        prueba_linea = f"{linea_actual} {palabra}".strip()
        bbox = dibujo.textbbox((0, 0), prueba_linea, font=fuente)
        text_width = bbox[2] - bbox[0]

        if text_width <= max_width:
            linea_actual = prueba_linea
        else:
            lineas.append(linea_actual)
            linea_actual = palabra

    if linea_actual:
        lineas.append(linea_actual)

    return lineas

def generar_imagenes(carpeta_destino, texto):
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    nombre_archivo = texto.replace(" ", "_")
    
    imagen = Image.new('RGBA', (WIDTH, HEIGHT), (255, 255, 255, 0))
    dibujo = ImageDraw.Draw(imagen)

    if len(texto) == 1:
        fuente = ImageFont.truetype(FONT_PATH, 150)
        lineas = [texto]  
    else:
       
        font_size = 150  
        fuente = ImageFont.truetype(FONT_PATH, font_size)
        lineas = ajustar_texto_a_imagen(dibujo, texto, fuente, WIDTH)

        
        while len(lineas) > 1 and font_size > 20:  
            font_size -= 10
            fuente = ImageFont.truetype(FONT_PATH, font_size)
            lineas = ajustar_texto_a_imagen(dibujo, texto, fuente, WIDTH)

    
    total_text_height = sum([dibujo.textbbox((0, 0), linea, font=fuente)[3] for linea in lineas])
    y_offset = (HEIGHT - total_text_height) // 2

    for linea in lineas:
        bbox = dibujo.textbbox((0, y_offset), linea, font=fuente)
        text_width = bbox[2] - bbox[0]
        x_offset = (WIDTH - text_width) // 2
        dibujo.text((x_offset, y_offset), linea, font=fuente, fill=(0, 0, 0, 255))
        y_offset += bbox[3] - bbox[1]  
    ruta_imagen = os.path.join(carpeta_destino, f"{nombre_archivo}.png")
    imagen.save(ruta_imagen, "PNG")

texto_usuario = input("Enter anything (letters, numbers, phrases, symbols idk): ")
generar_imagenes(WHERE_TO_SAVE, texto_usuario)
