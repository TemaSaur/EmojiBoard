from const import *
from PyQt5.QtWidgets import QScrollArea, QWidget, QGridLayout, QPushButton,\
	QSizePolicy
from PyQt5.QtGui import QFont
import emojis
import pyperclip
import pyautogui
import pygetwindow


emoji_db = emojis.db.get_emoji_aliases()


def get_clip():
	"""
	gets user's clipboard
	"""
	return pyperclip.paste()


def add_to_clipboard(txt):
	"""
	puts [txt] to the user's clipboard

	:param txt: Text to be copied
	:return: [txt]
	"""
	pyperclip.copy(txt)

	return txt


def paste():
	"""
	pastes anything from the clipboard
	"""
	# i don't like using pyautogui here since it could be ~affected by already
	# pressed keys
	pyautogui.hotkey('ctrl', 'v')


def activate():
	"""
	activates the window behind the EmojiBoard

	:return: Active window's title
	"""
	active = [win for win in pygetwindow.getAllWindows() if win.title != ""][1]
	active.activate()

	return active.title


def insert(txt):
	"""
	takes the user's original clipboard, changes it to the [txt], pastes it to
	the active window and retrieves the original clipboard.

	:param txt: Text to be copied/pasted
	:return: Original text
	"""
	original = get_clip()
	add_to_clipboard(txt)
	activate()
	paste()
	add_to_clipboard(original)

	return txt


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
