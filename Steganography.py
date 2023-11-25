from PIL import Image
import os
import string


# Read the image
img = Image.open("Desert.jpeg")

# Convert the image to RGB mode if it's not already
if img.mode != 'RGB':
    img = img.convert('RGB')

# Get the RGB values of each pixel
pixels = img.load()

# Create dictionaries for mapping characters to pixel values and vice versa
d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Embed the message into the image
message = input("Enter secret message: ")
password = input("Enter password: ")

m = 0  # Row index
n = 0  # Column index
z = 0  # Color channel index (RGB)

for char in message:
    pixel = pixels[n, m]
    pixel = (d[char], pixel[1], pixel[2])  # Replace one color channel with character value
    pixels[n, m] = pixel

    n = n + 1  # Move to the next pixel
    if n == img.width:
        n = 0  # Reset to the first column
        m = m + 1  # Move to the next row
    z = (z + 1) % 3  # Increment color channel index

# Save the encrypted image
img.save("Encryptedmsg.jpg")

# Open the encrypted image using the default image viewer
os.system("start Encryptedmsg.jpg")  # Correctly calls os.system() with one argument

# Decryption
passcode = input("Enter passcode for Decryption: ")

if password == passcode:
    decrypted_message = ""

    n = 0  # Row index
    m = 0  # Column index
    z = 0  # Color channel index (RGB)

    while True:
        pixel = pixels[n, m]

        if 0 <= pixel[z] <= 254:  # Check if pixel value is within valid range
            decrypted_message += c[pixel[z]]  # Extract character from one color channel

        n = n + 1  # Move to the next pixel
        if n == img.width:
            n = 0  # Reset to the first column
            m = m + 1  # Move to the next row
        z = (z + 1) % 3  # Increment color channel index

        if pixel[z] == 0:  # End-of-message marker
            break

    print("Decrypted message:", message)
else:
    print("Not a valid key")
