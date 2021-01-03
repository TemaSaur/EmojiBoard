import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QMainWindow, \
	QPushButton, QScrollArea, QWidget, QGridLayout, QSizePolicy, QFrame, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from TitleBar import TitleBar
import emojis
import pyperclip

X_POS = 200
Y_POS = 200
WIDTH = 400
HEIGHT = 360
TITLE_BAR_HEIGHT = 70

CLOSE_BTN_SIZE = 16

NAME = "EmojiBoard;)"
ICON_PLACE = "src/icon.png"
EMOJIS = emojis.db.get_emoji_aliases()

with open("index.css", "r") as f:
	styles = f.read()
	f.close()


def close_window():
	sys.exit()


def add_to_clipboard(txt):
	pyperclip.copy(txt)
	print(f"copied {txt}")
	return txt


# main function
def main():
	app = QApplication(sys.argv)
	app.setStyleSheet(styles)

	# set window
	window = QMainWindow(None, Qt.WindowStaysOnTopHint)
	window.setGeometry(X_POS, Y_POS, WIDTH, HEIGHT)
	window.setWindowTitle(NAME)
	window.setWindowIcon(QIcon(ICON_PLACE))
	window.setWindowFlag(Qt.FramelessWindowHint)

	# set title bar
	bar = TitleBar(window)

	# set tray icon
	tray_icon = QSystemTrayIcon(QIcon(ICON_PLACE), parent=app)
	tray_icon.setToolTip(NAME)

	# set sys tray menu
	menu = QMenu()
	exit_action = menu.addAction("Exit")
	exit_action.triggered.connect(app.quit)

	tray_icon.setContextMenu(menu)

	# add scrollable part
	scroll = QScrollArea(parent=window)
	scroll.setGeometry(10, TITLE_BAR_HEIGHT - 10, WIDTH - 20, HEIGHT - TITLE_BAR_HEIGHT)
	scroll.setFixedWidth(WIDTH - 20)
	scroll.setMinimumHeight(HEIGHT - TITLE_BAR_HEIGHT)
	scroll.setWidgetResizable(True)

	# content for scrollable
	scroll_contents = QWidget()
	scroll_contents.setFixedWidth(WIDTH - 40)
	scroll.setWidget(scroll_contents)

	# using grid layout for scrollable
	scroll_grid = QGridLayout()
	scroll_grid.setHorizontalSpacing(4)
	scroll_grid.setVerticalSpacing(10)
	scroll_contents.setLayout(scroll_grid)

	i = 0

	# the functionality
	# thanks stackoverflow
	font = QFont()
	font.setFamily("Times")
	font.setPixelSize(20)
	for a, b in EMOJIS.items():
		btn = QPushButton(b, parent=scroll_contents)
		btn.setToolTip(a)

		btn.setFont(font)
		btn.setFixedWidth(42)
		btn.setFixedHeight(42)

		btn.clicked.connect(lambda ch, txt=b: add_to_clipboard(txt))

		size_policy = QSizePolicy(QSizePolicy.Maximum,
				QSizePolicy.Fixed)
		size_policy.setHorizontalStretch(0)
		size_policy.setVerticalStretch(0)
		btn.setSizePolicy(size_policy)

		scroll_grid.addWidget(btn, i // 6, i % 6)
		i += 1

	# showing stuff
	tray_icon.show()
	window.show()

	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
