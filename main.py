from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Main(App):
    def build(self):
        # Erstelle ein Boxlayout
        layout = BoxLayout(orientation='vertical')
        
        # Füge einen Texteingabebereich hinzu
        self.text_input = TextInput(hint_text='Gib hier etwas ein...')
        layout.add_widget(self.text_input)
        
        # Füge einen Button hinzu
        button = Button(text='Drück mich!')
        # Weise dem Button die Funktion zum Drücken zu
        button.bind(on_press=self.on_button_click)
        layout.add_widget(button)
        
        return layout
    
    # Funktion, die aufgerufen wird, wenn der Button gedrückt wird
    def on_button_click(self, instance):
        # Hole den eingegebenen Text aus dem Texteingabebereich
        input_text = self.text_input.text
        # Gib den Text in der Konsole aus
        print("Eingegebener Text:", input_text)

if __name__ == '__main__':
    Main().run()