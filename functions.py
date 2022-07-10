"""
module with functions for the EmojiBoard app
============================================

"""

import pyperclip
import pyautogui
import pygetwindow
import sys
import ctypes
import json
import const
from PIL import Image, ImageDraw, ImageFont, ImageQt
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap
from pilmoji import Pilmoji
from pilmoji.source import GoogleEmojiSource
import os


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
	the active window and retrieves the original clipboard

	:param txt: Text to be copied/pasted
	:return: Original text
	"""
	original = get_clip()
	add_to_clipboard(txt)
	activate()
	paste()
	add_to_clipboard(original)

	return txt


def close_window():
	"""
	stops every process of app
	"""
	sys.exit()


def set_taskbar_icon():
	"""
	sets taskbar icon for windows machines
	"""
	id_ = u"TemaSaur.EmojiBoard"
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(id_)


def get_all_emojis():
	emojis = json.loads(open(const.EMOJI_JSON_PATH).read())

	used = set()
	bad = {'symbols', 'flags'}

	index = 0
	emojis = filter(lambda e: e['group'] not in bad and 'skin-tone' not in e['slug'], emojis)

	for emoji in emojis:
		if emoji['character'] not in used:
			yield emoji['slug'], emoji['character'], index
			used.add(emoji['character'])
			index += 1
	return


def create_image_from_character(char: str) -> Image:
	size = 160

	image = Image.new("RGBA", (size, size), (0, 0, 0, 0))

	font = ImageFont.truetype('arial.ttf', 109)
	pos = (28, 27)

	with Pilmoji(image, source=GoogleEmojiSource) as pilmoji:
		pilmoji.text(pos, char, (0, 0, 0), font)

	image = image.resize(
		(const.EMOJI_SIZE, const.EMOJI_SIZE),
		Image.ANTIALIAS)
	return image


def set_qt_image(char: str, element : QLabel) -> None:
	image = create_image_from_character(char)

	qt_image = ImageQt.ImageQt(image)
	pixmap = QPixmap.fromImage(qt_image)
	element.setPixmap(pixmap)


def set_qt_image_by_name(name: str, element: QLabel) -> None:
	tokens = const.EMOJI_IMAGE_DIR_PATH + [f"{name}.png"]
	path = os.path.join(*tokens)
	pixmap = QPixmap(path)
	element.setPixmap(pixmap)

