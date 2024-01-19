from time import sleep
from skytrack.icao_tail import *
from skytrack.osint import *
from skytrack.option import generate_option
from rich.console import Console
from skytrack.menu import rerun
import os

console = Console()

try: 
    def pdf_options_menu():
        pdf_options_menu.options = [
            "🛫  Input Tail Number",
            "🛬  Input ICAO Designator",
            "Back to Main Menu"
        ]
        
        option = generate_option(pdf_options_menu.options)

        if option == 1:
            value = console.input("Enter [bold blue]Tail Number[/]: ")
            osint_from_tail(value, True)

        if option == 2:
            value = console.input("Enter [bold blue]ICAO Designation[/]: ")
            osint_from_icao(value, True)
        
    pdf_options_menu()

except KeyboardInterrupt:
    print("\n")
    console.print("[bold][cyan] Exiting skytrack [/cyan][/bold]")
    sleep(1)

except TypeError:
    #os.system("clear")
    rerun()