import sys
from rich import print
from time import sleep
from rich.console import Console

console = Console()

def lyrics():
    lines = [
        ("....", 0.01),  # 1
        ("Gracias a quienes han protegido las montañas y ríos de Đại Việt durante mil años", 0.08),
        ("Gracias al Padre Viejo nuestro en el camino de salvar la nación\n", 0.08),
        ("Para que el país viva en paz desde entonces...", 0.07),
        ("Para que el rojo brille en la bandera de la libertad...", 0.07),  # 5
        ("Para que las risas resuenen por todas partes desde el día de la victoria", 0.09),
        ("Juntos continuemos escribiendo la historia de la paz", 0.05),
        ("Mirando la patria fresca y luminosa en el amanecer", 0.05),
        ("Mirando la luz del sol brillar intensamente en la bandera nacional ondeando al viento", 0.08),
        ("Juntos continuemos escribiendo la historia de la paz", 0.05),  # 10
        ("Mirando la patria fresca y luminosa en el amanecer", 0.05),
        ("Mirando la luz del sol brillar intensamente en la bandera nacional ondeando al viento", 0.08),
        ("Mirando la luz del sol brillar intensamente en la bandera nacional ondeando al viento", 0.08),
        ("...", 0.05),
    ]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(f"[bold][blue1]{char}[/bold][/blue1]", end="")
            sys.stdout.flush()
            sleep(char_delay)

        print()  # Salto de línea después de cada verso

lyrics()