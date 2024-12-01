import qrcode
from PIL import Image

# Create a QRCode object with high error correction
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

# Add data to the QR code
qr.add_data("https://kashanscripts.freewebhostmost.com/")
qr.make(fit=True)

# Generate the QR code image
qr_image = qr.make_image(fill_color="white", back_color="black")

# Save the QR code image to a file
qr_image.save("techKashan.png")  # Ensure you have write permissions in this directory
