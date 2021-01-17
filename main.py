import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QMainWindow, \
	QPushButton, QScrollArea, QWidget, QGridLayout, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
import emojis
import pyperclip
import ctypes
import pygetwindow
import pyautogui
from TitleBar import TitleBar
from EmojiGrid import EmojiGrid
from const import *


emoji_db = emojis.db.get_emoji_aliases()

with open("index.css", "r") as f:
	styles = f.read()
	f.close()


def main():
	app = QApplication(sys.argv)
	app.setStyleSheet(styles)

	icon = QIcon(ICON_PLACE)

	# set window
	window = QMainWindow(None, Qt.WindowStaysOnTopHint)
	window.setGeometry(X_POS, Y_POS, WIDTH, HEIGHT)
	window.setWindowTitle(NAME)
	window.setWindowIcon(icon)
	window.setWindowFlag(Qt.FramelessWindowHint)

	if sys.platform == "win32":
		id_ = u"TemaSaur.EmojiBoard"
		ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(id_)

	# set title bar
	bar = TitleBar(window)

	# set tray icon
	tray_icon = QSystemTrayIcon(icon, parent=app)
	tray_icon.setToolTip(NAME)

	# set sys tray menu
	menu = QMenu()
	exit_action = menu.addAction("Exit")
	exit_action.triggered.connect(app.quit)

	tray_icon.setContextMenu(menu)

	# add scrollable emojis block
	emoji_grid = EmojiGrid(parent=window)

	# showing stuff
	tray_icon.show()
	window.show()

	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
