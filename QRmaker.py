import pyqrcode

print("""

 .oOOOo.   `OooOOo.                        o                  
.O     o.   o     `o                       O                  
o       O   O      O                       o                  
O       o   o     .O                       o                  
o       O   OOooOO'        `oOOoOO. .oOoO' O  o  .oOo. `OoOo. 
O    Oo o   o    o          O  o  o O   o  OoO   OooO'  o     
`o     O'   O     O         o  O  O o   O  o  O  O      O     
 `OoooO Oo  O      o        O  o  o `OoO'o O   o `OoO'  o     
                                                              
                                                              
""")

link = input("\n\nPlease paste the link here. Our Program will generate QRcode of that link !\n:")
filename = input("Enter file name to save QRcode :")

# Generate QR code
qr_code = pyqrcode.create(link)

# Create and save the SVG file naming "myyoutube.svg"
qr_code.svg(f"{filename}.svg", scale=8)

print(f"QR code generated and saved as '{filename}.svg'")
