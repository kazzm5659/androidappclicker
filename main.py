# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.label = Label(text='Привет, Maks!', font_size=32)
        button = Button(text='Нажми меня', font_size=24)
        button.bind(on_press=self.on_button_press)

        layout.add_widget(self.label)
        layout.add_widget(button)
        return layout

    def on_button_press(self, instance):
        self.label.text = 'Ты нажал кнопку! 🎉'

if __name__ == '__main__':
    MyApp().run()