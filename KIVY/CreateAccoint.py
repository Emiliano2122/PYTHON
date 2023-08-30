from ast import Pass
from cProfile import label
from tkinter import Button, Widget
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder

kv='''
BoxLayout: 
    size:"100sp", "100sp"
    orientation:"vertical"
    Label:
        text:"Nombre y Apellido"
        size: "100sp", "100sp"
    TextInput:
        text:"Ingresa tu Nombre y Apellido"
    Label:
        text:"Correo Electronico"
    TextInput:
        text:"Ingresa tu correo electronico"
    Label:
        text:"Contraseña"
        size: "100sp", "100sp"
    TextInput:
        text:"Ingresa tu contraseña"
    Button:
        text:"Crear Cuenta"
        size: "100sp", "100sp"
    Button:
        text:"Regresar"
        size: "100dp", "100dp"
    
'''


class MiprimeraApp(App):
    def build(self):
        return Builder.load_string(kv)

MiprimeraApp().run()