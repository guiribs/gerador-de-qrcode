import qrcode

# Defina a URL que você deseja codificar no QR Code
url = "https://drive.google.com/file/d/1ckiV4Ks7h_6Em5TL67nSGzUU67n1GtvR/view?usp=drive_link"

# Crie um objeto QRCode com a URL
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Crie uma imagem do QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Salve a imagem do QR Code em um arquivo
img.save("qr_code.png")
