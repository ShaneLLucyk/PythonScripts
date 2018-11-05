#Import Libraries
import kivy
kivy.require('1.10.1') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation='horizontal'
        navC=Layout();
        navL=AnchorLayout(anchor_x='left', anchor_y='top')
        navR=AnchorLayout(anchor_x='right', anchor_y='top')

        self.add_widget(navL)
        self.add_widget(navR)


        navL.add_widget(Label(text="navLav1"))
        navR.add_widget(Label(text="navlav2"))
        self.add_widget(TextInput(text='AfterNavLav2'))


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
