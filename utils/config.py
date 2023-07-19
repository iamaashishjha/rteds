import customtkinter
import os
from PIL import Image

class Config:
    def __init__(self, parent):
        self.parent = parent

    def setup_basic_configuration(self):
        BASE_GEOMETRY = "700x450"
        BASE_TITLE = "Real Time Emotion Detection System"

        TEST_IMAGE_DIR = "../test_images"

        LOGO_IMAGE_NAME = "CustomTkinter_logo_single.png"
        IMAGE_ICON_NAME = "image_icon_light.png"
        HOME_IMAGE_NAME_LIGHT = "home_light.png"
        CHAT_IMAGE_NAME_LIGHT = "chat_light.png"
        ADD_USER_IMAGE_NAME_LIGHT = "add_user_light.png"
        HOME_IMAGE_NAME_DARK = "home_dark.png"
        CHAT_IMAGE_NAME_DARK = "chat_dark.png"
        ADD_USER_IMAGE_NAME_DARK = "add_user_dark.png"

        IMAGE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), TEST_IMAGE_DIR)

        LOGO_IMAGE_PATH = os.path.join(IMAGE_PATH, LOGO_IMAGE_NAME)
        IMAGE_ICON_PATH = os.path.join(IMAGE_PATH, IMAGE_ICON_NAME)
        HOME_IMAGE_PATH_LIGHT = os.path.join(IMAGE_PATH, HOME_IMAGE_NAME_LIGHT)
        CHAT_IMAGE_PATH_LIGHT = os.path.join(IMAGE_PATH, CHAT_IMAGE_NAME_LIGHT)
        ADD_USER_IMAGE_PATH_LIGHT = os.path.join(IMAGE_PATH, ADD_USER_IMAGE_NAME_LIGHT)
        HOME_IMAGE_PATH_DARK = os.path.join(IMAGE_PATH, HOME_IMAGE_NAME_DARK)
        CHAT_IMAGE_PATH_DARK = os.path.join(IMAGE_PATH, CHAT_IMAGE_NAME_DARK)
        ADD_USER_IMAGE_PATH_DARK = os.path.join(IMAGE_PATH, ADD_USER_IMAGE_NAME_DARK)


        self.parent.title(BASE_TITLE)
        self.parent.geometry(BASE_GEOMETRY)
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(1, weight=1)

        self.parent.logo_image = customtkinter.CTkImage(Image.open(LOGO_IMAGE_PATH), size=(26, 26))
        self.parent.image_icon_image = customtkinter.CTkImage(Image.open(IMAGE_ICON_PATH), size=(20, 20))
        self.parent.home_image = customtkinter.CTkImage(light_image=Image.open(HOME_IMAGE_PATH_DARK),dark_image=Image.open(HOME_IMAGE_PATH_LIGHT), size=(20, 20))
        self.parent.chat_image = customtkinter.CTkImage(light_image=Image.open(CHAT_IMAGE_PATH_DARK),dark_image=Image.open(CHAT_IMAGE_PATH_LIGHT), size=(20, 20))
        self.parent.add_user_image = customtkinter.CTkImage(light_image=Image.open(ADD_USER_IMAGE_PATH_DARK),dark_image=Image.open(ADD_USER_IMAGE_PATH_LIGHT), size=(20, 20))