import customtkinter
import os
from PIL import Image
from utils.camera import Camera

class Frames:
    def __init__(self, parent):
        self.parent = parent
        self.create_frames()
        self.camera = Camera(parent)

    def create_frames(self):
        # Configure and populate the home frame
        self.home_frame = customtkinter.CTkFrame(self.parent)

        # Configure and populate the second frame
        self.second_frame = customtkinter.CTkFrame(self.parent)

        # Configure and populate the third frame
        self.third_frame = customtkinter.CTkFrame(self.parent)

        # Configure and populate the camera frame
        self.camera_frame = customtkinter.CTkFrame(self.parent)

    # Add any additional methods or functions as needed
    def create_navigation_frame(self):
        self.navigation_frame = customtkinter.CTkFrame(self.parent, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="RTEDS", image=self.parent.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.parent.home_image, anchor="w", command=self.parent.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 2",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.parent.chat_image, anchor="w", command=self.parent.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")
        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.parent.add_user_image, anchor="w", command=self.parent.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

                # Create a submenu for "Face Detect"
        self.face_detect_submenu = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Camera Frame",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.parent.add_user_image, anchor="w", command=self.parent.camera_frame_button_event)
        self.face_detect_submenu.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.parent.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.face_detect_submenu.configure(fg_color=("gray75", "gray25") if name == "camera_frame" else "transparent")

        # show selected frame
        if name == "home":
            self.camera.release_camera()
            self.home_frame.grid(row=0, column=1, sticky="nsew")
            self.second_frame.grid_forget()
            self.third_frame.grid_forget()
            self.camera_frame.grid_forget()
        elif name == "frame_2":
            self.camera.release_camera()
            self.home_frame.grid_forget()
            self.second_frame.grid(row=0, column=1, sticky="nsew")
            self.third_frame.grid_forget()
            self.camera_frame.grid_forget()
        elif name == "frame_3":
            self.camera.release_camera()
            self.home_frame.grid_forget()
            self.second_frame.grid_forget()
            self.third_frame.grid(row=0, column=1, sticky="nsew")
            self.camera_frame.grid_forget()
        elif name == "camera_frame":
            self.camera.open_camera(self.camera_canvas_reference)
            self.home_frame.grid_forget()
            self.second_frame.grid_forget()
            self.third_frame.grid_forget()
            self.camera_frame.grid(row=0, column=1, sticky="nsew")

        self.current_frame_name = name


    def create_home_frame(self):
        self.home_frame = customtkinter.CTkFrame(self.parent, corner_radius=0, fg_color="transparent")
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
        self.home_frame_text_card.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.home_frame_text_label = customtkinter.CTkLabel(self.home_frame_text_card, text="This is the home frame text.\nYou can add any content here.",
                                                            font=customtkinter.CTkFont(size=14), fg_color="black", bg_color="white")
        self.home_frame_text_label.pack(fill="both", expand=True)

        # self.camera_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color="transparent")
        # self.camera_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        # self.camera_frame.grid_columnconfigure(0, weight=1)
        # self.camera_frame.grid_rowconfigure(0, weight=1)

        # self.camera_canvas = customtkinter.CTkCanvas(self.camera_frame)  # Remove the corner_radius option
        # self.camera_canvas.pack(fill="both", expand=True)
        # # self.camera_canvas = self.camera.open_camera  # Initialize self.camera_canvas with the camera's open camera
        # self.camera_canvas_reference = self.camera_canvas


    def create_camera_frame(self):
        self.camera_frame = customtkinter.CTkFrame(self.parent, corner_radius=0, fg_color="transparent")
        self.camera_frame.grid_columnconfigure(0, weight=1)
        self.camera_frame.grid_rowconfigure(0, weight=1)

        self.camera_frame_card = customtkinter.CTkFrame(self.camera_frame, corner_radius=10, fg_color="lightgray")
        self.camera_frame_card.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.camera_frame_card.grid_columnconfigure(0, weight=1)
        self.camera_frame_card.grid_rowconfigure(0, weight=0)
        self.camera_frame_card.grid_rowconfigure(1, weight=1)

        self.camera_frame_heading_card = customtkinter.CTkFrame(self.camera_frame_card, corner_radius=0, fg_color="lightgray")
        self.camera_frame_heading_card.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        self.camera_frame_heading_label = customtkinter.CTkLabel(self.camera_frame_heading_card, text="Home Frame", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.camera_frame_heading_label.pack()

        self.camera_frame_text_card = customtkinter.CTkFrame(self.camera_frame_card, corner_radius=0, fg_color="white")
        self.camera_frame_text_card.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.camera_frame_text_label = customtkinter.CTkLabel(self.camera_frame_text_card, text="This is the home frame text.\nYou can add any content here.",
                                                            font=customtkinter.CTkFont(size=14), fg_color="black", bg_color="white")
        self.camera_frame_text_label.pack(fill="both", expand=True)

        self.camera_frame_canvas = customtkinter.CTkFrame(self.camera_frame, corner_radius=0, fg_color="transparent")
        self.camera_frame_canvas.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.camera_frame_canvas.grid_columnconfigure(0, weight=1)
        self.camera_frame_canvas.grid_rowconfigure(0, weight=1)

        self.camera_canvas = customtkinter.CTkCanvas(self.camera_frame_canvas)  # Remove the corner_radius option
        self.camera_canvas.pack(fill="both", expand=True)
        # self.camera_canvas = self.camera.open_camera  # Initialize self.camera_canvas with the camera's open camera
        self.camera_canvas_reference = self.camera_canvas

    def create_second_frame(self):
        self.second_frame = customtkinter.CTkFrame(self.parent, corner_radius=0, fg_color="transparent")
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

    def create_third_frame(self):
        self.third_frame = customtkinter.CTkFrame(self.parent, corner_radius=0, fg_color="transparent")
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

    