import tkinter as tk

def save_text():
    for row in range(len(entry_fields)):
        for col in range(len(entry_fields[row])):
            text_data[row][col] = entry_fields[row][col].get()

def add_new_row():
    global num_rows
    num_rows += 1
    entry_fields.append([])
    for col in range(num_cols):
        entry = tk.Entry(root, width=10)
        entry.grid(row=num_rows, column=col)
        entry_fields[num_rows-1].append(entry)
    # Move the buttons to the next row
    add_row_button.grid(row=num_rows+1, columnspan=num_cols, pady=10)
    save_button.grid(row=num_rows+2, columnspan=num_cols, pady=10)

def create_grid():
    global add_row_button, save_button
    # Labels for text above the grid
    tk.Label(root, text="Estado").grid(row=0, column=0)
    tk.Label(root, text="Simbolo").grid(row=0, column=1)
    tk.Label(root, text="Objetivo").grid(row=0, column=2)

    # Create the initial row of Entry widgets
    for col in range(num_cols):
        entry = tk.Entry(root, width=10)
        entry.grid(row=1, column=col)
        entry_fields[0].append(entry)

    # Button to add a new row
    add_row_button = tk.Button(root, text="Add New Row", command=add_new_row)
    add_row_button.grid(row=2, columnspan=num_cols, pady=10)

    # Button to save the text data
    save_button = tk.Button(root, text="Save Data", command=save_text)
    save_button.grid(row=3, columnspan=num_cols, pady=10)

# Create the main window
root = tk.Tk()
root.title("Grid Text Input")

# Define the initial size of the grid
num_rows = 1
num_cols = 3

# Create a 2D array to store the text data
text_data = [["" for _ in range(num_cols)]]

# Create a 2D array to store the Entry widgets
entry_fields = [[] for _ in range(num_rows)]

# Create the grid of Entry widgets and buttons
create_grid()

# Run the application
root.mainloop()

# Now text_data contains the text entered in each Entry widget
print(text_data)
