from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from Computations import topCompute
from Computations import botCompute
from Computations import topcheck
from Computations import botcheck
from Computations import convert
from Computations import invalid2
from kivy.core.window import Window
from kivy.animation import Animation


Window.clearcolor = (0.847, 0.86, 0.886, 1)


class MainWindow(Screen):

    def topChange(self, widget):
        anim = Animation(size_hint=(0.75,0.25), pos_hint={"x":0.125,"top":0.775}, duration = 0.05)
        anim.start(widget)

    def botChange(self,widget):
        anim = Animation(size_hint=(0.75, 0.25), pos_hint={"x": 0.125, "top": 0.375}, duration=0.05)
        anim.start(widget)

    def topBtn(self, widget):
        sm.current = "top"
        anim = Animation(size_hint=(0.7,0.2), pos_hint={"x":0.15,"top":0.75}, duration = 0.05)
        anim.start(widget)

    def botBtn(self,widget):
        sm.current = "bottom"
        anim = Animation(size_hint=(0.7,0.2), pos_hint={"x":0.15,"top":0.35}, duration = 0.05)
        anim.start(widget)



class TopWindow(Screen):
    bigj = ObjectProperty(None)
    bigm = ObjectProperty(None)
    j1 = ObjectProperty(None)
    j2 = ObjectProperty(None)

    def Back(self,widget):
        self.bigj.text = self.bigm.text = self.j1.text = self.j2.text = ""
        sm.current = "main"
        anim = Animation(size_hint=(0.47, 0.18), pos_hint={"x": 0.01, "top": 0.01}, duration=0.03)
        anim.start(widget)

    def topChangeLeft(self, widget):
        anim = Animation(size_hint=(0.48,0.19), pos_hint={"x":0.01,"top":0.00}, duration = 0.03)
        anim.start(widget)

    def topChangeRight(self, widget):
        anim = Animation(size_hint=(0.48,0.19), pos_hint={"x":0.49,"top":0.01}, duration = 0.03)
        anim.start(widget)

    def topForw(self, widget):
        if topcheck(self.bigj.text, self.bigm.text, self.j1.text, self.j2.text):
            try:
                TopResultsWindow.coeff = topCompute(convert(self.bigj.text), convert(self.bigm.text),convert(self.j1.text), convert(self.j2.text))
            except OverflowError:
                invalid2()
            else:
                TopResultsWindow.og = "|" + self.bigj.text + " " + self.bigm.text + " " + self.j1.text + " " + self.j2.text + "\u27E9"
                sm.current = "topresults"
        anim = Animation(size_hint=(0.47, 0.18), pos_hint={"x": 0.511, "top": 0.01}, duration=0.03)
        anim.start(widget)


class TopResultsWindow(Screen):
    coeff = ""
    og = ""

    def on_enter(self, *args):
        self.coeffr.text = "=" + " " + str(self.coeff)
        self.ogr.text = "| J M j\u2081 j\u2082 \u27E9  = " + self.og

    def resBackChange(self, widget):
        anim = Animation(size_hint=(0.98, 0.18), pos_hint={"x": 0.01, "y": 0.01}, duration=0.03)
        anim.start(widget)

    def resBack(self, widget):
        sm.current = "top"
        anim = Animation(size_hint=(0.97, 0.17), pos_hint={"x": 0.01, "y": 0.01}, duration=0.03)
        anim.start(widget)


class BottomWindow(Screen):
    j1 = ObjectProperty(None)
    j2 = ObjectProperty(None)
    m1 = ObjectProperty(None)
    m2 = ObjectProperty(None)


    def botChangeLeft(self, widget):
        anim = Animation(size_hint=(0.48, 0.19), pos_hint={"x": 0.01, "top": 0.00}, duration=0.03)
        anim.start(widget)

    def botChangeRight(self, widget):
        anim = Animation(size_hint=(0.48, 0.19), pos_hint={"x": 0.49, "top": 0.01}, duration=0.03)
        anim.start(widget)

    def Back(self, widget):
        self.j1.text = self.j2.text = self.m1.text = self.m2.text = ""
        sm.current = "main"
        anim = Animation(size_hint=(0.47, 0.18), pos_hint={"x": 0.01, "top": 0.01}, duration=0.03)
        anim.start(widget)

    def botForw(self, widget):
        if botcheck(self.j1.text, self.j2.text, self.m1.text, self.m2.text):
            try:
                BottomResultsWindow.coeff = botCompute(convert(self.j1.text), convert(self.j2.text), convert(self.m1.text), convert(self.m2.text))
            except OverflowError:
                invalid2()
            else:
                BottomResultsWindow.og = "|" + self.j1.text + " " + self.j2.text + " " + self.m1.text + " " + self.m2.text + "\u27E9"
                sm.current = "botresults"
        anim = Animation(size_hint=(0.47, 0.18), pos_hint={"x": 0.511, "top": 0.01}, duration=0.03)
        anim.start(widget)


class BottomResultsWindow(Screen):
    coeff = ""
    og = ""

    def on_enter(self, *args):
        self.coeffr.text = "=" + " " + str(self.coeff)
        self.ogr.text = "| j\u2081 j\u2082 m\u2081 m\u2082 \u27E9  = " + self.og

    def resBackChange(self, widget):
        anim = Animation(size_hint=(0.98, 0.18), pos_hint={"x": 0.01, "y": 0.01}, duration=0.03)
        anim.start(widget)

    def resBack(self, widget):
        sm.current = "bottom"
        anim = Animation(size_hint=(0.97, 0.17), pos_hint={"x": 0.01, "y": 0.01}, duration=0.03)
        anim.start(widget)



class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")

sm = WindowManager()

screens = [MainWindow(name="main"), TopWindow(name="top"),BottomWindow(name="bottom"),TopResultsWindow(name="topresults"), BottomResultsWindow(name="botresults")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"

class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()

