#Run the code and observe the output.
# Task: 
# 1. Add two more buttons, "Encrypt" and "Decrypt", similar to the "Open" button.
# 2. Load the images for the "Encrypt" and "Decrypt" buttons using CTkImage, with the size 60x70.
# 3. Place the "Encrypt" button at coordinates (270, 365) and
#the "Decrypt" button at coordinates (430, 365).
import customtkinter as ctk   
from PIL import Image, ImageTk    

background = "#2E2E2E"
root = ctk.CTk()  

root.geometry("600x450")  
root.resizable(False, False)  
root.config(bg=background) 
root.title("Crypto Message")  

logo = ctk.CTkImage(Image.open('logo.png'), size=(100, 100))  

logo_image = ctk.CTkLabel(root, image=logo, text="", fg_color=background)
logo_image.place(x=0, y=0)

sender = Image.open('logo.jpg') # Open the image 'logo.jpg' to use it in the program
sender = sender.resize((240, 240)) # Resize the image to be 240 pixels wide and 240 pixels tall
label_image = ImageTk.PhotoImage(sender) # Convert the resized image into a format that Tkinter can use


open_file = ctk.CTkImage(Image.open('open_file.png'), size=(70, 70)) # Open the image and set its size

message_label = ctk.CTkLabel(root, text="Message Encrypter", font=("Cascadia Code SemiBold", 20, "bold"), fg_color=background, text_color="white")
message_label.place(x=100, y=20)

# Create a label in the window to display the image with no text, and set its size and color
PhotoLabel = ctk.CTkLabel(root, image=label_image, text="", width=247, height=247, fg_color="white")
PhotoLabel.place(x=10, y=100) # Place the label at position (10, 100) in the window

# Create a text box with specified width, height, and border_width
Data_entry = ctk.CTkTextbox(root, width=250, height=200, border_width=5)
Data_entry.place(x=270, y=100) # Position the text box at coordinates (270, 100) on the window

# Create a button with an image and custom colors for normal and hover states
open_button = ctk.CTkButton(root, image=open_file, text="", fg_color=background, hover_color=background)
open_button.place(x=100, y=355) # Position the button at (100, 355) on the window

#Add encrypt_button



#Add decrypt_botton



root.mainloop()
