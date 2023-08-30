from ast import Pass
from cProfile import label
from tkinter import Button, Widget
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

kv='''
BoxLayout: 
    size:"100sp", "100sp"
    orientation:"vertical"
    Label:
        text:"Numero de la piramide que le toco al Vehiculo"
        size: "100sp", "100sp"
    TextInput:
        text:"Ingresa el numero de la piramide del Vehiculo"
'''

class MiprimeraApp(App):
    def build(self):
        return Builder.load_string(kv)

MiprimeraApp().run()