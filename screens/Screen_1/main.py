from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.utils import get_color_from_hex

from kivymd.uix.list import MDList

from .components.MusicList.main import MusicListWithDropdown


class ScreenOne(Screen):
    def __init__(self, **kwargs):
        super(ScreenOne, self).__init__(**kwargs)
        self.primary_color = get_color_from_hex("#b6b6b7")
        self.secondary_color = get_color_from_hex("#6f7c82")
        Clock.schedule_once(self.post_init, 0)

    def post_init(self, *args):
        md_list = MDList()

        for i in range(0, 20 + 1):
            music_list = MusicListWithDropdown(
                text=f"{i}.Single line item",
                right_text='5.10',
                secondary_text="none",
                theme_text_color="Custom",
                secondary_theme_text_color="Custom",
                text_color=self.primary_color,
                secondary_text_color=self.secondary_color,
            )
            md_list.add_widget(music_list)

        self.ids.scr_1_music_list.add_widget(md_list)

