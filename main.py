import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        #User Interface has a Grid Layout
        self.inside.cols = 2
        #The Grid Layout has 2 collums on each side

        self.inside.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)
        #First Input Box

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Coffee Selection: "))
        self.other = TextInput(multiline=False)
        self.inside.add_widget(self.other)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        #When the submit button is pressed, then:
        name = self.name.text
        last = self.lastName.text
        email = self.email.text
        
        #^This happens
        print("Name:", name, "Last Name:", last, "Email:", email)
        #Prints the input
        self.name.text = ""
        self.lastName.text = ""
        self.email.text = ""

      
class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
