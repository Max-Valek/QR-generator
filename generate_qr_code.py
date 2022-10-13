import qrcode
import image

qr = qrcode.QRCode(
    version = 15, # version 15 (bigger = bigger and more complex code image)
    box_size = 10, 
    border = 5
)

data = "https://google.com" # link to google, for example

qr.add_data(data) 
qr.make(fit = True)
img = qr.make_image(fill="black",back_color = "white")
img.save("test.png")