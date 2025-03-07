#Run the code and observe the output.
#Task 1: Create a variable called background and assign the color code "#2E2E2E" to it.
#Task 2: Uncomment the line 15 and observe the difference.
#Task 3: Modify line 14 to make the window resizable.
#Task 4: Update the window title to "Crypto Message".
# Importing libraries we need
import customtkinter as ctk   # A library to make cool and modern windows
#Add the variable here

# Create the main window for our app
root = ctk.CTk()  # This makes the main window where everything will happen

root.geometry("600x450")  # This sets the size of the window to be 600 pixels wide and 450 pixels tall
root.resizable(False, False)  # This stops people from resizing the window (it stays the same size)
#root.config(bg=background)  # This makes the background color of the window 
root.title("Message Encoder")  # This gives the window a title, which shows at the top of the window

# This keeps the window open and ready to use
root.mainloop()  # This line runs the program and keeps the window open until you close it
