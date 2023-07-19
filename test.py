import tkinter as tk
from utils.frames import Frames
from utils.camera import Camera

root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

frames = Frames(root)  # Create an instance of Frames with the root window
frames.create_home_frame()  # Create the home frame and initialize the Camera instance

# Use the Camera instance from the Frames class
camera = frames.camera
camera.open_camera(canvas)  # Open the camera and display it on the canvas

root.mainloop()
