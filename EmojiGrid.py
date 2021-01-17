from const import *
from PyQt5.QtWidgets import QScrollArea, QWidget, QGridLayout, QPushButton,\
	QSizePolicy
from PyQt5.QtGui import QFont
import emojis
from functions import *


emoji_db = emojis.db.get_emoji_aliases()


class EmojiGrid(QScrollArea):
	def __init__(self, parent):
		super(EmojiGrid, self).__init__(parent)
		self.setGeometry(10, TITLE_BAR_HEIGHT - 10,
				WIDTH - 20, HEIGHT - TITLE_BAR_HEIGHT)
		self.setFixedWidth(WIDTH - 20)
		self.setMinimumHeight(HEIGHT - TITLE_BAR_HEIGHT)
		self.setWidgetResizable(True)

		# the contents of scrollable
		self.contents = QWidget()
		self.contents.setFixedWidth(WIDTH - 40)
		self.setWidget(self.contents)

		# the layout of contents
		self.grid = QGridLayout()
		self.grid.setHorizontalSpacing(4)
		self.grid.setVerticalSpacing(10)
		self.contents.setLayout(self.grid)

		self.fill()

	def fill(self):
		font = QFont()
		font.setFamily("Times")
		font.setPixelSize(20)

		i = 0
		for emoji_name, value in emoji_db.items():
			btn = QPushButton(value, parent=self.contents)
			btn.setToolTip(emoji_name)

			btn.setFont(font)
			btn.setFixedWidth(42)
			btn.setFixedHeight(42)

			btn.clicked.connect(lambda ch, txt=value: insert(txt))
			# btn.clicked.connect(lambda ch, txt=value: add_to_clipboard(txt))

			size_policy = QSizePolicy(QSizePolicy.Maximum,
					QSizePolicy.Fixed)
			size_policy.setHorizontalStretch(0)
			size_policy.setVerticalStretch(0)
			btn.setSizePolicy(size_policy)

			self.grid.addWidget(btn, i // 6, i % 6)
			i += 1
