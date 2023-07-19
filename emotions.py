import cv2
from utils.model import Model
import numpy as np
import argparse
from utils.camera import Camera

class Emotions:
    def __init__(self, frames):
        self.frames = frames  # Store the Frames instance
        self.emotion_dict = {
            0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy",
            4: "Neutral", 5: "Sad", 6: "Surprised"
        }
        self.model = Model(
            train_dir='data/train',
            val_dir='data/test',
            num_train=28709,
            num_val=7178,
            batch_size=64,
            num_epoch=50
        )

    def display_emotions(self):
        self.frames.select_frame_by_name("home")  # Ensure home frame is selected
        self.frames.camera.start_camera()  # Start the camera

    def stop_camera(self):
        self.frames.camera.release_camera()  # Release the camera

if __name__ == "__main__":
    emotions = Emotions()

    # command line argument
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode",help="train/display")
    mode = ap.parse_args().mode

    # If you want to train the same model or try other models, go for this
    if mode == "train":
        emotions.model.train_model()

    # emotions will be displayed on your face from the webcam feed
    elif mode == "display":
        emotions.display_emotions()

