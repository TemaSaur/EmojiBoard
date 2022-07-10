from const import *
from PyQt5.QtWidgets import QScrollArea, QGridLayout
from functions import *
from EmojiButton import EmojiButton


class EmojiGrid(QScrollArea):
	def __init__(self, parent):
		super(EmojiGrid, self).__init__(parent)

		self.setup_window()
		self.contents = QWidget()
		self.setup_content()
		self.grid = QGridLayout()
		self.setup_grid()

		self.fill_grid()

	def setup_window(self):
		self.setGeometry(10, TITLE_BAR_HEIGHT - 10,
			WIDTH - 20, HEIGHT - TITLE_BAR_HEIGHT)
		self.setFixedWidth(WIDTH - 20)
		self.setMinimumHeight(HEIGHT - TITLE_BAR_HEIGHT)
		self.setWidgetResizable(True)

	def setup_content(self):
		self.contents.setFixedWidth(WIDTH - 40)
		self.setWidget(self.contents)

	def setup_grid(self):
		self.grid.setHorizontalSpacing(4)
		self.grid.setVerticalSpacing(8)
		self.contents.setLayout(self.grid)

	def fill_grid(self):
		for emoji_name, emoji_value, index in get_all_emojis():
			btn = EmojiButton(self.contents, emoji_name, emoji_value)

			self.grid.addWidget(btn, index // 6, index % 6)
