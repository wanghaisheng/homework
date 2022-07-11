# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\shortVideo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1167, 886)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.group_box_upload = QtWidgets.QGroupBox(self.centralwidget)
        self.group_box_upload.setGeometry(QtCore.QRect(20, 670, 1131, 161))
        self.group_box_upload.setObjectName("group_box_upload")
        self.account_table = QtWidgets.QTableWidget(self.group_box_upload)
        self.account_table.setGeometry(QtCore.QRect(10, 20, 1071, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_table.sizePolicy().hasHeightForWidth())
        self.account_table.setSizePolicy(sizePolicy)
        self.account_table.setStyleSheet("color:rgb(0, 0, 0)")
        self.account_table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.account_table.setObjectName("account_table")
        self.account_table.setColumnCount(10)
        self.account_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.account_table.setHorizontalHeaderItem(9, item)
        self.account_table.horizontalHeader().setCascadingSectionResizes(False)
        self.account_table.horizontalHeader().setHighlightSections(False)
        self.account_table.horizontalHeader().setSortIndicatorShown(False)
        self.account_table.horizontalHeader().setStretchLastSection(True)
        self.add_account_btn = QtWidgets.QPushButton(self.group_box_upload)
        self.add_account_btn.setGeometry(QtCore.QRect(1080, 20, 31, 23))
        self.add_account_btn.setObjectName("add_account_btn")
        self.delete_account_btn = QtWidgets.QPushButton(self.group_box_upload)
        self.delete_account_btn.setGeometry(QtCore.QRect(1080, 50, 31, 23))
        self.delete_account_btn.setObjectName("delete_account_btn")
        self.group_box_download = QtWidgets.QGroupBox(self.centralwidget)
        self.group_box_download.setGeometry(QtCore.QRect(20, 110, 1131, 121))
        self.group_box_download.setMinimumSize(QtCore.QSize(0, 0))
        self.group_box_download.setSizeIncrement(QtCore.QSize(0, 0))
        self.group_box_download.setStyleSheet("border-color: rgb(255, 0, 0);")
        self.group_box_download.setObjectName("group_box_download")
        self.pick_web = QtWidgets.QComboBox(self.group_box_download)
        self.pick_web.setGeometry(QtCore.QRect(100, 30, 291, 31))
        self.pick_web.setObjectName("pick_web")
        self.pick_web.addItem("")
        self.pick_web.addItem("")
        self.input_home_url = QtWidgets.QLineEdit(self.group_box_download)
        self.input_home_url.setGeometry(QtCore.QRect(680, 30, 291, 31))
        self.input_home_url.setObjectName("input_home_url")
        self.label_web = QtWidgets.QLabel(self.group_box_download)
        self.label_web.setGeometry(QtCore.QRect(20, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.label_web.setFont(font)
        self.label_web.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_web.setObjectName("label_web")
        self.label_url = QtWidgets.QLabel(self.group_box_download)
        self.label_url.setGeometry(QtCore.QRect(590, 40, 54, 12))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_url.setFont(font)
        self.label_url.setObjectName("label_url")
        self.label_save_path_download = QtWidgets.QLabel(self.group_box_download)
        self.label_save_path_download.setGeometry(QtCore.QRect(20, 90, 54, 12))
        self.label_save_path_download.setObjectName("label_save_path_download")
        self.is_english_title = QtWidgets.QCheckBox(self.group_box_download)
        self.is_english_title.setGeometry(QtCore.QRect(1000, 40, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.is_english_title.setFont(font)
        self.is_english_title.setObjectName("is_english_title")
        self.web_confirm_btn = QtWidgets.QPushButton(self.group_box_download)
        self.web_confirm_btn.setGeometry(QtCore.QRect(440, 30, 75, 31))
        self.web_confirm_btn.setObjectName("web_confirm_btn")
        self.download_save_btn = QtWidgets.QPushButton(self.group_box_download)
        self.download_save_btn.setGeometry(QtCore.QRect(440, 80, 75, 31))
        self.download_save_btn.setObjectName("download_save_btn")
        self.download_btn = QtWidgets.QPushButton(self.group_box_download)
        self.download_btn.setGeometry(QtCore.QRect(590, 80, 61, 31))
        self.download_btn.setObjectName("download_btn")
        self.download_save_display = QtWidgets.QTextBrowser(self.group_box_download)
        self.download_save_display.setGeometry(QtCore.QRect(100, 80, 291, 31))
        self.download_save_display.setObjectName("download_save_display")
        self.download_progress_bar = QtWidgets.QProgressBar(self.group_box_download)
        self.download_progress_bar.setGeometry(QtCore.QRect(680, 80, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.download_progress_bar.setFont(font)
        self.download_progress_bar.setProperty("value", 0)
        self.download_progress_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.download_progress_bar.setObjectName("download_progress_bar")
        self.end_download_btn = QtWidgets.QPushButton(self.group_box_download)
        self.end_download_btn.setGeometry(QtCore.QRect(1000, 80, 71, 31))
        self.end_download_btn.setObjectName("end_download_btn")
        self.group_box_editor = QtWidgets.QGroupBox(self.centralwidget)
        self.group_box_editor.setGeometry(QtCore.QRect(20, 260, 1131, 391))
        self.group_box_editor.setObjectName("group_box_editor")
        self.groupBox_4 = QtWidgets.QGroupBox(self.group_box_editor)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 30, 1111, 61))
        self.groupBox_4.setObjectName("groupBox_4")
        self.select_background_pic_btn = QtWidgets.QPushButton(self.groupBox_4)
        self.select_background_pic_btn.setGeometry(QtCore.QRect(10, 20, 81, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_background_pic_btn.sizePolicy().hasHeightForWidth())
        self.select_background_pic_btn.setSizePolicy(sizePolicy)
        self.select_background_pic_btn.setObjectName("select_background_pic_btn")
        self.select_background_music_btn = QtWidgets.QPushButton(self.groupBox_4)
        self.select_background_music_btn.setGeometry(QtCore.QRect(290, 20, 81, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_background_music_btn.sizePolicy().hasHeightForWidth())
        self.select_background_music_btn.setSizePolicy(sizePolicy)
        self.select_background_music_btn.setObjectName("select_background_music_btn")
        self.select_water_logo_btn = QtWidgets.QPushButton(self.groupBox_4)
        self.select_water_logo_btn.setGeometry(QtCore.QRect(740, 20, 81, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_water_logo_btn.sizePolicy().hasHeightForWidth())
        self.select_water_logo_btn.setSizePolicy(sizePolicy)
        self.select_water_logo_btn.setObjectName("select_water_logo_btn")
        self.label_volume = QtWidgets.QLabel(self.groupBox_4)
        self.label_volume.setGeometry(QtCore.QRect(569, 28, 36, 16))
        self.label_volume.setObjectName("label_volume")
        self.input_volume = QtWidgets.QLineEdit(self.groupBox_4)
        self.input_volume.setGeometry(QtCore.QRect(611, 28, 31, 20))
        self.input_volume.setObjectName("input_volume")
        self.is_music_covered = QtWidgets.QCheckBox(self.groupBox_4)
        self.is_music_covered.setGeometry(QtCore.QRect(650, 30, 71, 16))
        self.is_music_covered.setObjectName("is_music_covered")
        self.water_logo_display = QtWidgets.QTextBrowser(self.groupBox_4)
        self.water_logo_display.setGeometry(QtCore.QRect(830, 20, 231, 31))
        self.water_logo_display.setObjectName("water_logo_display")
        self.background_pic_path_display = QtWidgets.QTextBrowser(self.groupBox_4)
        self.background_pic_path_display.setGeometry(QtCore.QRect(100, 20, 171, 31))
        self.background_pic_path_display.setObjectName("background_pic_path_display")
        self.background_music_path_display = QtWidgets.QTextBrowser(self.groupBox_4)
        self.background_music_path_display.setGeometry(QtCore.QRect(380, 20, 181, 31))
        self.background_music_path_display.setObjectName("background_music_path_display")
        self.groupBox_5 = QtWidgets.QGroupBox(self.group_box_editor)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 100, 561, 281))
        self.groupBox_5.setObjectName("groupBox_5")
        self.select_single_source_path_btn = QtWidgets.QPushButton(self.groupBox_5)
        self.select_single_source_path_btn.setGeometry(QtCore.QRect(20, 60, 75, 31))
        self.select_single_source_path_btn.setObjectName("select_single_source_path_btn")
        self.select_save_path_single_btn = QtWidgets.QPushButton(self.groupBox_5)
        self.select_save_path_single_btn.setGeometry(QtCore.QRect(20, 240, 75, 31))
        self.select_save_path_single_btn.setObjectName("select_save_path_single_btn")
        self.run_single_btn = QtWidgets.QPushButton(self.groupBox_5)
        self.run_single_btn.setGeometry(QtCore.QRect(370, 240, 141, 31))
        self.run_single_btn.setObjectName("run_single_btn")
        self.single_video_list = QtWidgets.QListWidget(self.groupBox_5)
        self.single_video_list.setGeometry(QtCore.QRect(20, 110, 491, 121))
        self.single_video_list.setObjectName("single_video_list")
        self.add_single_btn = QtWidgets.QPushButton(self.groupBox_5)
        self.add_single_btn.setGeometry(QtCore.QRect(510, 110, 31, 23))
        self.add_single_btn.setObjectName("add_single_btn")
        self.delete_single_btn = QtWidgets.QPushButton(self.groupBox_5)
        self.delete_single_btn.setGeometry(QtCore.QRect(510, 140, 31, 23))
        self.delete_single_btn.setObjectName("delete_single_btn")
        self.label_video_count = QtWidgets.QLabel(self.groupBox_5)
        self.label_video_count.setGeometry(QtCore.QRect(380, 70, 54, 12))
        self.label_video_count.setObjectName("label_video_count")
        self.editor_single_source_path_display = QtWidgets.QTextBrowser(self.groupBox_5)
        self.editor_single_source_path_display.setGeometry(QtCore.QRect(100, 60, 256, 31))
        self.editor_single_source_path_display.setObjectName("editor_single_source_path_display")
        self.video_count_display = QtWidgets.QTextBrowser(self.groupBox_5)
        self.video_count_display.setGeometry(QtCore.QRect(430, 60, 81, 31))
        self.video_count_display.setObjectName("video_count_display")
        self.label_end = QtWidgets.QLabel(self.groupBox_5)
        self.label_end.setGeometry(QtCore.QRect(100, 30, 41, 21))
        self.label_end.setObjectName("label_end")
        self.editor_single_save_path_display = QtWidgets.QTextBrowser(self.groupBox_5)
        self.editor_single_save_path_display.setGeometry(QtCore.QRect(110, 240, 241, 31))
        self.editor_single_save_path_display.setObjectName("editor_single_save_path_display")
        self.label_end_x = QtWidgets.QLabel(self.groupBox_5)
        self.label_end_x.setGeometry(QtCore.QRect(350, 31, 41, 21))
        self.label_end_x.setObjectName("label_end_x")
        self.input_end_x = QtWidgets.QLineEdit(self.groupBox_5)
        self.input_end_x.setGeometry(QtCore.QRect(397, 31, 31, 20))
        self.input_end_x.setObjectName("input_end_x")
        self.input_end_y = QtWidgets.QLineEdit(self.groupBox_5)
        self.input_end_y.setGeometry(QtCore.QRect(487, 31, 31, 20))
        self.input_end_y.setObjectName("input_end_y")
        self.label_end_y = QtWidgets.QLabel(self.groupBox_5)
        self.label_end_y.setGeometry(QtCore.QRect(440, 31, 41, 21))
        self.label_end_y.setObjectName("label_end_y")
        self.input_start_y = QtWidgets.QLineEdit(self.groupBox_5)
        self.input_start_y.setGeometry(QtCore.QRect(307, 31, 31, 20))
        self.input_start_y.setObjectName("input_start_y")
        self.label_start_y = QtWidgets.QLabel(self.groupBox_5)
        self.label_start_y.setGeometry(QtCore.QRect(270, 31, 41, 21))
        self.label_start_y.setObjectName("label_start_y")
        self.label_start_x = QtWidgets.QLabel(self.groupBox_5)
        self.label_start_x.setGeometry(QtCore.QRect(179, 30, 41, 21))
        self.label_start_x.setObjectName("label_start_x")
        self.input_start_x = QtWidgets.QLineEdit(self.groupBox_5)
        self.input_start_x.setGeometry(QtCore.QRect(220, 31, 31, 20))
        self.input_start_x.setObjectName("input_start_x")
        self.input_end_second = QtWidgets.QLineEdit(self.groupBox_5)
        self.input_end_second.setGeometry(QtCore.QRect(140, 30, 31, 20))
        self.input_end_second.setObjectName("input_end_second")
        self.input_front_second = QtWidgets.QLineEdit(self.groupBox_5)
        self.input_front_second.setGeometry(QtCore.QRect(60, 32, 31, 20))
        self.input_front_second.setObjectName("input_front_second")
        self.label_front = QtWidgets.QLabel(self.groupBox_5)
        self.label_front.setGeometry(QtCore.QRect(22, 32, 31, 21))
        self.label_front.setObjectName("label_front")
        self.groupBox_6 = QtWidgets.QGroupBox(self.group_box_editor)
        self.groupBox_6.setGeometry(QtCore.QRect(580, 100, 541, 281))
        self.groupBox_6.setObjectName("groupBox_6")
        self.normal_merge_btn = QtWidgets.QRadioButton(self.groupBox_6)
        self.normal_merge_btn.setGeometry(QtCore.QRect(100, 30, 89, 21))
        self.normal_merge_btn.setObjectName("normal_merge_btn")
        self.merge_type_btn_group = QtWidgets.QButtonGroup(MainWindow)
        self.merge_type_btn_group.setObjectName("merge_type_btn_group")
        self.merge_type_btn_group.addButton(self.normal_merge_btn)
        self.label_merge_videos = QtWidgets.QLabel(self.groupBox_6)
        self.label_merge_videos.setGeometry(QtCore.QRect(10, 30, 54, 21))
        self.label_merge_videos.setObjectName("label_merge_videos")
        self.top10_merge_btn = QtWidgets.QRadioButton(self.groupBox_6)
        self.top10_merge_btn.setGeometry(QtCore.QRect(210, 30, 71, 21))
        self.top10_merge_btn.setObjectName("top10_merge_btn")
        self.merge_type_btn_group.addButton(self.top10_merge_btn)
        self.select_merge_source_path_btn = QtWidgets.QPushButton(self.groupBox_6)
        self.select_merge_source_path_btn.setGeometry(QtCore.QRect(10, 60, 75, 31))
        self.select_merge_source_path_btn.setObjectName("select_merge_source_path_btn")
        self.label_total_duration = QtWidgets.QLabel(self.groupBox_6)
        self.label_total_duration.setGeometry(QtCore.QRect(360, 61, 54, 31))
        self.label_total_duration.setObjectName("label_total_duration")
        self.select_save_path_merge_btn = QtWidgets.QPushButton(self.groupBox_6)
        self.select_save_path_merge_btn.setGeometry(QtCore.QRect(10, 240, 75, 31))
        self.select_save_path_merge_btn.setObjectName("select_save_path_merge_btn")
        self.run_merge_btn = QtWidgets.QPushButton(self.groupBox_6)
        self.run_merge_btn.setGeometry(QtCore.QRect(360, 240, 141, 31))
        self.run_merge_btn.setObjectName("run_merge_btn")
        self.delete_merge_btn = QtWidgets.QPushButton(self.groupBox_6)
        self.delete_merge_btn.setGeometry(QtCore.QRect(500, 140, 31, 23))
        self.delete_merge_btn.setObjectName("delete_merge_btn")
        self.add_merge_btn = QtWidgets.QPushButton(self.groupBox_6)
        self.add_merge_btn.setGeometry(QtCore.QRect(500, 110, 31, 23))
        self.add_merge_btn.setObjectName("add_merge_btn")
        self.merge_video_list = QtWidgets.QListWidget(self.groupBox_6)
        self.merge_video_list.setGeometry(QtCore.QRect(10, 111, 491, 121))
        self.merge_video_list.setObjectName("merge_video_list")
        self.editor_merge_source_path_display = QtWidgets.QTextBrowser(self.groupBox_6)
        self.editor_merge_source_path_display.setGeometry(QtCore.QRect(100, 60, 231, 31))
        self.editor_merge_source_path_display.setObjectName("editor_merge_source_path_display")
        self.video_duration_display = QtWidgets.QTextBrowser(self.groupBox_6)
        self.video_duration_display.setGeometry(QtCore.QRect(410, 60, 81, 31))
        self.video_duration_display.setObjectName("video_duration_display")
        self.editor_merge_save_path_display = QtWidgets.QTextBrowser(self.groupBox_6)
        self.editor_merge_save_path_display.setGeometry(QtCore.QRect(100, 240, 231, 31))
        self.editor_merge_save_path_display.setObjectName("editor_merge_save_path_display")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 1121, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1167, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.group_box_upload.setTitle(_translate("MainWindow", "账号和上传管理"))
        item = self.account_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "account"))
        item = self.account_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "web"))
        item = self.account_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "title"))
        item = self.account_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "description"))
        item = self.account_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "caption"))
        item = self.account_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "title_tags"))
        item = self.account_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "tags"))
        item = self.account_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "video_path"))
        item = self.account_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "video_type"))
        item = self.account_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "user_file_title"))
        self.add_account_btn.setText(_translate("MainWindow", "+"))
        self.delete_account_btn.setText(_translate("MainWindow", "-"))
        self.group_box_download.setTitle(_translate("MainWindow", "视频下载"))
        self.pick_web.setItemText(0, _translate("MainWindow", "douyin"))
        self.pick_web.setItemText(1, _translate("MainWindow", "youtube"))
        self.label_web.setText(_translate("MainWindow", "视频网站："))
        self.label_url.setText(_translate("MainWindow", "主页链接："))
        self.label_save_path_download.setText(_translate("MainWindow", "保存目录："))
        self.is_english_title.setText(_translate("MainWindow", "英文标题"))
        self.web_confirm_btn.setText(_translate("MainWindow", "确认选择"))
        self.download_save_btn.setText(_translate("MainWindow", "路径选择"))
        self.download_btn.setText(_translate("MainWindow", "开始下载"))
        self.end_download_btn.setText(_translate("MainWindow", "结束下载"))
        self.group_box_editor.setTitle(_translate("MainWindow", "视频编辑"))
        self.groupBox_4.setTitle(_translate("MainWindow", "常规设置"))
        self.select_background_pic_btn.setText(_translate("MainWindow", "背景图"))
        self.select_background_music_btn.setText(_translate("MainWindow", "背景乐"))
        self.select_water_logo_btn.setText(_translate("MainWindow", "水印"))
        self.label_volume.setText(_translate("MainWindow", "音量："))
        self.input_volume.setText(_translate("MainWindow", "50"))
        self.is_music_covered.setText(_translate("MainWindow", "是否覆盖"))
        self.groupBox_5.setTitle(_translate("MainWindow", "单视频编辑"))
        self.select_single_source_path_btn.setText(_translate("MainWindow", "原视频目录"))
        self.select_save_path_single_btn.setText(_translate("MainWindow", "保存目录"))
        self.run_single_btn.setText(_translate("MainWindow", "开始剪辑"))
        self.add_single_btn.setText(_translate("MainWindow", "+"))
        self.delete_single_btn.setText(_translate("MainWindow", "-"))
        self.label_video_count.setText(_translate("MainWindow", "总数量："))
        self.label_end.setText(_translate("MainWindow", "片尾"))
        self.label_end_x.setText(_translate("MainWindow", "终点x"))
        self.label_end_y.setText(_translate("MainWindow", "终点y"))
        self.label_start_y.setText(_translate("MainWindow", "起点y"))
        self.label_start_x.setText(_translate("MainWindow", "起点x"))
        self.input_end_second.setText(_translate("MainWindow", "0"))
        self.input_front_second.setText(_translate("MainWindow", "0"))
        self.label_front.setText(_translate("MainWindow", "片头"))
        self.groupBox_6.setTitle(_translate("MainWindow", "合集"))
        self.normal_merge_btn.setText(_translate("MainWindow", "常规合集"))
        self.label_merge_videos.setText(_translate("MainWindow", "合集类型"))
        self.top10_merge_btn.setText(_translate("MainWindow", "top10"))
        self.select_merge_source_path_btn.setText(_translate("MainWindow", "原视频目录"))
        self.label_total_duration.setText(_translate("MainWindow", "总时长："))
        self.select_save_path_merge_btn.setText(_translate("MainWindow", "保存目录"))
        self.run_merge_btn.setText(_translate("MainWindow", "开始剪辑"))
        self.delete_merge_btn.setText(_translate("MainWindow", "-"))
        self.add_merge_btn.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; color:#00aa00;\">欢迎使用搬运工</span></p></body></html>"))

