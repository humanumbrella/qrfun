import pyqrcode
qr = pyqrcode.create("HORN O.K. PLEASE.")
qr.png("horn.png", scale=6)

for i in range (0,10):
    qr = pyqrcode.create(str(i)+" s")
    qr.png(str(i)+".png",scale=6)

