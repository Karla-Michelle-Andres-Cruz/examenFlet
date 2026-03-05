import flet as ft

def main(page: ft.Page):
    page.title = "Examen Final - Registro de Participantes"
    page.padding = 20

    ft.TextField(
        label="Nombre Completo",
        hint_text="Ingrese su nombre completo",
        prefix_icon=ft.Icons.PERSON
    )

    ft.TextField(
        label="Email",
        hint_text="Ingrese su correo electrónico",
        prefix_icon=ft.Icons.EMAIL
    )

    taller = ft.Dropdown(
        label="Taller de interés",
        options=[
            ft.dropdown.Option("Python para Principiantes"),
            ft.dropdown.Option("Flet Intermedio"),
            ft.dropdown.Option("Análisis de Datos con Pandas"),
        ]
    )

    pago = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="Pago completo", label="Pago completo"),
            ft.Radio(value="Pago por cuotas", label="Pago por cuotas")
        ])
    )

    laptop = ft.Checkbox(
        label="Requiere computadora portátil",
        value=False
    )

    nivel_slider = ft.Slider(
        min=0,
        max=5,
        divisions=5,
        label="{value}"
    )

    resumen = ft.Text(
        value="",
        size=16,
        color=ft.Colors.BLUE_900
    )

    def generar_resumen(e):
        requiere = "Sí" if laptop.value else "No"

        resumen.value = (
            "--- FICHA DEL PARTICIPANTE ---\n\n"
            f"Nombre: {nombre.value}\n\n"
            f"Email: {correo.value}\n\n"
            f"Taller: {taller.value}\n\n"
            f"Pago: {pago.value}\n\n"
            f"Requiere Portátil: {requiere}\n\n"
            f"Nivel de Experiencia: {int(nivel_slider.value)}\n\n"
            "--- Gracias por su registro ---"
        )

        page.update()

    boton = ft.Row(
        [
            ft.ElevatedButton(
                text="Mostrar Ficha del Participante",
                bgcolor=ft.Colors.GREEN_400,
                color=ft.Colors.WHITE,
                on_click=generar_resumen
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    contenido = ft.Column(
        [
            ft.Text(
                "Examen Final - Registro de Participantes",
                size=30,
                weight=ft.FontWeight.BOLD
            ),

            nombre,
            correo,
            taller,

            ft.Text("Tipo de Pago"),
            pago,

            laptop,

            ft.Text("Nivel de Experiencia"),
            nivel_slider,

            boton,

            resumen
        ],
        spacing=15
    )

    page.add(contenido)

ft.app(target=main)