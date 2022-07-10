from PyQt5.QtWidgets import QLabel, QWidget
from functions import *


class EmojiButton(QLabel):
	def __init__(self, parent: QWidget, emoji_name, emoji_value):
		super(EmojiButton, self).__init__("", parent)

		set_qt_image_by_name(emoji_name, self)

		self.setToolTip(emoji_name)

		self.emoji_value = emoji_value
		self.setProperty('name', 'emoji_btn')

	def mousePressEvent(self, event):
		insert(self.emoji_value)
