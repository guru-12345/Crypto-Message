#This code hides a secret message inside an image and lets you save the new image. 
#It shows a success message if done correctly, or a warning if something is missing.

import customtkinter as ctk   
from PIL import Image, ImageTk   
from tkinter import filedialog, messagebox 
from stegano import lsb 


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
background = "#2E2E2E"
file_types = [("PNG files", "*.png")] 
file_path = ""  

def toggle():
    current_mode = ctk.get_appearance_mode()
    if current_mode == "Dark":
        ctk.set_appearance_mode("Light")
        background = "#FFFFFF"
        toggle_button.configure(fg_color=background, hover_color=background, image=white_image)
    else:
        ctk.set_appearance_mode("Dark")
        background = "#2E2E2E"
        toggle_button.configure(fg_color=background, hover = background, image=dark_image)
    
    root.configure(fg_color=background)
    message_label.configure(fg_color=background, text_color="black")
    logo_image.configure(fg_color=background)
    PhotoLabel.configure(fg_color=background)
    Data_entry.configure(fg_color=background)
    open_button.configure(fg_color=background)
    encrypt_button.configure(fg_color=background)
    decrypt_button.configure(fg_color=background)
    

def open_image():
    global file_path
    file_path = filedialog.askopenfilename(title="Select an image file", filetypes=file_types)

    if file_path:
        image = Image.open(file_path)
        max_size = (240, 240)
        image.thumbnail(max_size, Image.Resampling.LANCZOS)
        label_image = ImageTk.PhotoImage(image)
        PhotoLabel.configure(image=label_image)
        PhotoLabel.image = label_image


# This function hides a secret message inside an image
def encrypt():
    # Get the message typed in the text box
    data = Data_entry.get(1.0, "end").strip()

    # Check if the user has selected an image file
    if file_path:
        # Hide the message inside the selected image
        encrypted_image = lsb.hide(file_path, data)

        # Ask the user where to save the new image with the hidden message
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

        # If the user selected a place to save the file
        if save_path:
            # Save the new image
            encrypted_image.save(save_path)

            # Show a message that it was successful
            messagebox.showinfo("Success", "Message encrypted in image successfully!")

            # Clear the text box after saving
            Data_entry.delete(1.0, "end")
        else:
            # If the user canceled the save, show a warning
            messagebox.showwarning("Save Cancelled", "Save operation was cancelled.")
    else:
        # If no image was selected, show a warning
        messagebox.showwarning("Error", "Please select an image and enter a message to encrypt.")



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
open_button = ctk.CTkButton(root, image=open_file, text="", fg_color=background, hover_color=background,command=open_image)
open_button.place(x=100, y=365)

encrypt_image = ctk.CTkImage(Image.open('encryption.png'), size=(60, 70))
encrypt_button = ctk.CTkButton(root, image=encrypt_image, text="", fg_color=background, hover_color=background,command=encrypt)
encrypt_button.place(x=270, y=365)

decrypt_image = ctk.CTkImage(Image.open('decrypt.png'), size=(60, 70))
decrypt_button = ctk.CTkButton(root, image=decrypt_image, text="", fg_color=background, hover_color=background)
decrypt_button.place(x=430, y=365)

Data_entry = ctk.CTkTextbox(root, width=250, height=200, border_width=5)
Data_entry.place(x=270, y=100)

white_image = ctk.CTkImage(Image.open('dark_mode.png'), size=(70, 45))
dark_image = ctk.CTkImage(Image.open('white_mode.png'), size=(70, 45))
toggle_button = ctk.CTkButton(root, image=dark_image, text="", fg_color=background, hover_color=background,command=toggle)
toggle_button.place(x=480, y=20)

root.mainloop()
