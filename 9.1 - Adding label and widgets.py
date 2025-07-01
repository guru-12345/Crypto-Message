#This line opens a picture named logo.png and resizes it to 50 by 50 pixels so it can be shown in the app.
#It helps us use pictures like icons or logos in our project.

#Task 1: Increase the size of the logo to (100,100).
#Task 2: Find out why the message label isn't showing on the window and place it at (100,20).

import customtkinter as ctk   
from PIL import Image, ImageTk    # A library to work with pictures

background = "#2E2E2E"
root = ctk.CTk()  

root.geometry("600x450")  
root.resizable(False, False)  
root.config(bg=background) 
root.title("Crypto Message")  

logo = ctk.CTkImage(Image.open('logo.png'), size=(50, 50))  # Open the image and set its size

# Create a label with the logo image, no text, and place it on the window at coordinates (0, 0)
logo_image = ctk.CTkLabel(root, image=logo, text="", fg_color=background)
logo_image.place(x=0, y=0)

# Add a text label on the window for the message encrypter title
message_label = ctk.CTkLabel(root, text="Message Encrypter", font=("Cascadia Code SemiBold", 20, "bold"), fg_color=background, text_color="white")


root.mainloop()
