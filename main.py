import sys
import os
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon


# main function
def main():
	app = QApplication(sys.argv)

	tray_icon = QSystemTrayIcon(QIcon("src/icon.png"), parent=app)
	tray_icon.setToolTip("Hello Icon")
	tray_icon.show()
	
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
