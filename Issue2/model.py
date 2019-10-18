import time
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)
        
        self.inside = FloatLayout()
        
        self.btn1 = Button(text="Create Report", size_hint=(.5, .5))
        
        self.add_widget(self.inside)
        self.btn1.bind(on_press=self.callback)
        self.add_widget(self.btn1)
    
    def callback(self, instance):
    		print('The button is being pressed...')
    		print("Timestamp: %s" % time.ctime())

class MainApp(App):

    def build(self):
    
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
            Color(0, 1, 0, 1)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


if __name__ == '__main__':
    MainApp().run()

