#We load two pictures named dark_mode.png and white_mode.png and set their size to 70×45 pixels. 
#These images will be used for the toggle (theme change) button.

#We create a button using one of the images and make sure it matches the background color, 
#so it looks good and works like a theme switch.

#Task 1: Add a Textbox to Type Your Message
#       You need to create a box where you can type a secret message.
#       🔹 Name it: Data_entry
#       🔹 Size: width = 250, height = 200
#       🔹 Border width: 5 (so the box has a visible border)
#       🔹 Place it at: x = 270, y = 100 (on the right side of the app)


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

message_label = ctk.CTkLabel(root, text="Message Encrypter", font=("Cascadia Code SemiBold", 20, "bold"), fg_color=background, text_color="white")
message_label.place(x=100, y=20)

sender = Image.open('logo.jpg') 
sender = sender.resize((240, 240)) 
label_image = ImageTk.PhotoImage(sender) 

PhotoLabel = ctk.CTkLabel(root, image=label_image, text="", width=247, height=247, fg_color="white")
PhotoLabel.place(x=10, y=100) 

open_file = ctk.CTkImage(Image.open('open_file.png'), size=(70, 70))
open_button = ctk.CTkButton(root, image=open_file, text="", fg_color=background, hover_color=background)
open_button.place(x=100, y=365)

encrypt_image = ctk.CTkImage(Image.open('encryption.png'), size=(60, 70))
encrypt_button = ctk.CTkButton(root, image=encrypt_image, text="", fg_color=background, hover_color=background)
encrypt_button.place(x=270, y=365)

decrypt_image = ctk.CTkImage(Image.open('decrypt.png'), size=(60, 70))
decrypt_button = ctk.CTkButton(root, image=decrypt_image, text="", fg_color=background, hover_color=background)
decrypt_button.place(x=430, y=365)

#Create a textbox here




#Load the image for Dark and Light mode
dark_image = ctk.CTkImage(Image.open('white_mode.png'), size=(70, 45))
white_image = ctk.CTkImage(Image.open('dark_mode.png'), size=(70, 45))

#Create a toggle button here
toggle_button = ctk.CTkButton(root, image=dark_image, text="", fg_color=background, hover_color=background)
toggle_button.place(x=480, y=20)  


root.mainloop()
