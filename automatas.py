import tkinter as tk

def update_display():
    text_to_display.set(text_entry.get())

# Create the main window
root = tk.Tk()
root.title("Text Display App")

# Create a text entry box
text_entry = tk.Entry(root, width=50)
text_entry.pack(pady=10)

# Create a label to display the text
text_to_display = tk.StringVar()
display_label = tk.Label(root, textvariable=text_to_display, width=50, height=10, relief="sunken", bg="white")
display_label.pack()

# Button to update the display
update_button = tk.Button(root, text="Update Display", command=update_display)
update_button.pack(pady=10)

# Run the application
root.mainloop()
