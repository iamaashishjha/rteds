import customtkinter
import os
from PIL import Image

class Config:
    CURRENT_DIRECTORY = os.getcwd()
    ASSETS_DIR = "assets"
    DATA_DIR = "data"
    MODEL_DIR = "model"
    DATA_TRAIN_DIR = DATA_DIR + "/train"
    DATA_TEST_DIR = DATA_DIR + "/test"
    # haarcascade_frontalface_default.xml
    HAARCASCADE_FRONTALFACE_PATH = os.path.join(CURRENT_DIRECTORY, ASSETS_DIR, "haarcascade_frontalface_default.xml")
    SAMPLE_VIDEO_PATH = os.path.join(CURRENT_DIRECTORY, ASSETS_DIR, "laughing-sample.mp4")

    def __init__(self, parent):
        self.parent = parent

    def setup_basic_configuration(self):
        BASE_GEOMETRY = "700x450"
        BASE_TITLE = "Real Time Emotion Detection System"
        CURRENT_DIRECTORY = self.CURRENT_DIRECTORY
        IMAGE_DIR = "assets/images"

        LOGO_IMAGE_PATH = os.path.join(CURRENT_DIRECTORY, IMAGE_DIR, "CustomTkinter_logo_single.png")
        IMAGE_ICON_PATH = os.path.join(CURRENT_DIRECTORY, IMAGE_DIR, "image_icon_light.png")
        HOME_IMAGE_PATH_LIGHT = os.path.join(CURRENT_DIRECTORY, IMAGE_DIR, "home_light.png")
        CHAT_IMAGE_PATH_LIGHT = os.path.join(CURRENT_DIRECTORY, IMAGE_DIR, "chat_light.png")
        ADD_USER_IMAGE_PATH_LIGHT = os.path.join(CURRENT_DIRECTORY, IMAGE_DIR, "add_user_light.png")
        HOME_IMAGE_PATH_DARK = os.path.join(CURRENT_DIRECTORY, IMAGE_DIR, "home_dark.png")
        CHAT_IMAGE_PATH_DARK = os.path.join(CURRENT_DIRECTORY, IMAGE_DIR, "chat_dark.png")
        ADD_USER_IMAGE_PATH_DARK = os.path.join(CURRENT_DIRECTORY, IMAGE_DIR, "add_user_dark.png")
        DASHBOARD_IMAGE_PATH = os.path.join(CURRENT_DIRECTORY, IMAGE_DIR, "dashboard.jpg")

        self.parent.title(BASE_TITLE)
        self.parent.geometry(BASE_GEOMETRY)

        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(1, weight=1)

        self.parent.logo_image = customtkinter.CTkImage(Image.open(LOGO_IMAGE_PATH), size=(26, 26))
        self.parent.image_icon_image = customtkinter.CTkImage(Image.open(IMAGE_ICON_PATH), size=(20, 20))
        self.parent.home_image = customtkinter.CTkImage(light_image=Image.open(HOME_IMAGE_PATH_DARK),dark_image=Image.open(HOME_IMAGE_PATH_LIGHT), size=(20, 20))
        self.parent.chat_image = customtkinter.CTkImage(light_image=Image.open(CHAT_IMAGE_PATH_DARK),dark_image=Image.open(CHAT_IMAGE_PATH_LIGHT), size=(20, 20))
        self.parent.add_user_image = customtkinter.CTkImage(light_image=Image.open(ADD_USER_IMAGE_PATH_DARK),dark_image=Image.open(ADD_USER_IMAGE_PATH_LIGHT), size=(20, 20))
        self.parent.dashboard_image = customtkinter.CTkImage(Image.open(DASHBOARD_IMAGE_PATH), size=(500, 150))
