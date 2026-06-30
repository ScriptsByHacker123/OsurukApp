from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import webbrowser

class MuzikUygulamasi(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        self.input = TextInput(hint_text="Ne çalalım?", multiline=False)
        self.btn = Button(text="YouTube'da Ara")
        self.btn.bind(on_press=self.arama_yap)
        
        self.add_widget(self.input)
        self.add_widget(self.btn)

    def arama_yap(self, instance):
        komut = self.input.text
        if komut:
            url = f"https://www.youtube.com/results?search_query={komut}"
            webbrowser.open(url)

class MuzikApp(App):
    def build(self):
        return MuzikUygulamasi()

if __name__ == "__main__":
    MuzikApp().run()
    
