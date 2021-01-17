"""
module with functions for the EmojiBoard app
============================================

"""

import pyperclip
import pyautogui
import pygetwindow
import sys
import ctypes


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
