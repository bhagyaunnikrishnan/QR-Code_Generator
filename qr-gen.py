import qrcode
print("This is a QR-Code Generator\n")
img = qrcode.make(input("Enter any data to generate its QR:"))
img.save("qr.jpg")
print("Qr code is generated")
img.show("qr.jpg")