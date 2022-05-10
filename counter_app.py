from cgitb import text
from msilib.schema import Font
from tkinter import font
from turtle import back, color
from webbrowser import BackgroundBrowser
from kivy.config import Config

Config.set('graphics', 'width', 720) 
Config.set('graphics', 'height', 1280)

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image

font = './font/Nunito-VariableFont_wght.ttf'

Window.clearcolor = (255, 255, 255, 1)


class MyApp(App):
    def build(self):
        self.onnazat = 0
        layout = FloatLayout()
        btn = Button(
            size_hint =(.505 , .10),
            pos=(-1,960),
            font_size = 124,
            background_color=[1, 245, 231, 1],
            on_press = self.btn_press,
            
        )
        layout.add_widget(btn)
        img = Image(
                source='1093271_red.png',
                size_hint =(.120 , .10),
                pos=(150 , 955)
        )
        layout.add_widget(img)
        
        btn2 = Button(
            size_hint =(.505 , .10),
            pos=(361,960),
            background_color=[1, 245, 231, 1],
            on_press = self.btn_press,
            text = '+',
            color = (9, 157, 186, 1),
            font_size = 128,
            )
        l_welcome = Label(
            text = 'ласкаво просимо в ',
            pos = ( 170 ,870),
            size_hint =(.505 , .10),
            disabled_color = [0,0,0,0],
            color = (9, 157, 186, 1),
            font_name='Nunito-VariableFont_wght.ttf',
            font_size = 52
            )
        l_header = Label(
            text = 'сountererg',
            pos = ( 170 ,800),
            size_hint =(.505 , .10),
            disabled_color = [0,0,0,0],
            color = (9, 157, 186, 1),
            font_name='Nunito-VariableFont_wght.ttf',
            font_size = 102
            )
        l_you_can = Label(
            text = 'тут ви можете:',
            pos = ( 170 ,700),
            size_hint =(.505 , .10),
            disabled_color = [0,0,0,0],
            color = (9, 157, 186, 1),
            font_name='Nunito-VariableFont_wght.ttf',
            font_size = 72
            )
        l_description = Label(
            text = 'створювати лічильники',
            pos = ( 170 ,630),
            size_hint =(.505 , .10),
            disabled_color = [0,0,0,0],
            color = (9, 157, 186, 1),
            font_name='Nunito-VariableFont_wght.ttf',
            font_size = 52
            )
        layout.add_widget(l_description)
        layout.add_widget(l_you_can)
        layout.add_widget(l_header)
        layout.add_widget(l_welcome)
        layout.add_widget(btn2)
        return layout
    def btn_press(self ,instance):
        instance.background_color = [0, 222, 209, 1]
        self.onnazat = self.onnazat + 1

        if self.onnazat == 2:
            instance.background_color=[1, 245, 231, 1]
            self.onnazat = 0

        


if __name__ == '__main__':
    MyApp().run()