from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import sys


class Ui_Form(object):
    def setupUi(self, Form): pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())