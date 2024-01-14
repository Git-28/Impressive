import qrcode
from PIL import image
data="https://github.com/SUKTHE-NIKHIL"
qr=qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(data)
qr.make(fit=True)
image=qr.make_image(fill='black',back_color='white')
image.save("qr_code.png")
image.open("qr_code.png")