import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

def save_text():
    for row in range(len(entry_fields)):
        row_data = []
        for col in range(len(entry_fields[row])):
            text = entry_fields[row][col].get().strip()
            if text:
                row_data.append(text)
            else:
                break
        else:
            # All columns in the row have non-null values, so save the row's data
            text_data[row] = row_data

    # Show pop-up notification
    messagebox.showinfo("Success", "Data saved successfully!")

def add_new_row():
    global num_rows
    num_rows += 1
    entry_fields.append([])
    for col in range(num_cols):
        entry = tk.Entry(root, width=10)
        entry.grid(row=num_rows, column=col)
        entry_fields[num_rows-1].append(entry)
    # Move the buttons to the next row
    add_row_button.grid(row=num_rows+1, column=0, pady=10)
    save_button.grid(row=num_rows+1, column=1, pady=10)
    plot_button.grid(row=num_rows+1, column=2, pady=10)
    
def plot_graph():
    # Save the plot as an image
    G = nx.DiGraph()

    # Add nodes to the directed graph
    G.add_nodes_from([1, 2, 3, 4])

    # Add directed edges between nodes with labels
    edges = [(1, 2, {'label': 'A'}), (1, 3, {'label': 'B'}), (2, 3, {'label': 'C'}), (3, 4, {'label': 'D'})]
    G.add_edges_from(edges)

    # Draw the directed graph with labels on the arrows
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, font_weight='bold', arrows=True)

    # Add labels to the arrows
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Save the plot as an image
    plt.savefig("graph.png")

    # Open the saved image using PIL
    img = Image.open("graph.png")

    # Resize the image if necessary
    img = img.resize((400, 300))

    # Convert the image to a format that tkinter can display
    img_tk = ImageTk.PhotoImage(img)

    # Display the image in a tkinter Label widget
    image_label = tk.Label(root, image=img_tk)
    image_label.image = img_tk  # Keep a reference to avoid garbage collection

    # Place the image label at specific pixel coordinates
    image_label.place(x=350, y=21)


def create_grid():
    global add_row_button, save_button, plot_button
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
    add_row_button = tk.Button(root, text="Nueva fila", command=add_new_row, width=10)
    add_row_button.grid(row=2, column=0, pady=10)

    # Button to save the text data
    save_button = tk.Button(root, text="Guardar", command=save_text, width=10)
    save_button.grid(row=2, column=1, pady=10)
    
    # Button to plot the graph
    plot_button = tk.Button(root, text="Graficar", command=plot_graph, width=10)
    plot_button.grid(row=2, column=2, pady=10)  # Adjust row position


# Create the main window
root = tk.Tk()
root.title("Grid Text Input")
root.geometry("775x400")
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
