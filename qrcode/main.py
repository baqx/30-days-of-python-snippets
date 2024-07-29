import qrcode
qr = qrcode.QRCode()
qr.add_data('https://www.tiktok.com/')
qr.make()
img = qr.make_image()
img.show()