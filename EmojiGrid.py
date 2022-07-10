from const import *
from PyQt5.QtWidgets import QScrollArea, QWidget, QGridLayout, QPushButton,\
	QSizePolicy
from functions import *
from const import EMOJI_BTN_SIZE


class EmojiGrid(QScrollArea):
	def __init__(self, parent):
		super(EmojiGrid, self).__init__(parent)

		self.setup_window()
		self.setup_content()
		self.setup_grid()

		self.fill_grid()

	def setup_window(self):
		self.setGeometry(10, TITLE_BAR_HEIGHT - 10,
			WIDTH - 20, HEIGHT - TITLE_BAR_HEIGHT)
		self.setFixedWidth(WIDTH - 20)
		self.setMinimumHeight(HEIGHT - TITLE_BAR_HEIGHT)
		self.setWidgetResizable(True)

	def setup_content(self):
		self.contents = QWidget()
		self.contents.setFixedWidth(WIDTH - 40)
		self.setWidget(self.contents)

	def setup_grid(self):
		self.grid = QGridLayout()
		self.grid.setHorizontalSpacing(4)
		self.grid.setVerticalSpacing(8)
		self.contents.setLayout(self.grid)

	def fill_grid(self):
		for emoji_name, emoji_value, index in get_all_emojis():
			btn = Button(self.contents, emoji_name, emoji_value)

			self.grid.addWidget(btn, index // 6, index % 6)


class Button(QLabel):
	def __init__(self, parent: QWidget, emoji_name, emoji_value):
		super(Button, self).__init__("", parent)

		get_qt_image(emoji_value, self)

		self.setToolTip(emoji_name)

		self.emoji_value = emoji_value
		self.setProperty('name', 'emoji_btn')

	def mousePressEvent(self, event):
		insert(self.emoji_value)
