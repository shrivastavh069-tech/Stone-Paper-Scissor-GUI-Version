import sys 
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtMultimedia import QMediaPlayer,QAudioOutput
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QMovie
from PyQt6.QtGui import QPixmap
from sto import Ui_MainWindow as gameUI
from story import Ui_MainWindow as stoUI

import random



class music_manager:
    def __init__(self):
        self.player=QMediaPlayer()
        self.audio=QAudioOutput()
        self.player.setAudioOutput(self.audio)
        self.player.mediaStatusChanged.connect(self.loop)

    def play_bg(self):
        self.player.setSource(QUrl.fromLocalFile("stuff/sound.mpeg"))
        self.audio.setVolume(0.8)
        self.player.play()

        
    def stop_bg (self):
        self.player.stop()

        
    def loop (self,status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.player.play()

    
class getWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=stoUI()
        self.ui.setupUi(self)
        self.player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.player.setAudioOutput(self.audio)
        print("background")
        self.video = QVideoWidget(self.ui.videowidget)
        self.video.setGeometry(self.ui.videowidget.rect())
        self.player.setVideoOutput(self.video)
        self.player.setSource(QUrl.fromLocalFile("stuff/vi.mp4"))
        self.audio.setVolume(0.5)
        self.player.play()
        


class gameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=gameUI()
        self.ui.setupUi(self)
        self.user_health = 100
        self.bot_health = 100
        self.match = 1
        self.ui.match.display(self.match)
        self.music=music_manager()
        self.music.play_bg()
        self.window()

    def window(self):
        #self.hide_labels("video")
        self.ui.play_window.raise_()
        self.ui.play_btn.raise_()
        self.show_labels("play")
        self.show_labels("playbutton")
        self.hide_labels("win")
        self.hide_labels("label")
        self.hide_labels("task")
        self.hide_labels("label_2")
        self.hide_labels("label_3")
        self.hide_labels("label_4")
        self.hide_labels("label_5")
        self.hide_labels("label_6")
        self.hide_labels("label_7")
        self.hide_labels("label_8")
        self.hide_labels("label_9")
        self.hide_labels("label_10")
        self.hide_labels("healthbar_user")
        self.hide_labels("healthbar_bot")
        self.hide_labels("u_health")
        self.hide_labels("b_health")
        self.hide_labels("bar")
        self.hide_labels("extra2_2")
        self.hide_labels("label_11")
        self.hide_labels("label_12")
        self.hide_labels("extra2")
        self.hide_labels("label_15")
        self.hide_labels("extra2_3")
        self.hide_labels("match")
        self.hide_labels("extra")
        self.hide_labels("label_16")
        self.hide_labels("label_21")
        self.hide_labels("label_22")
        self.hide_labels("win_screens")

        self.movie=QMovie("stuff/window.gif")
        self.ui.play_window.setMovie(self.movie)
        self.movie.start()
        self.ui.play_btn.clicked.connect(self.story)



    def hide_labels(self,hide):
        if hide == "play":
            self.ui.play_window.hide()
        if hide == "playbutton":
            self.ui.play_btn.hide()
        #if hide == "video":
            #self.ui.video_widget.hide()
        if  hide == "task":
            self.ui.task_label.hide()
        if hide =="label":
            self.ui.label.hide()
        if hide == "label_2":
            self.ui.label_2.hide()
        if hide =="label_3":
            self.ui.label_3.hide()
        if hide == "label_4":
            self.ui.label_4.hide()
        if hide=="label_5":
            self.ui.label_5.hide()
        if hide =="label_6":
            self.ui.label_6.hide()
        if hide=="label_7":
            self.ui.label_7.hide()
        if hide=="label_8":
            self.ui.label_8.hide()
        if hide=="label_9":
            self.ui.label_9.hide()
            
        if hide=="label_10":
            self.ui.label_10.hide()
        if hide =="bar":
            self.ui.Bar.hide()
        if hide =="win":
            self.ui.stackedWidget.hide()
        if hide =="label_12":
            self.ui.label_12.hide()      
        if hide =="label_11":
            self.ui.label_11.hide()
        if hide =="match":
            self.ui.match.hide()
        if hide =="label_15":
            self.ui.label_15.hide()
        if hide =="label_16":
            self.ui.label_16.hide()    
        if hide =="label_13":
            self.ui.label_13.hide()
        if hide=="extra2_2":
            self.ui.extra2_2.hide()
        if hide=="extra2_3":
            self.ui.extra2_3.hide()
        if hide=="extra2":
            self.ui.extra2.hide()
        if hide=="extra":
            self.ui.extra.hide()
        if hide=="label_21":
            self.ui.label_21.hide()
        if hide=="label_22":
            self.ui.label_22.hide()
        if hide =="win_screens":
            self.ui.win_screens.hide()
            
        if hide =="u_health":
            self.ui.u_health.hide()
        if hide =="b_health":
            self.ui.b_health.hide()
        if hide =="healthbar_user":
            self.ui.user_health.hide()
        if hide =="healthbar_bot":
            self.ui.user_health_2.hide()    
                     

            
            
    def show_labels(self,show):
        if show == "play":
            self.ui.play_window.show()
        if show == "playbutton":
            self.ui.play_btn.show()
        #if show == "video":
            #self.ui.video_widget.show()
        if  show == "task":
            self.ui.task_label.show()
        if show =="label":
            self.ui.label.show()
        if show == "label_2":
            self.ui.label_2.show()
        if show =="label_3":
            self.ui.label_3.show()
        if show == "label_4":
            self.ui.label_4.show()
        if show =="label_5":
            self.ui.label_5.show()
        if show =="label_6":
            self.ui.label_6.show()
        if show=="label_7":
            self.ui.label_7.show()
        if show=="label_8":
            self.ui.label_8.show()
        if show=="label_9":
            self.ui.label_9.show()         
        if show=="label_10":
            self.ui.label_10.show()
        if show =="bar":
            self.ui.Bar.show()
        if show =="win":
            self.ui.stackedWidget.show()
        if show =="label_12":
            self.ui.label_12.show()
        if show =="match":
            self.ui.match.show()
        if show =="label_11":
            self.ui.label_11.show()
        if show =="label_15":
            self.ui.label_15.show()
        if show =="label_16":
            self.ui.label_16.show()    
        if show=="extra2_2":
            self.ui.extra2_2.show()
        if show=="extra2":
            self.ui.extra2.show()
        if show=="extra":
            self.ui.extra.show()
        if show=="extra2_3":
            self.ui.extra2_3.show()
        if show=="label_21":
            self.ui.label_21.show()
        if show=="win_screens":
            self.ui.win_screens.show()
        if show=="label_22":
            self.ui.label_22.show()
        if show=="u_health":
            self.ui.u_health.show()
        if show=="b_health":
            self.ui.b_health.show()
        if show=="healthbar_user":
            self.ui.user_health.show()
        if show=="healthbar_bot":
            self.ui.user_health_2.show()    

    def story(self):
        self.hide_labels("play")
        self.hide_labels("playbutton")
        self.video=getWindow()
        self.video.show()
        QTimer.singleShot(52000,self.video.close)
        QTimer.singleShot(52000,self.task)


    def task (self):
        self.music.stop_bg()
        self.player=QMediaPlayer()
        self.audio=QAudioOutput()
        self.player.setAudioOutput(self.audio)
        self.player.setSource(QUrl.fromLocalFile("stuff/challenge.mpeg"))
        self.audio.setVolume(0.8)
        self.player.play()

        self.hide_labels("play")
        self.hide_labels("playbutton")
        self.hide_labels("win_screens")
        self.show_labels("task")
        self.movie=QMovie("stuff/task_game.gif")
        self.ui.task_label.setMovie(self.movie)
        self.movie.start()
        QTimer.singleShot(1000,self.remaining)       


    def remaining (self):
        print("hello")
        self.show_labels("label")
        QTimer.singleShot(1000,self.instruct)


    def instruct (self):
        self.show_labels("label_15")
        QTimer.singleShot(5000,self.start)
        
    def start (self):
        self.hide_labels("label_15")
        self.show_labels("label_2")
        QTimer.singleShot(500,self.actual)


    def actual(self):
        self.hide_labels("label_2")
        self.show_labels("label_5")
        self.show_labels("extra")
        self.show_labels("healthbar_user")
        self.show_labels("healthbar_bot")
        self.show_labels("u_health")
        self.show_labels("b_health")
        self.show_labels("extra2_3")
        self.show_labels("label_7")
        self.show_labels("label_6")
        self.show_labels("label_10")
        self.show_labels("label_3")
        self.show_labels("bar")
        self.show_labels("match")
        self.show_labels("bar")
        self.show_labels("label_9")
        self.show_labels("label_8")
        self.show_labels("extra2_2")
        self.show_labels("extra2")
        self.show_labels("label_11")
        self.show_labels("label_16")
        self.show_labels("label_11")
        self.show_labels("label_12")
        self.show_labels("label_22")
        QTimer.singleShot(40,self.game_start)

    def bot(self):
        self.bai=random.choice(["stone","paper","scissor"])
        if self.bai == "stone":
            self.ui.label_9.setPixmap(QPixmap("chance/stone.jpeg"))
        if self.bai == "paper":
            self.ui.label_9.setPixmap(QPixmap("chance/paper.jpeg"))
        if self.bai == "scissor":
            self.ui.label_9.setPixmap(QPixmap("chance/scissor.jpeg"))
            
        return self.bai
        
    def game_start(self):
        if self.match <= 10:
            self.ui.label_7.mousePressEvent=lambda event:self.winner("scissor")
            self.ui.label_5.mousePressEvent=lambda event:self.winner("stone")
            self.ui.label_6.mousePressEvent=lambda event:self.winner("paper")
        if self.match > 10:
            self.ui.label_7.mousePressEvent=lambda event:self.final_match("scissor")
            self.ui.label_5.mousePressEvent=lambda event:self.final_match("stone")
            self.ui.label_6.mousePressEvent=lambda event:self.final_match("paper")

            
        
        self.time = 3
        self.ui.Bar.setMaximum(3)
        self.ui.Bar.setValue(3)
        self.timer = QTimer()
        self.timer.timeout.connect(self.countdown)
        self.timer.start(400)

    def countdown(self):

        self.time -= 1
        self.ui.Bar.setValue(self.time)

        if self.time == 0:
            self.timer.stop()
            self.show_labels("win")
            self.health_bars("user")
            self.match+=1
            self.ui.match.display(self.match)
            self.ui.stackedWidget.setCurrentIndex(1)
        
            QTimer.singleShot(1000,self.hiding)
            print("Time Over")        


    def hiding (self):
        self.show_labels("label")
        self.show_labels("label_7")
        self.show_labels("label_5")
        self.show_labels("label_6")
        QTimer.singleShot(10,self.refresh)


    def health_bars (self,health):
        if health == "user" :
            self.user_health -=10
            self.ui.user_health.setValue(self.user_health)

        elif health == "bot":
            self.bot_health -=10
            self.ui.user_health_2.setValue(self.bot_health)
        elif health == "draw":
            self.user_health -=10
            self.ui.user_health.setValue(self.user_health)
            self.bot_health -=10
            self.ui.user_health_2.setValue(self.bot_health)


            

        
        
    def winner (self,user):
        self.timer.stop()
        self.show_labels("win")
        jannat=self.bot()
        if(user == "stone" and jannat=="stone"):
            self.ui.stackedWidget.setCurrentIndex(0)
            self.health_bars("draw")
        elif(user =="paper" and jannat=="paper"):
            self.ui.stackedWidget.setCurrentIndex(0)
            self.health_bars("draw")
        elif(user == "scissor" and jannat =="scissor"):
            self.ui.stackedWidget.setCurrentIndex(0)
            self.health_bars("draw")
        elif(user == "paper" and jannat == "stone"):
            self.ui.stackedWidget.setCurrentIndex(2)
            self.health_bars("bot")
        elif(jannat == "paper" and user == "stone"):
            self.ui.stackedWidget.setCurrentIndex(1)
            self.health_bars("user")
        elif(user == "paper" and jannat =="scissor"):
            self.ui.stackedWidget.setCurrentIndex(1)
            self.health_bars("user")
        elif(user =="stone" and jannat=="scissor"):
            self.ui.stackedWidget.setCurrentIndex(2)
            self.health_bars("bot")
        elif(jannat =="stone" and user=="scissor"):
            self.ui.stackedWidget.setCurrentIndex(1)
            self.health_bars("user")
        elif(user =="scissor" and jannat =="paper"):
            self.ui.stackedWidget.setCurrentIndex(2)
            self.health_bars("bot")

            
        print("user:",user)
        print("bot",jannat)
        if self.user_health == 0:
            self.bot_win()
            
        if  self.match == 10:
            self.match+=1
            self.show_labels("label_21")
            self.hide_labels("label_7")
            self.hide_labels("extra")
            self.hide_labels("label_6")
            self.hide_labels("label_5")
            self.hide_labels("label_3")
            QTimer.singleShot(2000,self.refresh)
            
        if self.match < 10:
            self.match += 1
            self.ui.match.display(self.match)
    
        QTimer.singleShot(1000,self.refresh)    
        
    def refresh (self):
        self.hide_labels("label_21")
        self.show_labels("label_7")
        self.show_labels("extra")
        self.show_labels("label_6")
        self.show_labels("label_5")
        self.show_labels("label_3")
        self.hide_labels("win")
        QTimer.singleShot(20,self.game_start)

        
    def checking (self):
        if self.user_health < self.bot_health :
            self.bot_win()

        elif self.user_health > self.bot_health:
            self.user_win()
        

    def final_match(self,user):
        self.show_labels("win")
        self.timer.stop()
        bot1=self.bot()
        bot2=self.bot()
        self.hide_labels("label_12")
        self.hide_labels("label_16")
        self.hide_labels("label_22")
        if(user == "stone" and bot1=="stone" and bot2=="stone"):
            self.ui.stackedWidget.setCurrentIndex(0)
            self.health_bars("draw")
        elif(user == "scissor" and bot1=="scissor" and bot2=="scissor"):
            self.ui.stackedWidget.setCurrentIndex(0)
            self.health_bars("draw")
        elif(user == "paper" and bot1=="paper" and bot2=="paper"):        
            self.ui.stackedWidget.setCurrentIndex(0)
            self.health_bars("draw")
        elif(user=="paper" and bot1== "stone" and bot2 =="stone"):
            self.ui.stackedWidget.setCurrentIndex(2)
            self.health_bars("user")
        elif(user =="stone" and bot1=="paper" and bot2=="paper"):
            self.ui.stackedWidget.setCurrentIndex(1)
            self.health_bars("bot")
        elif(user =="scissor" and bot1=="stone" and bot2=="stone"):
            self.ui.stackedWidget.setCurrentIndex(2)
            self.health_bars("user")
        elif(user =="stone" and bot1=="stone" and bot2=="scissor"):
            self.ui.stackedWidget.setCurrentIndex(1)
            self.health_bars("bot")
        elif(user =="scissor" and bot1=="stone" and bot2=="paper"):
            self.ui.stackedWidget.setCurrentIndex(0)
            self.health_bars("draw")
        elif(user =="scissor" and bot1=="paper" and bot2=="stone"):
            self.ui.stackedWidget.setCurrentIndex(0)
            self.health_bars("draw")
        elif(user =="paper" and bot1=="paper" and bot2=="stone"):
            self.ui.stackedWidget.setCurrentIndex(2)
            self.health_bars("user")
        elif(user =="stone" and bot1=="paper" and bot2=="scissor"):
            self.ui.stackedWidget.setCurrentIndex(0)
            self.health_bars("draw")
        elif(user =="stone" and bot1=="scissor" and bot2=="paper"):
            self.ui.stackedWidget.setCurrentIndex(0)
            self.health_bars("draw")
        elif(user =="paper" and bot1=="scissor" and bot2=="stone"):
            self.ui.stackedWidget.setCurrentIndex(0)
            self.health_bars("draw")
        elif(user =="stone" and bot1=="paper" and bot2=="stone"):
            self.ui.stackedWidget.setCurrentIndex(1)
            self.health_bars("bot")
        elif(user =="stone" and bot1=="scissor" and bot2=="stone"):
            self.ui.stackedWidget.setCurrentIndex(2)
            self.health_bars("user")
        elif(user =="stone" and bot1=="scissor" and bot2=="scissor"):
            self.ui.stackedWidget.setCurrentIndex(2)
            self.health_bars("user")
        elif(user =="paper" and bot1=="stone" and bot2=="paper"):
            self.ui.stackedWidget.setCurrentIndex(2)
            self.health_bars("user")
        elif(user =="paper" and bot1=="scissor" and bot2=="paper"):
            self.ui.stackedWidget.setCurrentIndex(1)
            self.health_bars("bot")
        elif(user =="paper" and bot1=="scissor" and bot2=="scissor"):
            self.ui.stackedWidget.setCurrentIndex(1)
            self.health_bars("bot")
        elif(user =="scissor" and bot1=="paper" and bot2=="paper"):
            self.ui.stackedWidget.setCurrentIndex(2)
            self.health_bars("user")
        elif(user =="scissor" and bot1=="paper" and bot2=="scissor"):
            self.ui.stackedWidget.setCurrentIndex(1)
            self.health_bars("bot")
        elif(user =="scissor" and bot1=="stone" and bot2=="scissor"):
            self.ui.stackedWidget.setCurrentIndex(1)
            self.health_bars("bot")
        elif(user =="paper" and bot1=="paper" and bot2=="scissor"):
            self.ui.stackedWidget.setCurrentIndex(1)
            self.health_bars("bot")
        elif(user =="scissor" and bot1=="scissor" and bot2=="stone"):
            self.ui.stackedWidget.setCurrentIndex(1)
            self.health_bars("bot")

        if self.match < 13:
            self.match += 1
            self.ui.match.display(self.match)
            

        if self.match == 13:
            if self.user_health > self.bot_health:
                self.user_win()
            if self.user_health< self.bot_health:
                self.bot_win()
            
            
        QTimer.singleShot(1000,self.hiding)
        print("Time Over")



    def user_win (self):
        self.music.stop_bg()
        self.hide_labels("task")
        self.show_labels("win_screens")
        self.ui.win_screens.setCurrentIndex(0)
        self.movie=QMovie("stuff/user_won.gif")
        self.ui.label_23.setMovie(self.movie)
        self.movie.start()
        self.player=QMediaPlayer()
        self.audio=QAudioOutput()
        self.player.setAudioOutput(self.audio)
        self.player.setSource(QUrl.fromLocalFile("stuff/user_music.mpeg"))
        self.audio.setVolume(0.8)
        self.player.play()
        QTimer.singleShot(500,self.window)
        

    def bot_win (self):
        self.music.stop_bg()
        self.ui.win_screens.setCurrentIndex(1)
        self.hide_labels("task")
        self.show_labels("win_screens")
        self.movie=QMovie("stuff/bot wins.gif")
        self.ui.label_24.setMovie(self.movie)
        self.movie.start()
        self.player=QMediaPlayer()
        self.audio=QAudioOutput()
        self.player.setAudioOutput(self.audio)
        self.player.setSource(QUrl.fromLocalFile("stuff/bot_music.mpeg"))
        self.audio.setVolume(0.8)
        self.player.play()
        QTimer.singleShot(18000,self.window)
        

        
    
        
    
app=QApplication(sys.argv)
Window=gameWindow()
Window.show()
sys.exit(app.exec())


        
        
