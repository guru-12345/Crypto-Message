#Run the code and observe the output.
#Line 19 To add an image as a label, first load the image using PIL's Image.open() method.
#Line 19 create a CTkImage object with the image, specifying its size.
#Line 22,23 create a CTkLabel widget with the image, and set the position.
#Task 1: Increase the size of the logo to (100,100).
#Task 2: Check line 26 to find out why the message label isn't showing on the window 
#and place it at (100,20).
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
