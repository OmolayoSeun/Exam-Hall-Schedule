import tkinter as tk
from tkinter import messagebox

# Function to handle item click
def on_item_click(event):
    selected_index = listbox.curselection()  # Get the selected index
    if selected_index:
        selected_text = listbox.get(selected_index)  # Get the selected item text
        messagebox.showinfo("Item Clicked", f"You selected: {selected_text}")

# Create the main application window
root = tk.Tk()
root.title("Clickable List")
root.geometry("300x200")

# Create a Listbox widget
listbox = tk.Listbox(root, font=("Arial", 12), selectmode="single")
listbox.pack(expand=True, fill="both", padx=10, pady=10)

# Add items to the listbox
items = ["Item 1: Info Log", "Item 2: Warning Log", "Item 3: Error Log"]
for item in items:
    listbox.insert(tk.END, item)

# Bind the click event
listbox.bind("<<ListboxSelect>>", on_item_click)

# Run the application
root.mainloop()
