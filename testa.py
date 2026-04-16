from flet import TextField, InputBorder, Page, ControlEvent, app

def main(page: Page):

    textfield = TextField(
        multiline=True,
        autofocus=True,
        border=InputBorder.NONE,
        min_lines=40,
        content_padding=30,
        cursor_color='yellow'
    )

    def save_text(e: ControlEvent):
        with open('save.txt', 'w') as f:
            f.write(textfield.value or "")

    def read_text():
        try:
            with open('save.txt', 'r') as f:
                return f.read()
        except FileNotFoundError:
            return ""

    # Load saved text
    saved = read_text()
    if saved:
        textfield.value = saved
    else:
        textfield.hint_text = "Welcome to the Text Editor!"

    textfield.on_change = save_text

    page.title = "Note Pad"
    page.scroll = True
    page.add(textfield)

app(target=main)



















