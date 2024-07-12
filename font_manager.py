def Setup(window, title, width, height):
    window_width = width  # Set the window width
    window_height = height  # Set the window height
    window.resizable(False, False)  # Make the window non-resizable

    screen_width = window.winfo_screenwidth()  # Get the screen width
    screen_height = window.winfo_screenheight()  # Get the screen height
    x_position = int((screen_width / 2) - (window_width / 2))  # Calculate the X position for centering the window
    y_position = int((screen_height / 2) - (window_height / 2))  # Calculate the Y position for centering the window

    window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")  # Set the window size and position
    window.title(title)  # Set the window title
