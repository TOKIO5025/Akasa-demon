import sys
from rich import print
from time import sleep
from rich.console import Console

console = Console()

def lyrics():
    lines = [
        ("\nNo quiero saber", 0.09),  # 1
        ("qué tipo de vestido llevas esta noche", 0.05),
        ("si él te está abrazando tan fuerte", 0.05),
        ("como yo lo hacía antes", 0.07),
        ("Me pasé de la raya", 0.2),  # 5
        ("debí saber que tu amor era un juego", 0.05),
        ("ahora no puedo sacarte de mi mente", 0.05),
        ("Oh, es una verdadera lástima", 0.07),
        ("que ya no hablamos más", 0.05),
        ("Ya no...", 0.04),  # 10
        ("Ya no...", 0.04),
        ("Ya no hablamos más", 0.05),
        ("Ya no...", 0.04),
        ("Ya no...", 0.04),
    ]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(f"[bold][green]{char}[/bold][/green]", end="")
            sys.stdout.flush()
            sleep(char_delay)

        print()  # Salto de línea después de cada verso

lyrics()