import flet as ft
from engine import split_text,current_block, forward, backward
def main(page: ft.Page):
    page.title = "Project Gaze"
    page.padding = 0
    page.spacing = 0
    page.window.width = 500
    page.window.height = 160
    page.window.always_on_top = True
    text = "Today I want to present my first project made in Python"
    blocks = split_text(text)
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

    

    speech = ft.Text(current_block(spot, blocks), size=28)
    page.add(
        ft.Container(
            content=speech,
            padding=20,
            expand=True,
            alignment=ft.Alignment.CENTER,
            on_click=advance_on_click,
            on_long_press= backward_on_hold
        )
    )


if __name__ == "__main__":
    ft.run(main)
