from skytrack import *
from time import sleep
from skytrack.rerun import rerun
from rich.console import Console
from skytrack.banner import *
from skytrack.option import *
import os

console = Console()

try:
    main_banner()

    def menu():
        menu.options = [
            "🛫 Extract Information about Plane",
            "📘 Generate Flight Information PDF",
            "🛬 Tail Number and ICAO Conversion",
            "🧭 About and Usage",
            "Exit Tool",
        ]

        option = generate_option(menu.options)

        if option == None:
            rerun()
            return

        if option == 1:
            import skytrack.osint_menu
            rerun()

        if option == 2:
            import skytrack.pdf_menu
            rerun()

        if option == 3:
            import skytrack.icao_tail_menu
            rerun()

        if option == 4:
            import skytrack.about
            rerun()

        if option == 5:
            console.print("[bold][blue] Exiting...[/blue][/bold]")
            sleep(1)

    menu()

except KeyboardInterrupt:
    print("\n")
    console.print("[bold][blue] Exiting...[/blue][/bold]")
    sleep(1)

except TypeError:
    os.system("clear")
    main_banner()
    console.print(f"\n[bold][red] INVALID COMMAND [/red][/bold]")
    rerun()