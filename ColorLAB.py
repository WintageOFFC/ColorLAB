from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        # Base Form
        Form.setObjectName("Form")
        Form.resize(1409, 758)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("background-color: rgb(41, 41, 41);")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # General Colorframe start {
        self.generalColor_frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generalColor_frame.sizePolicy().hasHeightForWidth())
        self.generalColor_frame.setSizePolicy(sizePolicy)
        self.generalColor_frame.setMinimumSize(QtCore.QSize(266, 752))
        self.generalColor_frame.setMaximumSize(QtCore.QSize(255, 16777215))
        self.generalColor_frame.setStyleSheet("background-color: rgb(51, 51, 51);")
        self.generalColor_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.generalColor_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.generalColor_frame.setObjectName("generalColor_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.generalColor_frame)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")

        # BW diogram start {
        self.blackWhite_frame = QtWidgets.QFrame(self.generalColor_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blackWhite_frame.sizePolicy().hasHeightForWidth())
        self.blackWhite_frame.setSizePolicy(sizePolicy)
        self.blackWhite_frame.setMinimumSize(QtCore.QSize(0, 8))
        self.blackWhite_frame.setMaximumSize(QtCore.QSize(16777215, 8))
        self.blackWhite_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.blackWhite_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.blackWhite_frame.setObjectName("blackWhite_frame")

        # WhiteBox
        self.white_frame = QtWidgets.QFrame(self.blackWhite_frame)
        self.white_frame.setGeometry(QtCore.QRect(250, 0, 8, 8))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.white_frame.sizePolicy().hasHeightForWidth())
        self.white_frame.setSizePolicy(sizePolicy)
        self.white_frame.setMinimumSize(QtCore.QSize(8, 8))
        self.white_frame.setMaximumSize(QtCore.QSize(8, 8))
        self.white_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.white_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.white_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.white_frame.setObjectName("white_frame")

        # BlackBox
        self.black_frame = QtWidgets.QFrame(self.blackWhite_frame)
        self.black_frame.setGeometry(QtCore.QRect(0, 0, 8, 8))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.black_frame.sizePolicy().hasHeightForWidth())
        self.black_frame.setSizePolicy(sizePolicy)
        self.black_frame.setMinimumSize(QtCore.QSize(8, 0))
        self.black_frame.setMaximumSize(QtCore.QSize(8, 8))
        self.black_frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.black_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.black_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.black_frame.setObjectName("black_frame")

        # BW diogram End };
        self.gridLayout.addWidget(self.blackWhite_frame, 0, 0, 1, 1)

        # RGB frame start {
        self.rgb_frame = QtWidgets.QFrame(self.generalColor_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rgb_frame.sizePolicy().hasHeightForWidth())
        self.rgb_frame.setSizePolicy(sizePolicy)
        self.rgb_frame.setMinimumSize(QtCore.QSize(260, 26))
        self.rgb_frame.setMaximumSize(QtCore.QSize(260, 26))
        self.rgb_frame.setStyleSheet("background-color: rgb(83, 83, 83);")
        self.rgb_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rgb_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rgb_frame.setObjectName("rgb_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.rgb_frame)
        self.horizontalLayout.setContentsMargins(46, 1, 1, 1)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # R label start {
        self.r_label = QtWidgets.QLabel(self.rgb_frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.r_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.r_label.setFont(font)
        self.r_label.setStyleSheet("color: rgb(200, 200, 200);")
        self.r_label.setTextFormat(QtCore.Qt.AutoText)
        self.r_label.setScaledContents(False)
        self.r_label.setWordWrap(False)
        self.r_label.setObjectName("r_label")

        # R label end };
        self.horizontalLayout.addWidget(self.r_label)

        # G label start {
        self.g_label = QtWidgets.QLabel(self.rgb_frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.g_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.g_label.setFont(font)
        self.g_label.setStyleSheet("color: rgb(200, 200, 200);")
        self.g_label.setTextFormat(QtCore.Qt.AutoText)
        self.g_label.setScaledContents(False)
        self.g_label.setWordWrap(False)
        self.g_label.setObjectName("g_label")

        # G label end };
        self.horizontalLayout.addWidget(self.g_label)

        # B label start {
        self.b_label = QtWidgets.QLabel(self.rgb_frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.b_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.b_label.setFont(font)
        self.b_label.setStyleSheet("color: rgb(200, 200, 200);")
        self.b_label.setTextFormat(QtCore.Qt.AutoText)
        self.b_label.setScaledContents(False)
        self.b_label.setWordWrap(False)
        self.b_label.setObjectName("b_label")

        # B label end };
        self.horizontalLayout.addWidget(self.b_label)

        # RGB frame end };
        self.gridLayout.addWidget(self.rgb_frame, 2, 0, 1, 1)

        # Primerise frame start {
        self.primerise_frame = QtWidgets.QFrame(self.generalColor_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.primerise_frame.sizePolicy().hasHeightForWidth())
        self.primerise_frame.setSizePolicy(sizePolicy)
        self.primerise_frame.setMinimumSize(QtCore.QSize(260, 607))
        self.primerise_frame.setMaximumSize(QtCore.QSize(260, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.primerise_frame.setFont(font)
        self.primerise_frame.setStyleSheet("background-color: rgb(83, 83, 83);")
        self.primerise_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.primerise_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.primerise_frame.setObjectName("primerise_frame")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.primerise_frame)
        self.gridLayout_8.setContentsMargins(20, -1, 20, -1)
        self.gridLayout_8.setVerticalSpacing(12)
        self.gridLayout_8.setObjectName("gridLayout_8")

        # PF frame start {
        self.pf_frame = QtWidgets.QFrame(self.primerise_frame)
        self.pf_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pf_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pf_frame.setObjectName("pf_frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.pf_frame)
        self.gridLayout_6.setContentsMargins(6, 1, 6, 1)
        self.gridLayout_6.setSpacing(1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.blur_label = QtWidgets.QLabel(self.pf_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")

        # Blur label, parm, slider start {
        self.blur_label.setFont(font)
        self.blur_label.setStyleSheet("color: rgba(200, 200, 200, 255);")
        self.blur_label.setObjectName("blur_label")
        self.gridLayout_6.addWidget(self.blur_label, 0, 0, 1, 1)
        self.blur_parm = QtWidgets.QLineEdit(self.pf_frame)
        self.blur_parm.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.blur_parm.setFont(font)
        self.blur_parm.setToolTipDuration(-1)
        self.blur_parm.setStyleSheet("QLineEdit {\n"
                                     "    border: 0px solid gray;\n"
                                     "    border-radius: 4px;\n"
                                     "    padding: 0 8px;\n"
                                     "    color: rgb(200, 200, 200);\n"
                                     "    background: rgb(71, 71, 71); \n"
                                     "    selection-background-color: darkgray;\n"
                                     "}")
        self.blur_parm.setCursorPosition(0)
        self.blur_parm.setObjectName("blur_parm")
        self.gridLayout_6.addWidget(self.blur_parm, 0, 1, 1, 1)
        self.blur_slider = QtWidgets.QSlider(self.pf_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blur_slider.sizePolicy().hasHeightForWidth())
        self.blur_slider.setSizePolicy(sizePolicy)
        self.blur_slider.setMinimumSize(QtCore.QSize(0, 10))
        self.blur_slider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.blur_slider.setStyleSheet("QSlider::groove:horizontal {\n"
                                       "    border: 0px solid #626262;\n"
                                       "    height: 4px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 98, 98, 255), stop:0.465909 rgba(118, 118, 118, 255), stop:1 rgba(200, 200, 200, 255));\n"
                                       "    margin: 0px 0;\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::handle:horizontal {\n"
                                       "    background: rgb(186, 186, 186);\n"
                                       "    width: 8px;\n"
                                       "    margin: -2px 0;\n"
                                       "    border-radius: 3.9px; /* измените это значение на ваш выбор */\n"
                                       "}")
        self.blur_slider.setMinimum(0)
        self.blur_slider.setMaximum(100)
        self.blur_slider.setProperty("value", 0)
        self.blur_slider.setSliderPosition(0)
        self.blur_slider.setOrientation(QtCore.Qt.Horizontal)
        self.blur_slider.setObjectName("blur_slider")

        # Blur label, parm, slider end };
        self.gridLayout_6.addWidget(self.blur_slider, 1, 0, 1, 2)

        # Bloom label, parm, slider start {
        self.bloom_label = QtWidgets.QLabel(self.pf_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bloom_label.setFont(font)
        self.bloom_label.setStyleSheet("color: rgba(200, 200, 200, 255);")
        self.bloom_label.setObjectName("bloom_label")
        self.gridLayout_6.addWidget(self.bloom_label, 2, 0, 1, 1)
        self.bloom_parm = QtWidgets.QLineEdit(self.pf_frame)
        self.bloom_parm.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.bloom_parm.setFont(font)
        self.bloom_parm.setMouseTracking(False)
        self.bloom_parm.setToolTipDuration(-1)
        self.bloom_parm.setStyleSheet("QLineEdit {\n"
                                      "    border: 0px solid gray;\n"
                                      "    border-radius: 4px;\n"
                                      "    padding: 0 8px;\n"
                                      "    color: rgb(200, 200, 200);\n"
                                      "    background: rgb(71, 71, 71); \n"
                                      "    selection-background-color: darkgray;\n"
                                      "}")
        self.bloom_parm.setCursorPosition(0)
        self.bloom_parm.setObjectName("bloom_parm")
        self.gridLayout_6.addWidget(self.bloom_parm, 2, 1, 1, 1)
        self.bloom_slider = QtWidgets.QSlider(self.pf_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bloom_slider.sizePolicy().hasHeightForWidth())
        self.bloom_slider.setSizePolicy(sizePolicy)
        self.bloom_slider.setMinimumSize(QtCore.QSize(0, 10))
        self.bloom_slider.setStyleSheet("QSlider::groove:horizontal {\n"
                                        "    border: 0px solid #626262;\n"
                                        "    height: 4px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 98, 98, 255), stop:0.465909 rgba(118, 118, 118, 255), stop:1 rgba(200, 200, 200, 255));\n"
                                        "    margin: 0px 0;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::handle:horizontal {\n"
                                        "    background: rgb(186, 186, 186);\n"
                                        "    width: 8px;\n"
                                        "    margin: -2px 0;\n"
                                        "    border-radius: 3.9px; /* измените это значение на ваш выбор */\n"
                                        "}")
        self.bloom_slider.setMinimum(0)
        self.bloom_slider.setMaximum(100)
        self.bloom_slider.setProperty("value", 0)
        self.bloom_slider.setSliderPosition(0)
        self.bloom_slider.setOrientation(QtCore.Qt.Horizontal)
        self.bloom_slider.setObjectName("bloom_slider")

        # Bloom label, parm, slider end };
        self.gridLayout_6.addWidget(self.bloom_slider, 3, 0, 1, 2)

        # Grain label, parm, slider start {
        self.grain_label = QtWidgets.QLabel(self.pf_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.grain_label.setFont(font)
        self.grain_label.setStyleSheet("color: rgba(200, 200, 200, 255);")
        self.grain_label.setObjectName("grain_label")
        self.gridLayout_6.addWidget(self.grain_label, 4, 0, 1, 1)
        self.grain_parm = QtWidgets.QLineEdit(self.pf_frame)
        self.grain_parm.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.grain_parm.setFont(font)
        self.grain_parm.setToolTipDuration(-1)
        self.grain_parm.setStyleSheet("QLineEdit {\n"
                                      "    border: 0px solid gray;\n"
                                      "    border-radius: 4px;\n"
                                      "    padding: 0 8px;\n"
                                      "    color: rgb(200, 200, 200);\n"
                                      "    background: rgb(71, 71, 71); \n"
                                      "    selection-background-color: darkgray;\n"
                                      "}")
        self.grain_parm.setCursorPosition(0)
        self.grain_parm.setObjectName("grain_parm")
        self.gridLayout_6.addWidget(self.grain_parm, 4, 1, 1, 1)
        self.grain_slider = QtWidgets.QSlider(self.pf_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grain_slider.sizePolicy().hasHeightForWidth())
        self.grain_slider.setSizePolicy(sizePolicy)
        self.grain_slider.setMinimumSize(QtCore.QSize(0, 10))
        self.grain_slider.setStyleSheet("QSlider::groove:horizontal {\n"
                                        "    border: 0px solid #626262;\n"
                                        "    height: 4px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 98, 98, 255), stop:0.465909 rgba(118, 118, 118, 255), stop:1 rgba(200, 200, 200, 255));\n"
                                        "    margin: 0px 0;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::handle:horizontal {\n"
                                        "    background: rgb(186, 186, 186);\n"
                                        "    width: 8px;\n"
                                        "    margin: -2px 0;\n"
                                        "    border-radius: 3.9px; /* измените это значение на ваш выбор */\n"
                                        "}")
        self.grain_slider.setMinimum(0)
        self.grain_slider.setMaximum(100)
        self.grain_slider.setProperty("value", 0)
        self.grain_slider.setSliderPosition(0)
        self.grain_slider.setOrientation(QtCore.Qt.Horizontal)
        self.grain_slider.setObjectName("grain_slider")

        # Bloom label, parm, slider end };
        self.gridLayout_6.addWidget(self.grain_slider, 5, 0, 1, 2)

        # Vignette label, parm, slider start {
        self.vignette_label = QtWidgets.QLabel(self.pf_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.vignette_label.setFont(font)
        self.vignette_label.setStyleSheet("color: rgba(200, 200, 200, 255);")
        self.vignette_label.setObjectName("vignette_label")
        self.gridLayout_6.addWidget(self.vignette_label, 6, 0, 1, 1)
        self.vignette_parm = QtWidgets.QLineEdit(self.pf_frame)
        self.vignette_parm.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.vignette_parm.setFont(font)
        self.vignette_parm.setMouseTracking(False)
        self.vignette_parm.setToolTipDuration(-1)
        self.vignette_parm.setStyleSheet("QLineEdit {\n"
                                         "    border: 0px solid gray;\n"
                                         "    border-radius: 4px;\n"
                                         "    padding: 0 8px;\n"
                                         "    color: rgb(200, 200, 200);\n"
                                         "    background: rgb(71, 71, 71); \n"
                                         "    selection-background-color: darkgray;\n"
                                         "}")
        self.vignette_parm.setCursorPosition(0)
        self.vignette_parm.setObjectName("vignette_parm")
        self.gridLayout_6.addWidget(self.vignette_parm, 6, 1, 1, 1)
        self.vignette_slider = QtWidgets.QSlider(self.pf_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vignette_slider.sizePolicy().hasHeightForWidth())
        self.vignette_slider.setSizePolicy(sizePolicy)
        self.vignette_slider.setMinimumSize(QtCore.QSize(0, 10))
        self.vignette_slider.setStyleSheet("QSlider::groove:horizontal {\n"
                                           "    border: 0px solid #626262;\n"
                                           "    height: 4px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 98, 98, 255), stop:0.465909 rgba(118, 118, 118, 255), stop:1 rgba(200, 200, 200, 255));\n"
                                           "    margin: 0px 0;\n"
                                           "}\n"
                                           "\n"
                                           "QSlider::handle:horizontal {\n"
                                           "    background: rgb(186, 186, 186);\n"
                                           "    width: 8px;\n"
                                           "    margin: -2px 0;\n"
                                           "    border-radius: 3.9px; /* измените это значение на ваш выбор */\n"
                                           "}")
        self.vignette_slider.setMinimum(-100)
        self.vignette_slider.setMaximum(100)
        self.vignette_slider.setProperty("value", 0)
        self.vignette_slider.setSliderPosition(0)
        self.vignette_slider.setOrientation(QtCore.Qt.Horizontal)
        self.vignette_slider.setObjectName("vignette_slider")

        # Vignette label, parm, slider end };
        self.gridLayout_6.addWidget(self.vignette_slider, 7, 0, 1, 2)

        # PF frame end };
        self.gridLayout_8.addWidget(self.pf_frame, 7, 0, 1, 1)

        # WB frame start {
        self.wb_frame = QtWidgets.QFrame(self.primerise_frame)
        self.wb_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wb_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wb_frame.setObjectName("wb_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.wb_frame)
        self.gridLayout_4.setContentsMargins(6, 1, 6, 1)
        self.gridLayout_4.setSpacing(1)
        self.gridLayout_4.setObjectName("gridLayout_4")

        # Temperature, Tint - label, parm, slider start {
        self.temperature_slider = QtWidgets.QSlider(self.wb_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temperature_slider.sizePolicy().hasHeightForWidth())
        self.temperature_slider.setSizePolicy(sizePolicy)
        self.temperature_slider.setMinimumSize(QtCore.QSize(0, 10))
        self.temperature_slider.setStyleSheet("QSlider::groove:horizontal {\n"
                                              "    border: 0px solid #626262;\n"
                                              "    height: 4px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
                                              "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 200, 200), stop:1 rgba(235, 235, 0, 255));\n"
                                              "    margin: 0px 0;\n"
                                              "}\n"
                                              "\n"
                                              "QSlider::handle:horizontal {\n"
                                              "    background: rgb(186, 186, 186);\n"
                                              "    width: 8px;\n"
                                              "    margin: -2px 0;\n"
                                              "    border-radius: 3.9px; /* измените это значение на ваш выбор */\n"
                                              "}")
        self.temperature_slider.setMinimum(-100)
        self.temperature_slider.setMaximum(100)
        self.temperature_slider.setProperty("value", 0)
        self.temperature_slider.setSliderPosition(0)
        self.temperature_slider.setOrientation(QtCore.Qt.Horizontal)
        self.temperature_slider.setObjectName("temperature_slider")
        self.gridLayout_4.addWidget(self.temperature_slider, 1, 0, 1, 2)
        self.temp_parm = QtWidgets.QLineEdit(self.wb_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temp_parm.sizePolicy().hasHeightForWidth())
        self.temp_parm.setSizePolicy(sizePolicy)
        self.temp_parm.setMinimumSize(QtCore.QSize(0, 0))
        self.temp_parm.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.temp_parm.setFont(font)
        self.temp_parm.setToolTipDuration(-1)
        self.temp_parm.setStyleSheet("QLineEdit {\n"
                                     "    border: 0px solid gray;\n"
                                     "    border-radius: 4px;\n"
                                     "    padding: 0 8px;\n"
                                     "    color: rgb(200, 200, 200);\n"
                                     "    background: rgb(71, 71, 71); \n"
                                     "    selection-background-color: darkgray;\n"
                                     "}")
        self.temp_parm.setCursorPosition(0)
        self.temp_parm.setObjectName("temp_parm")
        self.gridLayout_4.addWidget(self.temp_parm, 0, 1, 1, 1)
        self.tint_slider = QtWidgets.QSlider(self.wb_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tint_slider.sizePolicy().hasHeightForWidth())
        self.tint_slider.setSizePolicy(sizePolicy)
        self.tint_slider.setMinimumSize(QtCore.QSize(0, 10))
        self.tint_slider.setStyleSheet("QSlider::groove:horizontal {\n"
                                       "    border: 0px solid #626262;\n"
                                       "    height: 4px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 200, 0, 255), stop:1 rgba(200, 0, 200, 255));\n"
                                       "    margin: 0px 0;\n"
                                       "}\n"
                                       "\n"
                                       "QSlider::handle:horizontal {\n"
                                       "    background: rgb(186, 186, 186);\n"
                                       "    width: 8px;\n"
                                       "    margin: -2px 0;\n"
                                       "    border-radius: 3.9px; /* измените это значение на ваш выбор */\n"
                                       "}")
        self.tint_slider.setMinimum(-100)
        self.tint_slider.setMaximum(100)
        self.tint_slider.setProperty("value", 0)
        self.tint_slider.setSliderPosition(0)
        self.tint_slider.setOrientation(QtCore.Qt.Horizontal)
        self.tint_slider.setObjectName("tint_slider")
        self.gridLayout_4.addWidget(self.tint_slider, 4, 0, 1, 2)
        self.temperature_label = QtWidgets.QLabel(self.wb_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temperature_label.sizePolicy().hasHeightForWidth())
        self.temperature_label.setSizePolicy(sizePolicy)
        self.temperature_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.temperature_label.setFont(font)
        self.temperature_label.setStyleSheet("color: rgba(200, 200, 200, 255);")
        self.temperature_label.setObjectName("temperature_label")
        self.gridLayout_4.addWidget(self.temperature_label, 0, 0, 1, 1)
        self.tint_label = QtWidgets.QLabel(self.wb_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tint_label.sizePolicy().hasHeightForWidth())
        self.tint_label.setSizePolicy(sizePolicy)
        self.tint_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tint_label.setFont(font)
        self.tint_label.setStyleSheet("color: rgba(200, 200, 200, 255);")
        self.tint_label.setObjectName("tint_label")
        self.gridLayout_4.addWidget(self.tint_label, 3, 0, 1, 1)
        self.tint_parm = QtWidgets.QLineEdit(self.wb_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tint_parm.sizePolicy().hasHeightForWidth())
        self.tint_parm.setSizePolicy(sizePolicy)
        self.tint_parm.setMinimumSize(QtCore.QSize(0, 0))
        self.tint_parm.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.tint_parm.setFont(font)
        self.tint_parm.setMouseTracking(False)
        self.tint_parm.setToolTipDuration(-1)
        self.tint_parm.setStyleSheet("QLineEdit {\n"
                                     "    border: 0px solid gray;\n"
                                     "    border-radius: 4px;\n"
                                     "    padding: 0 8px;\n"
                                     "    color: rgb(200, 200, 200);\n"
                                     "    background: rgb(71, 71, 71); \n"
                                     "    selection-background-color: darkgray;\n"
                                     "}")
        self.tint_parm.setCursorPosition(0)
        self.tint_parm.setObjectName("tint_parm")

        # Temperature, Tint - label, parm, slider end };
        self.gridLayout_4.addWidget(self.tint_parm, 3, 1, 1, 1)

        # WB frame end };
        self.gridLayout_8.addWidget(self.wb_frame, 1, 0, 1, 1)

        # WB frame start {
        self.bc_frame = QtWidgets.QFrame(self.primerise_frame)
        self.bc_frame.setStyleSheet("")
        self.bc_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bc_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bc_frame.setObjectName("bc_frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.bc_frame)
        self.gridLayout_5.setContentsMargins(6, 1, 6, 1)
        self.gridLayout_5.setSpacing(1)
        self.gridLayout_5.setObjectName("gridLayout_5")

        # Exp, Cont, White, Black, Sharp, Sat - label, parm, slider start {
        self.sharpness_slider = QtWidgets.QSlider(self.bc_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sharpness_slider.sizePolicy().hasHeightForWidth())
        self.sharpness_slider.setSizePolicy(sizePolicy)
        self.sharpness_slider.setMinimumSize(QtCore.QSize(0, 10))
        self.sharpness_slider.setStyleSheet("QSlider::groove:horizontal {\n"
                                            "    border: 0px solid #626262;\n"
                                            "    height: 4px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
                                            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, \n"
                                            "stop:0 rgba(98, 98, 98, 255),\n"
                                            "stop:0.06 rgba(98, 98, 98, 255),\n"
                                            "stop:0.10 rgba(102, 102, 102, 255), \n"
                                            "stop:0.14 rgba(98, 98, 98, 255),\n"
                                            "stop:0.18 rgba(105, 105, 105, 255), \n"
                                            "stop:0.22 rgba(98, 98, 98, 255), \n"
                                            "stop:0.26 rgba(110, 110, 110, 255), \n"
                                            "stop:0.30 rgba(98, 98, 98, 255), \n"
                                            "stop:0.34 rgba(120, 120, 120, 255), \n"
                                            "stop:0.38 rgba(98, 98, 98, 255), \n"
                                            "stop:0.42 rgba(130, 130, 130, 255),\n"
                                            "stop:0.46 rgba(98, 98, 98, 255), \n"
                                            "stop:0.50 rgba(140, 140, 140, 255), \n"
                                            "stop:0.54 rgba(98, 98, 98, 255), \n"
                                            "stop:0.58 rgba(150, 150, 150, 255), \n"
                                            "stop:0.62 rgba(98, 98, 98, 255), \n"
                                            "stop:0.66 rgba(160, 160, 160, 255), \n"
                                            "stop:0.70 rgba(98, 98, 98, 255), \n"
                                            "stop:0.74 rgba(170, 170, 170, 255), \n"
                                            "stop:0.78 rgba(98, 98, 98, 255), \n"
                                            "stop:0.82 rgba(180, 180, 180, 255), \n"
                                            "stop:0.86 rgba(98, 98, 98, 255), \n"
                                            "stop:0.90 rgba(190, 190, 190, 255), \n"
                                            "stop:0.94 rgba(98, 98, 98, 255), \n"
                                            "stop:1 rgba(200, 200, 200, 255));\n"
                                            "    margin: 0px 0;\n"
                                            "}\n"
                                            "\n"
                                            "QSlider::handle:horizontal {\n"
                                            "    background: rgb(186, 186, 186);\n"
                                            "    width: 8px;\n"
                                            "    margin: -2px 0;\n"
                                            "    border-radius: 3.9px; /* измените это значение на ваш выбор */\n"
                                            "}")
        self.sharpness_slider.setMinimum(-100)
        self.sharpness_slider.setMaximum(100)
        self.sharpness_slider.setProperty("value", 0)
        self.sharpness_slider.setSliderPosition(0)
        self.sharpness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.sharpness_slider.setObjectName("sharpness_slider")
        self.gridLayout_5.addWidget(self.sharpness_slider, 10, 0, 1, 2)
        self.saturation_label = QtWidgets.QLabel(self.bc_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.saturation_label.setFont(font)
        self.saturation_label.setStyleSheet("color: rgba(200, 200, 200, 255);")
        self.saturation_label.setObjectName("saturation_label")
        self.gridLayout_5.addWidget(self.saturation_label, 11, 0, 1, 1)
        self.expo_parm = QtWidgets.QLineEdit(self.bc_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expo_parm.sizePolicy().hasHeightForWidth())
        self.expo_parm.setSizePolicy(sizePolicy)
        self.expo_parm.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.expo_parm.setFont(font)
        self.expo_parm.setToolTipDuration(-1)
        self.expo_parm.setStyleSheet("QLineEdit {\n"
                                     "    border: 0px solid gray;\n"
                                     "    border-radius: 4px;\n"
                                     "    padding: 0 8px;\n"
                                     "    color: rgb(200, 200, 200);\n"
                                     "    background: rgb(71, 71, 71); \n"
                                     "    selection-background-color: darkgray;\n"
                                     "}")
        self.expo_parm.setCursorPosition(0)
        self.expo_parm.setObjectName("expo_parm")
        self.gridLayout_5.addWidget(self.expo_parm, 1, 1, 1, 1)
        self.exposure_label = QtWidgets.QLabel(self.bc_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.exposure_label.setFont(font)
        self.exposure_label.setStyleSheet("color: rgba(200, 200, 200, 255);")
        self.exposure_label.setObjectName("exposure_label")
        self.gridLayout_5.addWidget(self.exposure_label, 1, 0, 1, 1)
        self.white_parm = QtWidgets.QLineEdit(self.bc_frame)
        self.white_parm.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.white_parm.setFont(font)
        self.white_parm.setToolTipDuration(-1)
        self.white_parm.setStyleSheet("QLineEdit {\n"
                                      "    border: 0px solid gray;\n"
                                      "    border-radius: 4px;\n"
                                      "    padding: 0 8px;\n"
                                      "    color: rgb(200, 200, 200);\n"
                                      "    background: rgb(71, 71, 71); \n"
                                      "    selection-background-color: darkgray;\n"
                                      "}")
        self.white_parm.setCursorPosition(0)
        self.white_parm.setObjectName("white_parm")
        self.gridLayout_5.addWidget(self.white_parm, 5, 1, 1, 1)
        self.sharpness_label = QtWidgets.QLabel(self.bc_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.sharpness_label.setFont(font)
        self.sharpness_label.setStyleSheet("color: rgba(200, 200, 200, 255);")
        self.sharpness_label.setObjectName("sharpness_label")
        self.gridLayout_5.addWidget(self.sharpness_label, 9, 0, 1, 1)
        self.black_parm = QtWidgets.QLineEdit(self.bc_frame)
        self.black_parm.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.black_parm.setFont(font)
        self.black_parm.setMouseTracking(False)
        self.black_parm.setToolTipDuration(-1)
        self.black_parm.setStyleSheet("QLineEdit {\n"
                                      "    border: 0px solid gray;\n"
                                      "    border-radius: 4px;\n"
                                      "    padding: 0 8px;\n"
                                      "    color: rgb(200, 200, 200);\n"
                                      "    background: rgb(71, 71, 71); \n"
                                      "    selection-background-color: darkgray;\n"
                                      "}")
        self.black_parm.setCursorPosition(0)
        self.black_parm.setObjectName("black_parm")
        self.gridLayout_5.addWidget(self.black_parm, 7, 1, 1, 1)
        self.cont_parm = QtWidgets.QLineEdit(self.bc_frame)
        self.cont_parm.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.cont_parm.setFont(font)
        self.cont_parm.setMouseTracking(False)
        self.cont_parm.setToolTipDuration(-1)
        self.cont_parm.setStyleSheet("QLineEdit {\n"
                                     "    border: 0px solid gray;\n"
                                     "    border-radius: 4px;\n"
                                     "    padding: 0 8px;\n"
                                     "    color: rgb(200, 200, 200);\n"
                                     "    background: rgb(71, 71, 71); \n"
                                     "    selection-background-color: darkgray;\n"
                                     "}")
        self.cont_parm.setCursorPosition(0)
        self.cont_parm.setObjectName("cont_parm")
        self.gridLayout_5.addWidget(self.cont_parm, 3, 1, 1, 1)
        self.white_label = QtWidgets.QLabel(self.bc_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.white_label.setFont(font)
        self.white_label.setStyleSheet("color: rgba(200, 200, 200, 255);")
        self.white_label.setObjectName("white_label")
        self.gridLayout_5.addWidget(self.white_label, 5, 0, 1, 1)
        self.black_label = QtWidgets.QLabel(self.bc_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.black_label.setFont(font)
        self.black_label.setStyleSheet("color: rgba(200, 200, 200, 255);")
        self.black_label.setObjectName("black_label")
        self.gridLayout_5.addWidget(self.black_label, 7, 0, 1, 1)
        self.sharp_parm = QtWidgets.QLineEdit(self.bc_frame)
        self.sharp_parm.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.sharp_parm.setFont(font)
        self.sharp_parm.setToolTipDuration(-1)
        self.sharp_parm.setStyleSheet("QLineEdit {\n"
                                      "    border: 0px solid gray;\n"
                                      "    border-radius: 4px;\n"
                                      "    padding: 0 8px;\n"
                                      "    color: rgb(200, 200, 200);\n"
                                      "    background: rgb(71, 71, 71); \n"
                                      "    selection-background-color: darkgray;\n"
                                      "}")
        self.sharp_parm.setCursorPosition(0)
        self.sharp_parm.setObjectName("sharp_parm")
        self.gridLayout_5.addWidget(self.sharp_parm, 9, 1, 1, 1)
        self.sat_parm = QtWidgets.QLineEdit(self.bc_frame)
        self.sat_parm.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.sat_parm.setFont(font)
        self.sat_parm.setMouseTracking(False)
        self.sat_parm.setToolTipDuration(-1)
        self.sat_parm.setStyleSheet("QLineEdit {\n"
                                    "    border: 0px solid gray;\n"
                                    "    border-radius: 4px;\n"
                                    "    padding: 0 8px;\n"
                                    "    color: rgb(200, 200, 200);\n"
                                    "    background: rgb(71, 71, 71); \n"
                                    "    selection-background-color: darkgray;\n"
                                    "}")
        self.sat_parm.setCursorPosition(0)
        self.sat_parm.setObjectName("sat_parm")
        self.gridLayout_5.addWidget(self.sat_parm, 11, 1, 1, 1)
        self.stauration_slider = QtWidgets.QSlider(self.bc_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stauration_slider.sizePolicy().hasHeightForWidth())
        self.stauration_slider.setSizePolicy(sizePolicy)
        self.stauration_slider.setMinimumSize(QtCore.QSize(0, 10))
        self.stauration_slider.setStyleSheet("QSlider::groove:horizontal {\n"
                                             "    border: 0px solid #626262;\n"
                                             "    height: 4px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
                                             "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, \n"
                                             "stop:0 rgba(113, 108, 115, 255),\n"
                                             "stop:0.2 rgba(105,110, 119, 255),\n"
                                             "stop:0.3 rgba(101, 116, 118, 255),\n"
                                             "stop:0.5 rgba(128, 143, 98, 255),\n"
                                             "stop:0.7 rgba(210, 186, 103, 255),\n"
                                             "stop:0.9 rgba(205, 125, 86, 255), \n"
                                             "stop:1 rgba(196, 69, 69, 255));\n"
                                             "    margin: 0px 0;\n"
                                             "}\n"
                                             "\n"
                                             "QSlider::handle:horizontal {\n"
                                             "    background: rgb(186, 186, 186);\n"
                                             "    width: 8px;\n"
                                             "    margin: -2px 0;\n"
                                             "    border-radius: 3.9px; /* измените это значение на ваш выбор */\n"
                                             "}")
        self.stauration_slider.setMinimum(-100)
        self.stauration_slider.setMaximum(100)
        self.stauration_slider.setProperty("value", 0)
        self.stauration_slider.setSliderPosition(0)
        self.stauration_slider.setOrientation(QtCore.Qt.Horizontal)
        self.stauration_slider.setObjectName("stauration_slider")
        self.gridLayout_5.addWidget(self.stauration_slider, 12, 0, 1, 2)
        self.black_slider = QtWidgets.QSlider(self.bc_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.black_slider.sizePolicy().hasHeightForWidth())
        self.black_slider.setSizePolicy(sizePolicy)
        self.black_slider.setMinimumSize(QtCore.QSize(0, 10))
        self.black_slider.setStyleSheet("QSlider::groove:horizontal {\n"
                                        "    border: 0px solid #626262;\n"
                                        "    height: 4px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 98, 98, 255), stop:0.465909 rgba(118, 118, 118, 255), stop:1 rgba(200, 200, 200, 255));\n"
                                        "    margin: 0px 0;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::handle:horizontal {\n"
                                        "    background: rgb(186, 186, 186);\n"
                                        "    width: 8px;\n"
                                        "    margin: -2px 0;\n"
                                        "    border-radius: 3.9px; /* измените это значение на ваш выбор */\n"
                                        "}")
        self.black_slider.setMinimum(-100)
        self.black_slider.setMaximum(100)
        self.black_slider.setProperty("value", 0)
        self.black_slider.setSliderPosition(0)
        self.black_slider.setOrientation(QtCore.Qt.Horizontal)
        self.black_slider.setObjectName("black_slider")
        self.gridLayout_5.addWidget(self.black_slider, 8, 0, 1, 2)
        self.white_slider = QtWidgets.QSlider(self.bc_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.white_slider.sizePolicy().hasHeightForWidth())
        self.white_slider.setSizePolicy(sizePolicy)
        self.white_slider.setMinimumSize(QtCore.QSize(0, 10))
        self.white_slider.setStyleSheet("QSlider::groove:horizontal {\n"
                                        "    border: 0px solid #626262;\n"
                                        "    height: 4px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 98, 98, 255), stop:0.465909 rgba(118, 118, 118, 255), stop:1 rgba(200, 200, 200, 255));\n"
                                        "    margin: 0px 0;\n"
                                        "}\n"
                                        "\n"
                                        "QSlider::handle:horizontal {\n"
                                        "    background: rgb(186, 186, 186);\n"
                                        "    width: 8px;\n"
                                        "    margin: -2px 0;\n"
                                        "    border-radius: 3.9px; /* измените это значение на ваш выбор */\n"
                                        "}")
        self.white_slider.setMinimum(-100)
        self.white_slider.setMaximum(100)
        self.white_slider.setProperty("value", 0)
        self.white_slider.setSliderPosition(0)
        self.white_slider.setOrientation(QtCore.Qt.Horizontal)
        self.white_slider.setObjectName("white_slider")
        self.gridLayout_5.addWidget(self.white_slider, 6, 0, 1, 2)
        self.contrast_slider = QtWidgets.QSlider(self.bc_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contrast_slider.sizePolicy().hasHeightForWidth())
        self.contrast_slider.setSizePolicy(sizePolicy)
        self.contrast_slider.setMinimumSize(QtCore.QSize(0, 10))
        self.contrast_slider.setStyleSheet("QSlider::groove:horizontal {\n"
                                           "    border: 0px solid #626262;\n"
                                           "    height: 4px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 98, 98, 255), stop:0.465909 rgba(118, 118, 118, 255), stop:1 rgba(200, 200, 200, 255));\n"
                                           "    margin: 0px 0;\n"
                                           "}\n"
                                           "\n"
                                           "QSlider::handle:horizontal {\n"
                                           "    background: rgb(186, 186, 186);\n"
                                           "    width: 8px;\n"
                                           "    margin: -2px 0;\n"
                                           "    border-radius: 3.9px; /* измените это значение на ваш выбор */\n"
                                           "}")
        self.contrast_slider.setMinimum(-100)
        self.contrast_slider.setMaximum(100)
        self.contrast_slider.setProperty("value", 0)
        self.contrast_slider.setSliderPosition(0)
        self.contrast_slider.setOrientation(QtCore.Qt.Horizontal)
        self.contrast_slider.setObjectName("contrast_slider")
        self.gridLayout_5.addWidget(self.contrast_slider, 4, 0, 1, 2)
        self.contrast_label = QtWidgets.QLabel(self.bc_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.contrast_label.setFont(font)
        self.contrast_label.setStyleSheet("color: rgba(200, 200, 200, 255);")
        self.contrast_label.setObjectName("contrast_label")
        self.gridLayout_5.addWidget(self.contrast_label, 3, 0, 1, 1)
        self.exposure_slider = QtWidgets.QSlider(self.bc_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exposure_slider.sizePolicy().hasHeightForWidth())
        self.exposure_slider.setSizePolicy(sizePolicy)
        self.exposure_slider.setMinimumSize(QtCore.QSize(0, 10))
        self.exposure_slider.setStyleSheet("QSlider::groove:horizontal {\n"
                                           "    border: 0px solid #626262;\n"
                                           "    height: 4px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(98, 98, 98, 255), stop:0.465909 rgba(118, 118, 118, 255), stop:1 rgba(200, 200, 200, 255));\n"
                                           "    margin: 0px 0;\n"
                                           "}\n"
                                           "\n"
                                           "QSlider::handle:horizontal {\n"
                                           "    background: rgb(186, 186, 186);\n"
                                           "    width: 8px;\n"
                                           "    margin: -2px 0;\n"
                                           "    border-radius: 3.9px; /* измените это значение на ваш выбор */\n"
                                           "}")
        self.exposure_slider.setMinimum(-100)
        self.exposure_slider.setMaximum(100)
        self.exposure_slider.setProperty("value", 0)
        self.exposure_slider.setSliderPosition(0)
        self.exposure_slider.setOrientation(QtCore.Qt.Horizontal)
        self.exposure_slider.setObjectName("exposure_slider")

        # Exp, Cont, White, Black, Sharp, Sat - label, parm, slider end };
        self.gridLayout_5.addWidget(self.exposure_slider, 2, 0, 1, 2)

        # BC frame end };
        self.gridLayout_8.addWidget(self.bc_frame, 4, 0, 1, 1)

        # OS frame start {
        self.os_frame = QtWidgets.QFrame(self.primerise_frame)
        self.os_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.os_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.os_frame.setObjectName("os_frame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.os_frame)
        self.gridLayout_7.setObjectName("gridLayout_7")

        # Open start {
        self.open_button = QtWidgets.QPushButton(self.os_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_button.sizePolicy().hasHeightForWidth())
        self.open_button.setSizePolicy(sizePolicy)
        self.open_button.setMinimumSize(QtCore.QSize(64, 24))
        self.open_button.setMaximumSize(QtCore.QSize(86, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.open_button.setFont(font)
        self.open_button.setToolTipDuration(-1)
        self.open_button.setStyleSheet("QPushButton {\n"
                                       "    border: 2px solid rgb(200, 200, 200);\n"
                                       "    color: rgb(200, 200, 200);\n"
                                       "    border-radius: 12px;\n"
                                       "    min-width: 60px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    border: 2px solid  rgb(235, 235, 235);\n"
                                       "    color: rgb(235, 235, 235);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    border: 2px solid rgb(235, 235, 235);\n"
                                       "    color: rgb(20, 20, 20);\n"
                                       "    background-color:  rgb(235, 235, 235);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:flat {\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:default {\n"
                                       "    border-color: navy; /* make the default button prominent */\n"
                                       "}")
        self.open_button.setObjectName("open_button")

        # Open end };
        self.gridLayout_7.addWidget(self.open_button, 0, 0, 1, 1)

        # Save start {
        self.save_button = QtWidgets.QPushButton(self.os_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)
        self.save_button.setMinimumSize(QtCore.QSize(60, 24))
        self.save_button.setMaximumSize(QtCore.QSize(86, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.save_button.setFont(font)
        self.save_button.setToolTipDuration(-1)
        self.save_button.setStyleSheet("QPushButton {\n"
                                       "    border: 0px solid #c8c8c8;\n"
                                       "    color: rgb(200, 200, 200);\n"
                                       "    border-radius: 12.49px;\n"
                                       "    min-width: 60px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    border: 2px solid rgb(235, 235, 235);\n"
                                       "    color: rgb(20, 20, 20);\n"
                                       "    background-color:  rgb(235, 235, 235);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    border: 2px solid rgb(235, 235, 235);\n"
                                       "    color: rgb(235, 235, 235);\n"
                                       "    background-color:  none;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:flat {\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:default {\n"
                                       "    border-color: navy; /* make the default button prominent */\n"
                                       "}")
        self.save_button.setObjectName("save_button")

        # Save end };
        self.gridLayout_7.addWidget(self.save_button, 0, 1, 1, 1)

        # OS frame end };
        self.gridLayout_8.addWidget(self.os_frame, 10, 0, 1, 1)

        # PF label start {
        self.pf_label = QtWidgets.QLabel(self.primerise_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pf_label.sizePolicy().hasHeightForWidth())
        self.pf_label.setSizePolicy(sizePolicy)
        self.pf_label.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pf_label.setFont(font)
        self.pf_label.setStyleSheet("color: rgba(235, 235, 235, 255);")
        self.pf_label.setObjectName("pf_label")

        # PF label end };
        self.gridLayout_8.addWidget(self.pf_label, 6, 0, 1, 1)

        # OS line start {
        self.os_line = QtWidgets.QFrame(self.primerise_frame)
        self.os_line.setStyleSheet("background-color: rgb(71, 71, 71);\n"
                                   "\n"
                                   "")
        self.os_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.os_line.setLineWidth(2)
        self.os_line.setMidLineWidth(-1)
        self.os_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.os_line.setObjectName("os_line")

        # OS line end };
        self.gridLayout_8.addWidget(self.os_line, 9, 0, 1, 1)

        # PF line start {
        self.pf_line = QtWidgets.QFrame(self.primerise_frame)
        self.pf_line.setStyleSheet("background-color: rgb(71, 71, 71);\n"
                                   "\n"
                                   "")
        self.pf_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pf_line.setLineWidth(2)
        self.pf_line.setMidLineWidth(-1)
        self.pf_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.pf_line.setObjectName("pf_line")

        # PF line end };
        self.gridLayout_8.addWidget(self.pf_line, 5, 0, 1, 1)

        # BC line start {
        self.bc_line = QtWidgets.QFrame(self.primerise_frame)
        self.bc_line.setStyleSheet("background-color: rgb(71, 71, 71);\n"
                                   "\n"
                                   "")
        self.bc_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bc_line.setLineWidth(2)
        self.bc_line.setMidLineWidth(-1)
        self.bc_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.bc_line.setObjectName("bc_line")

        # BC line end };
        self.gridLayout_8.addWidget(self.bc_line, 2, 0, 1, 1)

        # WB label start {
        self.wb_label = QtWidgets.QLabel(self.primerise_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wb_label.sizePolicy().hasHeightForWidth())
        self.wb_label.setSizePolicy(sizePolicy)
        self.wb_label.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.wb_label.setFont(font)
        self.wb_label.setStyleSheet("color: rgba(235, 235, 235, 255);")
        self.wb_label.setObjectName("wb_label")

        # WB label end };
        self.gridLayout_8.addWidget(self.wb_label, 0, 0, 1, 1)

        # BC label start {
        self.bc_label = QtWidgets.QLabel(self.primerise_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bc_label.sizePolicy().hasHeightForWidth())
        self.bc_label.setSizePolicy(sizePolicy)
        self.bc_label.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bc_label.setFont(font)
        self.bc_label.setStyleSheet("color: rgba(235, 235, 235, 255);")
        self.bc_label.setObjectName("bc_label")

        # BC label end };
        self.gridLayout_8.addWidget(self.bc_label, 3, 0, 1, 1)

        # Spacer start {
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # Spacer end };
        self.gridLayout_8.addItem(spacerItem, 8, 0, 1, 1)

        self.os_frame.raise_()
        self.pf_frame.raise_()
        self.bc_frame.raise_()
        self.pf_line.raise_()
        self.pf_label.raise_()
        self.os_line.raise_()
        self.wb_frame.raise_()
        self.wb_label.raise_()
        self.bc_line.raise_()
        self.bc_label.raise_()

        # Primerise frame end };
        self.gridLayout.addWidget(self.primerise_frame, 3, 0, 1, 1)

        # Diogram start {
        self.diogram_widget = QtWidgets.QWidget(self.generalColor_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diogram_widget.sizePolicy().hasHeightForWidth())
        self.diogram_widget.setSizePolicy(sizePolicy)
        self.diogram_widget.setMinimumSize(QtCore.QSize(260, 90))
        self.diogram_widget.setMaximumSize(QtCore.QSize(260, 90))
        self.diogram_widget.setObjectName("diogram_widget")

        # Diogram end };
        self.gridLayout.addWidget(self.diogram_widget, 1, 0, 1, 1)

        # General Color frame end };
        self.gridLayout_2.addWidget(self.generalColor_frame, 0, 2, 1, 1)

        # Workspace frame start {
        self.workSpace_frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workSpace_frame.sizePolicy().hasHeightForWidth())
        self.workSpace_frame.setSizePolicy(sizePolicy)
        self.workSpace_frame.setMinimumSize(QtCore.QSize(1134, 0))
        self.workSpace_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.workSpace_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.workSpace_frame.setObjectName("workSpace_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.workSpace_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")

        # D&D label start {
        self.dragDrop_label = QtWidgets.QLabel(self.workSpace_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dragDrop_label.setFont(font)
        self.dragDrop_label.setAcceptDrops(True)
        self.dragDrop_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dragDrop_label.setStyleSheet("QLabel {\n"
                                          "    color:  rgb(64, 64, 64);\n"
                                          "    border: 2px dashed solid rgb(50, 50, 50);\n"
                                          "    border-radius: 8px; \n"
                                          "}\n"
                                          "")
        self.dragDrop_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dragDrop_label.setObjectName("dragDrop_label")

        # D&D label end };
        self.gridLayout_3.addWidget(self.dragDrop_label, 0, 0, 1, 1)

        # Workspace frame end };
        self.gridLayout_2.addWidget(self.workSpace_frame, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())