import flet as ft
from engine import split_text,current_block, forward, backward
def main(page: ft.Page):
    page.title = "Project Gaze"
    page.padding = 0
    page.spacing = 0
    page.window.width = 350
    page.window.height = 300
    page.window.always_on_top = False
    blocks = []
    spot = 0
    def advance_on_click(event):
        nonlocal spot
        spot = forward(spot, blocks)
        speech.value = current_block(spot, blocks)
        page.update()

    def backward_on_hold(event):
        nonlocal spot
        spot = backward(spot,blocks)
        speech.value = current_block(spot,blocks)
        page.update()
    def edit_text(event):
        text_input.visible = True
        start_button.visible = True
        reading_area.visible = False
        edit_button.visible = False
        page.window.height = 400
        page.window.always_on_top = False
        page.update()


    text_input = ft.TextField(
        label="Your speech",
        hint_text="Type or paste your speech here",
        multiline=True,
        min_lines=4,
        max_lines=6,
    )

    speech = ft.Text(current_block(spot, blocks), size=28)
    def start_reading(event):
        nonlocal blocks, spot

        new_text = text_input.value or ""

        if not new_text.strip():
            text_input.error_text = "Enter your speech first."
            page.update()
            return

        text_input.error_text = None
        blocks = split_text(new_text)
        spot = 0
        speech.value = current_block(spot, blocks)
        text_input.visible = False
        start_button.visible = False
        edit_button.visible = True
        reading_area.visible = True
        page.window.height = 160
        page.update()

    reading_area = ft.Container(
    content=speech,
    padding=20,
    expand=True,
    alignment=ft.Alignment.CENTER,
    on_click=advance_on_click,
    on_long_press=backward_on_hold,
    visible=False,
    )
    start_button = ft.Button("Start reading", on_click=start_reading)
    edit_button = ft.Button(
        "Editar texto",
        on_click=edit_text,
        visible=False,
    )

    page.add(
        text_input,
        edit_button,
        start_button,
        reading_area,
        )
    

if __name__ == "__main__":
    ft.run(main)