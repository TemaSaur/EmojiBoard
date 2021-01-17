from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from TitleBar import TitleBar
from EmojiGrid import EmojiGrid
from const import *
from functions import *


with open("index.css", "r") as f:
	styles = f.read()
	f.close()


class EmojiBoard(QMainWindow):
	def __init__(self):
		super(EmojiBoard, self).__init__(None, Qt.WindowStaysOnTopHint)

		self.icon = QIcon(ICON_PLACE)

		self.setGeometry(X_POS, Y_POS, WIDTH, HEIGHT)
		self.setWindowTitle(NAME)
		self.setWindowIcon(self.icon)
		self.setWindowFlag(Qt.FramelessWindowHint)

		if sys.platform == "win32":
			set_taskbar_icon()

		self.populate()

		self.tray_icon = None
		self.set_tray()

		self.ready()

	def populate(self):
		TitleBar(self)
		EmojiGrid(self)

	def set_tray(self):
		self.tray_icon = QSystemTrayIcon(self.icon)
		self.tray_icon.setToolTip(NAME)

		menu = QMenu()
		exit_action = menu.addAction("Exit")
		exit_action.triggered.connect(app.quit)

		self.tray_icon.setContextMenu(menu)

	def ready(self):
		self.tray_icon.show()
		self.show()


if __name__ == "__main__":
	import sys

	app = QApplication(sys.argv)
	app.setStyleSheet(styles)

	EmojiBoard()

	sys.exit(app.exec_())
