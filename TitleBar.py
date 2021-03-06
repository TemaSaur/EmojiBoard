from const import *
import sys
from PyQt5.QtWidgets import QFrame, QPushButton, QLabel
from functions import *


class TitleBar(QFrame):
	def __init__(self, parent):
		super(TitleBar, self).__init__(parent)

		# pycharm please don't hurt me
		self.start = None
		self.pressing = None
		self.end = None
		self.movement = None

		self.setFixedSize(WIDTH, TITLE_BAR_HEIGHT)

		self.parent = parent
		self.title = NAME

		self.label = QLabel(self.title, self)

		self.close = QPushButton("", self)
		self.close.setGeometry(WIDTH-20-CLOSE_BTN_SIZE, 20,
				CLOSE_BTN_SIZE, CLOSE_BTN_SIZE)
		self.close.clicked.connect(close_window)

	# stackoverflow code
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
