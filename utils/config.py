import customtkinter
import os
from PIL import Image

class Config:
    def __init__(self, parent):
        self.parent = parent
        # self.setup_basic_configuration()

    def setup_basic_configuration(self):
        TEST_IMAGE_DIR = "../test_images"
        IMAGE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), TEST_IMAGE_DIR)


        self.parent.title("Real Time Emotion Detection System")
        self.parent.geometry("700x450")
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(1, weight=1)
        # load images with light and dark mode image
        image_path = IMAGE_PATH

        self.parent.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.parent.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.parent.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.parent.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.parent.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))