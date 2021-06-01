from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from pprint import pprint

class ScreenOne(Screen):

    def __init__(self, **kwargs):
        super(ScreenOne, self).__init__(**kwargs)
