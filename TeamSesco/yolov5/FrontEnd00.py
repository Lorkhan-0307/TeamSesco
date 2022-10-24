import sys

from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import *
from PyQt5 import uic
from yolov5 import detect_modify
import os
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QPalette
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import datetime

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.

form_class = uic.loadUiType("yolov5/BlackEyes.ui")[0]

media_class = uic.loadUiType("yolov5/MediaPlayer.ui")[0]

video_path = 'C:/Users/Public/Capstone_AIHackathon/yolov5/data/'




#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 연결하는 코드
        self.pushButton_Webcam.clicked.connect(self.button_Webcam_Function)
        self.pushButton_VideoInput.clicked.connect(self.button_Video_Input_Function)
        self.pushButton_VideoPlay.clicked.connect(self.button_Video_Play_Function)

        self.Video0.clicked.connect(self.VideoSelect)
        self.Video1.clicked.connect(self.VideoSelect)
        self.Video2.clicked.connect(self.VideoSelect)






    # 웹캠 선택
    def button_Webcam_Function(self) :
        print("btn_webcam Clicked")
        os.system('cmd /c python yolov5/detect_modify.py --weights yolov5s.pt --img 640 --conf 0.25 --source 1')




    # 영상 재생
    def button_Video_Play_Function(self) :
        print("btn_3 Clicked")
        filename, _ = QFileDialog.getOpenFileName(self, "select video")

        if filename != '':
            #self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            #self.playBtn.setEnabled(True)
            self.hide()
            self.media = MediaClass()
            self.media.exec()
            self.show()



    # 비디오 선택
    def VideoSelect(self):
        if self.Video0.isChecked():
            video_path = 'C:/Users/Public/Capstone_AIHackathon/yolov5/data/RecTest00'
            print(video_path)
        elif self.Video1.isChecked():
            video_path = 'C:/Users/Public/Capstone_AIHackathon/yolov5/data/RecTest01'
            print(video_path)
        elif self.Video2.isChecked():
            video_path = 'C:/Users/Public/Capstone_AIHackathon/yolov5/data/RecTest02'
            print(video_path)

            # 영상 선택

    def button_Video_Input_Function(self):
        print("btn_2 Clicked")
        if self.Video0.isChecked():
            video_path = 'C:/Users/Public/Capstone_AIHackathon/yolov5/data/RecTest00'
            print(video_path)
        elif self.Video1.isChecked():
            video_path = 'C:/Users/Public/Capstone_AIHackathon/yolov5/data/RecTest01'
            print(video_path)
        elif self.Video2.isChecked():
            video_path = 'C:/Users/Public/Capstone_AIHackathon/yolov5/data/RecTest02'
            print(video_path)
        #print(f'cmd /c python yolov5/detect_modify.py --weights yolov5s.pt --img 640 --conf 0.25 --source ' + video_path)
        os.system(f'cmd /c python yolov5/detect_modify.py --weights yolov5s.pt --img 640 --conf 0.25 --view-img --source ' + video_path)

class MediaClass(QMediaContent, media_class):
    def __init__(self):
        super(MediaClass, self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUI(self)


        """def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

        else:
            self.mediaPlayer.play()"""

        # create button for playing
        """self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)"""




if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()