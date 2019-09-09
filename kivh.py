from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):
    pass

class SettingsWindow(Screen):
    def btn1(self):
        print("Button 1 clicked")
    def btn2(self):
        print("Button 2 clicked")
    def btn3(self):
        print("Button 3 clicked")
    def btn4(self):
        print("Button 4 clicked")
    def btn5(self):
        print("Button 5 clicked")
    def btn6(self):
        print("Button 6 clicked")
    def btn7(self):
        print("Button 7 clicked")
    def btn8(self):
        print("Button 8 clicked")
class UserWindow(Screen):
    pass
class AdminWindow(Screen):
    pass
class MedicalWindow(Screen):
    def ambulance(self):
        print("Calling 108")
class SosWindow(Screen):
    def police(self):
        print("Calling Police")
class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()