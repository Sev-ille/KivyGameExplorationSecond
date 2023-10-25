from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget


class MyGameApp(App):

    pass


class Background(Widget):
    ground_texture = ObjectProperty(None)
    pass


MyGameApp().run()