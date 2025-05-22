from PIL import Image
import qrcode

# Generate QR
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data("https://abishake.onrender.com")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Add logo
logo = Image.open("abi.jpeg")# add a image file into the same directory
logo = logo.resize((50, 50))  # Resize logo as needed

# Calculate position to paste
pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
img.paste(logo, pos)

img.save("qrcode_with_logo.png")
