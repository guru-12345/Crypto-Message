#Run the code and observe the output.
# Task 1: Add an open image button
# Hint:-
#Step 1: Load the button's image, Use ctk.CTkImage(), Open 'open_file.png', Set size (70, 70).

#Step 2: Create the button, Use ctk.CTkButton(), Set the image you loaded, Set text to empty ""
#Set the fg_color and hover_color to the background color

#Step 3: Place the button, Use .place(x=100, y=355).

# Task 2: Add two more buttons — Encrypt and Decrypt. 
# Load their images and place them at (270, 365) and (430, 365).

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

#Write a code to create open_button here




#Write a code to create encrypt_button here




#Write a code to create decrypt_button here




root.mainloop()
