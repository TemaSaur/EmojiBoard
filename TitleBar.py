import sys
# from main import close_window, NAME, WIDTH, HEIGHT, TITLE_BAR_HEIGHT,\
# 	CLOSE_BTN_SIZE
from PyQt5.QtWidgets import QFrame, QPushButton, QLabel
from PyQt5.QtCore import QPoint


def close_window():
	sys.exit()

X_POS = 200
Y_POS = 200
WIDTH = 400
HEIGHT = 360
TITLE_BAR_HEIGHT = 70

CLOSE_BTN_SIZE = 16

NAME = "EmojiBoard;)"


class TitleBar(QFrame):
	def __init__(self, parent):
		super(TitleBar, self).__init__(parent)

		self.setFixedSize(WIDTH, TITLE_BAR_HEIGHT)

		self.parent = parent
		self.title = NAME

		self.label = QLabel(self.title, self)

		self.close = QPushButton("", self)
		self.close.setGeometry(WIDTH-20-CLOSE_BTN_SIZE, 20,
				CLOSE_BTN_SIZE, CLOSE_BTN_SIZE)
		self.close.clicked.connect(close_window)

	# github code
	def mousePressEvent(self, event):
		self.start = self.mapToGlobal(event.pos())
		self.pressing = True

	def mouseMoveEvent(self, event):
		if self.pressing:
			self.end = self.mapToGlobal(event.pos())
			self.movement = self.end - self.start
			self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
					self.mapToGlobal(self.movement).y(),
					self.parent.width(),
					self.parent.height())
			self.start = self.end

	def mouseReleaseEvent(self, QMouseEvent):
		self.pressing = False

	def btn_close_clicked(self):
		self.parent.close()