import qrcode

def generate_qr_code(data, filename):
    qr =qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,    
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    
    print("Qr Code image is Saved", filename)
    
generate_qr_code("https://abishake.xyz","ai_law.png")