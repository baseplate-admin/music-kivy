import os

from kivy.utils import get_color_from_hex

from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.menu import MDDropdownMenu

from kivy.metrics import dp

from .DropDownMenu.main import Item


class MusicListWithDropdown(TwoLineAvatarIconListItem):
    left_icon = "github"
    right_icon = f"{os.getcwd()}/assets/Icons/baseline_arrow_drop_down_white_24dp.png"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
