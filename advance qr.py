import qrcode as qr
from PIL import Image 
qrs = qr.QRCode(version=1,
                error_correction= qr.constants.ERROR_CORRECT_H,
                box_size=20,border=4,)
qrs.add_data("https://www.linkedin.com/in/sagarsinghchauhan-65a2a12bb/")
qrs.make(fit=True)
fil_col = input("enter the color: ")
bal_col = input("enter the background color of qr code: ")
image = qrs.make_image(fill_color=fil_col,back_color = bal_col)
image.save("my_linkdin_profile_qr.png")
