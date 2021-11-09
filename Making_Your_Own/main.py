import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

#This is the front end part of the application, however it uses the .kv file in this folder. 
class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    
    
    
#This is the back end of the application, the main focus of this file.
    def btn(self):
        print("Name:", self.name.text, "email:", self.email.text)
        self.name.text = ""
        self.email.text = ""

#Again, these part are to build the application, these are needed
class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
