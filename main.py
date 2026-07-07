import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    input = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100, read_only=True, filled=True)

    def minus_click(e):
        input.value = str(int(input.value) - 1)

    def plus_click(e):
        input.value = str(int(input.value) + 1)

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(ft.Icons.REMOVE_ROUNDED, on_click=minus_click),
                input,
                ft.IconButton(ft.Icons.ADD_ROUNDED, on_click=plus_click),
            ],
        )
    )

ft.run(main)
