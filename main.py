import flet as ft

def main(page: ft.Page):
    page.title = "Registro de Participantes"
    
    page.add(
    
        ft.Text(
            "Registro de Participantes", 
            size=30, 
            color=ft.Colors.BLACK,
            weight=ft.FontWeight.BOLD
        ),
        
        ft.TextField(
            label="Nombre Completo",
            hint_text="Ingrese su nombre completo",
            value = "",
            prefix_icon= ft.Icons.PERSON
        ),
        
        ft.TextField(
            label="Ingresa tu correo electronico",
            hint_text="Ingrese su correo electronico",
            value="",
            prefix_icon= ft.Icons.EMAIL
        ),
        
        ft.Text("Taller de interes"),
            
        ft.Dropdown(
            width=200,
            value="Taller de interes",
            options=[
                ft.DropdownOption(key="Python para Principiantes", text="Python para Principiantes"),
                ft.DropdownOption(key="Flet Intermedio", text="Flet Intermedio"),
                ft.DropdownOption(key="Análisis de Datos con Pandas", text="Análisis de Datos con Pandas"),
            ]
        ),
        
        ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Pago completo", label="Pago completo"),
                ft.Radio(value="Pago por cuotas", label="Pago por cuotas")
            ]),
            value="Pago completo",
            on_change=lambda e: print(f"Seleccionado: {e.control.value}")
        ),
        
        ft.Checkbox(
            label="Requiere computadora portátil",
            value=False
        ),
        
    )
    
    
    def nivel(e: ft.Event[ft.Slider]):
        message.value = f"Nivel Seleccionado: {e.control.value}"
        message.update()

    page.add(
        ft.Text("Nivel de Experiencia"),
        ft.Slider(
            key="slider",
            min=0,
            max=5,
            divisions=5,
            label="{value}",
            on_change=nivel,
        ),
        message := ft.Text(),
    )
    
    page.add(
        ft.ElevatedButton(
            text="Mostrar Ficha del Participante",
            on_click=lambda e: print("Ficha mostrada"),
            color=ft.Colors.PURPLE_400,
        )
    )
    
    


    page.update()


    
ft.app(target=main)





