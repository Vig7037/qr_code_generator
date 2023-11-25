import emoji
import qrcode
import os
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask
print("\033[H\033[2J","\033[42m*-"*25,"Welcome on QR Generator","*-"*25,"\033[0m",end="\n\n\n")
print(emoji.emojize(":grinning_face_with_big_eyes:"),"Hello!",end="\n\n")
data=input("Give the data for which you want to create the QR code:")
n_file=input("Type the file name:")
#n_file=n_file+".png"
print("Press 1 for gradiant.\nPress 2 for chose the colour by your prefance.\n")
chose=input("Give the no what is your choice:")
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)
qr.add_data(data)
qr.make(fit=True)
if chose==1:
    img = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
if chose==2:
    fc,bc=input("Enter the colour filling colour in qr code:"),input("Enter the colour of background colour:")
    img = qr.make_image(fill_color=fc, back_color=bc)
img.save(n_file)
print("\nYour QR is ready.\n")
os.system(n_file)