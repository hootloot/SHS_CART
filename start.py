#Read commments for information and instructions

#First, run this file
#Try using the application, write text in the input boxes
#Then look at the terminal, the information you input after you press "submit" should be outputted (If it doesn't ask for help). 
#Now, look at the rest of the comments to see how the program works. 


#After installing kivy, you can now import these modules. 
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#This section of code is for the user interface, basically how it looks like. 
#It has a grid like layout
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
        #This is using the function in the next section for input
        self.add_widget(self.submit)

    #This section is different, it is the "backend" of this application. 
    #This creates the actual action or function of the application, without this just the user interface is shown, you can't input anything. 
    def pressed(self, instance):
        #When button is pressed:
        
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
        #This is building the display, always include this
        return MyGrid()

#Always include this too
if __name__ == "__main__":
    MyApp().run()
    
    
#Instructions:
#Try changing part of the code, see what values you can change. 
#Example, in section one you change the label of the input boxes

#Open the "Using_Kv_Files" folder, open the "main.py" file.
    

    
    
