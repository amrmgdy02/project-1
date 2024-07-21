from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

class Interface(FloatLayout):
    def display(self):
        data = self.ids.textinput.text
        self.ids.label.text = data

class ProjectApp(App):
    def build(self):
        return Interface()

if __name__ == "__main__":
    ProjectApp().run()
