import io
from PIL import Image
import segno

out = io.BytesIO()
# Nothing special here, let Segno generate the QR code and save it as PNG in a buffer
segno.make('hello world', error='h').save(out, scale=10, kind='png')
out.seek(0)  # Important to let Pillow load the PNG
img = Image.open(out)
img = img.convert('RGB')  # Ensure colors for the output
img_width, img_height = img.size
logo_max_size = img_height // 3  # May use a fixed value as well
logo_img = Image.open('./SkyJu.png')  # The logo
# Resize the logo to logo_max_size
logo_img.thumbnail((logo_max_size, logo_max_size), Image.Resampling.LANCZOS)
# Calculate the center of the QR code
box = ((img_width - logo_img.size[0]) // 2, (img_height - logo_img.size[1]) // 2)
img.paste(logo_img, box)
img.save('helloQR.png')
