import customtkinter
import os
from PIL import Image

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Real Time Emotion Detection System")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="RTEDS", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 2",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_rowconfigure(0, weight=1)

        self.home_frame_card = customtkinter.CTkFrame(self.home_frame, corner_radius=10, fg_color="lightgray")
        self.home_frame_card.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.home_frame_card.grid_columnconfigure(0, weight=1)
        self.home_frame_card.grid_rowconfigure(0, weight=0)
        self.home_frame_card.grid_rowconfigure(1, weight=1)

        self.home_frame_heading_card = customtkinter.CTkFrame(self.home_frame_card, corner_radius=0, fg_color="lightgray")
        self.home_frame_heading_card.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        self.home_frame_heading_label = customtkinter.CTkLabel(self.home_frame_heading_card, text="Home Frame", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.home_frame_heading_label.pack()

        self.home_frame_text_card = customtkinter.CTkFrame(self.home_frame_card, corner_radius=0, fg_color="white")
        self.home_frame_text_card.grid(row=1, column=0, padx=20, pady=(10, 20), sticky="nsew")

        self.home_frame_text_label = customtkinter.CTkLabel(self.home_frame_text_card, text="This is the home frame text.\nYou can add any content here.",
                                                            font=customtkinter.CTkFont(size=14), fg_color="black", bg_color="white")
        self.home_frame_text_label.pack(fill="both", expand=True)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)
        self.second_frame.grid_rowconfigure(0, weight=1)

        self.second_frame_card = customtkinter.CTkFrame(self.second_frame, corner_radius=10, fg_color="lightgray")
        self.second_frame_card.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.second_frame_card.grid_columnconfigure(0, weight=1)
        self.second_frame_card.grid_rowconfigure(0, weight=0)
        self.second_frame_card.grid_rowconfigure(1, weight=1)

        self.second_frame_heading_card = customtkinter.CTkFrame(self.second_frame_card, corner_radius=0, fg_color="lightgray")
        self.second_frame_heading_card.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        self.second_frame_heading_label = customtkinter.CTkLabel(self.second_frame_heading_card, text="Frame 2", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.second_frame_heading_label.pack()

        self.second_frame_text_card = customtkinter.CTkFrame(self.second_frame_card, corner_radius=0, fg_color="white")
        self.second_frame_text_card.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.second_frame_text_label = customtkinter.CTkLabel(self.second_frame_text_card, text="This is the Frame 2 text.\nYou can add any content here.",
                                                            font=customtkinter.CTkFont(size=14), fg_color="black", bg_color="white")
        self.second_frame_text_label.pack(fill="both", expand=True)

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_columnconfigure(0, weight=1)
        self.third_frame.grid_rowconfigure(0, weight=1)

        self.third_frame_card = customtkinter.CTkFrame(self.third_frame, corner_radius=10, fg_color="lightgray")
        self.third_frame_card.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.third_frame_card.grid_columnconfigure(0, weight=1)
        self.third_frame_card.grid_rowconfigure(0, weight=0)
        self.third_frame_card.grid_rowconfigure(1, weight=1)

        self.third_frame_heading_card = customtkinter.CTkFrame(self.third_frame_card, corner_radius=0, fg_color="lightgray")
        self.third_frame_heading_card.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        self.third_frame_heading_label = customtkinter.CTkLabel(self.third_frame_heading_card, text="Frame 3", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.third_frame_heading_label.pack()

        self.third_frame_text_card = customtkinter.CTkFrame(self.third_frame_card, corner_radius=0, fg_color="white")
        self.third_frame_text_card.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.third_frame_text_label = customtkinter.CTkLabel(self.third_frame_text_card, text="This is the Frame 3 text.\nYou can add any content here.",
                                                            font=customtkinter.CTkFont(size=14), fg_color="black", bg_color="white")
        self.third_frame_text_label.pack(fill="both", expand=True)


        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
            self.second_frame.grid_forget()
            self.third_frame.grid_forget()
        elif name == "frame_2":
            self.home_frame.grid_forget()
            self.second_frame.grid(row=0, column=1, sticky="nsew")
            self.third_frame.grid_forget()
        elif name == "frame_3":
            self.home_frame.grid_forget()
            self.second_frame.grid_forget()
            self.third_frame.grid(row=0, column=1, sticky="nsew")

        self.current_frame_name = name

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()