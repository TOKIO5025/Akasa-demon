import sys
from rich import print
from time import sleep
from rich.console import Console

console = Console()

def lyrics():
    lines = [
        ("....", 0.02),  # 1
        ("¿Será que me sigues a donde voy?", 0.09),
        ("A un lugar donde no nos separe la vida", 0.09),
        ("Donde yo sonrío como en los años veinte", 0.09),
        ("Donde hasta las tormentas se calman...", 0.06),  # 5
        ("Porque ya nos tenemos", 0.06),
        ("O déjame seguirte de una vez", 0.09),
        ("Separarnos es un castigo que duele toda la vida", 0.08),
        ("Sin ti en este mundo...", 0.06),
        ("Solo queda oscuridad rodeándome", 0.07),  # 10
        ("Por favor no me dejes sola en medio...", 0.08),
        ("De esta vida tan vacía y sola", 0.07),
    ]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(f"[bold][blue1]{char}[/bold][/blue1]", end="")
            sys.stdout.flush()
            sleep(char_delay)

        print()

lyrics()