from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget


class MyGameApp(App):
    def on_start(self):
        Clock.schedule_interval(self.root.ids.background.scroll,1/2.)
    pass


class Background(Widget):
    groundf_texture = ObjectProperty(None)

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.groundf_texture = Image(source="player_walk_2.png").texture
        self.groundf_texture.wrap = 'repeat'
        self.groundf_texture.uvsize = (Window.width/self.groundf_texture.width,-1)

    def scroll(self, time_passed):
        self.backgroundf_textures.ucpos = ((self.backgroundf_texture.uvpos[0]+time_passed)%Window.width,self.backgroundf_textures)

        texture = self.properties('backgroundf_texture')
        texture.dipatch(self)
        print("scroll")



MyGameApp().run()