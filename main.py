from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        return Button(text='Array', pos=(300, 300), size_hint = (.20, .15))

if __name__ == '__main__':
    MyApp().run()
