
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import re


class LabanCalculator(App):

    def build(self):
        self.expression = ""

        main = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
        )

        self.display = Label(
            text="0",
            font_size=40,
            halign="right",
            valign="middle",
            size_hint=(1, 0.25)
        )

        self.display.bind(
            size=lambda obj, size:
            setattr(obj, "text_size", size)
        )

        main.add_widget(self.display)

        buttons = [
            ["AC", "DEL", "/", "*"],
            ["7", "8", "9", "-"],
            ["4", "5", "6", "+"],
            ["1", "2", "3", "="],
            ["0", ".", "(", ")"]
        ]

        grid = GridLayout(
            cols=4,
            spacing=6
        )

        for row in buttons:
            for item in row:
                btn = Button(
                    text=item,
                    font_size=25
                )
                btn.bind(
                    on_press=self.press
                )
                grid.add_widget(btn)

        main.add_widget(grid)

        return main

    def press(self, button):
        value = button.text

        if value == "AC":
            self.expression = ""

        elif value == "DEL":
            self.expression = self.expression[:-1]

        elif value == "=":
            try:
                if not re.fullmatch(
                    r"[0-9+\-*/(). ]+",
                    self.expression
                ):
                    raise ValueError()

                answer = eval(
                    self.expression,
                    {"__builtins__": None},
                    {}
                )

                self.expression = str(answer)

            except Exception:
                self.expression = "Error"

        else:
            if self.expression == "Error":
                self.expression = ""

            self.expression += value

        self.display.text = self.expression or "0"


if __name__ == "__main__":
    LabanCalculator().run()
