from kivy.app import App
from kivy.lang import Builder

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 20
    spacing: 10

    Label:
        text: 'Simple Assistant'
        font_size: '24sp'
        size_hint_y: None
        height: 60

    TextInput:
        id: input_box
        hint_text: 'Type something...'
        size_hint_y: None
        height: 120

    Button:
        text: 'Ask'
        size_hint_y: None
        height: 60
        on_release: app.respond()

    Label:
        id: output
        text: ''
        size_hint_y: None
        height: 120
'''

class SimpleAssistant(App):
    def build(self):
        return Builder.load_string(KV)

    def respond(self):
        text = self.root.ids.input_box.text.strip()
        if not text:
            self.root.ids.output.text = "Say something."
        else:
            self.root.ids.output.text = f"You said: {text}"

if __name__ == '__main__':
    SimpleAssistant().run()
