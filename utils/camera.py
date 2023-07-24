import cv2
import numpy as np
from PIL import Image, ImageTk
import os
from utils.config import Config
from utils.model import Model
# from utils.frames import Frames

class Camera:
    def __init__(self, parent):
        self.parent = parent
        self.video_capture = None
        self.image_id = None
        self.config = Config(self)
        # self.frames = Frames(self)  # Store the Frames instance
        self.emotion_dict = {
            0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy",
            4: "Neutral", 5: "Sad", 6: "Surprised"
        }
        self.model = Model(
            train_dir=Config.DATA_TRAIN_DIR,
            val_dir=Config.DATA_TEST_DIR,
            num_train=28709,
            num_val=7178,
            batch_size=64,
            num_epoch=50
        )

    def open_emotion_detection_camera(self, canvas):
        self.video_capture = cv2.VideoCapture(Config.SAMPLE_VIDEO_PATH)
        # self.video_capture = cv2.VideoCapture(0)
        if not self.video_capture.isOpened():
            print("Error: Could not open Emotion Detection camera.")
            return
        else:
            print("Video capture is successful.")
        self.update_emotion_detect_canvas(canvas)

    def detect_emotion_camera(self, frame):
        self.model.load_model()
        # prevents openCL usage and unnecessary logging messages
        cv2.ocl.setUseOpenCL(False)
        facecasc = cv2.CascadeClassifier(Config.HAARCASCADE_FRONTALFACE_PATH)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facecasc.detectMultiScale(gray_frame,scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
            roi_gray = gray_frame[y:y + h, x:x + w]
            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
            prediction = self.model.predict(cropped_img)
            maxindex = int(np.argmax(prediction))
            cv2.putText(frame, self.emotion_dict[maxindex], (x+20, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        # cv2.imshow('Video', cv2.resize(frame,(1600,960),interpolation = cv2.INTER_CUBIC))
        return frame
    
    def update_emotion_detect_canvas(self, canvas):
        cv2.ocl.setUseOpenCL(False)
        # ret, frame = cap.read()
        ret, frame = self.video_capture.read()
        # frame = cv2.resize(frame, (700, 600))
        if not ret:
            # Frame not read successfully, handle the error gracefully
            print("Error: Frame not read successfully")
            return

        print("Frame size:", frame.shape)  # Add this line to check the frame size

        frame = cv2.resize(frame, (700, 600))
        
        if ret:
            # Detect faces in the frame
            frame_with_faces = self.detect_emotion_camera(frame)
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
            self.parent.after(10, lambda: self.update_emotion_detect_canvas(canvas))

            # Return the frame with detected faces
            return frame_with_faces
        else:
            self.release_camera()

    def release_camera(self):
        if self.video_capture:
            self.video_capture.release()

