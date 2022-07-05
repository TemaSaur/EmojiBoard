from const import *
from PyQt5.QtWidgets import QScrollArea, QWidget, QGridLayout, QPushButton,\
	QSizePolicy
from PyQt5.QtGui import QFont
import emojis
from functions import *
from const import EMOJI_BTN_SIZE


def get_all_emojis():
	db = emojis.db.get_emoji_aliases().items()
	used_emojis = set()

	index = 0
	for emoji in db:
		if emoji[1] not in used_emojis:
			used_emojis.add(emoji[1])
			yield emoji[0], emoji[1], index

			index += 1


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
		self.grid.setVerticalSpacing(10)
		self.contents.setLayout(self.grid)

	def fill_grid(self):
		font = QFont()
		font.setFamily("Times")
		font.setPixelSize(20)

		for emoji_name, emoji_value, i in get_all_emojis():
			self.add_button(emoji_name, emoji_value, i, font)

	def add_button(self, emoji_name, emoji_value, index, font):
		btn = QPushButton(emoji_value, parent=self.contents)
		btn.setToolTip(emoji_name)

		btn.setFont(font)
		btn.setFixedWidth(EMOJI_BTN_SIZE)
		btn.setFixedHeight(EMOJI_BTN_SIZE)

		btn.clicked.connect(lambda ch, txt=emoji_value: insert(txt))

		size_policy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
		size_policy.setHorizontalStretch(0)
		size_policy.setVerticalStretch(0)
		btn.setSizePolicy(size_policy)

		self.grid.addWidget(btn, index // 6, index % 6)
