import cv2
import numpy as np
from PIL import Image, ImageTk
import os
from utils.config import Config

class Camera:
    def __init__(self, parent):
        self.parent = parent
        self.video_capture = None
        self.image_id = None
        self.config = Config(self)
        # self.config.setup_basic_configuration()

    def open_camera(self, canvas):
        self.video_capture = cv2.VideoCapture(Config.SAMPLE_VIDEO_PATH)

        if not self.video_capture.isOpened():
            print("Error: Could not open camera.")
            return

        self.update_canvas(canvas)

    def detect_face(self, frame):
        # Load the Haar Cascade classifier for face detection
        face_cascade = cv2.CascadeClassifier(Config.HAARCASCADE_FRONTALFACE_PATH)
        # Load the Haar Cascade classifier for face detection
        # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + Config.HAARCASCADE_FRONTALFACE_PATH)

        # Convert the frame to grayscale for face detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform face detection
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        return frame

    def release_camera(self):
        if self.video_capture:
            self.video_capture.release()

    def update_canvas(self, canvas):
        ret, frame = self.video_capture.read()

        if not ret:
            # Frame not read successfully, handle the error gracefully
            # For example, you could return None or raise an exception.
            # Here, I'm just printing an error message.
            print("Error: Frame not read successfully")
            return

        frame = cv2.resize(frame, (700, 600))
        if ret:
            # Detect faces in the frame
            frame_with_faces = self.detect_face(frame)

            # Convert the OpenCV BGR image to RGB (PIL format)
            frame_rgb = cv2.cvtColor(frame_with_faces, cv2.COLOR_BGR2RGB)

            # Convert the RGB image to ImageTk format
            image = Image.fromarray(frame_rgb)
            image_tk = ImageTk.PhotoImage(image)

            # Update the canvas with the new image
            if self.image_id:
                canvas.delete(self.image_id)

            # self.image_id = canvas.create_image(0, 0, anchor="nw", image=image_tk)
            self.image_id = canvas.create_image(0, 0, anchor="nw", image=image_tk)

            canvas.image = image_tk  # Save a reference to prevent garbage collection

            # Schedule the next update
            self.parent.after(10, lambda: self.update_canvas(canvas))

            # Return the frame with detected faces
            return frame_with_faces
        else:
            self.release_camera()