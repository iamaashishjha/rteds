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
        self.frames.create_home_frame()

        # create second frame
        self.frames.create_second_frame()

        # create third frame
        self.frames.create_third_frame()

        # create camera frame
        self.frames.create_camera_frame()

        # select default frame
        self.frames.select_frame_by_name("home")

    def start_camera_feed(self):
        self.camera.open_camera(self.frames.camera_canvas_reference)

    def on_close(self):
        self.emotions.stop_camera()
        self.destroy()
    
    def home_button_event(self):
        self.frames.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.frames.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.frames.select_frame_by_name("frame_3")

    def camera_frame_button_event(self):
        self.frames.select_frame_by_name("camera_frame")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.protocol("WM_DELETE_WINDOW", app.on_close)
    app.mainloop()