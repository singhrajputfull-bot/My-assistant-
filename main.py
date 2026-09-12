from kivy.app import App
from kivy.uix.button import Button

class MaxApp(App):
    def build(self):
        return Button(text='Hello Boss, Max is Ready!')

if __name__ == '__main__':
    MaxApp().run()
  
