from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard

import time
import webbrowser

from filesharer import  FileSharer

Builder.load_file('frontend.kv')


class CameraScreen(Screen):

    def start(self):
          self.ids.camera.play=True
          self.ids.camera.opacity=1
          self.ids.button_camera.text = "Stop Camera"
          self.ids.camera.texture=self.ids.camera._camera.texture
          #bring the texture back to the default camera
    def stop(self):
        self.ids.camera.play = False
        self.ids.camera.opacity=0
        self.ids.button_camera.text = "Start Camera"
        self.ids.camera.texture=None #clear the remained picture in the camera screen

    def capture(self):
        #capture an image and store it
        current_time=time.strftime('%Y%m%d-%H%M%S')
        self.filepath=f"files/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current='image_screen' #changing the current screen to image_screen the name of the other screen
        self.manager.current_screen.ids.img1.source=self.filepath


class ImageScreen(Screen):
    link_error='Create a link first!'

    def create_link(self):
        #get the file path from the camera_scree instance file_path attr
        file_path=App.get_running_app().root.ids.camera_screen.filepath

        #file_sharer=FileSharer(filepath=file_path,api_key="something-that-I-do-not-have")
        #url=file_sharer.share()
        self.url="https://www.google.com"
        self.ids.link_label.text=self.url
    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link_label.text=self.link_error
    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link_label.text=self.link_error
    def back(self):
        self.manager.current ='camera_screen'
        self.manager.current_screen.ids.camera.play=False
        self.manager.current_screen.ids.camera.texture=None


class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()
    
MainApp().run()