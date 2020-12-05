import sys
import os
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QMainWindow
from PyQt5.QtGui import QIcon


X_POS = 200
Y_POS = 200
WIDTH = 400
HEIGHT = 300

NAME = "EmojiBoard;)"
ICON_PLACE = "src/icon.png"


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

	tray_icon.show()
	window.show()
	
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
