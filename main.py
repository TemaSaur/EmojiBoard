import sys
import os
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QMainWindow, \
	QPushButton, QScrollArea, QWidget, QGridLayout, QWidget, QSizePolicy
from PyQt5.QtGui import QIcon
import emojis
import pyperclip

X_POS = 200
Y_POS = 200
WIDTH = 400
HEIGHT = 300

NAME = "EmojiBoard;)"
ICON_PLACE = "src/icon.png"
EMOJIS = emojis.db.get_emoji_aliases()


# TEST
# emoji_ = emojis.encode(":stuck_out_tongue_winking_eye:")


def add_to_clipboard(txt):
	pyperclip.copy(txt)
	print(f"copied {txt}")
	return txt


# TEST
# def copy():
# 	add_to_clipboard(emoji_)
# 	return emoji_


# main function
def main():
	app = QApplication(sys.argv)

	# set window
	window = QMainWindow()
	window.setGeometry(X_POS, Y_POS, WIDTH, HEIGHT)
	window.setWindowTitle(NAME)
	window.setWindowIcon(QIcon(ICON_PLACE))

	# set tray icon
	tray_icon = QSystemTrayIcon(QIcon(ICON_PLACE), parent=app)
	tray_icon.setToolTip(NAME)

	# set sys tray menu
	menu = QMenu()
	exit_action = menu.addAction("Exit")
	exit_action.triggered.connect(app.quit)

	# add scrollable part
	scroll = QScrollArea(parent=window)
	scroll.setGeometry(10, 10, WIDTH - 20, HEIGHT - 20)
	scroll.setFixedWidth(WIDTH - 20)
	scroll.setMinimumHeight(HEIGHT - 20)
	scroll.setWidgetResizable(True)
	# scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
	# doesn't work

	scroll_contents = QWidget()
	scroll_contents.setFixedWidth(WIDTH - 40)
	scroll.setWidget(scroll_contents)

	scroll_grid = QGridLayout()
	scroll_grid.setHorizontalSpacing(4)
	scroll_grid.setVerticalSpacing(10)
	scroll_contents.setLayout(scroll_grid)

	# scroll_grid.setColumnStretch(1, 4)
	# scroll_grid.setColumnStretch(2, 4)

	# the functionality
	# TODO:
	# make look ok
	i = 0
	emoji_buttons = []

	for a, b in EMOJIS.items():
		butt = QPushButton(b, parent=scroll_contents)
		butt.setFixedWidth(36)
		butt.setFixedHeight(36)

		size_policy = QSizePolicy(QSizePolicy.Maximum,
				QSizePolicy.Fixed)
		size_policy.setHorizontalStretch(0)
		size_policy.setVerticalStretch(0)
		butt.setSizePolicy(size_policy)

		# (10, i*35, 30, 30)
		butt.setToolTip(a)
		scroll_grid.addWidget(butt, i // 8, i % 8)
		emoji_buttons.append(butt)
		butt.show()
		i += 1

	for butt in emoji_buttons:
		butt.clicked.connect(lambda: add_to_clipboard(butt.text()))
	# butt.clicked.connect(lambda: add_to_clipboard(b))

	tray_icon.setContextMenu(menu)

	tray_icon.show()
	window.show()

	sys.exit(app.exec_())


if __name__ == "__main__":
	main()