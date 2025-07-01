# Task 1: Create the "Encrypt" button
#         Use an image called encryption.png
#         Set the size to (60, 70)
#         Add the button with no text (text="")
#         Set the button color to the background
#         Place it at (270, 365) on the window

#Task 2: Create the "Decrypt" button:
#        Use an image called decrypt.png
#        Set the size to (60, 70)
#        Add the button with no text (text="")
#        Set the button color to the background
#        Place it at (430, 365) on the window

import customtkinter as ctk   
from PIL import Image, ImageTk    
from tkinter import filedialog, messagebox


background = "#2E2E2E"
root = ctk.CTk()  

root.geometry("600x450")  
root.resizable(False, False)  
root.config(bg=background) 
root.title("Crypto Message")  

        
logo = ctk.CTkImage(Image.open('logo.png'), size=(100, 100))  
logo_image = ctk.CTkLabel(root, image=logo, text="", fg_color=background)
logo_image.place(x=0, y=0)

message_label = ctk.CTkLabel(root, text="Message Encrypter", font=("Cascadia Code SemiBold", 20, "bold"), fg_color=background, text_color="white")
message_label.place(x=100, y=20)

sender = Image.open('logo.jpg') # Open the image 'logo.jpg' to use it in the program
sender = sender.resize((240, 240)) # Resize the image to be 240 pixels wide and 240 pixels tall
label_image = ImageTk.PhotoImage(sender) # Convert the resized image into a format that Tkinter can use

# Create a label in the window to display the image with no text, and set its size and color
PhotoLabel = ctk.CTkLabel(root, image=label_image, text="", width=247, height=247, fg_color="white")
PhotoLabel.place(x=10, y=100) # Place the label at position (10, 100) in the window

#open_button 
open_file = ctk.CTkImage(Image.open('open_file.png'), size=(70, 70))
open_button = ctk.CTkButton(root, image=open_file, text="", fg_color=background, hover_color=background)
open_button.place(x=100, y=365)

#Write a code to create encrypt_button here




#Write a code to create decrypt_button here




root.mainloop()
