import customtkinter
from utils.frames import Frames
from utils.config import Config
from utils.camera import Camera
from emotions import Emotions

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.config = Config(self)
        self.config.setup_basic_configuration()

        self.frames = Frames(self)
        self.emotions = Emotions(self.frames)
        # Create the Camera instance
        self.camera = Camera(self)

        # create navigation frame
        self.frames.create_navigation_frame()

        # create home frame
        self.frames.create_dashboard_frame()

        # create camera frame
        self.frames.create_face_cam_frame()

        # create third frame
        self.frames.create_emotion_cam_frame()

        # select default frame
        self.frames.select_frame_by_name("dashboard")

    def on_close(self):
        self.emotions.stop_camera()
        self.destroy()
    
    def dashboard_button_event(self):
        self.frames.select_frame_by_name("dashboard")

    def emotion_cam_button_event(self):
        self.frames.select_frame_by_name("emotion_cam")

    def face_cam_frame_button_event(self):
        self.frames.select_frame_by_name("face_cam_frame")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.protocol("WM_DELETE_WINDOW", app.on_close)
    app.mainloop()