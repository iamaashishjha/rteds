import customtkinter

from PIL import Image
from utils.camera import Camera

class Frames:
    def __init__(self, parent):
        self.parent = parent
        self.create_frames()
        self.camera = Camera(parent)
        self.camera_canvas_reference = None

    def create_frames(self):
        # Configure and populate the home frame
        self.dashboard_frame = customtkinter.CTkFrame(self.parent)

        # Configure and populate the third frame
        self.emotion_cam_frame = customtkinter.CTkFrame(self.parent)

    def create_navigation_frame(self):
        self.navigation_frame = customtkinter.CTkFrame(self.parent, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="RTEDS", image=self.parent.logo_image,
                                                            compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.dashboard_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Dashboard",
                                                fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                image=self.parent.home_image, anchor="w", command=self.parent.dashboard_button_event)
        self.dashboard_button.grid(row=1, column=0, sticky="ew")

        self.emotion_cam_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Emotion Camera",
                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    image=self.parent.add_user_image, anchor="w", command=self.parent.emotion_cam_button_event)
        self.emotion_cam_button.grid(row=2, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.parent.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.dashboard_button.configure(fg_color=("gray75", "gray25") if name == "dashboard" else "transparent")
        self.emotion_cam_button.configure(fg_color=("gray75", "gray25") if name == "emotion_cam" else "transparent")

        # show selected frame
        if name == "dashboard":
            self.camera.release_camera()
            self.dashboard_frame.grid(row=0, column=1, sticky="nsew")
            self.emotion_cam_frame.grid_forget()
        elif name == "emotion_cam":
            self.camera.open_emotion_detection_camera(self.camera_canvas_reference)
            self.dashboard_frame.grid_forget()
            self.emotion_cam_frame.grid(row=0, column=1, sticky="nsew")

        self.current_frame_name = name

    def create_dashboard_frame(self):
        self.dashboard_frame = customtkinter.CTkFrame(self.parent, corner_radius=0, fg_color="transparent")
        self.dashboard_frame.grid_columnconfigure(0, weight=1)
        self.dashboard_frame_large_image_label = customtkinter.CTkLabel(self.dashboard_frame, text="", image=self.parent.dashboard_image)
        self.dashboard_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.dashboard_frame_button_1 = customtkinter.CTkButton(self.dashboard_frame, text="", image=self.parent.image_icon_image)
        self.dashboard_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.dashboard_frame_button_2 = customtkinter.CTkButton(self.dashboard_frame, text="CTkButton", image=self.parent.image_icon_image, compound="right")
        self.dashboard_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.dashboard_frame_button_3 = customtkinter.CTkButton(self.dashboard_frame, text="CTkButton", image=self.parent.image_icon_image, compound="top")
        self.dashboard_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.dashboard_frame_button_4 = customtkinter.CTkButton(self.dashboard_frame, text="CTkButton", image=self.parent.image_icon_image, compound="bottom", anchor="w")
        self.dashboard_frame_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.dashboard_frame = customtkinter.CTkFrame(self.parent, corner_radius=0, fg_color="transparent")
        self.dashboard_frame.grid_columnconfigure(0, weight=1)
        self.dashboard_frame.grid_rowconfigure(0, weight=1)

        self.dashboard_frame_card = customtkinter.CTkFrame(self.dashboard_frame, corner_radius=10, fg_color="lightgray")
        self.dashboard_frame_card.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.dashboard_frame_card.grid_columnconfigure(0, weight=1)
        self.dashboard_frame_card.grid_rowconfigure(0, weight=0)
        self.dashboard_frame_card.grid_rowconfigure(1, weight=1)

        self.dashboard_frame_heading_card = customtkinter.CTkFrame(self.dashboard_frame_card, corner_radius=0, fg_color="lightgray")
        self.dashboard_frame_heading_card.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        self.dashboard_frame_heading_label = customtkinter.CTkLabel(self.dashboard_frame_heading_card, text="Real Time Emotion Detection", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.dashboard_frame_heading_label.pack()

        self.dashboard_frame_text_card = customtkinter.CTkFrame(self.dashboard_frame_card, corner_radius=0, fg_color="white")
        self.dashboard_frame_text_card.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.dashboard_frame_text_label = customtkinter.CTkLabel(self.dashboard_frame_text_card, text="", image=self.parent.dashboard_image, font=customtkinter.CTkFont(size=14), fg_color="black", bg_color="white")
        self.dashboard_frame_text_label.pack(fill="both", expand=True)

    def create_emotion_cam_frame(self):
        self.emotion_cam_frame = customtkinter.CTkFrame(self.parent, corner_radius=0, fg_color="transparent")
        self.emotion_cam_frame.grid_columnconfigure(0, weight=1)
        self.emotion_cam_frame.grid_rowconfigure(0, weight=1)

        self.emotion_cam_frame_card = customtkinter.CTkFrame(self.emotion_cam_frame, corner_radius=10, fg_color="lightgray")
        self.emotion_cam_frame_card.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.emotion_cam_frame_card.grid_columnconfigure(0, weight=1)
        self.emotion_cam_frame_card.grid_rowconfigure(0, weight=0)
        self.emotion_cam_frame_card.grid_rowconfigure(1, weight=1)

        self.emotion_cam_frame_heading_card = customtkinter.CTkFrame(self.emotion_cam_frame_card, corner_radius=0, fg_color="lightgray")
        self.emotion_cam_frame_heading_card.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        self.emotion_cam_frame_heading_label = customtkinter.CTkLabel(self.emotion_cam_frame_heading_card, text="Frame 3", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.emotion_cam_frame_heading_label.pack()

        self.emotion_cam_frame_text_card = customtkinter.CTkFrame(self.emotion_cam_frame_card, corner_radius=0, fg_color="white")
        self.emotion_cam_frame_text_card.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.emotion_cam_frame_text_label = customtkinter.CTkLabel(self.emotion_cam_frame_text_card, text="This is the Frame 3 text.\nYou can add any content here.",
                                                            font=customtkinter.CTkFont(size=14), fg_color="yellow", bg_color="red")
        self.emotion_cam_frame_text_label.pack(fill="both", expand=True)

        self.emotion_cam_frame_canvas = customtkinter.CTkFrame(self.emotion_cam_frame, corner_radius=0, fg_color="transparent")
        self.emotion_cam_frame_canvas.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.emotion_cam_frame_canvas.grid_columnconfigure(0, weight=1)
        self.emotion_cam_frame_canvas.grid_rowconfigure(0, weight=1)

        self.camera_canvas = customtkinter.CTkCanvas(self.emotion_cam_frame_canvas)  # Remove the corner_radius option
        self.camera_canvas.pack(fill="both", expand=True)

        # Set the camera_canvas_reference attribute to the camera canvas
        self.camera_canvas_reference = self.camera_canvas

        # Call the open_emotion_detection_camera method of the Camera class
        self.camera.open_emotion_detection_camera(self.camera_canvas)


    