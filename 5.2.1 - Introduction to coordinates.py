#Run th code and observe the x and y coordinates.
#Task: Place a label at coordinates (430, 430) in the bottom-right corner.

import customtkinter as ctk

# Create the main window
root = ctk.CTk()
root.geometry("600x450")  # Window size 600x450

# Add a label at the top-left corner (0, 0)
label1 = ctk.CTkLabel(root, text="Top-left Corner")
label1.place(x=0, y=0)

# Add a label at the center of the window (300, 225)
label2 = ctk.CTkLabel(root, text="Center of the Window")
label2.place(x=300, y=225)



# Run the application
root.mainloop()# Write your code here :-)
