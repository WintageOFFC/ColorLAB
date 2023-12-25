import cv2
import sys
from PIL import Image
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QIcon


class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        font = self.font()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)
        self.setAcceptDrops(True)
        self.setLayoutDirection(Qt.LeftToRight)
        self.setStyleSheet("QLabel {\n"
                           "    color:  rgb(64, 64, 64);\n"
                           "    border: 2px dashed solid rgb(50, 50, 50);\n"
                           "    border-radius: 8px; \n"
                           "}\n"
                           "")
        self.setAlignment(Qt.AlignCenter)
        self.setObjectName("dragDrop_label")

        # Инициализируем поля
        self.image_array = None
        self.image_array_full = None

        self.temperature = 0
        self.tint = 0

        self.exposure = 0
        self.contrast = 0
        self.white = 0
        self.black = 0
        self.sharpness = 0
        self.saturation = 0

        self.blur = 0
        self.bloom = 0
        self.grain = 0
        self.vignette = 0

    def open_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Открыть изображение", "",
                                                   "Images (*.png *.jpg *.bmp *.tif *.tiff *.jpeg);;All Files (*)",
                                                   options=options)

        if file_name:
            self.load_image(file_name)

    def image_procces(self, image_path):
        image = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGBA)
        self.image_array_full = image

        aspect_ratio = image.shape[1] / image.shape[0]
        if image.shape[1] * image.shape[0] > 490_000 or (image.shape[1] > 700 or image.shape[0] > 700):
            # Масштаб с учетом высоты пикселей
            if aspect_ratio <= 1.54:
                aspect_ratio = image.shape[1] / image.shape[0]
                new_height = 700
                new_width = int(new_height * aspect_ratio)
                image = cv2.resize(image, (new_width, new_height))
            else:
                aspect_ratio = image.shape[0] / image.shape[1]
                new_width = 1080
                new_height = int(new_width * aspect_ratio)
                image = cv2.resize(image, (new_width, new_height))

        self.image_array = image
        self.update_image()

    def dragEnterEvent(self, event):
        mime_data = event.mimeData()

        # перетаскиваемые данные содержат изображение
        if mime_data.hasUrls() and len(mime_data.urls()) == 1:
            url = mime_data.urls()[0]
            if url.isLocalFile():
                event.acceptProposedAction()

    def dropEvent(self, event):
        image_path = event.mimeData().urls()[0].toLocalFile()
        try:
            self.image_procces(image_path)
        except Exception as e:
            self.show_error_message(f"The request cannot be executed, this is an incorrect file type.", 0)

    def load_image(self, image_path):
        try:
            self.image_procces(image_path)
        except Exception as e:
            self.show_error_message(f"Destructive failure, this is an incorrect file type.", 1)
            self.open_image()

    def save_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить изображение", "",
                                                   "Images (*.png *.xpm *.jpg *.bmp);;All Files (*)", options=options)
        if file_name:
            if self.image_array_full is not None:
                image_array = self.correction_applay(self.image_array_full)
                image_pil = Image.fromarray(image_array, 'RGBA')
                image_pil.save(file_name, 'PNG')
            else:
                self.show_error_message("The working space of the application does \nnot contain an image.", 1)

    def show_error_message(self, message, qicon):
        icon = [QMessageBox.Critical, QMessageBox.Warning]
        error_box = QMessageBox(self)

        style_sheet = """
                QLabel {
                    color: rgb(0, 0, 0);
                    background-color: white;
                    border: none;
                }

                QMessageBox {
                    background-color: white;
                    color: red;
                }
                QMessageBox QPushButton {
                    width: 86px;
                    height: 18px;
                    background-color: rgb(225, 225, 225);
                    color: black;
                    border: 2px solid rgb(0, 120, 215);
                }
                QMessageBox QPushButton:hover {
                    width: 86px;
                    height: 18px;
                    background-color: rgb(229, 241, 251);
                    color: black;
                    border: 1px solid rgb(0, 120, 215);
                }
                QMessageBox QPushButton:pressed {
                    width: 86px;
                    height: 18px;
                    background-color: rgb(219, 231, 241);
                    color: black;
                    border: 1px solid rgb(0, 120, 215);
                }
            """
        error_box.setStyleSheet(style_sheet)
        error_box.setIcon(icon[qicon])
        error_box.setWindowTitle("ColorLAB (Utility)")
        error_box.setText(message)
        error_box.setWindowIcon(QIcon("gui-resources\\colorlab1111.png"))
        error_box.setStandardButtons(QMessageBox.Ok)
        error_box.exec_()

    def correction_applay(self, image_array):
        # Копируем массив изображения
        corrected_image_array = image_array.copy()

        # Применяем коррекцию параметров
        corrected_image_array = self.apply_temperature(corrected_image_array)
        corrected_image_array = self.apply_tint(corrected_image_array)

        corrected_image_array = self.apply_exposure(corrected_image_array)
        corrected_image_array = self.apply_contrast(corrected_image_array)
        corrected_image_array = self.apply_white(corrected_image_array)
        corrected_image_array = self.apply_black(corrected_image_array)
        corrected_image_array = self.apply_sharpness(corrected_image_array)
        corrected_image_array = self.apply_saturation(corrected_image_array)

        corrected_image_array = self.apply_blur(corrected_image_array)
        corrected_image_array = self.apply_bloom(corrected_image_array)
        corrected_image_array = self.apply_grain(corrected_image_array)
        corrected_image_array = self.apply_vignette(corrected_image_array)

        return corrected_image_array

    def update_image(self):
        if self.image_array is not None:
            corrected_image_array = self.correction_applay(self.image_array)

            # массив в Qt и альфой
            height, width, channel = corrected_image_array.shape
            bytes_per_line = 4 * width  # 4 канала для RGBA
            q_image = QImage(corrected_image_array.data, width, height, bytes_per_line, QImage.Format_RGBA8888)

            self.setPixmap(QPixmap.fromImage(q_image))

    # WB
    def apply_temperature(self, image_array):
        if self.temperature != 0:
            b, g, r, a = cv2.split(image_array)
            image_rgb = cv2.merge((r, g, b))
            if self.temperature > 0:
                kelvin_matrix = np.array([[1, -0.1 * (self.temperature/20), 0], [0, 1, 0], [0, 0.1 * (self.temperature/10), 1]])
            else:
                kelvin_matrix = np.array([[1, -0.2 * (self.temperature/15), 0], [0, 1, 0], [0, 0, 1]])
            image_rgb = cv2.transform(image_rgb, kelvin_matrix)
            b, g, r = cv2.split(image_rgb)
            return cv2.merge((r, g, b, a))
        else:
            return image_array

    def apply_tint(self, image_array):
        if self.tint != 0:
            b, g, r, a = cv2.split(image_array)
            image_rgb = cv2.merge((r, g, b))
            if self.tint > 0:
                tint_matrix = np.array([[1, 0, 0], [0, 1, -0.2 * (self.tint/50)], [0.2 * (self.tint/50), 0, 1]])
            else:
                tint_matrix = np.array([[1, 0, 0], [0, 1, -0.2 * (self.tint / 50)], [0, 0, 1]])
            image_rgb = cv2.transform(image_rgb, tint_matrix)
            b, g, r = cv2.split(image_rgb)
            return cv2.merge((r, g, b, a))
        else:
            return image_array

    # BC
    def apply_exposure(self, image_array):
        if self.exposure != 0:
            b, g, r, a = cv2.split(image_array)
            image_rgb = cv2.merge((r, g, b))
            image_rgb = cv2.convertScaleAbs(image_rgb, alpha=(1 + self.exposure / 100), beta=0)
            b, g, r = cv2.split(image_rgb)
            return cv2.merge((r, g, b, a))
        else:
            return image_array

    def apply_contrast(self, image_array):
        if self.contrast != 0:
            b, g, r, a = cv2.split(image_array)

            lut_in = [0, 32, 64, 96, 128, 160, 192, 224, 255]
            lut_out = [0, 32-self.contrast/6.25, 64-self.contrast/12.5, 96-self.contrast/25, 128,
                       160+self.contrast/25, 192+self.contrast/12.5, 224+self.contrast/6.25, 255]
            lut_8u = np.interp(np.arange(0, 256), lut_in, lut_out).astype(np.uint8)

            r = cv2.LUT(r, lut_8u)
            g = cv2.LUT(g, lut_8u)
            b = cv2.LUT(b, lut_8u)

            return cv2.merge((b, g, r, a))
        else:
            return image_array

    def apply_white(self, image_array):
        if self.white != 0:
            b, g, r, a = cv2.split(image_array)

            lut_in = [0, 51, 102, 153, 204, 255]
            lut_out = [0, 51, 102+(self.white/10), 153+(self.white/5), 204+(self.white/4), 255]
            lut_8u = np.interp(np.arange(0, 256), lut_in, lut_out).astype(np.uint8)

            r = cv2.LUT(r, lut_8u)
            g = cv2.LUT(g, lut_8u)
            b = cv2.LUT(b, lut_8u)

            return cv2.merge((b, g, r, a))
        else:
            return image_array

    def apply_black(self, image_array):
        if self.black != 0:
            b, g, r, a = cv2.split(image_array)

            lut_in = [0, 51, 102, 153, 204, 255]
            lut_out = [0, 51 + (self.black / 10), 102 + (self.black / 15), 153 + (self.black / 25), 204, 255]
            lut_8u = np.interp(np.arange(0, 256), lut_in, lut_out).astype(np.uint8)

            r = cv2.LUT(r, lut_8u)
            g = cv2.LUT(g, lut_8u)
            b = cv2.LUT(b, lut_8u)

            return cv2.merge((b, g, r, a))
        else:
            return image_array

    def apply_sharpness(self, image_array):
        if self.sharpness != 0:
            blurred = cv2.GaussianBlur(image_array, (0, 0), 1)
            return cv2.addWeighted(image_array, 1 + self.sharpness / 100, blurred, -self.sharpness / 100, 0)
        else:
            return image_array

    def apply_saturation(self, image_array):
        if self.saturation != 0:
            b, g, r, a = cv2.split(image_array)
            image_hsv = cv2.cvtColor(cv2.merge((r, g, b)), cv2.COLOR_BGR2HSV)
            image_hsv[:, :, 1] = np.clip(image_hsv[:, :, 1] * (1 + self.saturation/100), 0, 255)
            b, g, r = cv2.split(cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR))
            return cv2.merge((r, g, b, a))
        else:
            return image_array

    # PF
    def apply_blur(self, image_array):
        if self.blur > 0:
            return cv2.GaussianBlur(image_array, (0, 0), self.blur/10)
        else:
            return image_array

    def apply_bloom(self, image_array):
        if self.bloom != 0:
            blurred = cv2.GaussianBlur(image_array, (0, 0), 8)
            result = cv2.addWeighted(image_array, 1 - self.bloom/200, blurred, self.bloom/50, 0)
            return result
        else:
            return image_array

    def apply_grain(self, image_array):
        if self.grain != 0:
            bgr_image = image_array[:, :, :3]
            alpha_channel = image_array[:, :, 3]

            gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
            noise = np.random.normal(0, self.grain/2, gray_image.shape)
            noise = cv2.GaussianBlur(noise, (0, 0), 0.5)
            noise = np.expand_dims(noise, axis=-1)
            noise = np.repeat(noise, 3, axis=-1)
            noisy_bgr_image = bgr_image + noise
            noisy_bgr_image = np.clip(noisy_bgr_image, 0, 255).astype(np.uint8)
            corrected_image_array = np.dstack((noisy_bgr_image, alpha_channel))
            return corrected_image_array
        else:
            return image_array

    def apply_vignette(self, image_array):
        if self.vignette != 0:
            rows, cols = image_array.shape[:2]

            X_resultant_kernel = cv2.getGaussianKernel(cols, 320)
            Y_resultant_kernel = cv2.getGaussianKernel(rows, 200)
            resultant_kernel = Y_resultant_kernel * X_resultant_kernel.T
            mask = 255 * resultant_kernel / np.linalg.norm(resultant_kernel)
            output = np.copy(image_array)
            for i in range(3):
                output[:, :, i] = output[:, :, i] * mask
            if self.vignette > 0:
                output = cv2.addWeighted(image_array, 1 + self.vignette / 100, output, -self.vignette / 100, 0)
            else:
                output = cv2.addWeighted(image_array, 1 + self.vignette / 100, output, -self.vignette / 60, 0)
            return output
        else:
            return image_array


