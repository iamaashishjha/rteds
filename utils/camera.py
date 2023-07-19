import cv2
import numpy as np
from PIL import Image, ImageTk

class Camera:
    def __init__(self, parent):
        self.parent = parent
        self.video_capture = None
        self.image_id = None

    def open_camera(self, canvas):
        self.video_capture = cv2.VideoCapture(0)

        if not self.video_capture.isOpened():
            print("Error: Could not open camera.")
            return

        self.update_canvas(canvas)

    def detect_face():
        print("Face Detection")

    def release_camera(self):
        if self.video_capture:
            self.video_capture.release()

    def update_canvas(self, canvas):
        ret, frame = self.video_capture.read()
        if ret:
            # Convert the OpenCV BGR image to RGB (PIL format)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert the RGB image to ImageTk format
            image = Image.fromarray(frame_rgb)
            image_tk = ImageTk.PhotoImage(image)

            # Update the canvas with the new image
            if self.image_id:
                canvas.delete(self.image_id)

            self.image_id = canvas.create_image(0, 0, anchor="nw", image=image_tk)
            canvas.image = image_tk  # Save a reference to prevent garbage collection

            # Schedule the next update
            self.parent.after(10, lambda: self.update_canvas(canvas))
        else:
            self.release_camera()
