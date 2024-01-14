from PIL import Image, ImageDraw, ImageFont
import random

def generate_captcha():
   # Configuración
   width, height = 200, 80
   image = Image.new('RGB', (width, height), color = 'white')
   draw = ImageDraw.Draw(image)
   font = ImageFont.truetype("arial.ttf", 40)

   # Generar texto aleatorio para el CAPTCHA
   captcha_text = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(6))

   # Dibujar el texto en la imagen
   text_color = (0, 0, 0)
   draw.text((10, 25), captcha_text, fill=text_color, font=font)

   # Agregar ruido a la imagen
   for _ in range(150):
       noise_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
       x = random.randint(0, width - 1)
       y = random.randint(0, height - 1)
       draw.point((x, y), fill=noise_color)

   # Guardar la imagen
   image.save("captcha.png")

generate_captcha()