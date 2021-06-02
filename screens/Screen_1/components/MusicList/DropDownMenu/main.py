from kivy.properties import StringProperty
from kivy.utils import get_color_from_hex

from kivymd.uix.list import OneLineAvatarIconListItem


class Item(OneLineAvatarIconListItem):
    primary_color = get_color_from_hex("#b6b6b7")
    left_icon = StringProperty()
    theme_text_color = "Custom"

    text_color = primary_color

