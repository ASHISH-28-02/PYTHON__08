from kivy.config import Config
Config.set('graphics', 'width', 720)
Config.set('graphics', 'height', 720)

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ObjectProperty
from kivy.core.audio import SoundLoader


class Timer(AnchorLayout):

    time_text = StringProperty("00:05:00")
    inputMenuState = BooleanProperty(False)
    popupState = BooleanProperty(False)
    startBtText = StringProperty("Start")
    hr_input = ObjectProperty()
    min_input = ObjectProperty()
    sc_input = ObjectProperty()
    maxTime = NumericProperty(0)
    timeNow = NumericProperty(0)

    hr = 0
    min = 5
    sc = 0

    tem = [0,5,0]

    paused = True

    alarmSound = None

    def __init__(self, **kwargs):
        super(Timer, self).__init__(**kwargs)

        self.alarmSound = SoundLoader.load("KdlAlarmTone.wav")

        Clock.schedule_interval(self.update, 1.0)

    def update(self, dt):
        if not self.paused:
            if self.hr != 0 or self.min != 0 or self.sc != 0:
                if self.sc == 0:
                    if self.min == 0:
                        if self.hr == 0:
                            self.over()
                        self.hr -= 1
                        self.min = 59
                        self.sc = 59
                    else:
                        self.min -= 1
                        self.sc = 59
                else:
                    self.sc -= 1
                self.rendText()
                self.timeNow = self.hr*3600 + self.min*60 + self.sc
            else:
                self.over()
            self.startBtText = "Pause"
        else:
            self.startBtText = "Start"

    def rendText(self):
        if self.hr < 10:
            self.time_text = "0"+str(self.hr)
        else:
            self.time_text = str(self.hr)
        self.time_text += ":"
        if self.min < 10:
            self.time_text += "0"+str(self.min)
        else:
            self.time_text += str(self.min)
        self.time_text += ":"
        if self.sc < 10:
            self.time_text += "0"+str(self.sc)
        else:
            self.time_text += str(self.sc)

    def over(self):
        self.rendText()
        self.paused = True
        self.alarmSound.loop = True
        self.alarmSound.play()
        self.popup()
        print("Over")

    def disableInputMenu(self):
        self.inputMenuState = False

    def ableInputMenu(self):
        self.inputMenuState = True

    def done(self, hr, mn, sec):
        self.hr = int(hr)
        self.min = int(mn)
        self.sc = int(sec)

        if self.sc > 59:
            self.sc = 59
        if self.sc < 0:
            self.sc = 0
        self.tem[2] = self.sc

        if self.min > 59:
            self.min = 59
        if self.min < 0:
            self.min = 0
        self.tem[1] = self.min

        if self.hr < 0:
            self.hr = 0
        self.tem[0] = self.hr

        self.disableInputMenu()
        self.rendText()

        self.maxTime = self.hr*3600 + self.min*60 + self.sc

    def startBt(self):
        if self.paused:
            self.paused = False
        else:
            self.paused = True

    def reset(self):
        self.hr = self.tem[0]
        self.min = self.tem[1]
        self.sc = self.tem[2]
        self.rendText()
        self.timeNow = 0
        self.paused = True

    def popup(self):
        self.popupState = True

    def stopAlarm(self):
        self.alarmSound.stop()
        self.popupState = False

    def resetAlarm(self):
        self.alarmSound.stop()
        self.popupState = False
        self.reset()
        self.paused = False


class TimerApp(App):
    pass


TimerApp().run()
