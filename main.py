import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QMainWindow, \
	QPushButton, QScrollArea, QWidget, QGridLayout, QSizePolicy
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


def add_to_clipboard(txt):
	pyperclip.copy(txt)
	print(f"copied {txt}")
	return txt


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

	tray_icon.setContextMenu(menu)

	# add scrollable part
	scroll = QScrollArea(parent=window)
	scroll.setGeometry(10, 10, WIDTH - 20, HEIGHT - 20)
	scroll.setFixedWidth(WIDTH - 20)
	scroll.setMinimumHeight(HEIGHT - 20)
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

	# TODO:
	# make look ok

	i = 0
	emoji_buttons = []

	# the functionality
	# thanks stackoverflow
	for a, b in EMOJIS.items():
		btn = QPushButton(b, parent=scroll_contents)
		btn.setToolTip(a)

		btn.setFixedWidth(36)
		btn.setFixedHeight(36)

		btn.clicked.connect(lambda ch, txt=b: add_to_clipboard(txt))

		size_policy = QSizePolicy(QSizePolicy.Maximum,
				QSizePolicy.Fixed)
		size_policy.setHorizontalStretch(0)
		size_policy.setVerticalStretch(0)
		btn.setSizePolicy(size_policy)

		scroll_grid.addWidget(btn, i // 8, i % 8)
		emoji_buttons.append(btn)
		i += 1

	# showing stuff
	tray_icon.show()
	window.show()

	sys.exit(app.exec_())


if __name__ == "__main__":
	main()