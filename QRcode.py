import qrcode

data = "https://github.com/sanjaykn8/py_pgrm" #Change this to wished url

qr = qrcode.QRCode(
    version=1, #change size
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")

img.show()
