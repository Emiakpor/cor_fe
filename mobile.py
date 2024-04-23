import json
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.utils import platform

import requests

class PictureUploader(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        # layout = GridLayout(cols=1, spacing=10, padding=10)
        # File chooser
        self.file_chooser = FileChooserListView()
        layout.add_widget(self.file_chooser)

         # Button to upload picture
        button_upload = Button(text="Upload Picture",   
                            size_hint_y=None, height=40, 
                            on_press=self.upload_picture)
        layout.add_widget(button_upload)

        # Image display
        self.image = Image(allow_stretch=True,
                           size_hint_y= None, height= 250)
        layout.add_widget(self.image)       

        button_send = Button(text="Send Picture",  
                            size_hint_y=None, height=40,  
                            on_press=self.send_picture)
        layout.add_widget(button_send)

        # Label to display API response
        self.response_label = Label(text='',size_hint_y=None, height=40)
        layout.add_widget(self.response_label)

        return layout
    
    
    def upload_picture(self, instance):
        # Get the path of the selected picture
        self.selected_path = self.file_chooser.selection and self.file_chooser.selection[0] or None

        if self.selected_path:

            self.image.source = self.selected_path

           
    def send_picture(self, instance):

        if self.selected_path:
            # Read the picture
            with open(self.selected_path, 'rb') as file:
                picture_data = file.read()

                 # Send the picture to the API
                api_url = 'http://127.0.0.1:8000/is_image_corrosive/'
                files = {'image': picture_data}
                response = requests.post(api_url, files=files)

                # Display the JSON response
                if response.status_code == 200:
                    response_data = response.json()
                    print(response_data)
                    data = json.loads(response_data)
                    print(data)
                    self.response_label.text =  data['message']
                else:
                    self.response_label.text = f'Error: {response.status_code} - {response.reason}'

    def get_initial_directory(self):
        # Determine the initial directory based on the platform
        if platform == 'win':
            return 'C:/Users/YourUsername/Pictures'  # Change to your desired directory
        elif platform == 'linux':
            return '/home/YourUsername/Pictures'  # Change to your desired directory
        elif platform == 'macosx':
            return '/Users/YourUsername/Pictures'  # Change to your desired directory
        else:
            # For other platforms, you can set a default directory or handle it accordingly
            return '/'


if __name__ == '__main__':
    PictureUploader().run()
