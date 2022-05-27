# Automate Whatsapp
# pip install pywhatkit
# pip install Flask
import pywhatkit as whatsapp
# Send Message
whatsapp.sendwhatmsg("+Phone", "Hello from Medium", 12, 30, 0)
# Send Message with Image
whatsapp.sendwhats_image("+Phone", "Img.png", "Hello from Medium")
# Send Message to Group
whatsapp.sendwhatmsg_to_group("+Phone", "Hey Everyone from Medium", 0, 0)