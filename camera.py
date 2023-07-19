import cv2
import customtkinter
def create_home_frame(self):
        # Create a Canvas widget
        self.camera_canvas = customtkinter.CTkCanvas(self.home_frame)
        self.camera_canvas.grid(row=0, column=0, sticky="nsew")

        # Open the camera
        self.cap = cv2.VideoCapture(0)

        # Start a loop to read frames from the camera
        while True:
            # Read a frame from the camera
            ret, frame = self.cap.read()

            # Display the frame in the Canvas widget
            self.camera_canvas.create_image((0, 0), image=frame)

            # Check for key press to stop the camera
            key = cv2.waitKey(1)
            if key == ord('q') or key == 27:  # 'q' key or Esc key
                break

        # Release the camera and close the window
        self.cap.release()
