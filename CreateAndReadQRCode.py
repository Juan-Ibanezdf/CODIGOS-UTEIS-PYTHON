# Generate and Read QR Code
import qrcode
import cv2
def Generate_QrCode():
    #colocar o link que se quer gerar
    qr=qrcode.make('https://medium.com/@codedev101')
    qr.save('codedev101.png')
def Read_QrCode():
    #formato do qr code
    qr=cv2.imread("codedev101.png")
    cv=cv2.QRCodeDetector()
    data, temp, temp2=cv.detectAndDecode(qr)
    print(data)
Generate_QrCode()
Read_QrCode() # https://medium.com/@codedev101