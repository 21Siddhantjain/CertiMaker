import qrcode

qr = qrcode.QRCode(version=1,box_size=15,border=5)

data = 'https://docs.google.com/forms/d/1ccfunW4JXh97uGvASx6IwphMaBuNWgahSwaNd7AFsYE'

qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill='black' , back_color='white')
image.save('QR.png')
