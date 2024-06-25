import flet as ft
from flet import Container, Page, Row, Text, border, colors, KeyboardEvent

class ButtonKey(Container):
    def __init__(self, text):
        super().__init__()
        self.content = Text(text, color='gray')
        self.border = border.all(1, colors.WHITE60)
        self.border_radius = 3
        self.bgcolor = "0x09000000"
        self.padding = 10
        self.visible = False
class ButtonShift(Container):
    def __init__(self, text):
        super().__init__()
        self.content = Text(text, color='red')
        self.border = border.all(1, colors.RED)
        self.border_radius = 3
        self.bgcolor = "0x09000000"
        self.padding = 10
        self.visible = False
class ButtonControl(Container):
    def __init__(self, text):
        super().__init__()
        self.content = Text(text, color='green')
        self.border = border.all(1, colors.GREEN)
        self.border_radius = 3
        self.bgcolor = "0x09000000"
        self.padding = 10
        self.visible = False
class ButtonAlt(Container):
    def __init__(self, text):
        super().__init__()
        self.content = Text(text, color='blue')
        self.border = border.all(1, colors.BLUE)
        self.border_radius = 3
        self.bgcolor = "0x09000000"
        self.padding = 10
        self.visible = False
class ButtonMeta(Container):
    def __init__(self, text):
        super().__init__()
        self.content = Text(text, color='yellow')
        self.border = border.all(1, colors.YELLOW_ACCENT)
        self.border_radius = 3
        self.bgcolor = "0x09000000"
        self.padding = 10
        self.visible = False

def main(page: Page) -> None:
    page.title = 'Keyword Shortcuts'
    page.spacing = 30
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    # Creating the text views
    key = ButtonKey("")
    shift = ButtonShift("Shift")
    ctrl = ButtonControl("Control")
    alt = ButtonAlt("Alt")
    meta = ButtonMeta("Meta")

    # Handling the keyboard events
    def on_keyboard(e: KeyboardEvent) -> None:
        key.content.value = e.key
        key.visible = True
        shift.visible = e.shift
        ctrl.visible = e.ctrl
        alt.visible = e.alt
        meta.visible = e.meta
        print(e.data)
        page.update()

    # Linking the keyboard
    page.on_keyboard_event = on_keyboard



    # Create basic page
    page.add(
        Text('Press any key with a combination of CTRL, ALT, SHIFT and META keys...'),
        Row(controls=[key, shift, ctrl, alt, meta],
            alignment=ft.MainAxisAlignment.CENTER),
    )

if __name__ == '__main__':
    ft.app(target=main)