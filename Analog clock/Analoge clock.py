from kivy.config import Config
Config.set('graphics', 'width', 720)
Config.set('graphics', 'height', 720)

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
import time
import math
from kivy.graphics import Line, Color, Ellipse


class RoundClock(Widget):
    winWd = NumericProperty(0)
    winHt = NumericProperty(0)
    clockScale = NumericProperty(0)
    clockPd = NumericProperty(0)

    secX = NumericProperty(0)
    secY = NumericProperty(0)
    secLen = .9
    minX = NumericProperty(0)
    minY = NumericProperty(0)
    minLen = .8
    hrX = NumericProperty(0)
    hrY = NumericProperty(0)
    hrLen = .5

    hrPoints = []

    def __init__(self, **kwargs):
        super(RoundClock, self).__init__(**kwargs)

        self.winWd = self.width
        self.winHt = self.height

        self.clockScale = self.height
        self.clockPd = self.clockScale / 10

        with self.canvas:
            self.clockCircle = Ellipse()
            Color(0, 0, 0)

            for i in range(12):
                self.hrPoints.append(Line())
            self.updateHrPoints()

        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, dt):
        if self.winWd != self.width or self.winHt != self.height:
            # print(self.width, self.height)
            self.winWd = self.width
            self.winHt = self.height

            if self.width < self.height:
                self.clockScale = self.width - 2 * self.clockPd
            else:
                self.clockScale = self.height - 2 * self.clockPd
            self.clockPd = self.clockScale / 10
            self.clockCircle.pos = (self.winWd / 2 - self.clockScale / 2, self.winHt / 2 - self.clockScale / 2)
            self.clockCircle.size = (self.clockScale, self.clockScale)

            self.updateHrPoints()

        self.secX = self.secLen * self.clockScale / 2 * math.sin(math.radians(6 * int(time.strftime('%S'))))
        self.secY = self.secLen * self.clockScale / 2 * math.cos(math.radians(6 * int(time.strftime('%S'))))

        self.minX = self.minLen * self.clockScale / 2 * math.sin(math.radians(6 * int(time.strftime('%M'))))
        self.minY = self.minLen * self.clockScale / 2 * math.cos(math.radians(6 * int(time.strftime('%M'))))

        self.hrX = self.hrLen * self.clockScale / 2 * math.sin(
            math.radians(.5 * (int(time.strftime('%H')) * 60 + int(time.strftime('%M')))))
        self.hrY = self.hrLen * self.clockScale / 2 * math.cos(
            math.radians(.5 * (int(time.strftime('%H')) * 60 + int(time.strftime('%M')))))

    def updateHrPoints(self):
        for i in range(12):
            self.hrPoints[i].width = self.clockScale/200
            self.hrPoints[i].points = (
                self.winWd / 2 + self.clockScale / 2 * math.sin(math.radians(30 * i)),
                self.winHt / 2 + self.clockScale / 2 * math.cos(math.radians(30 * i)),
                self.winWd / 2 + self.clockScale * .48 * math.sin(math.radians(30 * i)),
                self.winHt / 2 + self.clockScale * .48 * math.cos(math.radians(30 * i)),
            )


class AnalogClockApp(App):
    pass


AnalogClockApp().run()
