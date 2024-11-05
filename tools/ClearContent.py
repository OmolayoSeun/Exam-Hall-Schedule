# Clear the widgets of the frame content

def clear_content(current_frame):
    try:
        current_frame.destroy()
    except Exception as e:
        print("Null View error\n", e)
    pass
