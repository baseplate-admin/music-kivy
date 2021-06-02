import os

from kivy.utils import get_color_from_hex
from kivy.properties import StringProperty
from kivy.metrics import dp
from kivy.clock import Clock

from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.menu import MDDropdownMenu

from .DropDownMenu.main import Item


class MusicListWithDropdown(TwoLineAvatarIconListItem):
    right_text = StringProperty()

    left_icon = "github"
    right_icon = 'dots-vertical'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.post_init, 0)

    def post_init(self, *args):
        self.menu_background = get_color_from_hex("#191b1f")

        menu_items = [
            {
                "text": f"Item {i}",
                "left_icon": "git",
                "viewclass": "Item",
                "height": dp(54),
                # "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            }
            for i in range(5)
        ]

        self.menu = MDDropdownMenu(
            background_color=self.menu_background,
            caller=self.ids.music_list_icon_right,
            items=menu_items,
            width_mult=4,
            pos_hint={"center_y": 1},
        )

    def open_menu(self):
        self.menu.check_position_caller(None, None, None)
        self.menu.open()
