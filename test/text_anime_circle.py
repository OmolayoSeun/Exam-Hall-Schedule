import tkinter as tk


def update_loading_circle():
    # Increase the arc angle for the loading effect
    current_angle = canvas.itemcget(loading_circle, 'extent')  # Get current extent of the arc
    new_angle = float(current_angle) + angle_increment

    # Reset the angle after a full circle
    if new_angle > 360:
        new_angle = 0

    # Update the arc extent to create the animation
    canvas.itemconfig(loading_circle, extent=new_angle)

    # Schedule the next update
    root.after(25, update_loading_circle)  # Adjust delay for speed control


# Set up the Tkinter window
root = tk.Tk()
root.title("Animated Circular Loading Bar")

# Define dimensions and increments
canvas_width = 200
canvas_height = 200
circle_radius = 80
angle_increment = 5  # Amount of angle to add per frame for smoothness

# Create a canvas to draw the loading circle
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack(pady=20)

# Create an arc on the canvas that represents the circular loading bar
loading_circle = canvas.create_arc(
    (canvas_width // 2 - circle_radius, canvas_height // 2 - circle_radius,
     canvas_width // 2 + circle_radius, canvas_height // 2 + circle_radius),
    start=0, extent=0, outline="blue", width=10, style=tk.ARC
)

# Start the circular loading animation
update_loading_circle()

# Run the Tkinter event loop
root.mainloop()
