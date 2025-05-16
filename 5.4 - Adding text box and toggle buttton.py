#Run the code and observe the output.
#Task 1:Create a textbox named "Data_entry" with size width=250,height=200,border_width=5 and place it at (270, 100).
#Task 2: Load two images (dark_mode.png and white_mode.png) with size (70, 45)
#Task 3: Create a toggle button using dark_image,Set the fg_color and hover_color to the background color
#Task 4: Place the toggle button at (480, 20)

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




#Create a toggle button here





root.mainloop()
