#Run the code and observe the output.
#Task 1:Link the toggle button with command=toggle.
#Task 2:Complete the toggle function — write the missing part to switch back to "Dark" mode.
#Task 3:Update background color for all widgets — add .configure() for root,
#message_label, logo_image, PhotoLabel, Data_entry, open_button, encrypt_button, and decrypt_button.

import customtkinter as ctk   
from PIL import Image, ImageTk    

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
background = "#2E2E2E"

def toggle():
    current_mode = ctk.get_appearance_mode()
    if current_mode == "Dark":
        ctk.set_appearance_mode("Light")
        background = "#FFFFFF"
        toggle_button.configure(fg_color=background, hover_color=background, image=white_image)
    else:
        # Complete this part to set Dark mode back
        ...
    
    # Now update background of all widgets
    root.configure(fg_color=background)
    # Add more widgets here like message_label, logo_image etc.






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

Data_entry = ctk.CTkTextbox(root, width=250, height=200, border_width=5)
Data_entry.place(x=270, y=100)

white_image = ctk.CTkImage(Image.open('dark_mode.png'), size=(70, 45))
dark_image = ctk.CTkImage(Image.open('white_mode.png'), size=(70, 45))
toggle_button = ctk.CTkButton(root, image=dark_image, text="", fg_color=background, hover_color=background)
toggle_button.place(x=480, y=20)

root.mainloop()
