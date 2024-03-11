import os
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView

class ImageUploaderApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.image1 = Image(source='default_image.png', size_hint=(1, 0.4))
        layout.add_widget(self.image1)
        self.file_chooser1 = FileChooserIconView(path='.')
        layout.add_widget(self.file_chooser1)

        self.image2 = Image(source='default_image.png', size_hint=(1, 0.4))
        layout.add_widget(self.image2)
        self.file_chooser2 = FileChooserIconView(path='.')
        layout.add_widget(self.file_chooser2)

        btn_upload = Button(text='Upload Images', size_hint=(1, 0.1))
        btn_upload.bind(on_press=self.upload_images)
        layout.add_widget(btn_upload)
        self.response_label = Label(text='', size_hint=(1, 0.1))
        layout.add_widget(self.response_label)
        return layout

    def upload_images(self, instance):
        if self.file_chooser1.selection and self.file_chooser2.selection:
            file_path1 = self.file_chooser1.selection[0]
            file_path2 = self.file_chooser2.selection[0]
            url = 'YOUR_API_ENDPOINT'
            files = {'image1': open(file_path1, 'rb'), 'image2': open(file_path2, 'rb')}
            try:
                response = requests.post(url, files=files)
                if response.status_code == 200:
                    # Assuming API returns JSON response
                    result = response.json()
                    self.response_label.text = result.get('message', 'Unknown response')
                else:
                    self.response_label.text = 'Failed to upload images'
            except Exception as e:
                self.response_label.text = f'Error: {str(e)}'
        else:
            self.response_label.text = 'Please select two images to upload'

if __name__ == '__main__':
    ImageUploaderApp().run()