class Ui_Form(object):
    def __init__(self, Form):
        super().__init__()

        self.setupUi(Form)

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
        self.horizontalLayout.setContentsMargins(20, 1, 1, 1)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Author_label start {
        self.author_label = QtWidgets.QLabel(self.rgb_frame)
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
        self.author_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.author_label.setFont(font)
        self.author_label.setStyleSheet("color: rgb(200, 200, 200);")
        self.author_label.setTextFormat(QtCore.Qt.AutoText)
        self.author_label.setScaledContents(False)
        self.author_label.setWordWrap(False)
        self.author_label.setObjectName("r_label")

        # Author_label end };
        self.horizontalLayout.addWidget(self.author_label)

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
        self.blur_parm.setMaximumSize(QtCore.QSize(44, 16777215))
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
        self.blur_parm.setText("0")
        self.blur_parm.editingFinished.connect(self.enter_update_blur)
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
        self.blur_slider.setValue(0)
        self.blur_slider.valueChanged.connect(self.update_blur)
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
        self.bloom_parm.setMaximumSize(QtCore.QSize(44, 16777215))
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
        self.bloom_parm.setText("0")
        self.bloom_parm.editingFinished.connect(self.enter_update_bloom)
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
        self.bloom_slider.setValue(0)
        self.bloom_slider.valueChanged.connect(self.update_bloom)
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
        self.grain_parm.setMaximumSize(QtCore.QSize(44, 16777215))
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
        self.grain_parm.setText("0")
        self.grain_parm.editingFinished.connect(self.enter_update_grain)
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
        self.grain_slider.setValue(0)
        self.grain_slider.valueChanged.connect(self.update_grain)
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
        self.vignette_parm.setMaximumSize(QtCore.QSize(44, 16777215))
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
        self.vignette_parm.setText("0")
        self.vignette_parm.editingFinished.connect(self.enter_update_vignette)
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
        self.vignette_slider.setValue(0)
        self.vignette_slider.valueChanged.connect(self.update_vignette)
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
        self.temperature_slider.setValue(0)
        self.temperature_slider.valueChanged.connect(self.update_temperature)
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
        self.temp_parm.setMaximumSize(QtCore.QSize(44, 16777215))
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
        self.temp_parm.setText("0")
        self.temp_parm.editingFinished.connect(self.enter_update_temperature)
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
        self.tint_slider.setValue(0)
        self.tint_slider.valueChanged.connect(self.update_tint)
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
        self.tint_parm.setMaximumSize(QtCore.QSize(44, 16777215))
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
        self.tint_parm.setText("0")
        self.tint_parm.editingFinished.connect(self.enter_update_tint)

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
        self.sharpness_slider.setValue(0)
        self.sharpness_slider.valueChanged.connect(self.update_sharpness)
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
        self.expo_parm.setMaximumSize(QtCore.QSize(44, 16777215))
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
        self.expo_parm.setText("0")
        self.expo_parm.editingFinished.connect(self.enter_update_exposure)
        self.gridLayout_5.addWidget(self.expo_parm, 1, 1, 1, 1)
        self.exposure_label = QtWidgets.QLabel(self.bc_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.exposure_label.setFont(font)
        self.exposure_label.setStyleSheet("color: rgba(200, 200, 200, 255);")
        self.exposure_label.setObjectName("exposure_label")
        self.gridLayout_5.addWidget(self.exposure_label, 1, 0, 1, 1)
        self.white_parm = QtWidgets.QLineEdit(self.bc_frame)
        self.white_parm.setMaximumSize(QtCore.QSize(44, 16777215))
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
        self.white_parm.setText("0")
        self.white_parm.editingFinished.connect(self.enter_update_white)
        self.gridLayout_5.addWidget(self.white_parm, 5, 1, 1, 1)
        self.sharpness_label = QtWidgets.QLabel(self.bc_frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.sharpness_label.setFont(font)
        self.sharpness_label.setStyleSheet("color: rgba(200, 200, 200, 255);")
        self.sharpness_label.setObjectName("sharpness_label")
        self.gridLayout_5.addWidget(self.sharpness_label, 9, 0, 1, 1)
        self.black_parm = QtWidgets.QLineEdit(self.bc_frame)
        self.black_parm.setMaximumSize(QtCore.QSize(44, 16777215))
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
        self.black_parm.setText("0")
        self.black_parm.editingFinished.connect(self.enter_update_black)
        self.gridLayout_5.addWidget(self.black_parm, 7, 1, 1, 1)
        self.cont_parm = QtWidgets.QLineEdit(self.bc_frame)
        self.cont_parm.setMaximumSize(QtCore.QSize(44, 16777215))
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
        self.cont_parm.setText("0")
        self.cont_parm.editingFinished.connect(self.enter_update_contrast)
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
        self.sharp_parm.setMaximumSize(QtCore.QSize(44, 16777215))
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
        self.sharp_parm.setText("0")
        self.sharp_parm.editingFinished.connect(self.enter_update_sharpness)
        self.gridLayout_5.addWidget(self.sharp_parm, 9, 1, 1, 1)
        self.sat_parm = QtWidgets.QLineEdit(self.bc_frame)
        self.sat_parm.setMaximumSize(QtCore.QSize(44, 16777215))
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
        self.sat_parm.setText("0")
        self.sat_parm.editingFinished.connect(self.enter_update_saturation)
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
        self.stauration_slider.setValue(0)
        self.stauration_slider.valueChanged.connect(self.update_saturation)
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
        self.black_slider.setValue(0)
        self.black_slider.valueChanged.connect(self.update_black)
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
        self.white_slider.setValue(0)
        self.white_slider.valueChanged.connect(self.update_white)
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
        self.contrast_slider.setValue(0)
        self.contrast_slider.valueChanged.connect(self.update_contrast)
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
        self.exposure_slider.setValue(0)
        self.exposure_slider.valueChanged.connect(self.update_exposure)
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
        self.open_button.clicked.connect(self.open_button_clicked)

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
        self.save_button.clicked.connect(self.save_button_clicked)

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
        self.diogram_label = QtWidgets.QLabel(self.generalColor_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diogram_label.sizePolicy().hasHeightForWidth())
        self.diogram_label.setSizePolicy(sizePolicy)
        self.diogram_label.setMinimumSize(QtCore.QSize(260, 90))
        self.diogram_label.setMaximumSize(QtCore.QSize(260, 90))
        self.diogram_label.setObjectName("diogram_label")

        # Set image to the QLabel
        pixmap = QtGui.QPixmap("gui-resources\\plane.png")  # Replace with the actual path to your image
        self.diogram_label.setPixmap(pixmap)

        # Diogram end };
        self.gridLayout.addWidget(self.diogram_label, 1, 0, 1, 1)

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
        self.dragDrop_label = ImageLabel()
        # D&D label end };
        self.gridLayout_3.addWidget(self.dragDrop_label, 0, 0, 1, 1)

        # Workspace frame end };
        self.gridLayout_2.addWidget(self.workSpace_frame, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowIcon(QIcon("gui-resources\\colorlab1111.png"))
        Form.setWindowTitle(_translate("Form", "ColorLAB (Utility)"))
        self.author_label.setText(_translate("Form", "ColorLAB (utility version 2.0.0) from Bykov I.I."))

        self.blur_label.setText(_translate("Form", "Blur"))
        self.bloom_label.setText(_translate("Form", "Bloom"))
        self.grain_label.setText(_translate("Form", "Grain"))
        self.vignette_label.setText(_translate("Form", "Vignette"))
        self.temperature_label.setText(_translate("Form", "Temperature"))
        self.tint_label.setText(_translate("Form", "Tint"))
        self.saturation_label.setText(_translate("Form", "Saturation"))
        self.exposure_label.setText(_translate("Form", "Exposure"))
        self.sharpness_label.setText(_translate("Form", "Sharpness"))
        self.white_label.setText(_translate("Form", "White"))
        self.black_label.setText(_translate("Form", "Black"))
        self.contrast_label.setText(_translate("Form", "Contrast"))
        self.open_button.setText(_translate("Form", "Open"))
        self.save_button.setText(_translate("Form", "Save as"))
        self.pf_label.setText(_translate("Form", "POST FX"))
        self.wb_label.setText(_translate("Form", "WHITE BALANCE"))
        self.bc_label.setText(_translate("Form", "BASIC CORRECTION"))
        self.dragDrop_label.setText(_translate("Form",
                                               "<html><head/><body><p><span style=\" font-size:xx-large;\">DRAG &amp; DROP</span><br/>(*.png *.jpeg, *.jpg, *.jpe, *.jp2, *.tiff, *.tif, *.bmp, *.dib, *.sr, *.ras)</p></body></html>"))

    def open_button_clicked(self):
        self.author_label.setText("Image opening process...")
        self.dragDrop_label.open_image()
        self.author_label.setText("ColorLAB (utility version 2.0.0) from Bykov I.I.")

    def save_button_clicked(self):
        self.author_label.setText("Image saving process...")
        self.dragDrop_label.save_image()
        self.author_label.setText("ColorLAB (utility version 2.0.0) from Bykov I.I.")

    # WB
    def update_temperature(self, value):
        self.dragDrop_label.temperature = value
        self.temp_parm.setText(str(value))
        self.dragDrop_label.update_image()
        pass

    def enter_update_temperature(self):
        try:
            value = int(self.temp_parm.text())
            self.dragDrop_label.temperature = value
            self.temperature_slider.setValue(value)
            self.dragDrop_label.update_image()
        except:
            self.dragDrop_label.temperature = 0
            self.temperature_slider.setValue(0)

    def update_tint(self, value):
        self.dragDrop_label.tint = value
        self.tint_parm.setText(str(value))
        self.dragDrop_label.update_image()
        pass

    def enter_update_tint(self):
        try:
            value = int(self.tint_parm.text())
            self.dragDrop_label.tint = value
            self.tint_slider.setValue(value)
            self.dragDrop_label.update_image()
        except:
            self.dragDrop_label.tint = 0
            self.tint_slider.setValue(0)

    # BC
    def update_exposure(self, value):
        self.dragDrop_label.exposure = value
        self.expo_parm.setText(str(value))
        self.dragDrop_label.update_image()
        pass

    def enter_update_exposure(self):
        try:
            value = int(self.expo_parm.text())
            self.dragDrop_label.exposure = value
            self.exposure_slider.setValue(value)
            self.dragDrop_label.update_image()
        except:
            self.dragDrop_label.exposure = 0
            self.exposure_slider.setValue(0)

    def update_contrast(self, value):
        self.dragDrop_label.contrast = value
        self.cont_parm.setText(str(value))
        self.dragDrop_label.update_image()
        pass

    def enter_update_contrast(self):
        try:
            value = int(self.cont_parm.text())
            self.dragDrop_label.contrast = value
            self.contrast_slider.setValue(value)
            self.dragDrop_label.update_image()
        except:
            self.dragDrop_label.contrast = 0
            self.contrast_slider.setValue(0)

    def update_white(self, value):
        self.dragDrop_label.white = value
        self.white_parm.setText(str(value))
        self.dragDrop_label.update_image()
        pass

    def enter_update_white(self):
        try:
            value = int(self.white_parm.text())
            self.dragDrop_label.white = value
            self.white_slider.setValue(value)
            self.dragDrop_label.update_image()
        except:
            self.dragDrop_label.white = 0
            self.white_slider.setValue(0)

    def update_black(self, value):
        self.dragDrop_label.black = value
        self.black_parm.setText(str(value))
        self.dragDrop_label.update_image()
        pass

    def enter_update_black(self):
        try:
            value = int(self.black_parm.text())
            self.dragDrop_label.black = value
            self.black_slider.setValue(value)
            self.dragDrop_label.update_image()
        except:
            self.dragDrop_label.black = 0
            self.black_slider.setValue(0)

    def update_sharpness(self, value):
        self.dragDrop_label.sharpness = value
        self.sharp_parm.setText(str(value))
        self.dragDrop_label.update_image()
        pass

    def enter_update_sharpness(self):
        try:
            value = int(self.sharp_parm.text())
            self.dragDrop_label.sharpness = value
            self.sharpness_slider.setValue(value)
            self.dragDrop_label.update_image()
        except:
            self.dragDrop_label.sharpness = 0
            self.sharpness_slider.setValue(0)

    def update_saturation(self, value):
        self.dragDrop_label.saturation = value
        self.sat_parm.setText(str(value))
        self.dragDrop_label.update_image()
        pass

    def enter_update_saturation(self):
        try:
            value = int(self.sat_parm.text())
            self.dragDrop_label.saturation = value
            self.stauration_slider.setValue(value)
            self.dragDrop_label.update_image()
        except:
            self.dragDrop_label.saturation = 0
            self.stauration_slider.setValue(0)

    # PF
    def update_blur(self, value):
        self.dragDrop_label.blur = value
        self.blur_parm.setText(str(value))
        self.dragDrop_label.update_image()
        pass

    def enter_update_blur(self):
        try:
            value = int(self.blur_parm.text())
            self.dragDrop_label.blur = value
            self.blur_slider.setValue(value)
            self.dragDrop_label.update_image()
        except:
            self.dragDrop_label.blur = 0
            self.blur_slider.setValue(0)

    def update_bloom(self, value):
        self.dragDrop_label.bloom = value
        self.bloom_parm.setText(str(value))
        self.dragDrop_label.update_image()
        pass

    def enter_update_bloom(self):
        try:
            value = int(self.bloom_parm.text())
            self.dragDrop_label.bloom = value
            self.bloom_slider.setValue(value)
            self.dragDrop_label.update_image()
        except:
            self.dragDrop_label.bloom = 0
            self.bloom_slider.setValue(0)

    def update_grain(self, value):
        self.dragDrop_label.grain = value
        self.grain_parm.setText(str(value))
        self.dragDrop_label.update_image()
        pass

    def enter_update_grain(self):
        try:
            value = int(self.grain_parm.text())
            self.dragDrop_label.grain = value
            self.grain_slider.setValue(value)
            self.dragDrop_label.update_image()
        except:
            self.dragDrop_label.grain = 0
            self.grain_slider.setValue(0)

    def update_vignette(self, value):
        self.dragDrop_label.vignette = value
        self.vignette_parm.setText(str(value))
        self.dragDrop_label.update_image()
        pass

    def enter_update_vignette(self):
        try:
            value = int(self.vignette_parm.text())
            self.dragDrop_label.vignette = value
            self.vignette_slider.setValue(value)
            self.dragDrop_label.update_image()
        except:
            self.dragDrop_label.vignette = 0
            self.vignette_slider.setValue(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form(Form)
    Form.show()
    sys.exit(app.exec_())
