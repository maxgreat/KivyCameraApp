__version__ = '0.1'

from kivy.app import App
from kivy.lang import Builder
import sys
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.clock import Clock

class CameraLayout(BoxLayout):
    def textureEvent(self):
        print("Texture Event")
        Clock.schedule_interval(self.newImage, 1.0/33.0)
    def newImage(self, event):
        pass
        
class CameraApp(App):
    def build(self):
        return CameraLayout()

if __name__ == "__main__":
	CameraApp().run()
