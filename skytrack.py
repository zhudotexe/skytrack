import os
from rich.console import Console

console = Console()

try:
    from skytrack.menu import menu
except KeyboardInterrupt:
    os.system("clear")