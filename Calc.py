import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):

    def build(self):
        layout = GridLayout(cols=4, spacing=5, padding=5)

        buttons = [
            '(', ')', '%', '<--',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', '=', '+',
            'C'
        ]

        for button in buttons:
            btn = Button(text=button, font_size=18)
            if button not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
                btn.background_color = [1, 0.5, 0, 1]  # Orange color for operators
            btn.bind(on_press=self.on_button_press)

        self.result = TextInput(multiline=False, readonly=True, font_size=24, size_hint=(1, 0.1))
        layout.add_widget(self.result)

        for button in buttons:
            btn = Button(text=button, font_size=18)
            if button not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
                btn.background_color = [1, 0.5, 0, 1]  # Orange color for operators
            btn.bind(on_press=self.on_button_press)
            layout.add_widget(btn)

        return layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == '=':
            try:
                result = str(eval(current))
            except Exception as e:
                result = 'Error'
        elif button_text == 'C':
            result = ''
        elif button_text == '<--':
            result = current[:-1]
        elif button_text == '%':
            try:
                result = str(eval(current) / 100)
            except Exception as e:
                result = 'Error'
        else:
            result = current + button_text

        self.result.text = result


if __name__ == '__main__':
    CalculatorApp().run()