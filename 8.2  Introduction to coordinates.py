#In this code, labels are used to display text at specific (x, y) coordinates on the window 
#using the place() method.
#For example, (0, 0) places the label at the top-left corner, and (300, 225) 
#places it near the center of a 600×450 window.

#Run the code and observe the x and y coordinates of label1 and label2.
#Task-1: Create and place new label at coordinates (430, 430) in the bottom-right corner.

import customtkinter as ctk

# Create the main window
background = "#2E2E2E"
root = ctk.CTk()  

root.geometry("600x450")  
root.resizable(False, False)  
root.config(bg=background) 
root.title("Crypto Message")
# Add a label at the top-left corner (0, 0)
label1 = ctk.CTkLabel(root, text="Top-left Corner")
label1.place(x=0, y=0)

# Add a label at the center of the window (300, 225)
label2 = ctk.CTkLabel(root, text="Center of the Window")
label2.place(x=300, y=225)

#Add a label at the bottom right corner.



root.mainloop()
