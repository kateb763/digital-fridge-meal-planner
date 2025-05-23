from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.clock import Clock
from PIL import Image
from fridge import Fridge
from image_classifier import ImageClassifier

class MainScreen(BoxLayout):
    """
    Main UI screen of the app containing the camera widget and capture button.
    Handles photo capture and food item recognition to add items to the fridge.
    """

    def __init__(self, **kwargs):
        """
        Initializes the main screen with a live camera feed and a capture button.
        Creates a Fridge instance to store recognized food items.
        """
        super().__init__(**kwargs)
        self.fridge = Fridge()

        self.camera = Camera(play=True, resolution=(640, 480))
        self.add_widget(self.camera)

        capture_button = Button(text="Capture Photo", size_hint=(1, 0.1))
        capture_button.bind(on_press=self.capture_photo)
        self.add_widget(capture_button)

    def capture_photo(self, instance):
        """
        Callback triggered when the capture button is pressed.
        Schedules the photo capture on the next clock cycle.
        """
        Clock.schedule_once(self.take_photo)

    def take_photo(self, dt):
        """
        Captures the current frame from the camera widget and saves it as an image file.
        Then disables the camera feed and triggers image processing.
        """
        image_path = "captured_photo.png"
        self.camera.export_to_png(image_path)
        print(f"Photo saved to {image_path}")

        self.camera.play = False

        self.process_image(image_path)

    def process_image(self, image_path):
        """
        Opens the captured image, converts it to RGB, and uses the image classifier
        to recognize the food item in the photo.

        If an item is recognized, adds it to the fridge and prints confirmation.
        Otherwise, prints an appropriate message.

        Parameters:
        - image_path (str): Path to the saved captured image.
        """
        try:
            converted_rgb_image = Image.open(image_path).convert("RGB")

            recognizer = ImageClassifier(converted_rgb_image)
            item_name = recognizer.recognize_food_item()

            if item_name:
                print(f"{item_name.capitalize()} added to the fridge.")
                self.fridge.add_item(item_name)
            else:
                print("No item recognized")

        except Exception as e:
            print(f"Error: {str(e)}")

class MyApp(App):
    """
    The main Kivy application class that builds and runs the app.
    """

    def build(self):
        """
        Creates and returns the root widget (MainScreen) of the app.
        """
        return MainScreen()

if __name__ == "__main__":
    MyApp().run()
