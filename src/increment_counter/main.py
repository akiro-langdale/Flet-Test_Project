import flet as ft

def main(page: ft.Page):
    page.title = "Increment counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER    
    # page.theme_mode = 'light' # default theme 'system'

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

if __name__ == '__main__':
    ft.app(target=main)
    # ft.app(target=main, view=ft.AppView.WEB_BROWSER)